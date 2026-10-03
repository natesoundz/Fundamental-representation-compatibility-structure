# Augmented Explicit Character / Structural Network

This is a copy-and-augmentation of the original plain-text configuration diagram in `EXPLICIT_CHARACTER_STRUCTURAL_NETWORK.md`.

**Color key:** <span style="color:#d97706"><strong>[NEW—PHYSICAL/AUDIO]</strong></span> marks structures added after re-evaluating the canonical 437-representation workbook. GitHub renderers that suppress inline color still retain the explicit marker.

## Original baseline copied unchanged

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

## Augmented diagram

<pre>
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
        p0 -&gt; p1 -&gt; p2 -&gt; ...               voiced / unvoiced
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
                            +----&gt; COMPATIBILITY(Ri,Rj)
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
  voicing -----------+----&gt; LEGAL PHONETIC STATE
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

                       C(SAFE) &lt;----&gt; SAFE

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

       s -&gt; a -&gt; f -&gt; e   &lt;----&gt;   [SAFE]

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
                    SYMBOL &lt;-&gt; WORD CONNECTION
================================================================================

  ASCII SYMBOL                         DICTIONARY STRUCTURE

       +          &lt;-----------------&gt;       PLUS
       -          &lt;-----------------&gt;       MINUS / HYPHEN / NEGATION
       0          &lt;-----------------&gt;       ZERO
       7          &lt;-----------------&gt;       SEVEN
       (          &lt;-----------------&gt;       LEFT PARENTHESIS

Context resolves cases with multiple lexical/functional realizations.

Dictionary labels themselves return to the same substrate:

       +  &lt;-&gt;  PLUS  &lt;-&gt;  p l u s  &lt;-&gt; explicit character representations

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

 representation 1   -&gt; attention_1   --+
 representation 2   -&gt; attention_2     |
 representation 3   -&gt; attention_3     +--&gt; GQA / integration --&gt; residual
 ...
 representation 437 -&gt; attention_437 --+

================================================================================
                      FFN / EXPERT CREATION
================================================================================

Observe actual transitions through representation space:

        R(before) --&gt; computation --&gt; R(after)

        DeltaR = R(after) - R(before)

Interpret:
  DeltaR[k] &gt; 0  representation promoted
  DeltaR[k] &lt; 0  representation demoted
  DeltaR[k] ~= 0 representation preserved

Across dictionary and corpus:

  occurrence 1 -&gt; DeltaR1
  occurrence 2 -&gt; DeltaR2
  occurrence 3 -&gt; DeltaR3
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
   -&gt; explicit state transitions
   -&gt; recurring transformation
   -&gt; validated operator
   -&gt; FFN block

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

        C(SAFE)   &lt;-&gt; SAFE
        C(SAFETY) &lt;-&gt; SAFETY
        C(UNSAFE) &lt;-&gt; UNSAFE

The label never destroys the structure.

SAFE
  -&gt; word structure
  -&gt; substructures
  -&gt; character occurrences
  -&gt; explicit representations
  -&gt; physical / visual / morphological / orthographic /
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
                            +------------------&gt; repeat traversal

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
      -&gt; compatibility
      -&gt; representations
      -&gt; character occurrences
      -&gt; ASCII95

================================================================================

<span style="color:#d97706"><strong>[NEW—PHYSICAL/AUDIO]</strong>
================================================================================
              EXPANDED PHYSICAL / MULTIMODAL COMPATIBILITY FIELD
================================================================================

The original PHYSICAL COMPATIBILITY NETWORK is expanded from the small
summary set into the broader physical families exposed by the workbook.

                          PHYSICAL STATE
                                |
        +-----------------------+------------------------+
        |                                                |
        v                                                v
 SPEECH / ARTICULATION                            GLYPH / VISIBLE FORM
        |                                                |
        |                                   geometry / topology /
        |                                   spatial field / dimensions
        |
        +--> GENERAL ARTICULATORY FEATURES
        |      syllabic / sonorant / consonantal
        |      continuant / delayed release
        |      lateral / nasal / strident
        |      voice / spread glottis / constricted glottis
        |      anterior / coronal / distributed / labial
        |      high / low / back / round / velaric
        |      tense / long
        |
        +--> VOWEL / TONGUE-BODY CONFIGURATION
        |      HEIGHT:
        |        close -> near-close -> close-mid -> mid
        |        -> open-mid -> near-open -> open
        |
        |      BACKNESS:
        |        front -> near-front -> central -> near-back -> back
        |
        |      DISPLACEMENT / ROOT:
        |        raised / lowered / centralized
        |        advanced / retracted
        |        advanced tongue root / retracted tongue root
        |
        |      LIP CONFIGURATION:
        |        rounded / unrounded
        |
        +--> CONSONANT PLACE
        |      bilabial / labiodental / dental / alveolar /
        |      postalveolar / retroflex / palatal / velar /
        |      uvular / pharyngeal / glottal / ...
        |
        +--> CONSONANT MANNER
        |      stop / nasal / trill / tap-flap / fricative /
        |      sibilant / affricate / approximant / lateral / ...
        |
        +--> LARYNGEAL / PHONATION
        |      voiced / voiceless / aspirated / unaspirated /
        |      breathy / creaky / glottalized /
        |      spread glottis / constricted glottis
        |
        +--> SECONDARY ARTICULATION
        |      labialized / palatalized / velarized /
        |      pharyngealized / nasalized /
        |      centralized / advanced / retracted
        |
        +--> AIRSTREAM
        |      pulmonic / ejective / implosive / velaric / click
        |
        +--> TEMPORAL
               short / normal / long / extra-long / geminate


================================================================================
                    PHYSICAL CONSTRAINT PROPAGATION
================================================================================

Physical representations are not treated as independent labels.

 known physical state
        |
        +--> REQUIRES ------------+
        +--> EXCLUDES ------------|
        +--> IMPLIES -------------+--> remaining legal state field
        +--> NARROWS -------------|
        +--> SUPPORTS ------------|
        +--> OPPOSES -------------+
        |
        v
 compatibility closure

Examples of cross-description constraints already exposed by the workbook:

 general "voice" ---------> laryngeal voiced / voiceless state
 high / low / back ------> vowel height/backness configuration
 round ------------------> rounded / unrounded configuration
 articulatory state -----> compatible acoustic region
 phonetic duration ------> compatible temporal measurements

This redundancy is usable evidence: two representation families can
independently describe or constrain the same physical realization.


================================================================================
                     ARTICULATION -> ACOUSTICS
================================================================================

                 ARTICULATORY CONFIGURATION
                            |
                            v
                  VOCAL-TRACT CONFIGURATION
                            |
                            v
                     ACOUSTIC EVENT
                            |
          +-----------------+------------------+
          |                 |                  |
          v                 v                  v
         F0             F1 / F2 / F3       DURATION
          |                 |                  |
          +-----------------+------------------+
                            |
                            v
              trajectories / normalized measures /
              speaker-conditioned measurements

Cause-side and consequence-side representations therefore coexist:

 tongue / lips / larynx / airflow
                |
                v
       physical configuration
                |
                v
       measurable acoustics

The mapping is constraining rather than assumed one-to-one.


================================================================================
                AUDIO <-> TEXT SHARED REPRESENTATION PATH
================================================================================

                         AUDIO WAVEFORM
                              |
                              v
                    ACOUSTIC MEASUREMENTS
                              |
                              v
                   PHYSICAL COMPATIBILITY
              tongue / lips / larynx / airflow
              place / manner / airstream / time
                              |
                              v
                       PHONETIC STATE
                              |
                              v
                    PRONUNCIATION STRUCTURE
                              |
                              v
                    CHARACTER ALIGNMENT
                              |
                              v
                         ORTHOGRAPHY
                              |
                              v
                            TEXT

The same path is traversable in the opposite direction:

                            TEXT
                              |
                              v
                         ORTHOGRAPHY
                              |
                              v
                    DICTIONARY / LEXICON
                              |
                              v
                    PRONUNCIATION STRUCTURE
                              |
                              v
                       PHONETIC STATE
                              |
                              v
                 ARTICULATORY CONFIGURATION
                              |
                              v
                   EXPECTED ACOUSTIC REGION
                              |
                              v
                    WAVEFORM REALIZATION

Compact form:

 AUDIO <-> ACOUSTICS <-> ARTICULATION <-> PHONETICS
       <-> PRONUNCIATION <-> ORTHOGRAPHY <-> TEXT

Each arrow means compatibility, not guaranteed one-to-one inversion:

        X -> {Y : Y is compatible with X}

Audio-to-text narrows compatible states.
Text-to-audio instantiates one legal compatible realization.


================================================================================
                     TWO PHYSICAL REALIZATION DOMAINS
================================================================================

                         CHARACTER IDENTITY
                               |
                 +-------------+-------------+
                 |                           |
                 v                           v
          SPEECH REALIZATION           GLYPH REALIZATION
                 |                           |
          articulation / air          visible geometry /
                 |                    topology / spatial field
                 v                           |
              acoustics                      v
                 |                     rendered character
                 +-------------+-------------+
                               |
                               v
                     SHARED ORTHOGRAPHY

The same abstract character can therefore be grounded through physically
different modalities while retaining one explicit provenance network.


================================================================================
                  PHYSICAL -> NONPHYSICAL BRIDGES
================================================================================

 physical articulation
        |
        v
 acoustics
        |
        v
 phone / phonetic structure
        |
        v
 pronunciation
        |
        v
 character-phone alignment
        |
        v
 orthographic character structure
        |
        v
 lexical structure
        |
        +-------------> morphology
        +-------------> grammatical possibilities
        +-------------> semantic / lexical relations
        +-------------> structural-token identity

Physical evidence can therefore constrain representations that are not
themselves physical.


================================================================================
                STRUCTURAL INAPPLICABILITY AS EVIDENCE
================================================================================

 pronunciation-bearing character/word
                |
                v
         physical state available
                |
                v
             ASCII 32
                |
       phoneme/articulation/
       tongue/voicing/acoustics
              IMPOSSIBLE
                |
                v
        boundary state available
                |
                v
        next pronunciation-bearing
             structure

The transition

 PHYSICAL STATE -> PHYSICAL STATE -> PHYSICAL STATE IMPOSSIBLE
                -> NEW PHYSICAL STATE

is itself a strong compatibility/boundary signal.


================================================================================
               AUGMENTED COMPLETE ARCHITECTURE
================================================================================

                           AUDIO
                             |
                             v
                         ACOUSTICS
                             |
                             v
                    PHYSICAL ARTICULATION
                             |
                             v
                          PHONETICS
                             |
                             v
                       PRONUNCIATION
                             |
                             +---------------------------+
                             |                           |
                             v                           v
                         ASCII95                  GLYPH PHYSICS
                             |                    / VISUAL FORM
                             v                           |
                    95 x 437 FOUNDATION <---------------+
                             |
                             v
                 OCCURRENCE REPRESENTATIONS
                             |
              +--------------+--------------+
              |                             |
              v                             v
        TEXT SEQUENCE                COMPATIBILITY NETWORK
              |                             |
              +--------------+--------------+
                             |
                             v
                    CONSTRAINT PROPAGATION
                             |
                             v
                     MULTIPLE TRAVERSALS
                             |
                             v
                    STRUCTURAL CLOSURE
                             |
          +------------------+------------------+
          |                  |                  |
          v                  v                  v
      PHONETIC          MORPHOLOGICAL         VISUAL
      STRUCTURE          STRUCTURE           STRUCTURE
          |                  |                  |
          +------------------+------------------+
                             |
                             v
                        WORD STRUCTURE
                             |
                             v
                    DICTIONARY / LEXICON
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
                             +--------------------> repeat

The upper speech path is bidirectional:

 AUDIO <----------------------------------------------> TEXT

and the entire path remains decomposable through explicit representations,
compatibility constraints, dictionary evidence, and source provenance.
</strong></span>
</pre>

## What changed

The original diagram remains the baseline. The augmentation makes six workbook-derived consequences explicit:

1. The physical speech representation is broader than tongue height, tongue position, rounding, voicing, place, manner, and duration. It includes general articulatory features, laryngeal/phonation state, secondary articulation, airstream, detailed vowel configuration, and temporal structure.
2. Acoustic dimensions are connected as measurable consequences/evidence of physical articulation rather than treated as an unrelated representation family.
3. Audio and text become opposite traversals through a shared compatibility network.
4. Glyph geometry/topology forms a second physical realization domain connected to the same character identity.
5. Physical state can propagate constraints upward into phones, pronunciation, orthography, lexical identity, morphology, and other nonphysical representations.
6. Structural inapplicability, especially the phonetic break at ASCII 32, becomes explicit compatibility evidence.

The detailed `SAFE` traversal is recorded separately in `BIDIRECTIONAL_SPEECH_TEXT_COMPATIBILITY.md`.
