# Explicit Character / Structural Network

This document codifies the architecture in which ASCII95 remains the invariant character substrate while multiple overlapping structural resolutions are compiled from the canonical 437 explicit representations.

## Core invariant

Nothing at a higher structural level replaces the character-level representation.

A word, phonetic span, morpheme, operator, boundary, grammatical structure, or later symbolic object is a configuration over the explicit substrate. Every higher structure retains a path back through its compatibility relations to explicit representation occurrences and ultimately to ASCII95.

## Configuration diagram

```text
================================================================================
                 EXPLICIT CHARACTER / STRUCTURAL NETWORK
================================================================================

                         +-----------------------------+
                         |       ASCII95 SUBSTRATE     |
                         | 95 printable characters     |
                         | ASCII 32 ... ASCII 126      |
                         +--------------+--------------+
                                        |
                                        v
                  +------------------------------------------+
                  |      CANONICAL 437 REPRESENTATIONS       |
                  | identity / phonetic / articulatory       |
                  | visual / acoustic / orthographic         |
                  | positional / morphology / grammar        |
                  | semantic / punctuation / programming     |
                  | mathematical / contextual / capability   |
                  | evidence / provenance / source class     |
                  +-------------------+----------------------+
                                      |
                                      v
                    CHARACTER x REPRESENTATION FIELD
                       95 x 437 = 41,515 addresses
                         (character, representation)
                                      |
                                      v
                          OCCURRENCE AT POSITION p
                                      |
                                      v
                  +----------------------------------+
                  | R[p] = 437-D explicit state     |
                  | support / oppose / neutral      |
                  | eligible / impossible           |
                  | relational / measurement        |
                  | contextual / resolved           |
                  +----------------+-----------------+
                                   |
                 +-----------------+------------------+
                 |                                    |
                 v                                    v
        TEXTUAL COORDINATE                  REPRESENTATION COORDINATE
        p0 -> p1 -> p2 -> ...               voiced / unvoiced
        distance / direction                tongue height/backness
        adjacency / boundaries              rounding / place / manner
        left/right                          duration / morphology
                 |                          visual / syntax / ...
                 +-----------------+------------------+
                                   |
                                   v
================================================================================
                       COMPATIBILITY MECHANISM
================================================================================

Compatibility is not intrinsically defined by a fixed text span.

     adjacent positions ----+
                            +----> COMPATIBILITY(Ri,Rj)
     distant positions -----+

Selection may be driven by:
  text distance
  representation compatibility
  physical compatibility
  pronunciation compatibility
  morphology
  structural relationship
  current relevance
  current unresolved question

The same evidence can therefore be traversed in multiple orders:

  TEXT ORDER       PHONETIC ORDER        RELEVANCE ORDER
  p0               close                 strongest evidence
  p1               near-close            next strongest
  p2               close-mid             ...
  p3               mid
  ...              open-mid
                   near-open
                   open

Additional traversals can use tongue position, voicing, manner,
morphology, visual structure, compatibility, or any explicit relation.

================================================================================
                    PHYSICAL COMPATIBILITY NETWORK
================================================================================

  tongue height -----+
  tongue position ---|
  rounding ----------|
  voicing -----------+----> LEGAL PHONETIC STATE
  place -------------|
  manner ------------|
  duration ----------+

437 explicit representations are not 437 independent degrees of freedom.

Known representation states constrain:
    implied states
    remaining legal states
    impossible states

The legal state field is a constrained subset of the nominal 437-D space.
Resolution can therefore propagate through compatibility relations.

================================================================================
                         DICTIONARY / LEXICON
================================================================================

                         HEADWORD
                            |
              +-------------+-------------+
              |                           |
              v                           v
       CHARACTER SEQUENCE           PRONUNCIATION(S)
              |                           |
              |                           v
              |                    PHONEME SEQUENCE
              |                           |
              |                           v
              |                 PHYSICAL REALIZATION
              |                           |
              +-------------+-------------+
                            |
                            v
                  EXPLICIT REPRESENTATION STATES
                            |
                            v
                    COMPATIBILITY STRUCTURE

For w = c1 c2 ... cn:

  C(w) = [R(c1), R(c2), ... R(cn)]
         + verified relationships among those states

The literal dictionary headword can label the compiled structure:

                       C(SAFE) <----> SAFE

No opaque word-token ID is required.

================================================================================
                    WORD TOKEN FROM CHARACTERS
================================================================================

               s       a       f       e
               |       |       |       |
              437     437     437     437
               |       |       |       |
               +-------+---+---+-------+
                           |
                           v
                 compatibility closure
                           |
                           v
                        [SAFE]

Both resolutions coexist:

       s -> a -> f -> e   <---->   [SAFE]

A word token is a verified composite character structure, not an
indivisible replacement for its characters.

================================================================================
                     MULTI-CHARACTER PHONETICS
================================================================================

The same mechanism handles multi-character pronunciation structures:

  T + H
  C + H
  S + H
  T + I + O + N
  vowel combinations
  suffix structures
  other pronunciation spans

Example:

       R(T)                 R(H)
        |                    |
        +---------+----------+
                  |
                  v
          compatibility structure
                  |
                  v
        pronunciation realization

T and H remain independently addressable.

A new phenomenon does not automatically require a new canonical column.
If the existing 437 representations express it compositionally, compile
the structure. Expand the canonical representation set only when evidence
shows a genuinely missing kind of representation.

================================================================================
                         ASCII 32 - SPACE
================================================================================

                 PRONOUNCED WORD
                       |
                       v
                PHONETIC STRUCTURE
                       |
                       v
                +--------------+
                |   ASCII 32   |
                |    SPACE     |
                +--------------+
                       |
             pronunciation = N/A
             phoneme       = N/A
             articulation  = N/A
                       |
                       v
             COMPLETE PHONETIC BREAK
                       |
                       v
                 NEXT WORD BEGINS

Example:

   u n s a f e   [32]   s a f e t y
   +----------+         +-----------+
        |                    |
     [UNSAFE]              [SAFETY]

ASCII 32 is not "nothing." Its lack of pronunciation is structurally
informative while identity, positional, orthographic, boundary,
contextual, and other applicable representations remain available.

Punctuation, operators, delimiters, digits, mathematical symbols, and
programming symbols can create related but distinguishable structures.

================================================================================
                    SYMBOL <-> WORD CONNECTION
================================================================================

  ASCII SYMBOL                         DICTIONARY STRUCTURE

       +          <----------------->       PLUS
       -          <----------------->       MINUS / HYPHEN / NEGATION
       0          <----------------->       ZERO
       7          <----------------->       SEVEN
       (          <----------------->       LEFT PARENTHESIS

Context resolves cases with multiple lexical/functional realizations.

Dictionary labels themselves return to the same substrate:

       +  <->  PLUS  <->  p l u s  <-> explicit character representations

================================================================================
                         HOMOPHONES
================================================================================

              WRITE                         RIGHT
                |                             |
                v                             v
        complete explicit              complete explicit
            structure                      structure
                |                             |
                +-------------+---------------+
                              |
                              v
                    pronunciation projection
                              |
                              v
                         SAME SOUND

pronunciation(WRITE) = pronunciation(RIGHT)
does not imply C(WRITE) = C(RIGHT).

Character identity, glyph geometry, orthography, character-phone
alignment, morphology, lexical relations, contextual states, and the
complete explicit trajectories remain distinguishable.

================================================================================
                  MULTIPLE TOKEN SYSTEMS AT ONCE
================================================================================

                        RAW CHARACTERS
                             |
                             v
                     EXPLICIT 437 FIELD
                             |
        +------------+-------+--------+---------------+
        |            |       |        |               |
        v            v       v        v               v
     PHONETIC      VISUAL   MORPH.   LEXICAL      MATH/PROGRAM
     STRUCTURES   STRUCT.  STRUCT.   STRUCT.       STRUCTURES
        |            |       |        |               |
        +------------+-------+--------+---------------+
                             |
                             v
                    OVERLAPPING STRUCTURES

One occurrence can simultaneously belong to character, phonetic, visual,
morpheme, word, grammatical, mathematical, and programming structures.

There is no invariant requirement that one position equal one token.

================================================================================
                    GENERAL STRUCTURAL TOKEN
================================================================================

A structural token contains:

  participating character occurrences
  participating explicit representations
  compatibility constraints
  ordering/traversal
  support relationships
  opposing relationships
  provenance/evidence

It does not inherently require:
  fixed character count
  fixed text window
  contiguous positions
  predefined tokenizer unit

It requires a satisfied structure.

================================================================================
                       ATTENTION CONNECTION
================================================================================

Each occurrence begins with:

                    R[p] in R^437
                         |
                         v
                       Q / K / V

Q = what relationships need resolving
K = what this occurrence can be matched on
V = what explicit information it contributes

                         Q
                         |
                         v
              representation question
                         |
                         v
              compatibility search
                         |
             +-----------+-----------+
             |                       |
             v                       v
       TEXT NEIGHBORS         REPRESENTATION NEIGHBORS
             |                       |
             +-----------+-----------+
                         |
                         v
                     ATTENTION
                         |
                         v
                 SELECTED EVIDENCE

Possible explicit-column architecture:

 representation 1   -> attention_1   --+
 representation 2   -> attention_2     |
 representation 3   -> attention_3     +--> GQA / integration --> residual
 ...
 representation 437 -> attention_437 --+

================================================================================
                      FFN / EXPERT CREATION
================================================================================

Observe actual transitions through representation space:

        R(before) --> computation --> R(after)

        DeltaR = R(after) - R(before)

Interpret:
  DeltaR[k] > 0  representation promoted
  DeltaR[k] < 0  representation demoted
  DeltaR[k] ~= 0 representation preserved

Across dictionary and corpus:

  occurrence 1 -> DeltaR1
  occurrence 2 -> DeltaR2
  occurrence 3 -> DeltaR3
  ...
                    |
                    v
             recurring transition?
              /             \
            no               yes
            |                 |
            v                 v
      retain evidence   candidate operator
                              |
                              v
                         falsification
                              |
                              v
                           recurrence
                              |
                              v
                      COMPILED FFN BLOCK

================================================================================
                    REPRESENTATION-DERIVED MoE
================================================================================

                       CURRENT STATE R
                             |
                             v
                  compatibility structure
                             |
                             v
                     applicable operators
                             |
           +-----------------+-----------------+
           |                 |                 |
           v                 v                 v
        FFN_A             FFN_B             FFN_C
     pronunciation      morphology          boundary
      resolution      transformation      transformation
           |                 |                 |
           +-----------------+-----------------+
                             |
                             v
                        composed DeltaR
                             |
                             v
                          R(next)

Experts are derived from:

 evidence
   -> explicit state transitions
   -> recurring transformation
   -> validated operator
   -> FFN block

Each block can retain input conditions, representations used,
promotions, demotions, invariants, evidence counts, source records,
exceptions, and falsifiers.

================================================================================
                  LAYERS = SUCCESSIVE RESOLUTION
================================================================================

  Layer 0: all currently legal explicit states
       |
  Layer 1: resolve immediate compatibility
       |
  Layer 2: relationships among already resolved relationships
       |
  Layer N: increasingly fine structural discrimination

Depth need not mean "see more characters."

Depth can mean "perform another resolution over already established
structure."

================================================================================
                       COMPILED LEXICON
================================================================================

                       SQL DICTIONARY
                            |
                 authoritative evidence
                            |
                            v
                     COMPILE / VERIFY
                            |
                            v
                  FAST HSCM-LIKE INDEX
                            |
             +--------------+--------------+
             |              |              |
             v              v              v
         HEADWORD        PHONETIC       STRUCTURAL
          INDEX           INDEX           INDEX
             |              |              |
             +--------------+--------------+
                            |
                            v
                       PARTIAL QUERY
                            |
                            v
                  compatible structures
                            |
                            v
                   remaining candidates
                            |
                            v
            most discriminating unresolved
                    representation
                            |
                            v
                     attention target

The lexicon becomes an active constraint-solving component rather than
only an external lookup table.

================================================================================
                     FORCED MEMORIZATION
================================================================================

Explicit compatibility structures can be memorized exactly:

        C(SAFE)   <-> SAFE
        C(SAFETY) <-> SAFETY
        C(UNSAFE) <-> UNSAFE

The label never destroys the structure.

SAFE
  -> word structure
  -> substructures
  -> character occurrences
  -> explicit representations
  -> physical / visual / morphological / orthographic /
     contextual evidence

================================================================================
                     COMPLETE ARCHITECTURE
================================================================================

                         ASCII95
                            |
                            v
                  95 x 437 FOUNDATION
                            |
                            v
                OCCURRENCE REPRESENTATIONS
                            |
               +------------+------------+
               |                         |
               v                         v
        TEXT SEQUENCE              COMPATIBILITY
                                     NETWORK
               |                         |
               +------------+------------+
                            |
                            v
                    MULTIPLE TRAVERSALS
                            |
                            v
                   STRUCTURAL CLOSURE
                            |
          +-----------------+------------------+
          |                 |                  |
          v                 v                  v
      PHONETIC          MORPHOLOGICAL        VISUAL
      STRUCTURE          STRUCTURE          STRUCTURE
          |                 |                  |
          +-----------------+------------------+
                            |
                            v
                       WORD STRUCTURE
                            |
                            v
                       DICTIONARY ID
                            |
                            v
                    STRUCTURAL TOKENS
                            |
                            v
                    ATTENTION / GQA
                            |
                            v
                     RESIDUAL STATE
                            |
                            v
              REPRESENTATION TRANSITION
                            |
                            v
                          DeltaR
                            |
                            v
              RECURRING TRANSFORMATION?
                            |
                           YES
                            |
                            v
                  COMPILED FFN BLOCK
                            |
                            v
                  STRUCTURAL EXPERT
                            |
                            v
                    NEXT RESOLUTION
                            |
                            +------------------> repeat traversal

================================================================================
                         CENTRAL PROPERTY
================================================================================

The architecture does not choose between:

  character-level
  phoneme-level
  subword-level
  word-level
  morphology-level
  symbolic-level

They can coexist as simultaneous structural resolutions:

                         TEXT
                          |
                          v
                     CHARACTERS
                          |
                          v
               EXPLICIT REPRESENTATIONS
                          |
                          v
                COMPATIBILITY STRUCTURES
                          |
          +---------------+-----------------+
          |               |                 |
          v               v                 v
       phonetic         lexical          symbolic
       structures       structures       structures
          |               |                 |
          +---------------+-----------------+
                          |
                          v
                HIGHER COMPOSITIONS

Every higher structure retains a path back:

  higher structure
      -> compatibility
      -> representations
      -> character occurrences
      -> ASCII95

================================================================================
```

