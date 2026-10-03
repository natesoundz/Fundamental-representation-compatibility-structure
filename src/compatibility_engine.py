"""Canonical compatibility substrate, auditor, store and query engine."""
from __future__ import annotations
import json, base64, zlib
from pathlib import Path

RELATIONS={"LEGAL","IMPOSSIBLE","CONDITIONAL","IMPLIED","EXCLUDED","SUPPORTIVE","OPPOSING","NEUTRAL","INDEPENDENT","UNRESOLVED","DERIVED","CONTEXT_DEPENDENT","SEQUENCE_DEPENDENT","LANGUAGE_DEPENDENT"}
STATUSES={"CANDIDATE","SUPPORTED","VALIDATED","REJECTED","UNRESOLVED"}
CELL_STATES={"X","1","0","E","R","M","U","V","K","S"}

def _ensure_data(root):
    specs=[
        (["canonical_registry.json.zlib.b64"],"canonical_registry.json"),
        (["canonical_matrix.payload.1","canonical_matrix.payload.2","canonical_matrix.payload.3a","canonical_matrix.payload.3b","canonical_matrix.payload.4"],"canonical_matrix.jsonl"),
    ]
    for parts,dst in specs:
        out=root/"data"/dst
        if not out.exists():
            encoded="".join((root/"data"/p).read_text(encoding="ascii").strip() for p in parts)
            raw=zlib.decompress(base64.b64decode(encoded))
            out.write_bytes(raw)

class CanonicalEngine:
    def __init__(self, root):
        self.root=Path(root); _ensure_data(self.root)
        reg=json.loads((self.root/"data/canonical_registry.json").read_text(encoding="utf-8"))
        if reg.get("representation_count")!=437 or len(reg.get("representations",[]))!=437:
            raise ValueError("canonical registry invariant failed")
        self.registry={r["canonical_id"]:r for r in reg["representations"]}
        self.index={r["canonical_id"]:int(r["index"])-1 for r in reg["representations"]}
        self.rows={}
        for line in (self.root/"data/canonical_matrix.jsonl").read_text(encoding="utf-8").splitlines():
            if line.strip():
                row=json.loads(line)
                if len(row["states"])!=437: raise ValueError("matrix row width invariant failed")
                self.rows[int(row["ascii_dec"])]=row
        if set(self.rows)!=set(range(32,127)): raise ValueError("ASCII95 row invariant failed")
        observed={s for r in self.rows.values() for s in r["states"]}
        if not observed<=CELL_STATES: raise ValueError(f"unknown cell states: {observed-CELL_STATES}")

    def get_representation(self, canonical_id):
        return self.registry.get(canonical_id)

    def get_cell(self, character, canonical_id):
        if len(character)!=1: raise ValueError("character must be exactly one printable ASCII character")
        code=ord(character)
        if code not in self.rows: raise ValueError("character outside printable ASCII 0x20..0x7E")
        if canonical_id not in self.index: raise KeyError(canonical_id)
        return self.rows[code]["states"][self.index[canonical_id]]

    def validate_claim(self, claim):
        errors=[]; warnings=[]
        required={"record_id","subject","relation","object","conditions","evidence","sources","derivation","counterexamples","status","falsifier"}
        missing=sorted(required-set(claim))
        rel=claim.get("relation"); status=claim.get("status")
        if rel is not None and rel not in RELATIONS: errors.append(f"noncanonical relation: {rel}")
        if status is not None and status not in STATUSES: errors.append(f"invalid status: {status}")
        for side in ("subject","object"):
            ep=claim.get(side)
            if not isinstance(ep,dict) or not ep.get("canonical_id"):
                errors.append(f"{side} must contain canonical_id"); continue
            cid=ep["canonical_id"]
            if cid not in self.registry:
                errors.append(f"{side} canonical_id not in registry: {cid}"); continue
            ch=ep.get("character")
            if ch is not None:
                try: state=self.get_cell(ch,cid)
                except Exception as e: errors.append(f"{side}: {e}"); continue
                if state=="X": errors.append(f"{side} addresses canonical X: {ch!r} x {cid}")
                elif state=="E": warnings.append(f"{side} is deferred and requires context/source resolution")
                elif state in {"R","M","U","S"}: warnings.append(f"{side} cell state {state} is not a primitive free coordinate")
        if status in {"SUPPORTED","VALIDATED"} and not claim.get("evidence"):
            errors.append(f"{status} claim requires evidence")
        if status=="VALIDATED" and not claim.get("sources"):
            errors.append("VALIDATED claim requires provenance sources")
        if status=="VALIDATED" and claim.get("falsifier") is None:
            errors.append("VALIDATED claim requires an explicit falsifier")
        return {"valid":not errors and not missing,"errors":errors,"warnings":warnings,"missing_fields":missing}

    def iter_edges(self):
        p=self.root/"data/compatibility_edges.jsonl"
        if not p.exists(): return
        for line in p.read_text(encoding="utf-8").splitlines():
            if line.strip(): yield json.loads(line)

    def query_relationship(self, subject_id, object_id, include_rejected=False):
        return [r for r in (self.iter_edges() or []) if r["subject"]["canonical_id"]==subject_id and r["object"]["canonical_id"]==object_id and (include_rejected or r["status"]!="REJECTED")]

    def explain_status(self, record_id):
        for r in self.iter_edges() or []:
            if r["record_id"]==record_id:
                return {k:r[k] for k in ("record_id","status","relation","conditions","evidence","sources","derivation","counterexamples","falsifier")}
        return None

    def submit_claim(self, claim, persist=False):
        audit=self.validate_claim(claim)
        if persist:
            if not audit["valid"]: raise ValueError(json.dumps(audit,indent=2))
            with (self.root/"data/compatibility_edges.jsonl").open("a",encoding="utf-8") as f:
                f.write(json.dumps(claim,ensure_ascii=False,separators=(",",":"))+"\n")
        return audit
