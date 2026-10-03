# Compatibility Engine

This branch is the executable infrastructure layer for the Fundamental Representation Compatibility Structure.

## Canonical separation

1. Canonical registry: exact 437 representation columns and workbook metadata.
2. Canonical matrix: exact 95 x 437 cell-state payload.
3. Relationship schema: allowed claim contract.
4. Compatibility edges: initially empty. No relationship is invented or silently imported.
5. Validator/query engine: audits claims against the canonical substrate.

The canonical registry and matrix are stored losslessly as zlib+base64 source payloads because GitHub connector writes are text-only. `bootstrap_canonical_data.py` reconstructs the literal `data/canonical_registry.json` and `data/canonical_matrix.jsonl` files byte-for-byte. The runtime performs the same reconstruction automatically when those materialized files are absent.

## Invariants

- Registry != matrix != compatibility atlas.
- X is impossible/ineligible, not merely unobserved.
- E remains deferred until context/source resolution.
- R, M, U, and S are not silently converted into primitive numeric coordinates.
- A model or external source may propose a claim; plausibility alone never promotes it to project knowledge.
- SUPPORTED and VALIDATED require evidence.
- VALIDATED additionally requires provenance sources and an explicit falsifier.
- No Claude, Meta, phonetic, or other external results are preloaded into compatibility_edges.jsonl.
- The workbook serializes the canonical substrate only; it is not evidence for new compatibility edges.

## Relationship vocabulary

LEGAL, IMPOSSIBLE, CONDITIONAL, IMPLIED, EXCLUDED, SUPPORTIVE, OPPOSING, NEUTRAL, INDEPENDENT, UNRESOLVED, DERIVED, CONTEXT_DEPENDENT, SEQUENCE_DEPENDENT, LANGUAGE_DEPENDENT.

## API

- get_representation(id)
- get_cell(character, id)
- validate_claim(claim)
- submit_claim(claim, persist=False)
- query_relationship(A, B)
- explain_status(record_id)

Discovery, contrast mining, active discrimination, and MCP transport can be layered on this contract without changing the canonical substrate.
