# Canonical ASCII95 × 437 Matrix — Plain-Text Map

> **⚠️ DEPRECATION / CANONICAL AUTHORITY NOTICE**
>
> **All former ASCII95 representation substrates—including the 95×192, 95×254, and any superseded intermediate matrix/registry versions—are DEPRECATED and MUST NOT be used as the execution, compilation, or experimental substrate for current work. They are retained only as historical lineage where referenced.**
>
> **CURRENT AUTHORITY: use the most recent functioning Canonical ASCII95 workbook (95 printable ASCII characters × 437 canonical representation dimensions) and its current 103-piece physical system. The canonical workbook itself is authoritative; derived exports, older matrices, diagrams, and historical compiler artifacts do not override it.**


This document is a plain-text map of the canonical workbook. It lists the complete row axis (95 printable ASCII characters), the complete column axis (437 named representation dimensions), the workbook metadata fields, and the cell-state legend. It is intended to make the structure of the matrix directly inspectable in GitHub and by automated research systems.

```text
CANONICAL MATRIX

                         437 EXPLICIT REPRESENTATION COLUMNS
                    r001  r002  r003  ...                 r437
                      |     |     |                         |
ASCII 32  [space]  ---+-----+-----+-------------------------+
ASCII 33  !        ---+-----+-----+-------------------------+
ASCII 34  "        ---+-----+-----+-------------------------+
   ...
ASCII 126 ~        ---+-----+-----+-------------------------+

Each intersection = the canonical state of one printable ASCII character
on one explicitly named representation dimension.
```

## Matrix dimensions

- **Rows:** 95 printable ASCII characters, ASCII 32 through 126.
- **Representation columns:** 437 canonical named dimensions.
- **Row-identification columns:** `#`, `Character`, `ASCII Dec`, `ASCII Hex`, `Unicode Name`.
- **Worksheet extent:** 104 rows × 442 columns, including title and metadata rows.

## Column metadata carried by the workbook

Each representation column has metadata rows for:

```text
Group
Interaction
Eligibility
Positive / Candidate
Defer / Scope
Display Name
Canonical ID
STATUS
```

## Complete column axis — 437 canonical representations

### 01 Character Identity (30)

001. **character** — `character_identity.character` — interaction: `KEY` — eligibility: `ALL95`
002. **ASCII integer** — `character_identity.ascii_integer` — interaction: `KEY` — eligibility: `ALL95`
003. **Unicode code point** — `character_identity.unicode_code_point` — interaction: `KEY` — eligibility: `ALL95`
004. **Unicode name** — `character_identity.unicode_name` — interaction: `KEY` — eligibility: `ALL95`
005. **Unicode general category** — `character_identity.unicode_general_category` — interaction: `GATE + DISCRIMINATE` — eligibility: `ALL95`
006. **script** — `character_identity.script` — interaction: `DISCRIMINATE` — eligibility: `ALL95`
007. **alphabetic** — `character_identity.alphabetic` — interaction: `GATE` — eligibility: `ALL95`
008. **uppercase** — `character_identity.uppercase` — interaction: `DISCRIMINATE` — eligibility: `LETTERS`
009. **lowercase** — `character_identity.lowercase` — interaction: `DERIVED` — eligibility: `LETTERS`
010. **case mapping** — `character_identity.case_mapping` — interaction: `RELATION` — eligibility: `LETTERS`
011. **case-fold mapping** — `character_identity.case_fold_mapping` — interaction: `RELATION` — eligibility: `LETTERS`
012. **digit status** — `character_identity.digit_status` — interaction: `GATE` — eligibility: `ALL95`
013. **decimal status** — `character_identity.decimal_status` — interaction: `DERIVED` — eligibility: `ALL95`
014. **numeric type** — `character_identity.numeric_type` — interaction: `STRUCTURAL` — eligibility: `DIGITS`
015. **numeric value** — `character_identity.numeric_value` — interaction: `DISCRIMINATE` — eligibility: `DIGITS`
016. **punctuation status** — `character_identity.punctuation_status` — interaction: `GATE` — eligibility: `ALL95`
017. **symbol status** — `character_identity.symbol_status` — interaction: `GATE` — eligibility: `ALL95`
018. **whitespace status** — `character_identity.whitespace_status` — interaction: `GATE` — eligibility: `ALL95`
019. **math status** — `character_identity.math_status` — interaction: `GATE` — eligibility: `ALL95`
020. **identifier-start status** — `character_identity.identifier_start` — interaction: `GATE` — eligibility: `ALL95`
021. **identifier-continue status** — `character_identity.identifier_continue` — interaction: `GATE` — eligibility: `ALL95`
022. **bidirectional class** — `character_identity.bidirectional_class` — interaction: `DISCRIMINATE` — eligibility: `ALL95`
023. **bidirectional mirrored** — `character_identity.bidirectional_mirrored` — interaction: `DISCRIMINATE` — eligibility: `ALL95`
024. **East Asian width** — `character_identity.east_asian_width` — interaction: `DISCRIMINATE` — eligibility: `ALL95`
025. **line-break class** — `character_identity.line_break_class` — interaction: `DISCRIMINATE` — eligibility: `ALL95`
026. **word-break class** — `character_identity.word_break_class` — interaction: `DISCRIMINATE` — eligibility: `ALL95`
027. **sentence-break class** — `character_identity.sentence_break_class` — interaction: `DISCRIMINATE` — eligibility: `ALL95`
028. **grapheme-break class** — `character_identity.grapheme_break_class` — interaction: `DISCRIMINATE` — eligibility: `ALL95`
029. **decomposition mapping** — `character_identity.decomposition_mapping` — interaction: `STRUCTURAL` — eligibility: `ALL95`
030. **decomposition type** — `character_identity.decomposition_type` — interaction: `STRUCTURAL` — eligibility: `ALL95`

### 02 Mathematical / Numeric Invariants (13)

031. **numeric value** — `numeric.decimal.numeric_value` — interaction: `DISCRIMINATE` — eligibility: `DIGITS`
032. **integer** — `numeric.decimal.integer` — interaction: `DERIVED` — eligibility: `DIGITS`
033. **zero** — `numeric.decimal.zero` — interaction: `DISCRIMINATE` — eligibility: `DIGITS`
034. **nonzero** — `numeric.decimal.nonzero` — interaction: `DERIVED` — eligibility: `DIGITS`
035. **positive** — `numeric.decimal.positive` — interaction: `DERIVED` — eligibility: `DIGITS`
036. **even** — `numeric.decimal.even` — interaction: `DISCRIMINATE` — eligibility: `DIGITS`
037. **odd** — `numeric.decimal.odd` — interaction: `DERIVED` — eligibility: `DIGITS`
038. **prime** — `numeric.decimal.prime` — interaction: `DISCRIMINATE` — eligibility: `DIGITS`
039. **composite** — `numeric.decimal.composite` — interaction: `DISCRIMINATE` — eligibility: `DIGITS`
040. **square** — `numeric.decimal.square` — interaction: `DISCRIMINATE` — eligibility: `DIGITS`
041. **digit rank** — `numeric.decimal.digit_rank` — interaction: `DERIVED` — eligibility: `DIGITS`
042. **binary value** — `numeric.decimal.binary_value` — interaction: `DERIVED` — eligibility: `DIGITS`
043. **hexadecimal value** — `numeric.hexadecimal.value` — interaction: `DEFER + DISCRIMINATE` — eligibility: `HEX`

### 03 Phonetic / Articulatory — General (22)

