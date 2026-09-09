"""Import the explicitly prepared repositories, never incidental site packages."""
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEPS = Path(os.environ.get('VELVET_ACCEPTANCE_DEPS', str(ROOT / '.acceptance-deps')))
for name in ('velvet-runtime', 'velvet-ai-core', 'velvet-language', 'velours_library',
             'velvet-event-protocol', 'velvet-receipts', 'velvet-continuity-spine'):
    repo = DEPS / name
    if not repo.is_dir():
        raise RuntimeError('prepare exact acceptance sources first: %s' % repo)
    sys.path[:0] = [str(repo), str(repo / 'src')]
sys.path.insert(0, str(ROOT))
