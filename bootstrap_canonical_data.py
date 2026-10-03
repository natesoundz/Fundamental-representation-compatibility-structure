from pathlib import Path
import base64, zlib, hashlib

ROOT=Path(__file__).resolve().parent

def decode_one(parts, dst):
    encoded="".join((ROOT/p).read_text(encoding="ascii").strip() for p in parts)
    raw=zlib.decompress(base64.b64decode(encoded))
    expected={"data/canonical_registry.json":"8df3500fa4f1251c4adae17c7b78935c86d879cec74926515ba216df10c085b6","data/canonical_matrix.jsonl":"20955aa0a1842621312807e198d51f3df0e242e37a1e017bd08209033897ed8d"}[dst]\n    if hashlib.sha256(raw).hexdigest()!=expected: raise ValueError(f"checksum failure: {dst}")\n    (ROOT/dst).write_bytes(raw)
    print(f"WROTE {dst} {len(raw)} bytes")

decode_one(["data/canonical_registry.json.zlib.b64"],"data/canonical_registry.json")
decode_one(["data/canonical_matrix.payload.1","data/canonical_matrix.payload.2","data/canonical_matrix.payload.3a","data/canonical_matrix.payload.3b","data/canonical_matrix.payload.4"],"data/canonical_matrix.jsonl")
