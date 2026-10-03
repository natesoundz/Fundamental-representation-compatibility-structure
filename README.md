# Fundamental Representation Compatibility Structure

This repository investigates a specific architectural possibility: **an explicit character-level representation can support many simultaneous higher-order structures when the legal relationships among its representations are compiled rather than hidden inside an opaque token embedding.**

The foundation is the canonical ASCII95 workbook: 95 printable ASCII characters described through **437 explicit named representations**. Those representations include character identity, phonetic and articulatory properties, pronunciation distributions, acoustics, visual geometry and topology, orthographic position, corpus statistics, morphology, grammar, lexical relations, punctuation, programming roles, mathematical roles, contextual state, capability distributions, evidence, provenance, and source classes.

The central object of study is not any single column or any single text span. It is the **compatibility structure formed by combinations of explicit representations**.

## What the diagram shows

The architecture diagram is in:

**[EXPLICIT_CHARACTER_STRUCTURAL_NETWORK.md](EXPLICIT_CHARACTER_STRUCTURAL_NETWORK.md)**

It shows the current structural hypothesis:

```text
ASCII95 characters
        |
        v
437 explicit representations
        |
        v
character x representation states
        |
        +--------------------+
        |                    |
        v                    v
text relationships     representation relationships
        |                    |
        +---------+----------+
                  |
                  v
          compatibility structures
                  |
       +----------+-----------+
       |          |           |
       v          v           v
    phonetic   lexical     symbolic
    structures structures  structures
       |          |           |
       +----------+-----------+
                  |
                  v
        attention / resolution
                  |
                  v
      representation transition
                  |
                  v
                DeltaR
                  |
                  v
      recurring validated operator
                  |
                  v
          compiled FFN block
```

The important property is that these structures can coexist. Character-level, phonetic, word-level, morphological, visual, grammatical, mathematical, programming, and symbolic resolutions do not have to replace one another.

## Physical compatibility is a primary test case

The phonetic/articulatory portion is particularly important because many of its representations have physical constraints.

Examples include:

- voiced / unvoiced state
- tongue height
- tongue front/back position
- lip rounding
- place of articulation
- manner of articulation
- consonantal / vocalic properties
- continuancy
- nasality
- laterality
- stridency
- glottal state
- secondary articulation
- airstream
- duration
- stress and pronunciation realization

These should not be treated as unrelated labels.

A physical realization occupies a **legal combination** of states. Some combinations support one another. Some constrain the remaining possibilities. Some imply another representation. Some are mutually incompatible in a particular respect. Some are possible only under additional conditions. Some relationships are language-, context-, or realization-dependent.

For example, the canonical phonetic literature itself treats vowel height and backness as articulatory control dimensions, while work on articulatory feature structure reports interactions among voicing, place, and manner rather than complete independence. The project therefore treats the phonetic portion of the workbook as a particularly strong place to test explicit compatibility compilation.

## Critical status: the diagram is intentionally incomplete

The current diagram **does not claim to contain an exhaustive enumeration of the legal compatibility structures among all 437 representations.**

It currently defines:

1. the representation substrate;
2. the notion of legal, impossible, implied, conditional, supportive, opposing, neutral, and unresolved states;
3. the ability to form compatibility structures without requiring a fixed text span;
4. multiple possible traversal orders through the same representation field;
5. the connection from dictionary pronunciation to physical/articulatory structure;
6. simultaneous character-level and word-level composition;
7. multi-character phonetic structures;
8. boundary structures such as ASCII 32;
9. overlapping phonetic, lexical, morphological, visual, grammatical, mathematical, programming, and symbolic structures;
10. attention over explicit representation relationships;
11. representation-state transitions;
12. discovery of recurring transitions;
13. compilation of validated recurring transitions into FFN blocks or experts.

What remains incomplete is the **actual compatibility atlas**.

The project has not yet exhaustively established, for every relevant combination of the 437 explicit representations:

```text
which combinations are legal
which combinations are impossible
which combinations are conditionally legal
which states imply other states
which states exclude other states
which states constrain the range of another representation
which states are independent
which states co-vary without implication
which relationships depend on sequence
which relationships do not require textual adjacency
which relationships depend on language or pronunciation
which relationships arise only at multi-character scale
which relationships arise at word or morpheme scale
which relationships cross representation families
which transformations recur strongly enough to become operators
```

That is a major goal of this repository.

## The compatibility-atlas objective

Let the canonical explicit representation set be:

```text
R = {r1, r2, ..., r437}
```

The objective is not merely to inspect all pairs.

The objective is to discover valid structures over subsets:

```text
C = {ri, rj, rk, ...}
```

and determine the constraints governing them.

A compatibility record should ultimately be able to distinguish at least:

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