044. **syllabic** — `phonetic.phonetic_articulatory_general.syllabic` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
045. **sonorant** — `phonetic.phonetic_articulatory_general.sonorant` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
046. **consonantal** — `phonetic.phonetic_articulatory_general.consonantal` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
047. **continuant** — `phonetic.phonetic_articulatory_general.continuant` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
048. **delayed release** — `phonetic.phonetic_articulatory_general.delayed_release` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
049. **lateral** — `phonetic.phonetic_articulatory_general.lateral` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
050. **nasal** — `phonetic.phonetic_articulatory_general.nasal` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
051. **strident** — `phonetic.phonetic_articulatory_general.strident` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
052. **voice** — `phonetic.phonetic_articulatory_general.voice` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
053. **spread glottis** — `phonetic.phonetic_articulatory_general.spread_glottis` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
054. **constricted glottis** — `phonetic.phonetic_articulatory_general.constricted_glottis` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
055. **anterior** — `phonetic.phonetic_articulatory_general.anterior` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
056. **coronal** — `phonetic.phonetic_articulatory_general.coronal` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
057. **distributed** — `phonetic.phonetic_articulatory_general.distributed` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
058. **labial** — `phonetic.phonetic_articulatory_general.labial` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
059. **high** — `phonetic.phonetic_articulatory_general.high` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
060. **low** — `phonetic.phonetic_articulatory_general.low` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
061. **back** — `phonetic.phonetic_articulatory_general.back` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
062. **round** — `phonetic.phonetic_articulatory_general.round` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
063. **velaric** — `phonetic.phonetic_articulatory_general.velaric` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
064. **tense** — `phonetic.phonetic_articulatory_general.tense` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
065. **long** — `phonetic.phonetic_articulatory_general.long` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`

### 04 Vowel / Tongue-Body Position (21)

066. **close** — `phonetic.vowel_tongue_body_position.close` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
067. **near-close** — `phonetic.vowel_tongue_body_position.near_close` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
068. **close-mid** — `phonetic.vowel_tongue_body_position.close_mid` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
069. **mid** — `phonetic.vowel_tongue_body_position.mid` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
070. **open-mid** — `phonetic.vowel_tongue_body_position.open_mid` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
071. **near-open** — `phonetic.vowel_tongue_body_position.near_open` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
072. **open** — `phonetic.vowel_tongue_body_position.open` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
073. **front** — `phonetic.vowel_tongue_body_position.front` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
074. **near-front** — `phonetic.vowel_tongue_body_position.near_front` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
075. **central** — `phonetic.vowel_tongue_body_position.central` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
076. **near-back** — `phonetic.vowel_tongue_body_position.near_back` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
077. **back** — `phonetic.vowel_tongue_body_position.back` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
078. **raised** — `phonetic.vowel_tongue_body_position.raised` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
079. **lowered** — `phonetic.vowel_tongue_body_position.lowered` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
080. **centralized** — `phonetic.vowel_tongue_body_position.centralized` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
081. **advanced** — `phonetic.vowel_tongue_body_position.advanced` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
082. **retracted** — `phonetic.vowel_tongue_body_position.retracted` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
083. **advanced tongue root** — `phonetic.vowel_tongue_body_position.advanced_tongue_root` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
084. **retracted tongue root** — `phonetic.vowel_tongue_body_position.retracted_tongue_root` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
085. **rounded** — `phonetic.vowel_tongue_body_position.rounded` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
086. **unrounded** — `phonetic.vowel_tongue_body_position.unrounded` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`

### 05 Consonant Place of Articulation (20)

087. **bilabial** — `phonetic.consonant_place_of_articulation.bilabial` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
088. **labiodental** — `phonetic.consonant_place_of_articulation.labiodental` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
089. **dental** — `phonetic.consonant_place_of_articulation.dental` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
090. **alveolar** — `phonetic.consonant_place_of_articulation.alveolar` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
091. **postalveolar** — `phonetic.consonant_place_of_articulation.postalveolar` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
092. **retroflex** — `phonetic.consonant_place_of_articulation.retroflex` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
093. **alveolo-palatal** — `phonetic.consonant_place_of_articulation.alveolo_palatal` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
094. **palatal** — `phonetic.consonant_place_of_articulation.palatal` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
095. **velar** — `phonetic.consonant_place_of_articulation.velar` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
096. **uvular** — `phonetic.consonant_place_of_articulation.uvular` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
097. **pharyngeal** — `phonetic.consonant_place_of_articulation.pharyngeal` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
098. **epiglottal** — `phonetic.consonant_place_of_articulation.epiglottal` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
099. **glottal** — `phonetic.consonant_place_of_articulation.glottal` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
100. **labial-velar** — `phonetic.consonant_place_of_articulation.labial_velar` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
101. **anterior** — `phonetic.consonant_place_of_articulation.anterior` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
102. **coronal** — `phonetic.consonant_place_of_articulation.coronal` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
103. **distributed** — `phonetic.consonant_place_of_articulation.distributed` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
104. **dorsal** — `phonetic.consonant_place_of_articulation.dorsal` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
105. **labial** — `phonetic.consonant_place_of_articulation.labial` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
106. **laryngeal** — `phonetic.consonant_place_of_articulation.laryngeal` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`

### 06A Consonant Manner of Articulation (13)

107. **stop** — `phonetic.consonant_manner_of_articulation.stop` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
108. **plosive** — `phonetic.consonant_manner_of_articulation.plosive` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
109. **nasal** — `phonetic.consonant_manner_of_articulation.nasal` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
110. **trill** — `phonetic.consonant_manner_of_articulation.trill` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
111. **tap** — `phonetic.consonant_manner_of_articulation.tap` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
112. **flap** — `phonetic.consonant_manner_of_articulation.flap` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
113. **fricative** — `phonetic.consonant_manner_of_articulation.fricative` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
114. **sibilant** — `phonetic.consonant_manner_of_articulation.sibilant` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
115. **affricate** — `phonetic.consonant_manner_of_articulation.affricate` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
116. **approximant** — `phonetic.consonant_manner_of_articulation.approximant` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
117. **lateral approximant** — `phonetic.consonant_manner_of_articulation.lateral_approximant` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
118. **lateral fricative** — `phonetic.consonant_manner_of_articulation.lateral_fricative` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
119. **click** — `phonetic.consonant_manner_of_articulation.click` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`

### 06B Laryngeal / Phonation (9)

120. **voiced** — `phonetic.laryngeal_phonation.voiced` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
121. **voiceless** — `phonetic.laryngeal_phonation.voiceless` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
122. **aspirated** — `phonetic.laryngeal_phonation.aspirated` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
123. **unaspirated** — `phonetic.laryngeal_phonation.unaspirated` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
124. **breathy** — `phonetic.laryngeal_phonation.breathy` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
125. **creaky** — `phonetic.laryngeal_phonation.creaky` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
126. **glottalized** — `phonetic.laryngeal_phonation.glottalized` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
127. **spread glottis** — `phonetic.laryngeal_phonation.spread_glottis` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
128. **constricted glottis** — `phonetic.laryngeal_phonation.constricted_glottis` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`

### 06C Secondary Articulation (8)

129. **labialized** — `phonetic.secondary_articulation.labialized` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
130. **palatalized** — `phonetic.secondary_articulation.palatalized` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
131. **velarized** — `phonetic.secondary_articulation.velarized` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
132. **pharyngealized** — `phonetic.secondary_articulation.pharyngealized` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
133. **nasalized** — `phonetic.secondary_articulation.nasalized` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
134. **centralized** — `phonetic.secondary_articulation.centralized` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
135. **advanced** — `phonetic.secondary_articulation.advanced` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
136. **retracted** — `phonetic.secondary_articulation.retracted` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`

### 06D Airstream (5)

137. **pulmonic** — `phonetic.airstream.pulmonic` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
138. **ejective** — `phonetic.airstream.ejective` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
139. **implosive** — `phonetic.airstream.implosive` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
140. **velaric** — `phonetic.airstream.velaric` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
141. **click** — `phonetic.airstream.click` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`

### 06E Phonetic Temporal Properties (5)

142. **short** — `phonetic.phonetic_temporal_properties.short` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
143. **normal length** — `phonetic.phonetic_temporal_properties.normal_length` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
144. **long** — `phonetic.phonetic_temporal_properties.long` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
145. **extra-long** — `phonetic.phonetic_temporal_properties.extra_long` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`
146. **geminate** — `phonetic.phonetic_temporal_properties.geminate` — interaction: `GATE + DEFER + DISCRIMINATE` — eligibility: `LETTERS`

### 07 Pronunciation Distributions (9)

