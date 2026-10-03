from pathlib import Path
import argparse, json
from compatibility_engine import CanonicalEngine
def main():
    p=argparse.ArgumentParser(); p.add_argument("--root",default=str(Path(__file__).resolve().parents[1]))
    s=p.add_subparsers(dest="cmd",required=True)
    a=s.add_parser("representation"); a.add_argument("canonical_id")
    a=s.add_parser("cell"); a.add_argument("character"); a.add_argument("canonical_id")
    a=s.add_parser("validate"); a.add_argument("claim_json")
    a=s.add_parser("query"); a.add_argument("subject"); a.add_argument("object")
    a=s.add_parser("explain"); a.add_argument("record_id")
    x=p.parse_args(); e=CanonicalEngine(x.root)
    if x.cmd=="representation": out=e.get_representation(x.canonical_id)
    elif x.cmd=="cell": out={"state":e.get_cell(x.character,x.canonical_id)}
    elif x.cmd=="validate": out=e.validate_claim(json.loads(Path(x.claim_json).read_text()))
    elif x.cmd=="query": out=e.query_relationship(x.subject,x.object)
    else: out=e.explain_status(x.record_id)
    print(json.dumps(out,indent=2,ensure_ascii=False))
if __name__=="__main__": main()
