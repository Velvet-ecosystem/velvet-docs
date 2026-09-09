"""Real software composition on temporary state and authenticated loopback HTTP.

Only sensor/hardware input and deployment secrets are synthetic. Source custody,
retrieval service/client, Runtime composition, Core, Language and Receipts are
the actual prepared implementations. No installed identity or vault is touched.
"""
import hashlib
import json
import threading
import time
from http.server import ThreadingHTTPServer
from types import SimpleNamespace
from unittest.mock import patch

import pytest

import scripts.bootstrap_dev_state as bootstrap
from ghost import distributed_body_run
from receipt_logger import ReceiptLogger
from services.body_state_bridge import BodyStateSnapshotBridge
from services.continuity_activation import ContinuityBootPaths, load_configured_identity_context
from services.court_authority import resolve_authority
from services.library_conversation_provider import RuntimeLibraryEvidenceProvider
from services.local_conversation import LocalConversationError, build_local_conversation_gateway
from velvet.core.native_brain.conversation_ingress import handle_conversation_turn
from velours_library.catalog import Library
from velours_library.remote_client import RemoteLibraryClient, RemoteLibraryError
from velours_library.retrieval_service import PeerSecretStore, RetrievalAudit, build_handler

QUERY = 'What does the Library say about the violet fixture inspection?'
PASSAGE = 'Inspect the violet fixture connector before recording the inspection result.'
TEST_TOKEN = 'synthetic-acceptance-only-never-deploy-0123456789'


@pytest.fixture
def bench(tmp_path, monkeypatch):
    # Keep unrelated deployment configuration from changing this synthetic run.
    for name in ('VELVET_LIBRARY_URL', 'VELVET_VAULT_FILESYSTEM_UUID'):
        monkeypatch.delenv(name, raising=False)
    snapshot = tmp_path / 'body.json'
    journal = tmp_path / 'body-events.jsonl'
    bridge = BodyStateSnapshotBridge(snapshot, journal)
    now = time.time()
    bridge.publish({
        'event_id': 'synthetic-environment-1', 'event_type': 'SENSOR_PACKET_OBSERVED',
        'source': 'acceptance.environment', 'family': 'sensor', 'schema_version': '1.0',
        'timestamp': now,
        'payload': {'module_id': 'acceptance.environment', 'node_id': 'acceptance-founder',
                    'owning_handmaiden': 'Velvet', 'timestamp': now, 'monotonic_time': time.monotonic(),
                    'sensor_type': 'environmental_conditions', 'interface_type': 'synthetic',
                    'health_state': 'ONLINE', 'confidence': 0.95,
                    'payload': {'cabin_temperature_c': 21.5},
                    'receipt_id': 'synthetic-environment-evidence', 'source_clock': 'host',
                    'stale_after_ms': 60000, 'calibration_version': 'synthetic-v1',
                    'raw_reference': 'fixture://environment'}})
    library = Library(tmp_path / 'library')
    source = tmp_path / 'reference.txt'
    source.write_text(PASSAGE + '\n', encoding='utf-8')
    item = library.add(source, title='Synthetic violet inspection reference',
                       source='software acceptance fixture', trust_class='owner',
                       source_uri='fixture://violet-inspection')
    secret_dir = tmp_path / 'peer-secrets'
    secret_dir.mkdir(mode=0o700)
    token_file = secret_dir / 'acceptance-founder.token'
    token_file.write_text(TEST_TOKEN, encoding='utf-8')
    token_file.chmod(0o600)
    audit_path = tmp_path / 'retrieval-audit.jsonl'
    handler = build_handler(library, PeerSecretStore(secret_dir), RetrievalAudit(audit_path))
    server = ThreadingHTTPServer(('127.0.0.1', 0), handler)
    thread = threading.Thread(target=server.serve_forever, kwargs={'poll_interval': 0.05}, daemon=True)
    thread.start()
    host, port = server.server_address
    client = RemoteLibraryClient.from_token_file('http://%s:%s' % (host, port),
        node_id='acceptance-founder', token_file=token_file, timeout_seconds=1.0)
    meanings = []

    def capture(event, *, resolver):
        meaning = handle_conversation_turn(event, resolver=resolver)
        meanings.append(meaning)
        return meaning

    gateway = build_local_conversation_gateway(snapshot_path=snapshot,
        conversation_id='software-acceptance', handle_turn=capture,
        library_evidence_provider=RuntimeLibraryEvidenceProvider(client))
    try:
        yield SimpleNamespace(root=tmp_path, snapshot=snapshot, journal=journal, library=library,
            item=item, token_file=token_file, audit=audit_path, client=client,
            gateway=gateway, meanings=meanings, bridge=bridge)
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=2)
        assert not thread.is_alive()


def ask(bench, text):
    exchange = bench.gateway.submit(text)
    assert not exchange.request.authority_granted
    assert not exchange.reply.authority_granted
    assert not exchange.reply.speak
    meaning = bench.meanings[-1]
    assert meaning['authority'] == 'none'
    for key in ('grants_authority', 'grants_execution', 'grants_actuation'):
        assert meaning[key] is False
    return exchange.reply, meaning


def assert_library_reference(bench, reply, meaning):
    assert meaning['response_kind'] == 'evidence'
    assert 'library:item:' + bench.item.item_id in reply.source_refs
    assert 'library:sha256:' + bench.item.sha256 in reply.source_refs
    assert 'reference-only' in reply.qualifiers
    assert 'violet fixture connector' in reply.text