147. **possible phoneme realizations** — `pronunciation.possible_phoneme_realizations` — interaction: `DEFER + RELATION` — eligibility: `LETTERS`
148. **phoneme occurrence frequency** — `pronunciation.phoneme_occurrence_frequency` — interaction: `RELATION + MODULATE` — eligibility: `LETTERS`
149. **phoneme conditional probability** — `pronunciation.phoneme_conditional_probability` — interaction: `RELATION + MODULATE` — eligibility: `LETTERS`
150. **articulatory-feature probability** — `pronunciation.articulatory_feature_probability` — interaction: `RELATION + MODULATE` — eligibility: `LETTERS`
151. **pronunciation variant frequency** — `pronunciation.pronunciation_variant_frequency` — interaction: `RELATION + MODULATE` — eligibility: `LETTERS`
152. **stress** — `pronunciation.stress` — interaction: `DEFER + DISCRIMINATE` — eligibility: `LETTERS`
153. **lexical stress** — `pronunciation.lexical_stress` — interaction: `DEFER + DISCRIMINATE` — eligibility: `LETTERS`
154. **character-to-phone distribution** — `pronunciation.character_to_phone_distribution` — interaction: `RELATION + MODULATE` — eligibility: `LETTERS`
155. **context-conditioned character-to-phone distribution** — `pronunciation.context_conditioned_character_to_phone_distribution` — interaction: `RELATION + MODULATE` — eligibility: `LETTERS`

### 08 Acoustics (27)

156. **fundamental frequency F0** — `acoustic.fundamental_frequency_f0` — interaction: `DEFER + MEASUREMENT` — eligibility: `LETTERS`
157. **first formant F1** — `acoustic.first_formant_f1` — interaction: `DEFER + MEASUREMENT` — eligibility: `LETTERS`
158. **second formant F2** — `acoustic.second_formant_f2` — interaction: `DEFER + MEASUREMENT` — eligibility: `LETTERS`
159. **third formant F3** — `acoustic.third_formant_f3` — interaction: `DEFER + MEASUREMENT` — eligibility: `LETTERS`
160. **segment duration** — `acoustic.segment_duration` — interaction: `DEFER + MEASUREMENT` — eligibility: `LETTERS`
161. **phoneme duration** — `acoustic.phoneme_duration` — interaction: `DEFER + MEASUREMENT` — eligibility: `LETTERS`
162. **vowel duration** — `acoustic.vowel_duration` — interaction: `DEFER + MEASUREMENT` — eligibility: `LETTERS`
163. **within-segment temporal position** — `acoustic.within_segment_temporal_position` — interaction: `DEFER + MEASUREMENT` — eligibility: `LETTERS`
164. **speaker-normalized formants** — `acoustic.speaker_normalized_formants` — interaction: `DEFER + MEASUREMENT` — eligibility: `LETTERS`
165. **formant trajectory** — `acoustic.formant_trajectory` — interaction: `DEFER + MEASUREMENT` — eligibility: `LETTERS`
166. **F0 mean** — `acoustic.f0_mean` — interaction: `DEFER + MODULATE` — eligibility: `LETTERS`
167. **F0 variance** — `acoustic.f0_variance` — interaction: `DEFER + MODULATE` — eligibility: `LETTERS`
168. **F1 mean** — `acoustic.f1_mean` — interaction: `DEFER + MODULATE` — eligibility: `LETTERS`
169. **F1 variance** — `acoustic.f1_variance` — interaction: `DEFER + MODULATE` — eligibility: `LETTERS`
170. **F2 mean** — `acoustic.f2_mean` — interaction: `DEFER + MODULATE` — eligibility: `LETTERS`
171. **F2 variance** — `acoustic.f2_variance` — interaction: `DEFER + MODULATE` — eligibility: `LETTERS`
172. **F3 mean** — `acoustic.f3_mean` — interaction: `DEFER + MODULATE` — eligibility: `LETTERS`
173. **F3 variance** — `acoustic.f3_variance` — interaction: `DEFER + MODULATE` — eligibility: `LETTERS`
174. **F1 minimum** — `acoustic.f1_minimum` — interaction: `DEFER + MODULATE` — eligibility: `LETTERS`
175. **F1 maximum** — `acoustic.f1_maximum` — interaction: `DEFER + MODULATE` — eligibility: `LETTERS`
176. **F2 minimum** — `acoustic.f2_minimum` — interaction: `DEFER + MODULATE` — eligibility: `LETTERS`
177. **F2 maximum** — `acoustic.f2_maximum` — interaction: `DEFER + MODULATE` — eligibility: `LETTERS`
178. **F3 minimum** — `acoustic.f3_minimum` — interaction: `DEFER + MODULATE` — eligibility: `LETTERS`
179. **F3 maximum** — `acoustic.f3_maximum` — interaction: `DEFER + MODULATE` — eligibility: `LETTERS`
180. **between-speaker variance** — `acoustic.between_speaker_variance` — interaction: `DEFER + MODULATE` — eligibility: `LETTERS`
181. **sex-conditioned acoustic distribution** — `acoustic.sex_conditioned_acoustic_distribution` — interaction: `DEFER + MODULATE` — eligibility: `LETTERS`
182. **age-conditioned acoustic distribution** — `acoustic.age_conditioned_acoustic_distribution` — interaction: `DEFER + MODULATE` — eligibility: `LETTERS`

### 09A Glyph / Visual Geometry (16)

183. **bounding width** — `glyph.geometry.bounding_width` — interaction: `DEFER + MEASUREMENT` — eligibility: `ALL95`
184. **bounding height** — `glyph.geometry.bounding_height` — interaction: `DEFER + MEASUREMENT` — eligibility: `ALL95`
185. **aspect ratio** — `glyph.geometry.aspect_ratio` — interaction: `DEFER + MEASUREMENT` — eligibility: `ALL95`
186. **advance width** — `glyph.geometry.advance_width` — interaction: `DEFER + MEASUREMENT` — eligibility: `ALL95`
187. **ink area** — `glyph.geometry.ink_area` — interaction: `DEFER + MEASUREMENT` — eligibility: `ALL95`
188. **ink density** — `glyph.geometry.ink_density` — interaction: `DEFER + MEASUREMENT` — eligibility: `ALL95`
189. **centroid x** — `glyph.geometry.centroid_x` — interaction: `DEFER + MEASUREMENT` — eligibility: `VISIBLE94`
190. **centroid y** — `glyph.geometry.centroid_y` — interaction: `DEFER + MEASUREMENT` — eligibility: `VISIBLE94`
191. **left-right balance** — `glyph.geometry.left_right_balance` — interaction: `DEFER + MEASUREMENT` — eligibility: `VISIBLE94`
192. **top-bottom balance** — `glyph.geometry.top_bottom_balance` — interaction: `DEFER + MEASUREMENT` — eligibility: `VISIBLE94`
193. **orientation spectrum** — `glyph.geometry.orientation_spectrum` — interaction: `DEFER + MEASUREMENT` — eligibility: `VISIBLE94`
194. **horizontal energy** — `glyph.geometry.horizontal_energy` — interaction: `DEFER + MEASUREMENT` — eligibility: `VISIBLE94`
195. **vertical energy** — `glyph.geometry.vertical_energy` — interaction: `DEFER + MEASUREMENT` — eligibility: `VISIBLE94`
196. **diagonal energy** — `glyph.geometry.diagonal_energy` — interaction: `DEFER + MEASUREMENT` — eligibility: `VISIBLE94`
197. **curvature** — `glyph.geometry.curvature` — interaction: `DEFER + MEASUREMENT` — eligibility: `VISIBLE94`
198. **symmetry** — `glyph.geometry.symmetry` — interaction: `DEFER + MEASUREMENT` — eligibility: `VISIBLE94`

### 09B Glyph / Visual Topology (17)