## Explanation

The architecture begins with ASCII95 and the canonical 437 explicit representations. The 95 printable characters remain the physical text substrate. Each character occurrence exposes an explicit 437-dimensional state rather than being replaced by an opaque token embedding.

The important shift is that the 437 representations are not assumed to be independent. Physical and linguistic constraints create compatibility structure among them. Voicing, tongue height, tongue position, rounding, place, manner, duration, and other representations can constrain, imply, exclude, or leave unresolved other states. The legal configurations therefore occupy a constrained region of the nominal representation space.

Compatibility is also not inherently tied to a fixed span of text. Textual distance remains available and useful, but it is only one possible coordinate system. The same evidence can be traversed according to textual position, phonetic compatibility, tongue position, voicing, morphology, visual structure, current relevance, or another explicit relation. Positions distant in the source can become computational neighbors when they participate in the same relevant structure.

The dictionary provides grounded lexical and pronunciation evidence. A headword is still an ordered sequence of characters, but its pronunciation allows the system to resolve phoneme and physical-articulatory relationships across those characters. The resulting word-level object is therefore a compiled compatibility structure over character occurrences. The literal headword can serve as the label for that structure without becoming an opaque replacement for it.

Multi-character phonetic structures such as TH, CH, SH, TION, vowel combinations, or other spans are compositions over the underlying character representations. T and H remain fundamental; TH is a higher compatibility structure involving them. A new multi-character phenomenon should cause expansion of the canonical representation set only when the existing explicit representations cannot express the phenomenon compositionally.

