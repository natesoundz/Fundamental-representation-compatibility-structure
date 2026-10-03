from pathlib import Path
import base64, zlib

ROOT=Path(__file__).resolve().parent
PAIRS=[
("data/canonical_registry.json.zlib.b64","data/canonical_registry.json"),
("data/canonical_matrix.jsonl.zlib.b64","data/canonical_matrix.jsonl"),
]
for src,dst in PAIRS:
    raw=zlib.decompress(base64.b64decode((ROOT/src).read_text(encoding="ascii")))
    (ROOT/dst).write_bytes(raw)
    print(f"WROTE {dst} {len(raw)} bytes")