199. **connected-component count** — `glyph.topology.connected_component_count` — interaction: `DEFER + DISCRIMINATE` — eligibility: `ALL95`
200. **contour count** — `glyph.topology.contour_count` — interaction: `DEFER + DISCRIMINATE` — eligibility: `ALL95`
201. **enclosed-region count** — `glyph.topology.enclosed_region_count` — interaction: `DEFER + DISCRIMINATE` — eligibility: `ALL95`
202. **counter count** — `glyph.topology.counter_count` — interaction: `DEFER + DISCRIMINATE` — eligibility: `ALL95`
203. **Euler characteristic** — `glyph.topology.euler_characteristic` — interaction: `DEFER + DISCRIMINATE` — eligibility: `ALL95`
204. **skeleton endpoint count** — `glyph.topology.skeleton_endpoint_count` — interaction: `DEFER + DISCRIMINATE` — eligibility: `ALL95`
205. **skeleton junction count** — `glyph.topology.skeleton_junction_count` — interaction: `DEFER + DISCRIMINATE` — eligibility: `ALL95`
206. **crossing count** — `glyph.topology.crossing_count` — interaction: `DEFER + DISCRIMINATE` — eligibility: `ALL95`
207. **open-path count** — `glyph.topology.open_path_count` — interaction: `DEFER + DISCRIMINATE` — eligibility: `ALL95`
208. **closed-path count** — `glyph.topology.closed_path_count` — interaction: `DEFER + DISCRIMINATE` — eligibility: `ALL95`
209. **loop occurrence rate** — `glyph.topology.loop_occurrence_rate` — interaction: `DEFER + MODULATE` — eligibility: `VISIBLE94`
210. **crossbar occurrence rate** — `glyph.topology.crossbar_occurrence_rate` — interaction: `DEFER + MODULATE` — eligibility: `VISIBLE94`
211. **vertical-stroke occurrence rate** — `glyph.topology.vertical_stroke_occurrence_rate` — interaction: `DEFER + MODULATE` — eligibility: `VISIBLE94`
212. **horizontal-stroke occurrence rate** — `glyph.topology.horizontal_stroke_occurrence_rate` — interaction: `DEFER + MODULATE` — eligibility: `VISIBLE94`
213. **diagonal-stroke occurrence rate** — `glyph.topology.diagonal_stroke_occurrence_rate` — interaction: `DEFER + MODULATE` — eligibility: `VISIBLE94`
214. **ascender occurrence rate** — `glyph.topology.ascender_occurrence_rate` — interaction: `DEFER + MODULATE` — eligibility: `VISIBLE94`
215. **descender occurrence rate** — `glyph.topology.descender_occurrence_rate` — interaction: `DEFER + MODULATE` — eligibility: `VISIBLE94`

### 09C Glyph / Spatial Field (11)

216. **normalized ink-density field** — `glyph.spatial.normalized_ink_density_field` — interaction: `DEFER + MEASUREMENT` — eligibility: `ALL95`
217. **pixel/cell occupancy field** — `glyph.spatial.pixel_cell_occupancy_field` — interaction: `DEFER + MEASUREMENT` — eligibility: `ALL95`
218. **mean ink-density field** — `glyph.spatial.mean_ink_density_field` — interaction: `DEFER + MODULATE` — eligibility: `ALL95`
219. **ink-density variance field** — `glyph.spatial.ink_density_variance_field` — interaction: `DEFER + MODULATE` — eligibility: `ALL95`
220. **pixel/cell occupancy probability** — `glyph.spatial.pixel_cell_occupancy_probability` — interaction: `DEFER + MODULATE` — eligibility: `ALL95`
221. **spatial stability** — `glyph.spatial.spatial_stability` — interaction: `DEFER + MODULATE` — eligibility: `ALL95`
222. **spatial variation** — `glyph.spatial.spatial_variation` — interaction: `DEFER + MODULATE` — eligibility: `ALL95`
223. **font realization count** — `glyph.spatial.font_realization_count` — interaction: `DEFER + MODULATE` — eligibility: `ALL95`
224. **visual feature occurrence rate** — `glyph.spatial.visual_feature_occurrence_rate` — interaction: `DEFER + MODULATE` — eligibility: `ALL95`
225. **visual feature variance** — `glyph.spatial.visual_feature_variance` — interaction: `DEFER + MODULATE` — eligibility: `ALL95`
226. **font-conditioned realization** — `glyph.spatial.font_conditioned_realization` — interaction: `DEFER` — eligibility: `ALL95`

### 10 Character Confusability (12)

227. **pairwise visual distance** — `confusability.pairwise_visual_distance` — interaction: `RELATION + MEASUREMENT` — eligibility: `VISIBLE94`
228. **font-conditioned character distance** — `confusability.font_conditioned_character_distance` — interaction: `RELATION + DEFER + MEASUREMENT` — eligibility: `VISIBLE94`
229. **confusability probability** — `confusability.confusability_probability` — interaction: `RELATION + MODULATE` — eligibility: `VISIBLE94`
230. **nearest visual neighbors** — `confusability.nearest_visual_neighbors` — interaction: `RELATION` — eligibility: `VISIBLE94`
231. **distribution overlap** — `confusability.distribution_overlap` — interaction: `RELATION + MODULATE` — eligibility: `VISIBLE94`
232. **O-versus-0 similarity** — `confusability.o_versus_0_similarity` — interaction: `RELATION + MEASUREMENT` — eligibility: `0O`
233. **I-versus-l similarity** — `confusability.i_versus_l_similarity` — interaction: `RELATION + MEASUREMENT` — eligibility: `Il`
234. **I-versus-1 similarity** — `confusability.i_versus_1_similarity` — interaction: `RELATION + MEASUREMENT` — eligibility: `1I`
235. **S-versus-5 similarity** — `confusability.s_versus_5_similarity` — interaction: `RELATION + MEASUREMENT` — eligibility: `5S`
236. **B-versus-8 similarity** — `confusability.b_versus_8_similarity` — interaction: `RELATION + MEASUREMENT` — eligibility: `8B`
237. **period-versus-comma similarity** — `confusability.period_versus_comma_similarity` — interaction: `RELATION + MEASUREMENT` — eligibility: `,.`
238. **hyphen-versus-underscore similarity** — `confusability.hyphen_versus_underscore_similarity` — interaction: `RELATION + MEASUREMENT` — eligibility: `-_`

### 11 Orthographic / Positional Occurrence (20)

239. **absolute character position** — `orthographic.absolute_character_position` — interaction: `DEFER` — eligibility: `ALL95`
240. **relative word position** — `orthographic.relative_word_position` — interaction: `DEFER` — eligibility: `ALL95`
241. **relative sentence position** — `orthographic.relative_sentence_position` — interaction: `DEFER` — eligibility: `ALL95`
242. **word-initial** — `orthographic.word_initial` — interaction: `DEFER` — eligibility: `ALL95`
243. **word-medial** — `orthographic.word_medial` — interaction: `DEFER` — eligibility: `ALL95`
244. **word-final** — `orthographic.word_final` — interaction: `DEFER` — eligibility: `ALL95`
245. **sentence-initial** — `orthographic.sentence_initial` — interaction: `DEFER` — eligibility: `ALL95`
246. **sentence-medial** — `orthographic.sentence_medial` — interaction: `DEFER` — eligibility: `ALL95`
247. **sentence-final** — `orthographic.sentence_final` — interaction: `DEFER` — eligibility: `ALL95`
248. **line-initial** — `orthographic.line_initial` — interaction: `DEFER` — eligibility: `ALL95`
249. **line-final** — `orthographic.line_final` — interaction: `DEFER` — eligibility: `ALL95`
250. **preceded-by-space** — `orthographic.preceded_by_space` — interaction: `DEFER` — eligibility: `ALL95`
251. **followed-by-space** — `orthographic.followed_by_space` — interaction: `DEFER` — eligibility: `ALL95`
252. **distance to left boundary** — `orthographic.distance_to_left_boundary` — interaction: `DEFER` — eligibility: `ALL95`
253. **distance to right boundary** — `orthographic.distance_to_right_boundary` — interaction: `DEFER` — eligibility: `ALL95`
254. **word length** — `orthographic.word_length` — interaction: `DEFER` — eligibility: `ALL95`
255. **repeated-character status** — `orthographic.repeated_character_status` — interaction: `DEFER` — eligibility: `ALL95`
256. **character repetition count** — `orthographic.character_repetition_count` — interaction: `DEFER` — eligibility: `ALL95`
257. **left character** — `orthographic.left_character` — interaction: `DEFER + RELATION` — eligibility: `ALL95`
258. **right character** — `orthographic.right_character` — interaction: `DEFER + RELATION` — eligibility: `ALL95`

