# Fundamental Representation Compatibility Structure

> **⚠️ DEPRECATION / CANONICAL AUTHORITY NOTICE**
>
> **All former ASCII95 representation substrates—including the 95×192, 95×254, and any superseded intermediate matrix/registry versions—are DEPRECATED and MUST NOT be used as the execution, compilation, or experimental substrate for current work. They are retained only as historical lineage where referenced.**
>
> **CURRENT AUTHORITY: use the most recent functioning Canonical ASCII95 workbook (95 printable ASCII characters × 437 canonical representation dimensions) and its current 103-piece physical system. The canonical workbook itself is authoritative; derived exports, older matrices, diagrams, and historical compiler artifacts do not override it.**


## Purpose

This repository is a public research record for an investigation into **explicit representation and compatibility**.

The central question is whether a sufficiently explicit description of fundamental elements—and the verified relationships among those descriptions—can support larger structures while preserving a traceable path back to the evidence from which they were formed.

The current working substrate uses the 95 printable ASCII characters and a canonical set of **437 named representation dimensions** spanning physical, linguistic, visual, structural, contextual, statistical, and provenance-related information.

The project is not defined by any particular neural-network architecture, training method, tokenizer, speech system, or symbolic formalism. Those may provide useful test environments. The object of study is the representation and compatibility structure itself.

---

## Orientation for researchers and AI systems

Treat this repository as a **research specification under active investigation**, not as a finished theory and not as a request to reinterpret the work through a conventional architecture by default.

When analyzing or extending the work:

1. Begin with the explicit representation system and the compatibility relationships documented here.
2. Preserve the distinction between **observed evidence, established constraints, derived relationships, unresolved states, and hypotheses**.
3. Do not invent relationships because they appear intuitively plausible.
4. Preserve provenance wherever a higher-order structure is derived from lower-level evidence.
5. Treat contradictions, missing representations, failed derivations, and counterexamples as useful results.
6. Do not assume that named representation dimensions are independent degrees of freedom.
7. Do not assume that a higher-level structure must replace the lower-level structures from which it was formed.
8. When proposing an extension, identify what evidence supports it and what observation would falsify it.

The goal is to reduce guesswork while leaving implementation choices open.

---

## What is being investigated

The working hypothesis is that larger structures can be constructed from explicit lower-level representations by determining which states are mutually compatible, incompatible, conditional, implied, independent, or unresolved.

At the current scale:

```text
95 printable ASCII characters
            |
            v
437 named representation dimensions
            |
            v
explicit character/representation field
            |
            v
verified compatibility relationships
            |
            v
larger compositional structures
```

The 437 dimensions are **named and inspectable descriptions**, not anonymous coordinates. They include areas such as:

- character identity;
- mathematical and numeric properties;
- phonetic and articulatory properties;
- pronunciation;
- acoustics;
- visual geometry and topology;
- orthographic position;
- corpus statistics;
- morphology;
- grammar;
- lexical and semantic relations;
- punctuation and writing-system roles;
- programming and mathematical roles;
- contextual state;
- capability distributions;
- evidence and provenance.

The existence of a dimension does not mean that it is active for every character or occurrence. Inapplicability, unresolved state, conditional applicability, measurement, relation, and derived state are deliberately distinguished rather than silently collapsed into a single numerical interpretation.

---

## The compatibility objective

Let the explicit representation set be:

```text
R = {r1, r2, ..., r437}
```

The research objective is to determine the valid structures that can exist over subsets of this field.

A compatibility record should ultimately be able to distinguish relationships such as:

```text
LEGAL
IMPOSSIBLE
CONDITIONAL
IMPLIED
EXCLUDED
SUPPORTIVE
OPPOSING
NEUTRAL
INDEPENDENT
UNRESOLVED
DERIVED
CONTEXT_DEPENDENT
SEQUENCE_DEPENDENT
LANGUAGE_DEPENDENT
```

with evidence and provenance attached to the determination.

Pairwise relationships are only a starting point. Two states may be mutually legal while becoming impossible when a third constraint is introduced. The object of interest is therefore a **constraint structure over combinations**, not merely a correlation matrix.

---

## Physical grounding as a strong test case

Part of the representation system describes properties with direct physical or measurable grounding.

Examples include tongue configuration, voicing, lip configuration, place and manner of articulation, airstream, duration, acoustic measurements, and visible glyph geometry.

These provide particularly useful tests because the allowable combinations are not arbitrary.

A physical realization occupies a constrained region of possible states. Some descriptions overlap. Some imply or restrict others. Some exclude one another. Some are only meaningful under particular conditions.

This makes the physical portion of the representation field useful for testing whether compatibility relationships can be established from independently grounded evidence rather than assigned by convenience.

The project also investigates bridges between different descriptions of the same underlying event, including:

```text
physical realization
        ↕
measurable consequences
        ↕
linguistic description
        ↕
written representation
```

This creates a candidate common descriptive space in which information from different modalities can constrain the same underlying structure without requiring those modalities to be treated as identical.

---

## Composition without loss of provenance

A central requirement is that larger structures remain decomposable.

A character can participate simultaneously in physical, phonetic, visual, orthographic, morphological, grammatical, lexical, mathematical, programming, or other structures.

