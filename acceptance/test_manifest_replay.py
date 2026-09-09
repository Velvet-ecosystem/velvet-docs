"""Guard reproducibility, exact overlays and refusal to overwrite local work."""
import copy
import json
from pathlib import Path
import subprocess

import pytest

from acceptance import prepare_sources as replay


def manifest():
    return json.loads((Path(__file__).resolve().parents[1] /
                       'compatibility/current-2026-09-07.json').read_text())


@pytest.mark.parametrize('field,value', [
    ('commit', 'main'), ('commit', 'abc1234'), ('expected_tree', None),
    ('expected_tree', '../outside'),
])
def test_manifest_refuses_unpinned_inputs(field, value):
    document = manifest()
    document['repositories']['velvet-runtime'][field] = value
    with pytest.raises(ValueError, match='exact'):
        replay.validate_manifest(document)


def test_manifest_refuses_unknown_repository_and_duplicate_overlay():
    document = manifest()
    document['repositories']['unreviewed-repository'] = {}
    with pytest.raises(ValueError, match='explicit public set'):
        replay.validate_manifest(document)
    document = manifest()
    document['repositories']['velvet-runtime']['repairs'] *= 2
    with pytest.raises(ValueError, match='unique exact'):
        replay.validate_manifest(document)


def test_existing_destination_is_never_overwritten(tmp_path):
    marker = tmp_path / 'user-work.txt'
    marker.write_text('keep me')
    with pytest.raises(ValueError, match='must not exist'):
        replay.prepare(Path(__file__).resolve().parents[1] /
                       'compatibility/current-2026-09-07.json', tmp_path)
    assert marker.read_text() == 'keep me'


@pytest.fixture
def tiny_repository(tmp_path, monkeypatch):
    # These commits belong to a disposable test repository, never an ecosystem main.
    mirror = tmp_path / 'mirrors'
    repo = mirror / 'fixture'
    repo.mkdir(parents=True)
    replay.git(repo, 'init', '--quiet', '--initial-branch=fixture')
    def commit(value):
        (repo / 'contract.txt').write_text(value)
        replay.git(repo, 'add', 'contract.txt')
        replay.git(repo, '-c', 'user.name=Synthetic Acceptance', '-c',
                   'user.email=acceptance@example.invalid', 'commit', '--quiet', '-m', 'fixture')
        return replay.git(repo, 'rev-parse', 'HEAD')
    base = commit('base\n')
    commit('base\nfirst repair change\n')
    head = commit('base\nfirst repair change\nsecond repair change\n')
    tree = replay.git(repo, 'rev-parse', 'HEAD^{tree}')
    document = {'schema': 'velvet.compatibility.software.v1', 'repositories': {
        'fixture': {'commit': base, 'expected_tree': tree,
                    'repairs': [{'base_commit': base, 'commit': head, 'pr': 1}]}}}
    path = tmp_path / 'manifest.json'
    path.write_text(json.dumps(document))
    monkeypatch.setattr(replay, 'PUBLIC_REPOS', frozenset({'fixture'}))
    return path, mirror, document


def test_multi_commit_repair_is_replayed_from_explicit_base(tiny_repository, tmp_path):
    path, mirror, document = tiny_repository
    target = tmp_path / 'prepared'
    evidence = replay.prepare(path, target, mirror_root=mirror)
    expected = document['repositories']['fixture']
    assert evidence['repositories']['fixture']['tree'] == expected['expected_tree']
    assert (target / 'fixture/contract.txt').read_text() == 'base\nfirst repair change\nsecond repair change\n'
    assert replay.git(target / 'fixture', 'rev-parse', 'HEAD') == expected['commit']
    assert evidence['preparation_complete'] is True


def test_incorrect_tree_pin_fails_and_preserves_failed_input_evidence(tiny_repository, tmp_path):
    path, mirror, document = tiny_repository
    document['repositories']['fixture']['expected_tree'] = '0' * 40
    path.write_text(json.dumps(document))
    target = tmp_path / 'prepared'
    with pytest.raises(ValueError, match='pinned tree mismatch'):
        replay.prepare(path, target, mirror_root=mirror)
    evidence = json.loads((target / 'tested-inputs.json').read_text())
    assert evidence['preparation_complete'] is False
    assert evidence['repositories']['fixture']['tree'] != '0' * 40


def test_exact_override_is_candidate_and_already_present_repair_is_recorded(tiny_repository, tmp_path):
    path, mirror, document = tiny_repository
    head = document['repositories']['fixture']['repairs'][0]['commit']
    evidence = replay.prepare(path, tmp_path / 'prepared', mirror_root=mirror,
                              override='fixture=' + head)
    assert evidence['mode'] == 'candidate'
    assert evidence['repositories']['fixture']['commit'] == head
    assert evidence['repositories']['fixture']['repairs'][0]['state'] == 'already-present'
    assert json.loads(path.read_text()) == document


def test_override_requires_full_sha_before_creating_destination(tmp_path):
    path = Path(__file__).resolve().parents[1] / 'compatibility/current-2026-09-07.json'
    target = tmp_path / 'prepared'
    with pytest.raises(ValueError, match='full-commit-SHA'):
        replay.prepare(path, target, override='velvet-runtime=main')
    assert not target.exists()