### 12 Corpus Statistics (20)

259. **unigram frequency** — `corpus.unigram_frequency` — interaction: `MODULATE` — eligibility: `ALL95`
260. **left-neighbor distribution** — `corpus.left_neighbor_distribution` — interaction: `RELATION + MODULATE` — eligibility: `ALL95`
261. **right-neighbor distribution** — `corpus.right_neighbor_distribution` — interaction: `RELATION + MODULATE` — eligibility: `ALL95`
262. **bigram frequency** — `corpus.bigram_frequency` — interaction: `RELATION + MODULATE` — eligibility: `ALL95`
263. **trigram frequency** — `corpus.trigram_frequency` — interaction: `RELATION + MODULATE` — eligibility: `ALL95`
264. **higher-order n-gram frequency** — `corpus.higher_order_n_gram_frequency` — interaction: `RELATION + MODULATE` — eligibility: `ALL95`
265. **next-character probability** — `corpus.next_character_probability` — interaction: `RELATION + MODULATE` — eligibility: `ALL95`
266. **previous-character probability** — `corpus.previous_character_probability` — interaction: `RELATION + MODULATE` — eligibility: `ALL95`
267. **conditional probability** — `corpus.conditional_probability` — interaction: `RELATION + MODULATE` — eligibility: `ALL95`
268. **pointwise mutual information** — `corpus.pointwise_mutual_information` — interaction: `RELATION + MODULATE` — eligibility: `ALL95`
269. **k-character history** — `corpus.k_character_history` — interaction: `DEFER + RELATION` — eligibility: `ALL95`
270. **next-character entropy** — `corpus.next_character_entropy` — interaction: `MODULATE` — eligibility: `ALL95`
271. **conditional entropy** — `corpus.conditional_entropy` — interaction: `MODULATE` — eligibility: `ALL95`
272. **mutual information** — `corpus.mutual_information` — interaction: `MODULATE` — eligibility: `ALL95`
273. **position distribution** — `corpus.position_distribution` — interaction: `MODULATE` — eligibility: `ALL95`
274. **word-initial frequency** — `corpus.word_initial_frequency` — interaction: `MODULATE` — eligibility: `ALL95`
275. **word-medial frequency** — `corpus.word_medial_frequency` — interaction: `MODULATE` — eligibility: `ALL95`
276. **word-final frequency** — `corpus.word_final_frequency` — interaction: `MODULATE` — eligibility: `ALL95`
277. **sentence-initial frequency** — `corpus.sentence_initial_frequency` — interaction: `MODULATE` — eligibility: `ALL95`
278. **sentence-final frequency** — `corpus.sentence_final_frequency` — interaction: `MODULATE` — eligibility: `ALL95`

### 13 Morphology (18)

279. **morpheme membership** — `morphology.morpheme_membership` — interaction: `DEFER` — eligibility: `ALL95`
280. **morpheme boundary** — `morphology.morpheme_boundary` — interaction: `DEFER` — eligibility: `ALL95`
281. **prefix participation** — `morphology.prefix_participation` — interaction: `DEFER` — eligibility: `ALL95`
282. **suffix participation** — `morphology.suffix_participation` — interaction: `DEFER` — eligibility: `ALL95`
283. **root participation** — `morphology.root_participation` — interaction: `DEFER` — eligibility: `ALL95`
284. **stem participation** — `morphology.stem_participation` — interaction: `DEFER` — eligibility: `ALL95`
285. **inflectional suffix participation** — `morphology.inflectional_suffix_participation` — interaction: `DEFER` — eligibility: `ALL95`
286. **derivational suffix participation** — `morphology.derivational_suffix_participation` — interaction: `DEFER` — eligibility: `ALL95`
287. **plural-marker participation** — `morphology.plural_marker_participation` — interaction: `DEFER` — eligibility: `ALL95`
288. **possessive-marker participation** — `morphology.possessive_marker_participation` — interaction: `DEFER` — eligibility: `ALL95`
289. **comparative-marker participation** — `morphology.comparative_marker_participation` — interaction: `DEFER` — eligibility: `ALL95`
290. **superlative-marker participation** — `morphology.superlative_marker_participation` — interaction: `DEFER` — eligibility: `ALL95`
291. **tense-marker participation** — `morphology.tense_marker_participation` — interaction: `DEFER` — eligibility: `ALL95`
292. **number-marker participation** — `morphology.number_marker_participation` — interaction: `DEFER` — eligibility: `ALL95`
293. **case-marker participation** — `morphology.case_marker_participation` — interaction: `DEFER` — eligibility: `ALL95`
294. **word-form relation** — `morphology.word_form_relation` — interaction: `DEFER` — eligibility: `ALL95`
295. **lemma relation** — `morphology.lemma_relation` — interaction: `DEFER` — eligibility: `ALL95`
296. **inflection relation** — `morphology.inflection_relation` — interaction: `DEFER` — eligibility: `ALL95`

### 14 Grammar / Syntax (14)

297. **part of speech** — `grammar.part_of_speech` — interaction: `DEFER` — eligibility: `ALL95`
298. **syntactic dependency relation** — `grammar.syntactic_dependency_relation` — interaction: `DEFER` — eligibility: `ALL95`
299. **syntactic head relation** — `grammar.syntactic_head_relation` — interaction: `DEFER` — eligibility: `ALL95`
300. **subject participation** — `grammar.subject_participation` — interaction: `DEFER` — eligibility: `ALL95`
301. **object participation** — `grammar.object_participation` — interaction: `DEFER` — eligibility: `ALL95`
302. **predicate participation** — `grammar.predicate_participation` — interaction: `DEFER` — eligibility: `ALL95`
303. **modifier participation** — `grammar.modifier_participation` — interaction: `DEFER` — eligibility: `ALL95`
304. **determiner participation** — `grammar.determiner_participation` — interaction: `DEFER` — eligibility: `ALL95`
305. **auxiliary participation** — `grammar.auxiliary_participation` — interaction: `DEFER` — eligibility: `ALL95`
306. **clause-boundary participation** — `grammar.clause_boundary_participation` — interaction: `DEFER` — eligibility: `ALL95`
307. **phrase-boundary participation** — `grammar.phrase_boundary_participation` — interaction: `DEFER` — eligibility: `ALL95`
308. **sentence-boundary participation** — `grammar.sentence_boundary_participation` — interaction: `DEFER` — eligibility: `ALL95`
309. **grammatical role distribution** — `grammar.grammatical_role_distribution` — interaction: `DEFER + MODULATE` — eligibility: `ALL95`
310. **context-conditioned grammatical role** — `grammar.context_conditioned_grammatical_role` — interaction: `DEFER + MODULATE` — eligibility: `ALL95`

### 15 Semantic / Lexical Relations (15)

311. **lexeme membership** — `semantic.lexeme_membership` — interaction: `DEFER` — eligibility: `ALL95`
312. **sense membership** — `semantic.sense_membership` — interaction: `DEFER` — eligibility: `ALL95`
313. **definition relation** — `semantic.definition_relation` — interaction: `DEFER` — eligibility: `ALL95`
314. **synonym relation** — `semantic.synonym_relation` — interaction: `DEFER` — eligibility: `ALL95`
315. **antonym relation** — `semantic.antonym_relation` — interaction: `DEFER` — eligibility: `ALL95`
316. **hypernym relation** — `semantic.hypernym_relation` — interaction: `DEFER` — eligibility: `ALL95`
317. **hyponym relation** — `semantic.hyponym_relation` — interaction: `DEFER` — eligibility: `ALL95`
318. **meronym relation** — `semantic.meronym_relation` — interaction: `DEFER` — eligibility: `ALL95`
319. **holonym relation** — `semantic.holonym_relation` — interaction: `DEFER` — eligibility: `ALL95`
320. **derivational relation** — `semantic.derivational_relation` — interaction: `DEFER` — eligibility: `ALL95`
321. **similar-to relation** — `semantic.similar_to_relation` — interaction: `DEFER` — eligibility: `ALL95`
322. **semantic-frame participation** — `semantic.semantic_frame_participation` — interaction: `DEFER` — eligibility: `ALL95`
323. **VerbNet class participation** — `semantic.verbnet_class_participation` — interaction: `DEFER` — eligibility: `ALL95`
324. **FrameNet frame participation** — `semantic.framenet_frame_participation` — interaction: `DEFER` — eligibility: `ALL95`
325. **WordNet synset participation** — `semantic.wordnet_synset_participation` — interaction: `DEFER` — eligibility: `ALL95`

