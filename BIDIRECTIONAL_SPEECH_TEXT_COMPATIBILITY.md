# Bidirectional Speech / Text Compatibility Example

This document extends the explicit-character architecture with a concrete bidirectional traversal through the same compatibility network.

The example uses the word `SAFE`. The important claim is not that speech recognition or speech synthesis is new. The architectural claim being tested is whether the canonical explicit representation system can serve as a shared, inspectable intermediate state connecting acoustic evidence, physical articulation, phonetic realization, pronunciation, orthography, and text.

## Direction A — audio to text

```text
AUDIO WAVEFORM
      |
      v
ACOUSTIC OBSERVATIONS
      |
      v
PHYSICAL / ARTICULATORY COMPATIBILITY
      |
      v
PHONETIC STRUCTURES
      |
      v
PRONUNCIATION STRUCTURE
      |
      v
CHARACTER COMPATIBILITY
      |
      v
SAFE
```

The waveform is first treated as measured evidence rather than as a word guess. Relevant observations can include F0, F1, F2, F3, duration, energy, spectral structure, periodicity, and other acoustic measurements already represented or supported by the canonical workbook.

For a spoken realization of `safe`, the signal contains approximately:

```text
time -------------------------------------------------------------->

      /s/                    /eI/                    /f/

  turbulent noise        vowel/formants         turbulent noise
       |                      |                       |
       v                      v                       v
  consonantal              syllabic               consonantal
  fricative                voiced                 fricative
  voiceless                vowel                  voiceless
```

Acoustic evidence constrains compatible physical states. For the vowel region, formant evidence can constrain tongue/vowel height and front/back position; periodicity constrains voicing; temporal measurements constrain duration. These are compatibility constraints, not direct letter assignments.

The initial consonant can support a configuration involving consonantal, fricative, sibilant/strident, voiceless, alveolar, and continuant properties. The final consonant can support consonantal, fricative, voiceless, labiodental, and continuant properties. Intersecting the legal physical configurations narrows compatible phones toward:

```text
/s/ + vowel compatible with /eI/ + /f/
```

The resulting pronunciation structure can then be resolved against dictionary evidence. Pronunciation alone is not assumed to determine spelling uniquely because homophones and pronunciation variants exist. The physical, acoustic, ordering, boundary, and pronunciation evidence remain available while candidate lexical structures are narrowed.

For `SAFE`, the dictionary-supported pronunciation connects to the character sequence:

```text
            /s eI f/
                |
                v
        pronunciation structure
                |
       +--------+--------+
       |        |        |
       v        v        v
      /s/      /eI/     /f/
       |        |         |
       v        v         v
       s       a/e        f
                |
                v
        orthographic pattern

             s a f e
```

The final `e` is not asserted to independently realize /eI/. Its explicit occurrence can instead resolve facts such as character identity, word-final position, boundary distance, and lack of an independently pronounced phone in this realization, while its relation to the preceding structure participates in the lexical pronunciation pattern.

The retained provenance chain is therefore:

```text
audio
  -> acoustics
  -> physical articulation
  -> phones
  -> pronunciation
  -> orthography
  -> SAFE
```

## Direction B — text to audio

Reverse traversal begins from the same lexical structure:

```text
SAFE
 |
 v
s a f e
```

Each character occurrence exposes its canonical explicit representation state. Many pronunciation-related dimensions begin as eligible or unresolved rather than being permanently assigned by character identity.

The complete character sequence resolves against dictionary evidence:

```text
HEADWORD: safe
PRONUNCIATION: /seIf/
```

That pronunciation constrains physical articulation.

For /s/:

```text
/s/
 |
 +-- voiceless
 +-- alveolar
 +-- fricative
 +-- sibilant / strident
 +-- continuant
 +-- consonantal
```

For the vowel, the diphthong is a trajectory rather than a single static physical point:

```text
first vowel region
       |
       v
tongue / lip configuration
       |
       v
articulatory movement
       |
       v
second vowel region
```

For /f/:

```text
/f/
 |
 +-- voiceless
 +-- labiodental
 +-- fricative
 +-- continuant
 +-- consonantal
```

The articulatory trajectory constrains an expected acoustic trajectory. Tongue height constrains expected formant regions; tongue front/back position constrains other formant relationships; voicing constrains periodic excitation; duration constrains temporal structure; constrictions and airflow constrain frication/noise characteristics.

A synthesizer or vocoder can then instantiate one compatible acoustic realization as waveform samples.

```text
SAFE
 |
 v
s a f e
 |
 v
/s eI f/
 |
 v
physical articulatory trajectory
 |
 v
acoustic trajectory
 |
 v
waveform
 |
 v
spoken "safe"
```

## Shared bidirectional structure

```text
                         AUDIO
                           |
                           v
                 ACOUSTIC MEASUREMENTS
                           |
                           v
                PHYSICAL REPRESENTATIONS
             tongue / lips / larynx / airflow
             place / manner / duration / etc.
                           |
                           v
                    PHONETIC STATE
                           |
                           v
                     /s eI f/
                           |
                           v
                 PRONUNCIATION STRUCTURE
                           |
                           v
                     s  a  f  e
                           |
                           v
                         SAFE
                           |
                     reverse traversal
                           |
                           v
                     s  a  f  e
                           |
                           v
                     /s eI f/
                           |
                           v
                PHYSICAL REPRESENTATIONS
                           |
                           v
                  ACOUSTIC TARGETS
                           |
                           v
                        AUDIO
```

The central operation in either direction is not assumed to be a perfect mathematical inverse. Speech is many-to-many: speakers, accents, rates, coarticulation, pronunciation variants, and homophones prevent a simple one-to-one mapping.

Instead, each edge is treated as a compatibility relation:

```text
X -> {Y : Y is compatible with X}
```

Audio-to-text progressively narrows the compatible state field. Text-to-audio progressively instantiates one legal realization from that field.

The resulting research hypothesis is therefore:

```text
AUDIO
  <->
ACOUSTICS
  <->
PHYSICAL ARTICULATION
  <->
PHONETICS
  <->
PRONUNCIATION
  <->
ORTHOGRAPHY
  <->
TEXT
```

can be represented as opposite traversals through one explicit compatibility network while preserving provenance at each transition.