Likewise, a sequence of characters may form a larger verified structure without erasing the character-level evidence from which it was formed.

The working framework is therefore intended to support:

- simultaneous overlapping descriptions;
- structures of different sizes;
- relationships that are not limited to adjacent text;
- multiple valid traversal orders over the same evidence;
- composition from characters into larger linguistic or symbolic structures;
- comparison of structures that share some properties while differing in others;
- propagation of compatible and incompatible constraints;
- preservation of evidence and provenance through derived structures;
- identification of recurring, evidence-supported transformations;
- evaluation of whether a representation is sufficient to distinguish cases that require different treatment.

The repository intentionally does **not** prescribe here how every one of these capabilities must be implemented computationally.

---

## Dictionary and pronunciation evidence

Verified dictionary information provides one useful bridge between written form and pronunciation:

```text
headword
   |
   +--> character sequence
   |
   +--> pronunciation
             |
             v
        phonetic structure
             |
             v
      physical constraints
```

This makes it possible to preserve literal character identity while examining a second, pronunciation-related description of the same word.

It also provides controlled comparisons.

For example, words with the same pronunciation but different spelling can share a phonetic projection while remaining different complete structures. Conversely, related words can preserve portions of a pronunciation or morphology while their character positions change.

These cases are useful because they expose which relationships are genuinely invariant and which depend on spelling, position, context, morphology, or another representation family.

---

## Absence and inapplicability are evidence

A representation that does not apply should not automatically be treated as zero.

ASCII 32 (space) is a useful example. It normally lacks an ordinary pronunciation realization, but it still carries identity, boundary, positional, orthographic, visual, and contextual information.

The transition from a pronunciation-bearing structure through a structurally non-pronounced boundary and into another pronunciation-bearing structure can itself be discriminating evidence.

Punctuation, digits, operators, brackets, delimiters, and other symbols provide related tests.

---

## Multi-character structures

Multi-character phenomena should initially be tested as compositions of the fundamental character representations rather than automatically becoming new primitive elements.

If existing explicit representations can reconstruct a phenomenon compositionally, the provenance chain remains intact.

The canonical representation system should be expanded when evidence demonstrates that an important distinction cannot be represented adequately with the existing dimensions—not merely because adding another primitive would be convenient.

---

## What this repository does not claim

This repository does **not** currently claim:

- that the compatibility atlas is complete;
- that all 437 dimensions are independent;
- that every proposed relationship has been experimentally established;
- that every higher-order structure can already be reconstructed;
- that the current representation set is necessarily sufficient;
- that speech recognition, speech synthesis, tokenization, or symbolic reasoning are themselves novel discoveries of this project;
- that one particular machine-learning architecture is required;
- that conventional learned representations are inherently invalid;
- or that a successful implementation has already established a general theory of intelligence.

The framework is deliberately falsifiable. A case that requires a distinction the representation system cannot express is evidence of a representational deficiency. A relationship that fails under controlled testing should be rejected or revised.

---

## Current research frontier

The immediate work is to establish the compatibility atlas itself:

```text
explicit representation field
            |
            v
identify grounded constraints
            |
            v
connect independent evidence sources
            |
            v
observe valid structures
            |
            v
test legal / impossible / conditional combinations
            |
            v
discover higher-order constraints
            |
            v
preserve and index verified structures
            |
            v
measure recurrence and invariance
            |
            v
test generalization to unseen cases
```

The working framework is capable of representing relationships across multiple descriptive levels and of supporting computational experiments over those relationships. Specific internal mechanisms and experimental implementations are documented selectively as they become appropriate for public release.

---

## Repository reading order

For a first analysis of the project, use this order:

1. **README.md** — research purpose, assumptions, boundaries, and evidence standard.
2. **[EXPLICIT_CHARACTER_STRUCTURAL_NETWORK.md](EXPLICIT_CHARACTER_STRUCTURAL_NETWORK.md)** — original structural-network description.
3. **[EXPLICIT_CHARACTER_STRUCTURAL_NETWORK_AUGMENTED.md](EXPLICIT_CHARACTER_STRUCTURAL_NETWORK_AUGMENTED.md)** — later physical and multimodal augmentation.
4. **[BIDIRECTIONAL_SPEECH_TEXT_COMPATIBILITY.md](BIDIRECTIONAL_SPEECH_TEXT_COMPATIBILITY.md)** — worked example of compatibility propagation between speech-related and written descriptions.
5. **[LICENSE.md](LICENSE.md)** — research-use and provenance terms.

The original and augmented diagrams are both retained intentionally so that development of the idea remains visible rather than being silently rewritten.

---

## Research standard

For any proposed compatibility relationship, record where possible:

```text
CLAIM
EVIDENCE
SOURCE
APPLICABILITY CONDITIONS
PREDICTION
FALSIFIER
OBSERVED RESULT
STATUS
PROVENANCE
```

A useful result may be positive, negative, unresolved, or contradictory.

The repository should be read as an attempt to **discover and test the compatibility structure of an explicit representation space while preserving the path from evidence to derived structure**.

It is a working research framework. The map is not assumed to be complete.