### 16 Punctuation / Writing-System Roles (19)

326. **sentence terminator** — `punctuation.sentence_terminator` — interaction: `GATE + DISCRIMINATE` — eligibility: `!.?`
327. **clause separator** — `punctuation.clause_separator` — interaction: `GATE + DISCRIMINATE` — eligibility: `,:;`
328. **phrase separator** — `punctuation.phrase_separator` — interaction: `GATE + DISCRIMINATE` — eligibility: `,-:;`
329. **quotation delimiter** — `punctuation.quotation_delimiter` — interaction: `GATE + DISCRIMINATE` — eligibility: `QUOTES`
330. **parenthetical delimiter** — `punctuation.parenthetical_delimiter` — interaction: `GATE + DISCRIMINATE` — eligibility: `()[]{}`
331. **scope opener** — `punctuation.scope_opener` — interaction: `GATE + DISCRIMINATE` — eligibility: `GROUP_OPEN`
332. **scope closer** — `punctuation.scope_closer` — interaction: `GATE + DISCRIMINATE` — eligibility: `GROUP_CLOSE`
333. **list separator** — `punctuation.list_separator` — interaction: `GATE + DISCRIMINATE` — eligibility: `,;`
334. **decimal marker** — `punctuation.decimal_marker` — interaction: `GATE + DISCRIMINATE` — eligibility: `.`
335. **thousands separator** — `punctuation.thousands_separator` — interaction: `GATE + DISCRIMINATE` — eligibility: `,`
336. **apostrophe** — `punctuation.apostrophe` — interaction: `GATE + DISCRIMINATE` — eligibility: `'`
337. **hyphen** — `punctuation.hyphen` — interaction: `GATE + DISCRIMINATE` — eligibility: `-`
338. **dash** — `punctuation.dash` — interaction: `GATE + DISCRIMINATE` — eligibility: `-`
339. **underscore** — `punctuation.underscore` — interaction: `GATE + DISCRIMINATE` — eligibility: `_`
340. **colon** — `punctuation.colon` — interaction: `GATE + DISCRIMINATE` — eligibility: `:`
341. **semicolon** — `punctuation.semicolon` — interaction: `GATE + DISCRIMINATE` — eligibility: `;`
342. **question marker** — `punctuation.question_marker` — interaction: `GATE + DISCRIMINATE` — eligibility: `?`
343. **exclamation marker** — `punctuation.exclamation_marker` — interaction: `GATE + DISCRIMINATE` — eligibility: `!`
344. **quotation marker** — `punctuation.quotation_marker` — interaction: `GATE + DISCRIMINATE` — eligibility: `QUOTES`

### 17 Programming-Language Roles (20)

345. **identifier participation** — `programming.identifier_participation` — interaction: `DEFER + GATE + DISCRIMINATE` — eligibility: `ALL95`
346. **operator participation** — `programming.operator_participation` — interaction: `DEFER + GATE + DISCRIMINATE` — eligibility: `ALL95`
347. **assignment operator** — `programming.assignment_operator` — interaction: `DEFER + GATE + DISCRIMINATE` — eligibility: `ALL95`
348. **comparison operator** — `programming.comparison_operator` — interaction: `DEFER + GATE + DISCRIMINATE` — eligibility: `ALL95`
349. **arithmetic operator** — `programming.arithmetic_operator` — interaction: `DEFER + GATE + DISCRIMINATE` — eligibility: `ALL95`
350. **logical operator** — `programming.logical_operator` — interaction: `DEFER + GATE + DISCRIMINATE` — eligibility: `ALL95`
351. **bitwise operator** — `programming.bitwise_operator` — interaction: `DEFER + GATE + DISCRIMINATE` — eligibility: `ALL95`
352. **delimiter** — `programming.delimiter` — interaction: `DEFER + GATE + DISCRIMINATE` — eligibility: `ALL95`
353. **scope opener** — `programming.scope_opener` — interaction: `DEFER + GATE + DISCRIMINATE` — eligibility: `ALL95`
354. **scope closer** — `programming.scope_closer` — interaction: `DEFER + GATE + DISCRIMINATE` — eligibility: `ALL95`
355. **indexing delimiter** — `programming.indexing_delimiter` — interaction: `DEFER + GATE + DISCRIMINATE` — eligibility: `ALL95`
356. **argument separator** — `programming.argument_separator` — interaction: `DEFER + GATE + DISCRIMINATE` — eligibility: `ALL95`
357. **statement terminator** — `programming.statement_terminator` — interaction: `DEFER + GATE + DISCRIMINATE` — eligibility: `ALL95`
358. **comment marker** — `programming.comment_marker` — interaction: `DEFER + GATE + DISCRIMINATE` — eligibility: `ALL95`
359. **string delimiter** — `programming.string_delimiter` — interaction: `DEFER + GATE + DISCRIMINATE` — eligibility: `ALL95`
360. **escape marker** — `programming.escape_marker` — interaction: `DEFER + GATE + DISCRIMINATE` — eligibility: `ALL95`
361. **member-access marker** — `programming.member_access_marker` — interaction: `DEFER + GATE + DISCRIMINATE` — eligibility: `ALL95`
362. **decorator marker** — `programming.decorator_marker` — interaction: `DEFER + GATE + DISCRIMINATE` — eligibility: `ALL95`
363. **type-syntax participation** — `programming.type_syntax_participation` — interaction: `DEFER + GATE + DISCRIMINATE` — eligibility: `ALL95`
364. **language-conditioned token role** — `programming.language_conditioned_token_role` — interaction: `DEFER + GATE + DISCRIMINATE` — eligibility: `ALL95`

### 18 Mathematical-Syntax Roles (22)

365. **operator** — `math_syntax.operator` — interaction: `DEFER + GATE + DISCRIMINATE` — eligibility: `ALL95`
366. **relation** — `math_syntax.relation` — interaction: `DEFER + GATE + DISCRIMINATE` — eligibility: `ALL95`
367. **equality relation** — `math_syntax.equality_relation` — interaction: `DEFER + GATE + DISCRIMINATE` — eligibility: `ALL95`
368. **inequality relation** — `math_syntax.inequality_relation` — interaction: `DEFER + GATE + DISCRIMINATE` — eligibility: `ALL95`
369. **sign** — `math_syntax.sign` — interaction: `DEFER + GATE + DISCRIMINATE` — eligibility: `ALL95`
370. **variable** — `math_syntax.variable` — interaction: `DEFER + GATE + DISCRIMINATE` — eligibility: `ALL95`
371. **unknown** — `math_syntax.unknown` — interaction: `DEFER + GATE + DISCRIMINATE` — eligibility: `ALL95`
372. **constant** — `math_syntax.constant` — interaction: `DEFER + GATE + DISCRIMINATE` — eligibility: `ALL95`
373. **operand** — `math_syntax.operand` — interaction: `DEFER + GATE + DISCRIMINATE` — eligibility: `ALL95`
374. **coefficient** — `math_syntax.coefficient` — interaction: `DEFER + GATE + DISCRIMINATE` — eligibility: `ALL95`
375. **exponent** — `math_syntax.exponent` — interaction: `DEFER + GATE + DISCRIMINATE` — eligibility: `ALL95`
376. **radical marker** — `math_syntax.radical_marker` — interaction: `DEFER + GATE + DISCRIMINATE` — eligibility: `ALL95`
377. **fraction separator** — `math_syntax.fraction_separator` — interaction: `DEFER + GATE + DISCRIMINATE` — eligibility: `ALL95`
378. **decimal marker** — `math_syntax.decimal_marker` — interaction: `DEFER + GATE + DISCRIMINATE` — eligibility: `ALL95`
379. **grouping opener** — `math_syntax.grouping_opener` — interaction: `DEFER + GATE + DISCRIMINATE` — eligibility: `ALL95`
380. **grouping closer** — `math_syntax.grouping_closer` — interaction: `DEFER + GATE + DISCRIMINATE` — eligibility: `ALL95`
381. **set delimiter** — `math_syntax.set_delimiter` — interaction: `DEFER + GATE + DISCRIMINATE` — eligibility: `ALL95`
382. **function-argument delimiter** — `math_syntax.function_argument_delimiter` — interaction: `DEFER + GATE + DISCRIMINATE` — eligibility: `ALL95`
383. **coordinate separator** — `math_syntax.coordinate_separator` — interaction: `DEFER + GATE + DISCRIMINATE` — eligibility: `ALL95`
384. **ratio marker** — `math_syntax.ratio_marker` — interaction: `DEFER + GATE + DISCRIMINATE` — eligibility: `ALL95`
385. **percentage marker** — `math_syntax.percentage_marker` — interaction: `DEFER + GATE + DISCRIMINATE` — eligibility: `ALL95`
386. **mathematical role conditioned on context** — `math_syntax.context_conditioned_role` — interaction: `DEFER + GATE + DISCRIMINATE` — eligibility: `ALL95`

