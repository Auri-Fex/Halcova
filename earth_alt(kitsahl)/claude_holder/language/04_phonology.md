---
title: "Sybari Phonology & Orthography"
project: "Oracles-TBD"
section: "03_language"
type: "linguistic-reference"
version: "1.0"
created: "2025-12-21"
tags: [language, sybari, phonology, pronunciation, orthography]
related: [01_language_overview, 05_morphology]
---

# Sybari Phonology & Orthography

**Purpose**: How Sybari sounds and how it's written

**Design Principle**: Open syllables, no complex clusters, relatively simple phonology (influenced by Tav'mora)

---

## Consonants

### Inventory

| Manner | Labial | Dental | Alveolar | Palatal | Velar | Glottal |
|--------|--------|--------|----------|---------|-------|---------|
| **Stops** | p, b | t, d | | | k, g | ' (glottal) |
| **Fricatives** | f, v | th | s, z | sh | | h |
| **Nasals** | m | | n | | | |
| **Liquids** | | | l, r | | | |
| **Glides** | | | | y | w | |

**Total**: 21 consonants

---

### Pronunciation Guide

**Stops**:
- **p, t, k**: Like English (unaspirated)
- **b, d, g**: Like English (voiced)
- **'** (apostrophe): Glottal stop (brief catch in throat; like "uh-oh")

**Fricatives**:
- **f, v**: Like English
- **th**: Like "thin" (never "this")
- **s, z**: Like English
- **sh**: Like "ship"
- **h**: Like English

**Nasals, Liquids, Glides**:
- **m, n, l, r, y, w**: Like English

---

### Distribution

**Initial Position**: All consonants allowed
- peth (place)
- kael (sight)
- 'im (to/at)

**Medial Position**: All consonants; no clusters
- petak (location)
- kaeloth (seer)

**Final Position**: Only p, t, k, m, n, th, sh
- vep (end)
- kaeth (oracle device)
- shen (speak)

**Clusters**: NOT ALLOWED in native Sybari
- No "str", "spl", "kt" etc.
- Loanwords from Common may have clusters (adapted)

---

## Vowels

### Inventory

| Height | Front | Central | Back |
|--------|-------|---------|------|
| **High** | i | | u |
| **Mid** | e | | o |
| **Low** | | a | |

**Total**: 5 vowels (simple system)

---

### Pronunciation

- **i**: Like "see"
- **e**: Like "say" (never "pet")
- **a**: Like "father"
- **o**: Like "go"
- **u**: Like "boot"

---

### Diphthongs

| Diphthong | Pronunciation | Example |
|-----------|---------------|---------|
| **ae** | "eye" | kael ("k-eye-l") |
| **ei** | "ay" | keil ("k-ay-l") |
| **ai** | "eye" | kail ("k-eye-l") |
| **au** | "ow" | naul ("n-ow-l") |
| **oi** | "oy" | koi ("k-oy") |

**Note**: Diphthongs count as single vowel for syllable structure

---

## Syllable Structure

### Pattern: (C)V(C)

**Components**:
- **(C)**: Optional initial consonant
- **V**: Required vowel or diphthong
- **(C)**: Optional final consonant (only p, t, k, m, n, th, sh)

**Valid Syllables**:
- V: a, i, u
- CV: ka, shen, tav
- VC: im, eth, oth
- CVC: kael, petak, vesh

**Invalid**:
- CCV: ✗ stra (no clusters)
- VCC: ✗ ampt (only one final consonant)
- CVCC: ✗ kalmt (no clusters)

---

### Examples

**Monosyllabic**:
- kael (sight): CV → CVVC
- mar (true): CVC
- im (to): VC

**Disyllabic**:
- petak (location): CV-CVC
- kaeloth (seer): CVVC-CVC
- nareta (forecast): CV-CV-CV

**Trisyllabic**:
- naresheth (prophecy-worker): CV-CV-CVC
- veshkaeim (violence-location): CVC-CVV-VC

---

## Stress

### Rules

**Default**: Stress falls on **penultimate** (second-to-last) syllable

**Examples**:
- pe-TAK (location)
- na-RE-ta (forecast)
- KAE-loth (seer, only two syllables so first stressed)

**Exceptions**:
- Evidential suffixes don't shift stress
  - kael (sight): KAEL
  - kaelmar (sight-witnessed): KAEL-mar (stress stays on root)

**Compounds**: Each element keeps its own stress
- vesh-nareta: VESH + na-RE-ta

---

## Orthography (Writing System)

### Roman Alphabet

Sybari uses Roman alphabet (26 letters) with modifications:

**Standard Letters**: a, b, d, e, f, g, h, i, k, l, m, n, o, p, r, s, t, u, v, w, y, z

**Digraphs** (two letters, one sound):
- **ae**: /ai/ as in "eye"
- **ei**: /ei/ as in "say"
- **sh**: /ʃ/ as in "ship"
- **th**: /θ/ as in "thin"

**Special Characters**:
- **'** (apostrophe): Glottal stop
- **-** (hyphen): Marks morpheme boundaries in formal writing

---

### Spelling Rules

**Phonemic**: One letter/digraph = one sound (mostly)
- kael is always pronounced "k-eye-l"
- shen is always "sh-en"

**Morpheme Boundaries**: Marked with hyphen in formal texts
- Formal: kael-oth-el (sight-agent-plural)
- Informal: kaelothel (same meaning, no hyphens)

**Capitalization**: 
- Proper nouns (personal names, place names)
- First word of sentence
- Technical Sybari capitalizes all affixes in formal documents (kael-Oth-El)

---

## Phonological Changes (Historical)

### Lost Features from Source Languages

**Tones** (from Shen'kali):
- Original Shen'kali had 3 tones (high, mid, low)
- Europeans couldn't hear/produce them
- **Eliminated in Sybari** (created homophones; context disambiguates)

**Honorifics** (from Tav'mora):
- Original Tav'mora had complex honorific sounds (special consonants for respect)
- **Eliminated**: "Egalitarian" pretense (really: Europeans didn't want to show respect)

**Consonant Clusters** (from Kael'nir):
- Original Kael'nir allowed clusters (kr-, gl-, -kt, -mn)
- **Simplified**: Open syllable structure imposed

---

### European Influence

**New Sounds** (not in original languages):
- **z**: Added from European languages
- **j**: Rare; appears in loanwords only

**Standardized Pronunciation**:
- Original languages had regional variation
- Sybari enforces single "correct" pronunciation
- **Purpose**: Control; mark education level

---

## Register Variation

### Technical Sybari (Formal)

**Characteristics**:
- Precise pronunciation (every sound enunciated)
- Glottal stops pronounced
- Hyphens in writing
- No contractions

**Example**: kael-oth-el mar-shen petak-nul-im
(sight-agent-plural true-speak location-place-at)
"The seers truthfully speak at the location"

---

### Bureaucratic Sybari (Standard)

**Characteristics**:
- Slightly relaxed (glottal stops sometimes dropped)
- Fewer hyphens
- Standardized phrases (memorized)

**Example**: kaelothel marshen petaknulim
(Same meaning, less formal writing)

---

### Street Sybari (Informal)

**Characteristics**:
- Rapid speech (sounds run together)
- Vowel reduction (unstressed vowels → schwa)
- Mixed with Common (code-switching)

**Example**: "Kaeloth says vesh-prob high, yeah?"
(Seer says violence-probability high, right?)
- Drops evidentials
- Mixes Common grammar
- Seeks confirmation in Common

---

## Forbidden Pronunciations

### Indigenous "Corruptions" (Criminalized)

**Traditional Kael'nir Features** (Illegal if used):
- Consonant clusters (krae instead of karae)
- Different stress patterns (KA-el-oth instead of kael-OTH)
- **Charge**: "Linguistic Corruption" (Bureau arrest)

**Tav'mora Features** (Illegal):
- Honorific sounds (special /p/ and /t/ for respected persons)
- Open syllable extensions (kae-la-el instead of kael-el)

**Shen'kali Features** (Illegal):
- Tonal pronunciation (high tone kael ≠ low tone kael)
- Musical phrasing (singing oracle terms)

**Enforcement**: Bureau monitors public speech; arrest indigenous speakers using traditional features

---

## Pronunciation Examples

### Common Words

| Sybari | IPA | English Sound-Alike | Meaning |
|--------|-----|---------------------|---------|
| kael | kaɪl | "kyle" | sight |
| shen | ʃɛn | "shen" | speak |
| petak | pɛtɑk | "peh-tahk" | location |
| nareta | nɑɹɛtɑ | "nah-reh-tah" | forecast |
| kaeth | kaɪθ | "kai-th" | oracle device |
| vesh | vɛʃ | "vesh" | violence |
| mora | moɹɑ | "moh-rah" | truth |
| drift | dɹɪft | "drift" (same) | temporal instability |

---

### Full Sentences

**Technical Sybari**:
- **Written**: Kael-oth-el shen-mar nareta-kaeth-im petak-nul-shen
- **Pronunciation**: "KAE-loth-el SHEN-mar na-RE-ta-KAETH-im pe-TAK-nul-SHEN"
- **Literal**: Sight-agent-plural speak-witnessed forecast-device-at location-place-speak
- **English**: "The seers witnessed the oracle device speaking at the location"

**Street Sybari**:
- **Written**: Kaeloth says kaeth broke, yeah?
- **Pronunciation**: "KAE-loth sez KAETH broke, ya?"
- **Literal**: Seer says device broke, confirmation?
- **English**: "The seer says the oracle is broken, right?"

---

## Phonological Aesthetics

### Intended Feel

**Open, flowing**: CV structure creates smooth sound
**Technical but approachable**: Not too alien; learnable
**Hints of otherness**: Glottal stops, diphthongs mark it as "exotic"

**Contrast**:
- **Technical Sybari**: Precise, formal, educated (reinforces class)
- **Street Sybari**: Relaxed, mixed, practical (marks working-class)

---

**Navigation**: [Return to Language](README.md) | [Previous: Overview](01_language_overview.md) | [Next: Morphology](05_morphology.md)
