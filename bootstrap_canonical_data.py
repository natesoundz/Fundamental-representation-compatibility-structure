from pathlib import Path
import base64, zlib

ROOT=Path(__file__).resolve().parent

def decode_one(parts, dst):
    encoded="".join((ROOT/p).read_text(encoding="ascii").strip() for p in parts)
    raw=zlib.decompress(base64.b64decode(encoded))
    (ROOT/dst).write_bytes(raw)
    print(f"WROTE {dst} {len(raw)} bytes")

decode_one(["data/canonical_registry.json.zlib.b64"],"data/canonical_registry.json")
decode_one(["data/canonical_matrix.jsonl.zlib.b64.part1","data/canonical_matrix.jsonl.zlib.b64.part2"],"data/canonical_matrix.jsonl")