### 19 Contextual / Situated Character State (17)

387. **active pronunciation** — `context.active_pronunciation` — interaction: `DEFER` — eligibility: `LETTERS`
388. **active phoneme** — `context.active_phoneme` — interaction: `DEFER` — eligibility: `LETTERS`
389. **active articulatory properties** — `context.active_articulatory_properties` — interaction: `DEFER` — eligibility: `LETTERS`
390. **active acoustic realization** — `context.active_acoustic_realization` — interaction: `DEFER` — eligibility: `LETTERS`
391. **active morphological role** — `context.active_morphological_role` — interaction: `DEFER` — eligibility: `ALL95`
392. **active grammatical role** — `context.active_grammatical_role` — interaction: `DEFER` — eligibility: `ALL95`
393. **active semantic role** — `context.active_semantic_role` — interaction: `DEFER` — eligibility: `ALL95`
394. **active punctuation role** — `context.active_punctuation_role` — interaction: `DEFER` — eligibility: `ALL95`
395. **active programming role** — `context.active_programming_role` — interaction: `DEFER` — eligibility: `ALL95`
396. **active mathematical role** — `context.active_mathematical_role` — interaction: `DEFER` — eligibility: `ALL95`
397. **active delimiter role** — `context.active_delimiter_role` — interaction: `DEFER` — eligibility: `ALL95`
398. **active operator role** — `context.active_operator_role` — interaction: `DEFER` — eligibility: `ALL95`
399. **active variable role** — `context.active_variable_role` — interaction: `DEFER` — eligibility: `ALL95`
400. **active numeric role** — `context.active_numeric_role` — interaction: `DEFER` — eligibility: `ALL95`
401. **active boundary role** — `context.active_boundary_role` — interaction: `DEFER` — eligibility: `ALL95`
402. **active scope role** — `context.active_scope_role` — interaction: `DEFER` — eligibility: `ALL95`
403. **context-conditioned capability activation** — `context.context_conditioned_capability_activation` — interaction: `DEFER` — eligibility: `ALL95`

### 20 Character Capability Distributions (10)

404. **probability of phonetic feature** — `capability.probability_phonetic_feature` — interaction: `MODULATE` — eligibility: `LETTERS`
405. **probability of articulatory feature** — `capability.probability_articulatory_feature` — interaction: `MODULATE` — eligibility: `LETTERS`
406. **probability of visual feature** — `capability.probability_visual_feature` — interaction: `MODULATE` — eligibility: `ALL95`
407. **probability of morphological role** — `capability.probability_morphological_role` — interaction: `MODULATE` — eligibility: `ALL95`
408. **probability of syntactic role** — `capability.probability_syntactic_role` — interaction: `MODULATE` — eligibility: `ALL95`
409. **probability of punctuation role** — `capability.probability_punctuation_role` — interaction: `MODULATE` — eligibility: `ALL95`
410. **probability of programming role** — `capability.probability_programming_role` — interaction: `MODULATE` — eligibility: `ALL95`
411. **probability of mathematical role** — `capability.probability_mathematical_role` — interaction: `MODULATE` — eligibility: `ALL95`
412. **probability of word position** — `capability.probability_word_position` — interaction: `MODULATE` — eligibility: `ALL95`
413. **probability of contextual realization** — `capability.probability_contextual_realization` — interaction: `MODULATE` — eligibility: `ALL95`

### 21 Evidence / Provenance (19)

414. **source dataset** — `evidence.source_dataset` — interaction: `MODULATE` — eligibility: `ALL95`
415. **source standard** — `evidence.source_standard` — interaction: `MODULATE` — eligibility: `ALL95`
416. **source version** — `evidence.source_version` — interaction: `MODULATE` — eligibility: `ALL95`
417. **source record** — `evidence.source_record` — interaction: `MODULATE` — eligibility: `ALL95`
418. **evidence class** — `evidence.evidence_class` — interaction: `MODULATE` — eligibility: `ALL95`
419. **observation count** — `evidence.observation_count` — interaction: `MODULATE` — eligibility: `ALL95`
420. **support count** — `evidence.support_count` — interaction: `MODULATE` — eligibility: `ALL95`
421. **contradiction count** — `evidence.contradiction_count` — interaction: `MODULATE` — eligibility: `ALL95`
422. **sample size** — `evidence.sample_size` — interaction: `MODULATE` — eligibility: `ALL95`
423. **coverage** — `evidence.coverage` — interaction: `MODULATE` — eligibility: `ALL95`
424. **occurrence rate** — `evidence.occurrence_rate` — interaction: `MODULATE` — eligibility: `ALL95`
425. **mean** — `evidence.mean` — interaction: `MODULATE` — eligibility: `ALL95`
426. **variance** — `evidence.variance` — interaction: `MODULATE` — eligibility: `ALL95`
427. **minimum** — `evidence.minimum` — interaction: `MODULATE` — eligibility: `ALL95`
428. **maximum** — `evidence.maximum` — interaction: `MODULATE` — eligibility: `ALL95`
429. **confidence** — `evidence.confidence` — interaction: `MODULATE` — eligibility: `ALL95`
430. **missing-data status** — `evidence.missing_data_status` — interaction: `MODULATE` — eligibility: `ALL95`
431. **derivation method** — `evidence.derivation_method` — interaction: `MODULATE` — eligibility: `ALL95`
432. **compilation method** — `evidence.compilation_method` — interaction: `MODULATE` — eligibility: `ALL95`

### 22 Source Classes (5)

433. **authoritative standard** — `source_class.authoritative_standard` — interaction: `MODULATE` — eligibility: `ALL95`
434. **established database** — `source_class.established_database` — interaction: `MODULATE` — eligibility: `ALL95`
435. **corpus-derived statistic** — `source_class.corpus_derived_statistic` — interaction: `MODULATE` — eligibility: `ALL95`
436. **published physical measurement** — `source_class.published_physical_measurement` — interaction: `MODULATE` — eligibility: `ALL95`
437. **deterministic extraction from published raw data** — `source_class.deterministic_extraction_from_published_raw_data` — interaction: `MODULATE` — eligibility: `ALL95`

## Complete row axis — 95 printable ASCII characters

