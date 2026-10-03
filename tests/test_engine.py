from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT/"src"))
from compatibility_engine import CanonicalEngine
e=CanonicalEngine(ROOT)
assert len(e.registry)==437
assert len(e.rows)==95
assert all(len(r["states"])==437 for r in e.rows.values())
assert {s for r in e.rows.values() for s in r["states"]}=={"X","1","0","E","R","M","U","V","K","S"}
assert e.get_cell("s","phonetic.phonetic_articulatory_general.voice")=="E"
bad={"record_id":"x","subject":{"canonical_id":"not.real"},"relation":"IMPLIED","object":{"canonical_id":"phonetic.phonetic_articulatory_general.voice"},"conditions":[],"evidence":[],"sources":[],"derivation":[],"counterexamples":[],"status":"CANDIDATE","falsifier":None}
assert not e.validate_claim(bad)["valid"]
v={"record_id":"v","subject":{"canonical_id":"phonetic.phonetic_articulatory_general.voice"},"relation":"IMPLIED","object":{"canonical_id":"phonetic.phonetic_articulatory_general.strident"},"conditions":[],"evidence":[],"sources":[],"derivation":[],"counterexamples":[],"status":"VALIDATED","falsifier":None}
a=e.validate_claim(v); assert not a["valid"] and any("evidence" in x for x in a["errors"])
print("ALL TESTS PASSED")