with evidence and provenance attached to every determination.

The pairwise field is only the beginning. A state may be legal pairwise but illegal when a third or fourth representation is added. Therefore the object of interest is a **constraint structure over combinations**, not merely a 437 x 437 correlation matrix.

## Compatibility does not require a predefined span

One of the central hypotheses is that a compatibility structure does not inherently require a predefined number of characters or a predefined text window.

A structure may involve:

- one character;
- two adjacent characters;
- multiple characters;
- a whole word;
- a morpheme;
- nonadjacent positions;
- a pronunciation sequence;
- a physical articulation sequence;
- a visual configuration;
- a grammatical relation;
- a mathematical or programming structure;
- or another configuration selected because its explicit representations satisfy the relevant constraints.

Text order remains available, but it is not the only traversal.

The same evidence can potentially be traversed by:

```text
character position
distance
direction
tongue height
tongue position
voicing
place
manner
duration
pronunciation
morphology
visual geometry
grammatical relation
mathematical role
programming role
compatibility strength
current relevance
unresolved discrimination
```

## Dictionary composition

A dictionary with verified pronunciation supplies a direct bridge:

```text
HEADWORD
   |
   +--> character sequence
   |
   +--> pronunciation
             |
             v
        phoneme sequence
             |
             v
     physical/articulatory states
             |
             v
     explicit compatibility structure
```

This allows a character-level system to preserve the literal sequence of characters while simultaneously constructing a word-level structure.

The word can itself label that structure:

```text
C(SAFE) <--> SAFE
```

The label is not intended to erase the underlying composition. It provides an address for a verified structure whose complete path back to characters and explicit representations remains available.

This also provides a direct way to test homophones. WRITE and RIGHT may share a pronunciation projection while remaining different complete compatibility structures because their character identities, visual states, orthographic trajectories, morphology, lexical relations, character-to-phone mappings, and other explicit representations differ.

## ASCII 32 as structural evidence

ASCII 32 is an important boundary case.

A space has no ordinary pronunciation realization, so it creates a strong discontinuity in the phonetic/articulatory structure:

```text
pronunciation-bearing structure
          |
          v
       ASCII 32
          |
     phoneme = N/A
  articulation = N/A
          |
          v
next pronunciation-bearing structure
```

But space is not an empty representation. Identity, boundary, position, orthography, visual state, contextual state, and other applicable representations remain available.

The absence of pronunciation is itself discriminating information.

Punctuation, digits, operators, brackets, delimiters, and programming symbols provide additional cases. Their dictionary names can create another bridge between symbolic characters and lexical structures:

```text
+ <--> PLUS <--> p l u s
0 <--> ZERO <--> z e r o
( <--> LEFT PARENTHESIS <--> character sequence
```

## Multi-character phonetics

Structures such as TH, CH, SH, TION, vowel combinations, suffixes, and other pronunciation-bearing sequences should initially be treated as **compositions of the fundamental character representations**.

For example:

```text
T explicit state ----+
                     +--> compatibility structure --> pronunciation realization
H explicit state ----+
```

The canonical workbook should be expanded only when evidence shows that an important phenomenon cannot be represented compositionally by the existing explicit dimensions.

## Connection to FFN construction

Compatibility structures are also potential sources of computation.

For an observed transformation:

```text
R(before) --> R(after)
```

define:

```text
DeltaR = R(after) - R(before)
```

Then identify which representations were promoted, demoted, or preserved.

If the same distinguishable transformation recurs across verified dictionary or corpus evidence, it can become a candidate operator:

```text
evidence
   |
   v
explicit state transitions
   |
   v
recurring transformation
   |
   v
falsification / validation
   |
   v
compiled FFN block
```

This means FFN blocks or experts can potentially be **derived from recurrent paths through explicit representation space**, rather than being divided into arbitrary expert categories beforehand.

## Research program

The immediate research program is therefore:

```text
CANONICAL 437 REPRESENTATIONS
            |
            v
identify representation families
            |
            v
compile known physical / logical constraints
            |
            v
connect dictionary pronunciation evidence
            |
            v
enumerate observed compatibility structures
            |
            v
test legal / impossible / conditional combinations
            |
            v
discover higher-order constraints
            |
            v
index verified structures
            |
            v
measure recurrence across corpus / dictionary
            |
            v
discover useful traversal paths
            |
            v
identify recurring state transformations
            |
            v
compile validated operators / FFN blocks
            |
            v
test whether higher symbolic structures emerge
without discarding character-level provenance
```

The repository should therefore be read as an attempt to **map the compatibility structure of the canonical explicit representation space**, not as a claim that this map is already complete.

The architecture diagram defines the framework. The next scientific task is to uncover, verify, record, and compile the actual compatibility structures.