ASCII 32 is especially informative. It has no ordinary pronunciation, phoneme, or articulation state, producing a complete phonetic discontinuity between pronunciation-bearing word structures. That absence is not equivalent to an all-zero character. Space still has identity, positional, orthographic, boundary, contextual, visual, and other applicable representations. Punctuation, mathematical symbols, digits, operators, delimiters, and programming symbols provide related structural cases, and many also connect bidirectionally to dictionary words such as PLUS, MINUS, ZERO, SEVEN, or LEFT PARENTHESIS.

Homophones demonstrate why pronunciation is one projection rather than the whole representation. WRITE and RIGHT can converge to the same pronunciation while retaining different complete character-by-representation trajectories. Their spelling, character identities, glyph geometry, character-to-phone alignment, morphology, lexical relations, and contextual states remain available simultaneously.

This allows multiple token systems to coexist over one character stream. A position can participate simultaneously in phonetic, visual, morphological, lexical, grammatical, mathematical, programming, and other structures. Structural tokens therefore do not require a fixed length, a fixed context window, contiguity, or one-token-per-position assignment. A structural token is a satisfied configuration of participating character occurrences, selected explicit representations, compatibility constraints, ordering, support/opposition relationships, and provenance.

Attention operates over this explicit field. Q can be interpreted as the relationships that currently need resolution, K as the explicit relationships on which an occurrence can be matched, and V as the explicit information the occurrence contributes when selected. Text neighbors and representation neighbors can both participate. A column-preserving architecture can maintain representation-specific attention pathways and then integrate them through GQA or another explicit routing mechanism.

