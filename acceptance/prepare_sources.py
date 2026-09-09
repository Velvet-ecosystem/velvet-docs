"""Reproduce exact public software inputs; never modify an existing checkout.

Accepted, unmerged repairs are explicit commit overlays. The resulting Git tree
is verified in pinned mode and recorded in candidate mode. No branch is merged,
no commit is authored, and no failed candidate updates the reviewed manifest.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

PUBLIC_REPOS = frozenset({
    'velvet-runtime', 'velvet-ai-core', 'velvet-language', 'velours_library',
    'velvet-event-protocol', 'velvet-receipts', 'velvet-continuity-spine',
    'velvet-interface', 'velvet-audio-studio', 'velvet-communications',
    'velvet-vehicle-can',
})
SHA = re.compile(r'^[0-9a-f]{40}$')


def git(path, *args, input_bytes=None, raw=False):
    output = subprocess.run(
        ['git', '-C', str(path)] + list(args), input=input_bytes,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True,
        timeout=180,
    ).stdout
    return output if raw else output.decode('utf-8').strip()


def validate_manifest(document):
    if document.get('schema') != 'velvet.compatibility.software.v1':
        raise ValueError('unsupported compatibility manifest')
    repos = document.get('repositories')
    if not isinstance(repos, dict) or set(repos) != PUBLIC_REPOS:
        raise ValueError('manifest must name the complete explicit public set')
    for name, entry in repos.items():
        for field in ('commit', 'expected_tree'):
            if not isinstance(entry.get(field), str) or not SHA.fullmatch(entry[field]):
                raise ValueError('%s requires an exact %s SHA' % (name, field))
        overlays = entry.get('repairs')
        if (not isinstance(overlays, list) or len(overlays) > 8
                or any(not isinstance(item, dict) or any(
                    not isinstance(item.get(field), str) or not SHA.fullmatch(item[field])
                    for field in ('commit', 'base_commit')) for item in overlays)
                or len({item['commit'] for item in overlays}) != len(overlays)):
            raise ValueError('repairs must name bounded unique exact base/head commit pairs')
    return document


def prepare(manifest, destination, *, candidate=False, mirror_root=None, override=None):
    document = validate_manifest(json.loads(Path(manifest).read_text(encoding='utf-8')))
    destination = Path(destination)
    # Refuse before any work if a target exists. No reset/clean/delete of user work.
    if destination.exists():
        raise ValueError('dependency destination must not exist')
    if override is not None:
        name, separator, sha = override.partition('=')
        if not separator or name not in PUBLIC_REPOS or not SHA.fullmatch(sha):
            raise ValueError('override must be a known repository=full-commit-SHA')
    destination.mkdir(parents=True)
    evidence = {'schema': 'velvet.compatibility.tested-inputs.v1',
                'mode': 'candidate' if candidate or override else 'pinned',
                'source_manifest': str(manifest), 'repositories': {},
                'authority': 'none', 'hardware_acceptance': False,
                'preparation_complete': False}
    output = destination / 'tested-inputs.json'
    try:
        for name, entry in document['repositories'].items():
            checkout = destination / name
            selected = entry['commit']
            if mirror_root:
                git(Path(mirror_root) / name, 'worktree', 'add', '--detach',
                    str(checkout.resolve()), selected)
            else:
                checkout.mkdir()
                git(checkout, 'init', '--quiet')
                git(checkout, 'remote', 'add', 'origin',
                    'https://github.com/Velvet-ecosystem/%s.git' % name)
            if candidate:
                # Resolve the moving default once, then use only the resolved SHA.
                git(checkout, 'fetch', '--depth=1', 'origin', 'main')
                selected = git(checkout, 'rev-parse', 'FETCH_HEAD')
            if override and name == override.split('=')[0]:
                selected = override.split('=')[1]
            try:
                git(checkout, 'cat-file', '-e', selected + '^{commit}')
            except subprocess.CalledProcessError:
                git(checkout, 'fetch', '--depth=1', 'origin', selected)
            git(checkout, 'checkout', '--detach', selected)
            record = {'commit': selected, 'repairs': [], 'tree': None}
            evidence['repositories'][name] = record
            for repair in entry['repairs']:
                for sha in (repair['base_commit'], repair['commit']):
                    try:
                        git(checkout, 'cat-file', '-e', sha + '^{commit}')
                    except subprocess.CalledProcessError:
                        git(checkout, 'fetch', '--depth=1', 'origin', sha)
                patch = git(checkout, 'diff', '--binary', repair['base_commit'], repair['commit'], raw=True)
                try:
                    git(checkout, 'apply', '--reverse', '--check', '-', input_bytes=patch)
                    state = 'already-present'
                except subprocess.CalledProcessError:
                    git(checkout, 'apply', '--index', '--3way', '-', input_bytes=patch)
                    state = 'applied'
                record['repairs'].append(dict(repair, state=state))
            record['tree'] = git(checkout, 'write-tree')
            if not candidate and not override and record['tree'] != entry['expected_tree']:
                raise ValueError('pinned tree mismatch: %s' % name)
        evidence['preparation_complete'] = True
    finally:
        output.write_text(json.dumps(evidence, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    return evidence


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--manifest', default='compatibility/current-2026-09-07.json')
    parser.add_argument('--destination', required=True)
    parser.add_argument('--candidate', action='store_true')
    parser.add_argument('--mirror-root', type=Path)
    parser.add_argument('--override', help='known-public-repository=full-commit-SHA')
    args = parser.parse_args()
    try:
        result = prepare(args.manifest, args.destination, candidate=args.candidate,
                         mirror_root=args.mirror_root, override=args.override)
    except subprocess.CalledProcessError as exc:
        print(exc.stderr.decode('utf-8', errors='replace'), file=sys.stderr)
        raise SystemExit(exc.returncode)
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