def test_startup_generated_policy_through_real_context_loaders(tmp_path):
    state = tmp_path / '.velvet-dev/state'
    # Real Continuity creates a disposable development identity. Fixed test
    # bytes and synthetic surface input cannot represent production identity.
    with patch.object(bootstrap, 'ROOT', tmp_path), patch.object(bootstrap, 'DEV_ROOT', state), \
         patch.object(bootstrap, 'collect_surface_identity', return_value=SimpleNamespace(fingerprint='synthetic-acceptance-surface')), \
         patch.object(bootstrap.secrets, 'token_bytes', return_value=b'synthetic-only-test-key-material!'):
        assert bootstrap.main() == 0
    paths = ContinuityBootPaths(
        identity_chain=state / 'continuity/identity_chain.json',
        proof_material=state / 'continuity/proof_material.bin',
        surface_metadata=state / 'continuity/surface_identity.json',
        body_registry=state / 'body/registry.json', profile_registry=state / 'profiles/registry.json',
        session_context=state / 'session/current.json', capability_policy=state / 'policy/capability_context.json',
        receipt_ledger=state / 'receipts/continuity.log')
    context = load_configured_identity_context(paths)
    assert context.session.profile.profile_type == 'guest'
    assert not context.session.owner_verified
    assert not context.session.physical_presence
    capability = context.capability_context
    assert capability.proposed_capabilities == ('observe.telemetry',)
    assert capability.court_authority == 'guest'
    assert capability.authorization_required and not capability.actuation_granted
    assert resolve_authority(capability).selected_profile == 'guest'


def test_ordinary_typed_conversation_uses_runtime_snapshot(bench):
    reply, meaning = ask(bench, 'What is the cabin temperature?')
    assert meaning['fact_id'] == 'cabin.temperature'
    assert meaning['value'] == 21.5
    assert '21.5' in reply.text
    assert 'stale' not in reply.qualifiers
    assert 'receipt:synthetic-environment-evidence' in reply.source_refs


def test_real_authenticated_library_retrieval_retains_source_custody(bench):
    before = hashlib.sha256(bench.library.db_path.read_bytes()).hexdigest()
    reply, meaning = ask(bench, QUERY)
    assert_library_reference(bench, reply, meaning)
    assert hashlib.sha256(bench.library.db_path.read_bytes()).hexdigest() == before
    audit = [json.loads(line) for line in bench.audit.read_text().splitlines()]
    assert audit[-1]['status'] == 'ok'
    assert audit[-1]['result_count'] >= 1
    assert audit[-1]['raw_query_recorded'] is False
    assert audit[-1]['authority'] == 'none'
    assert QUERY not in bench.audit.read_text()


def test_library_lost_then_restored_in_same_conversation(bench):
    first, meaning = ask(bench, QUERY)
    assert_library_reference(bench, first, meaning)
    moved = bench.library.root.with_name('library-disconnected')
    bench.library.root.rename(moved)
    try:
        lost, meaning = ask(bench, QUERY)
        assert meaning['response_kind'] == 'unavailable'
        assert 'library-retrieval-unavailable' in meaning['qualifiers']
        assert not lost.source_refs and not lost.evidence_texts
        assert 'violet fixture connector' not in lost.text
        assert 'same guidance' not in lost.text
        assert not bench.library.root.exists()
        body, _ = ask(bench, 'What is the cabin temperature?')
        assert '21.5' in body.text
    finally:
        moved.rename(bench.library.root)
    restored, meaning = ask(bench, QUERY)
    assert_library_reference(bench, restored, meaning)
    assert restored.source_refs == first.source_refs


def test_library_peer_rejection_degrades_without_bypassing_authentication(bench):
    bench.token_file.unlink()
    with pytest.raises(RemoteLibraryError, match='401'):
        bench.client.evidence(QUERY)
    reply, meaning = ask(bench, QUERY)
    assert meaning['response_kind'] == 'unavailable'
    assert not reply.source_refs
    body, _ = ask(bench, 'What is the cabin temperature?')
    assert '21.5' in body.text


def test_body_service_loss_preserves_error_contract_and_library_independence(bench):
    content = bench.snapshot.read_bytes()
    bench.snapshot.unlink()
    with pytest.raises(LocalConversationError, match='snapshot is unavailable'):
        bench.gateway.submit('What is the cabin temperature?')
    reply, meaning = ask(bench, QUERY)
    assert_library_reference(bench, reply, meaning)
    bench.snapshot.write_bytes(content)
    recovered, _ = ask(bench, 'What is the cabin temperature?')
    assert '21.5' in recovered.text


def test_insufficient_library_evidence_has_no_invented_reference(bench):
    reply, meaning = ask(bench, 'What does the Library say about zyxqnonexistent?')
    assert meaning['response_kind'] == 'unavailable'
    assert 'library-no-passage' in meaning['qualifiers']
    assert not reply.source_refs and not reply.evidence_texts


def test_existing_ghost_receipts_form_verifiable_observation_trail(tmp_path):
    path = tmp_path / 'ghost-receipts.jsonl'
    logger = ReceiptLogger(str(path))
    real_builder = distributed_body_run.runtime_receipt_from_envelope
    def persist(envelope):
        return logger.log(real_builder(envelope))
    with patch.object(distributed_body_run, 'runtime_receipt_from_envelope', side_effect=persist):
        result = distributed_body_run.run_distributed_ghost()
    assert result.authority == 'none'
    assert not result.execution_authorized and not result.actuation_authorized
    before = path.read_bytes()
    assert logger.verify_chain() == (True, [])
    entries = [json.loads(line) for line in before.splitlines()]
    assert tuple(entry['receipt_id'] for entry in entries) == result.queen_result.receipt_ids
    assert tuple(entry['event'] for entry in entries) == result.lifecycle_events
    assert len(entries) == 5
    assert path.read_bytes() == before