The FFN is connected to the same representation space through observed state transitions. For a transition from R(before) to R(after), DeltaR identifies which explicit representations were promoted, demoted, or preserved. Recurring, distinguishable, predictive transitions across dictionary and corpus evidence can become candidate transformation operators. After falsification and validation, those operators can be compiled into FFN blocks or experts. The experts are therefore derived from recurring representation transformations rather than arbitrarily assigned semantic categories.

Additional layers can perform successive resolution rather than merely extending text reach. A first layer can resolve immediate compatibility; later layers can resolve relationships among structures already established by earlier computation. Context breadth and computational depth are therefore separate quantities.

The existing SQL dictionary can remain the authoritative evidence and provenance store while an HSCM-like binary/indexed representation provides fast runtime traversal. Indexes can support headword, pronunciation, physical-articulatory, and complete structural queries. Partial explicit states can progressively narrow compatible structures and headwords, and the remaining candidates can identify which unresolved representation would be most discriminating next.

Forced memorization can bind a verified compatibility structure exactly to its dictionary headword while preserving the complete path back to the underlying characters and explicit evidence.

The complete computational loop is:

```text
explicit state
    -> compatibility
    -> traversal
    -> attention / resolution
    -> representation transition
    -> DeltaR
    -> recurrent validated operator
    -> compiled FFN block
    -> new explicit state
    -> repeat
```

The resulting system does not have to choose character-level versus phoneme-level versus word-level versus symbolic-level representation. These become simultaneous, overlapping resolutions of the same explicit character-representation field.