```text
01. ASCII  32   '0x20  [space]     SPACE
02. ASCII  33   '0x21  !           EXCLAMATION MARK
03. ASCII  34   '0x22  "           QUOTATION MARK
04. ASCII  35   '0x23  #           NUMBER SIGN
05. ASCII  36   '0x24  $           DOLLAR SIGN
06. ASCII  37   '0x25  %           PERCENT SIGN
07. ASCII  38   '0x26  &           AMPERSAND
08. ASCII  39   '0x27  '           APOSTROPHE
09. ASCII  40   '0x28  (           LEFT PARENTHESIS
10. ASCII  41   '0x29  )           RIGHT PARENTHESIS
11. ASCII  42   '0x2A  *           ASTERISK
12. ASCII  43   '0x2B  +           PLUS SIGN
13. ASCII  44   '0x2C  ,           COMMA
14. ASCII  45   '0x2D  -           HYPHEN-MINUS
15. ASCII  46   '0x2E  .           FULL STOP
16. ASCII  47   '0x2F  /           SOLIDUS
17. ASCII  48   '0x30  0           DIGIT ZERO
18. ASCII  49   '0x31  1           DIGIT ONE
19. ASCII  50   '0x32  2           DIGIT TWO
20. ASCII  51   '0x33  3           DIGIT THREE
21. ASCII  52   '0x34  4           DIGIT FOUR
22. ASCII  53   '0x35  5           DIGIT FIVE
23. ASCII  54   '0x36  6           DIGIT SIX
24. ASCII  55   '0x37  7           DIGIT SEVEN
25. ASCII  56   '0x38  8           DIGIT EIGHT
26. ASCII  57   '0x39  9           DIGIT NINE
27. ASCII  58   '0x3A  :           COLON
28. ASCII  59   '0x3B  ;           SEMICOLON
29. ASCII  60   '0x3C  <           LESS-THAN SIGN
30. ASCII  61   '0x3D  =           EQUALS SIGN
31. ASCII  62   '0x3E  >           GREATER-THAN SIGN
32. ASCII  63   '0x3F  ?           QUESTION MARK
33. ASCII  64   '0x40  @           COMMERCIAL AT
34. ASCII  65   '0x41  A           LATIN CAPITAL LETTER A
35. ASCII  66   '0x42  B           LATIN CAPITAL LETTER B
36. ASCII  67   '0x43  C           LATIN CAPITAL LETTER C
37. ASCII  68   '0x44  D           LATIN CAPITAL LETTER D
38. ASCII  69   '0x45  E           LATIN CAPITAL LETTER E
39. ASCII  70   '0x46  F           LATIN CAPITAL LETTER F
40. ASCII  71   '0x47  G           LATIN CAPITAL LETTER G
41. ASCII  72   '0x48  H           LATIN CAPITAL LETTER H
42. ASCII  73   '0x49  I           LATIN CAPITAL LETTER I
43. ASCII  74   '0x4A  J           LATIN CAPITAL LETTER J
44. ASCII  75   '0x4B  K           LATIN CAPITAL LETTER K
45. ASCII  76   '0x4C  L           LATIN CAPITAL LETTER L
46. ASCII  77   '0x4D  M           LATIN CAPITAL LETTER M
47. ASCII  78   '0x4E  N           LATIN CAPITAL LETTER N
48. ASCII  79   '0x4F  O           LATIN CAPITAL LETTER O
49. ASCII  80   '0x50  P           LATIN CAPITAL LETTER P
50. ASCII  81   '0x51  Q           LATIN CAPITAL LETTER Q
51. ASCII  82   '0x52  R           LATIN CAPITAL LETTER R
52. ASCII  83   '0x53  S           LATIN CAPITAL LETTER S
53. ASCII  84   '0x54  T           LATIN CAPITAL LETTER T
54. ASCII  85   '0x55  U           LATIN CAPITAL LETTER U
55. ASCII  86   '0x56  V           LATIN CAPITAL LETTER V
56. ASCII  87   '0x57  W           LATIN CAPITAL LETTER W
57. ASCII  88   '0x58  X           LATIN CAPITAL LETTER X
58. ASCII  89   '0x59  Y           LATIN CAPITAL LETTER Y
59. ASCII  90   '0x5A  Z           LATIN CAPITAL LETTER Z
60. ASCII  91   '0x5B  [           LEFT SQUARE BRACKET
61. ASCII  92   '0x5C  \           REVERSE SOLIDUS
62. ASCII  93   '0x5D  ]           RIGHT SQUARE BRACKET
63. ASCII  94   '0x5E  ^           CIRCUMFLEX ACCENT
64. ASCII  95   '0x5F  _           LOW LINE
65. ASCII  96   '0x60  `           GRAVE ACCENT
66. ASCII  97   '0x61  a           LATIN SMALL LETTER A
67. ASCII  98   '0x62  b           LATIN SMALL LETTER B
68. ASCII  99   '0x63  c           LATIN SMALL LETTER C
69. ASCII 100   '0x64  d           LATIN SMALL LETTER D
70. ASCII 101   '0x65  e           LATIN SMALL LETTER E
71. ASCII 102   '0x66  f           LATIN SMALL LETTER F
72. ASCII 103   '0x67  g           LATIN SMALL LETTER G
73. ASCII 104   '0x68  h           LATIN SMALL LETTER H
74. ASCII 105   '0x69  i           LATIN SMALL LETTER I
75. ASCII 106   '0x6A  j           LATIN SMALL LETTER J
76. ASCII 107   '0x6B  k           LATIN SMALL LETTER K
77. ASCII 108   '0x6C  l           LATIN SMALL LETTER L
78. ASCII 109   '0x6D  m           LATIN SMALL LETTER M
79. ASCII 110   '0x6E  n           LATIN SMALL LETTER N
80. ASCII 111   '0x6F  o           LATIN SMALL LETTER O
81. ASCII 112   '0x70  p           LATIN SMALL LETTER P
82. ASCII 113   '0x71  q           LATIN SMALL LETTER Q
83. ASCII 114   '0x72  r           LATIN SMALL LETTER R
84. ASCII 115   '0x73  s           LATIN SMALL LETTER S
85. ASCII 116   '0x74  t           LATIN SMALL LETTER T
86. ASCII 117   '0x75  u           LATIN SMALL LETTER U
87. ASCII 118   '0x76  v           LATIN SMALL LETTER V
88. ASCII 119   '0x77  w           LATIN SMALL LETTER W
89. ASCII 120   '0x78  x           LATIN SMALL LETTER X
90. ASCII 121   '0x79  y           LATIN SMALL LETTER Y
91. ASCII 122   '0x7A  z           LATIN SMALL LETTER Z
92. ASCII 123   '0x7B  {           LEFT CURLY BRACKET
93. ASCII 124   '0x7C  |           VERTICAL LINE
94. ASCII 125   '0x7D  }           RIGHT CURLY BRACKET
95. ASCII 126   '0x7E  ~           TILDE
```

## Cell-state legend

ASCII95 Matrix Legend and Canonical Interpretation |  | 
Code | Meaning | Interpretation
X | Impossible / ineligible | This character cannot participate in this attribute under the canonical gate.
1 | Fixed positive | Intrinsic/derived boolean is true for this character.
0 | Fixed negative | Attribute is defined for this character but the boolean is false.
E | Eligible / deferred | Can exist, but requires context/source/defer-axis resolution.
R | Relation | Character can participate in a pair/triple/higher-arity relation.
M | Measurement | Continuous measurement can exist after its declared realization axis is bound.
U | Modulator / statistic | Evidence statistic/provenance can exist; never a primitive coordinate.
V | Resolved scalar category/value slot | A non-boolean scalar/categorical value is defined for eligible characters.
K | Key | Identity field; never a weight input.
S | Structural / derived | No independent free degree of freedom.
Matrix property | Value | 
Printable ASCII rows | 95 | 
Canonical attribute columns | 437 | 
First attribute column | F | 
Last attribute column | PZ | 
Source duplicate collapsed | Consonant-place 'pharyngeal' repeated twice in source taxonomy; retained once. | 
Unicode math intrinsic set | +<=>^|~ | 
Programming/math role hints | Hints only; contextual roles remain source/language/notation derived. | 
Permanent invariant |  | 
X means structurally impossible, not merely unobserved. |  | 
Eligibility is not activation. |  | 
Contextual properties are not permanently assigned to characters. |  | 
Missing/undefined is not zero. |  | 
Relations remain relational unless an explicit projection is compiled. |  | 
Measurements require declared deterministic transforms before ranking/selection. |  | 

## Structural reading

```text
character occurrence
      |
      v
one of 95 canonical ASCII rows
      |
      +---- intersects ----> each of 437 named representation columns
                              |
                              v
                    canonical cell state
                              |
                              v
             explicit representation field
```

The 437 columns are named, inspectable representation dimensions. They are not asserted to be 437 independent physical degrees of freedom. The matrix preserves distinctions among fixed state, eligibility, relation, measurement, modulation/statistics, resolved values, key identity, structural/derived state, and structural inapplicability.