"""Check archived UE asset bytes and report static symbols, without Unreal Engine.

Added for the 2026 repository preparation. This is not the 2025 experiment code.
"""
from pathlib import Path
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SYMBOLS = (
    'AddMovementInput', 'PerformMoveAction_SnapTurn', 'GripObjectByInterface',
    'DropObjectByInterface', 'AddMappingContext', 'VRGripInterface',
)


def main():
    manifest = json.loads((ROOT / 'asset_manifest.json').read_text('utf8'))
    problems, inspected = [], []
    for item in manifest['assets']:
        path = (ROOT / item['path']).resolve()
        if not path.is_relative_to(ROOT):
            raise ValueError('Manifest path leaves the repository')
        if not path.is_file():
            problems.append({'path': item['path'], 'problem': 'missing file'})
            continue
        data = path.read_bytes()
        if len(data) != item['bytes'] or hashlib.sha256(data).hexdigest() != item['sha256']:
            problems.append({'path': item['path'], 'problem': 'size or hash mismatch'})
        strings = set(s.decode('ascii') for s in re.findall(rb'[\x20-\x7e]{5,}', data))
        refs = sorted(s for s in strings if re.fullmatch(r'/Game/[A-Za-z0-9_/]+', s))
        for ref in refs:
            package = ROOT / 'unreal/Content' / ref.removeprefix('/Game/')
            if not any(package.with_suffix(ext).is_file() for ext in ('.uasset', '.umap')):
                problems.append({'path': item['path'], 'problem': 'unresolved project reference', 'reference': ref})
        inspected.append({'path': item['path'], 'bytes': len(data),
                          'symbols': [s for s in SYMBOLS if s in strings],
                          'project_references': refs})
    report = {'status': 'FAIL' if problems else 'PASS', 'files_checked': len(inspected),
              'scope': 'Static archive integrity and literal package references; no UE compilation or execution.',
              'problems': problems, 'assets': inspected}
    print(json.dumps(report, indent=2))
    return 1 if problems else 0


if __name__ == '__main__':
    sys.exit(main())
