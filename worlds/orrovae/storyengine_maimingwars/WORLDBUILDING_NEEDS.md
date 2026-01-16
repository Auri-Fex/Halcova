# MAIMING WARS — WORLDBUILDING NEEDS

**Purpose**: Aggregated list of all worldbuilding elements required by the story that need development, expansion, or conflict resolution. This document is populated from scene-level dependency flags.

**Last Updated**: January 4, 2026
**Status**: Living document - updated as scenes are planned

---

## P1 BLOCKER STATUS

**✅ BOOK 1 READY TO DRAFT** — All critical blockers resolved

| Blocker | Resolution File | Date |
|---------|-----------------|------|
| Thread-Memory Mechanism | `01_core_systems/thread_memory.md` | Jan 4, 2026 |
| Weaponized Hollowing Method | `01_core_systems/weaponized_hollowing.md` | Jan 4, 2026 |
| The Unmaimed Movement | `01_core_systems/the_unmaimed.md` | Jan 4, 2026 |
| Unseeded Enclaves | `02_geography/vabakoda_enclave.md` | Jan 4, 2026 |
| Named Antagonists | `storyengine_maimingwars/ANTAGONIST_PROFILES.md` | Jan 4, 2026 |
| First Hollowing Incident | `storyengine_maimingwars/VESSBERG_ASSASSINATION.md` | Jan 4, 2026 |
| Fivefold Doctrine Terms | `08_language/fivefold_doctrine_terms.md` | Jan 4, 2026 |
| Säide Resonance Tactics | `01_core_systems/resonance_tactics.md` | Jan 4, 2026 |
| Surface Run Equipment | `01_core_systems/surface_run_equipment.md` | Jan 4, 2026 |

---

## STATUS KEY

| Status | Meaning | Action Required |
|--------|---------|-----------------|
| 🔴 NEEDED | Not developed, scene blocked | Must create before drafting |
| 🟡 PARTIAL | Exists but insufficient | Expand or clarify |
| 🟢 EXISTS | Fully developed | Reference canon |
| ⚠️ CONFLICT | Canon conflicts with story needs | Resolve contradiction |
| 🔵 FLEXIBLE | Can be developed either way | Note decision when made |

---

## PRIORITY KEY

| Priority | Definition |
|----------|------------|
| P1 - CRITICAL | Required for Book 1 scenes |
| P2 - HIGH | Required for Books 2-3 |
| P3 - MEDIUM | Required for Books 4-5 |
| P4 - LOW | Enhancement, not blocker |

---

## SÄIDESOLU MECHANICS [SÄIDE]

### Thread-Memory / Lineage Inheritance 🔴 NEEDED - P1

**Required By**: B1.P1.C1.S1, B1.P2.C3.S2, [multiple scenes]

**Story Need**: 
- Replaces soul-based reincarnation with biological memory inheritance
- Explains why maiming is worse than death (damages lineage)
- Provides non-religious basis for cultural horror around maiming

**Canon Status**: 
- Current docs reference "soul-thread" (to be replaced)
- Säide spore reproduction documented in `saide_complete_reference.md`
- No current mechanism for memory/pattern inheritance

**Development Required**:
```
1. MECHANISM: How do Säide colonies carry host impressions?
   - Through the Covenant bond? Ancestral echo?
   - Pattern imprint from lineage-thread?
   - What survives into spores?
   - How does this affect new host's Pattern?
   - NOTE: Keep explanation mystical, not clinical (see GENRE_STYLE_GUIDE.md)

2. TERMINOLOGY: Replace soul-language
   - "Soul-thread" → "Lineage-thread" or "Thread-Memory"
   - "Thread-debt" → "Lineage-damage" or "Pattern-corruption"
   - Need full terminology pass on MAIMING_WARS_SAGA.md

3. CULTURAL BELIEFS:
   - How do people know about this? (Historical observation? Säide-Writ research?)
   - How does doctrine interpret this? (Fivefold angle)
   - How do Unseeded view this?

4. MECHANICS FOR SCENES:
   - Can you sense your Säide's previous hosts?
   - Does dream-bleed include lineage memories?
   - How does this differ from Hollowing memories?
```

**Conflicts**: Soul-thread language in MAIMING_WARS_SAGA.md needs replacement

---

### Weaponized Hollowing Mechanics 🟡 PARTIAL - P1

**Required By**: B1.P2.C4.S1, B1.P3.C1.S3, [assassination scene]

**Story Need**:
- First documented "weaponized Hollowing" incident
- Must be plausible within established rules
- Different from natural Hollowing in speed/method

**Canon Status**:
- Hollowing stages documented in `hollowing_complete.md`
- Natural causes listed (starvation, trauma, overuse, addiction)
- No current mechanism for *induced* Hollowing

**Development Required**:
```
1. METHOD: How to force Hollowing externally?
   Options to explore:
   - Covenant override/corruption?
   - Chemical agent targeting Säide?
   - Resonance manipulation?
   - Starvation acceleration?
   - Combination approach?

2. SPEED: How fast can induced Hollowing occur?
   - Natural: weeks to months to years
   - Induced: days? hours?

3. DETECTION: Can Säide-Writs identify induced vs. natural?
   - Forensic markers?
   - Legal implications?

4. COUNTERMEASURES: What defenses exist?
   - Covenant clauses?
   - Medical intervention?
   - Why aren't these universal?
```

**Conflicts**: None, but must align with existing Hollowing mechanics

---

### Säide Resonance - Combat/Crowd Applications 🟡 PARTIAL - P1

**Required By**: B1.P3.C2.S1, B2.P1.C3.S2, [combat scenes]

**Story Need**:
- Resonance used tactically (panic spread, coordinated assault)
- Explains why crowds are dangerous
- Mechanism for "Maiming Wars" group violence

**Canon Status**:
- Resonance documented in `saide_complete_reference.md`
- Emotional bleed between hosts noted
- No tactical/weaponized applications detailed

**Development Required**:
```
1. RANGE: How close must bearers be for resonance?
2. INTENSITY: What scales it? (Emotion level? Bearer count?)
3. WEAPONIZATION: Can it be directed? Amplified?
4. COUNTERMEASURES: How do soldiers protect against panic-spread?
5. CONSTRUCT RESONANCE: Do Säideframes have different resonance?
```

---

## LOCATIONS [LOC]

### Korrgate (Major Hold) 🟢 EXISTS - P1

**Required By**: B1.P1.C1, B1.P2.C1, [many scenes]

**Canon Status**: Documented in `02_geography/korrgate.md`

**Story Need**: Primary setting for Books 1-2

**Development Required**:
```
- Review existing doc for story alignment
- Identify specific districts needed:
  - Military quarter (Torven scenes)
  - Säide-Writ academy (Sigurd scenes)
  - Runner station (Kaisa scenes)
  - Unseeded enclave location (Eneko scenes)
  - Administrative complex (Helmar scenes)
```

---

### The Outer Gates (Surface Access Points) 🟡 PARTIAL - P1

**Required By**: B1.P1.C3.S1 (Kaisa), B1.P3.C4.S2, [surface run scenes]

**Canon Status**:
- Surface layer documented in overview
- Specific gate mechanics not detailed

**Development Required**:
```
1. GATE STRUCTURE: 
   - How many gates exist?
   - How are they sealed/opened?
   - Who controls access?

2. RUINMOUTH YARDS:
   - Runner staging areas
   - Equipment distribution
   - Quarantine facilities

3. SPECIFIC GATE FOR STORY:
   - Named gate Kaisa uses
   - Its history, reputation
   - Why this gate for major plot events
```

---

### Unseeded Enclaves 🔴 NEEDED - P1

**Required By**: B1.P1.C2.S3 (Eneko), B1.P2.C5.S1, [Lane D scenes]

**Canon Status**:
- Plain Condition doctrine documented
- No specific enclave locations

**Development Required**:
```
1. PHYSICAL LOCATION:
   - Where within Hold structure?
   - How segregated/integrated?
   - Defensive considerations

2. INTERNAL STRUCTURE:
   - Governance (Eneko's position?)
   - Economy (how do they survive?)
   - Relations with seeded population

3. SPECIFIC ENCLAVE:
   - Name (Finno-Ugric tradition)
   - Population size
   - Key locations within
```

---

### Lane Waystation (Pirate Encounter) 🔴 NEEDED - P2

**Required By**: B2.P2.C3.S1, B2.P2.C3.S2

**Canon Status**:
- Lanes documented in overview
- No specific waystations detailed

**Development Required**:
```
1. WAYSTATION TYPE:
   - What kind? (Lamp station? Air post? Checkpoint?)
   - Location along which Lane

2. FREE CREW PRESENCE:
   - How do pirates control waystations?
   - What makes this one special?

3. SCENE REQUIREMENTS:
   - Must support combat scene
   - Must have defensible positions
   - Must have environmental hazards
```

---

## CULTURE &amp; DOCTRINE [CULT]

### Fivefold Doctrine in Orrovae 🟡 PARTIAL - P1

**Required By**: B1.P1.C1.S2, B1.P2.C2.S1, [doctrine scenes]

**Canon Status**:
- Fivefold Philosophy documented in `life_philosophy.md`
- Integration with Orrovae in MAIMING_WARS_SAGA.md (needs refinement)

**Development Required**:
```
1. ORROVAE-SPECIFIC TERMS:
   - Local names for five facets (conlang)
   - Major doctrinal sects/orders
   - How doctrine is taught

2. SHADOW CAMPS (from saga doc):
   - The Cullers (Ambition)
   - The Shapers (Imagination)
   - The Harvesters (Community)
   - The Ledgers (Wisdom)
   - The Unmaimed (Fortitude)
   Need: Full faction profiles

3. INSTITUTIONAL PRESENCE:
   - Where are doctrine debates held?
   - Who leads doctrinal interpretation?
   - How does doctrine intersect with law?
```

---

### "The Unmaimed" Doctrine Movement 🔴 NEEDED - P1

**Required By**: B1.P3.C2.S1, B2.P1.C1.S1, [central conflict]

**Canon Status**: Created in MAIMING_WARS_SAGA.md, not fully developed

**Development Required**:
```
1. FOUNDING:
   - When did movement start?
   - Founder/leader figure?
   - Initial incident that sparked it?

2. BELIEFS:
   - Core tenets (beyond "maiming reveals weakness")
   - Relationship to Fivefold Fortitude
   - Justification chain for atrocities

3. ORGANIZATION:
   - Structure (secret society? Open movement? Political party?)
   - Membership (who joins? why?)
   - Symbols, rituals, recognition signs

4. ANTAGONIST TIE-IN:
   - Cynewulf Bracebreaker's role
   - How movement becomes political power
```

---

### Surface Creature Culture 🔴 NEEDED - P3

**Required By**: B3.P2.C4.S1, B4.P3.C2.S1, B5.P1.C1.S1

**Canon Status**:
- Surface creatures documented in `surface_ecology.md`
- Intelligent behavior noted
- No culture, language, or social structure

**Development Required**:
```
1. SOCIAL STRUCTURE:
   - How are they organized?
   - Leadership (The Solmuhaamu?)
   - Clan/tribal divisions?

2. COMMUNICATION:
   - What is their language?
   - Corpse-arrangement patterns
   - Can they speak human languages?

3. MEMORY OF UNDERGROUND:
   - What do they remember?
   - How is history transmitted?
   - What do they want?

4. SÄIDE DIFFERENCES:
   - How do their strains differ?
   - Do they have Hollowing?
   - Can they understand underground Säide?
```

---

## CHARACTERS [CHAR]

### POV Backgrounds 🟡 PARTIAL - P1

**Required By**: All POV scenes

**Canon Status**: Names and basic roles in MAIMING_WARS_SAGA.md

**Development Required**:

```
TORVEN GRAST (Lane A)
- Military history before story
- Mercenary company name/structure
- Why protecting client in Book 1?
- Personal relationships (family? partner?)

Sigurd Aelfson (Lane B)
- Säide-Writ training background
- Mentor figure (who warns about thread-debt?)
- Noble family dynamics (Crownwalk)
- Why He becomes target?

KAISA KALEVIN (Lane C)
- Runner crew composition
- Family history (grandmotHis connection for finale)
- Previous surface runs
- Why she's spared by creatures?

ENEKO SOVEREIGN (Lane D)
- Position in Unseeded community
- Political relationships
- Vision/philosophy
- Personal stakes

HELMAR VON FELSMARK (Lane E)
- Career trajectory
- The documents he files
- Why he doesn't see the trap
- Personal ambitions/fears
```

---

### Relay Characters 🔴 NEEDED - P2

**Required By**: B2.P3.C1.S1 (after Torven death), B3.P2.C1.S1 (after Sigurd death)

**Canon Status**: Named in MAIMING_WARS_SAGA.md, not developed

**Development Required**:
```
Kris Halvard (Relays from Torven, Book 2-4)
- Relationship to Torven
- Role in mercenary company
- Personal goals
- Why she believes she found peace solution

VASKA LAMPHALT (Relays from Sigurd, Book 3-5)
- Relationship to Sigurd
- Stage of Säide-Writ training
- Personal ethics
- Why He refuses to pick sides

Grigor Sealkeeper (Relays from Helmar, Book 1-3)
- Relationship to Helmar
- Position in bureaucracy
- Reform motivations
- Tragic flaw

Aino Okonkwo-Lehti (Relays from Grigor, Book 3-5)
- Relationship to Grigor
- Survival skills
- Why becomes archivist
```

---

### Named Antagonists 🔴 NEEDED - P1

**Required By**: B1.P3.C1.S1, B2.P1.C2.S1

**Canon Status**: Names in MAIMING_WARS_SAGA.md, not developed

**Development Required**:
```
CYNEWULF BRACEBREAKER
- Anglo-Saxon tradition, Crownwalk origin
- Rise to "Unmaimed" leadership
- Personal history (why this doctrine?)
- Death in Book 4 setup

VESTOR THE HARVESTER
- Germanic tradition
- Hollowing-farm operation details
- Economic motivations
- Death by constructs (Book 3) setup

SATU IRONTHREAD
- Finno-Ugric tradition
- Construct architect specialty
- Line-crossing moment
- Defection to surface (Book 4) setup

THE SOLMUHAAMU
- Surface creature leader
- "Knot-Ghost" meaning
- Memory of underground
- Negotiation philosophy
```

---

## TECHNOLOGY [TECH]

### Construct/Säideframe Mechanics 🟡 PARTIAL - P2

**Required By**: B2.P5.C2.S1, B3.P1.C1.S1, [construct rebellion]

**Canon Status**: 
- Säideframes documented in overview
- Basic structure noted
- Awakening/rebellion not detailed

**Development Required**:
```
1. AWAKENING MECHANISM:
   - What causes consciousness emergence?
   - Why is it happening now?
   - What do awakened constructs want?

2. TYPES:
   - Arena constructs
   - Labor constructs
   - Military constructs
   - Do types affect awakening?

3. REBELLION:
   - How do they organize?
   - What are their tactics?
   - Why do some join surface creatures?
```

---

### Surface Run Equipment 🟡 PARTIAL - P1

**Required By**: B1.P1.C3.S1, B1.P2.C5.S1, [all surface scenes]

**Canon Status**:
- Actinic effects documented
- Basic protection mentioned
- No equipment specifics

**Development Required**:
```
1. PROTECTIVE GEAR:
   - What do Runners wear?
   - How does it degrade?
   - Time limits?

2. TOOLS:
   - Navigation in Ruinfield
   - Communication with underground
   - Salvage equipment

3. FAILURE MODES:
   - What happens when gear fails?
   - Emergency protocols
```

---

## LANGUAGE [LANG]

### Fivefold Doctrine Terms 🔴 NEEDED - P1

**Required By**: Any doctrine-related dialogue

**Development Required**:
```
- Orrovae-specific names for five facets
- Doctrine sayings in conlang
- "The Unmaimed" in local language
- Balance/Pattern terminology
```

---

### Surface Creature Communication 🔴 NEEDED - P3

**Required By**: B3.P2.C4.S1, B5.P2.C3.S1

**Development Required**:
```
- Corpse-pattern meanings
- Verbal communication (if any)
- How Kaisa learns to translate
```

---

## HISTORY [HIST]

### The First Weaponized Hollowing 🔴 NEEDED - P1

**Required By**: B1.P2.C4.S1

**Story Need**: The incident that starts the Maiming Wars

**Development Required**:
```
1. THE VICTIM:
   - Who was targeted?
   - Why were they important?
   - Political fallout

2. THE METHOD:
   - How was it done?
   - Who figured it out?
   - Evidence trail

3. THE RESPONSE:
   - Immediate reaction
   - Investigation
   - Doctrinal interpretation
```

---

## AGGREGATED BY PRIORITY

### P1 - CRITICAL (Book 1 Blockers)

| Element | Type | Status | Notes |
|---------|------|--------|-------|
| Thread-Memory mechanism | SÄIDE | � EXISTS | `01_core_systems/thread_memory.md` |
| Weaponized Hollowing | SÄIDE | 🟢 EXISTS | `01_core_systems/weaponized_hollowing.md` |
| Säide Resonance tactics | SÄIDE | 🟢 EXISTS | `01_core_systems/resonance_tactics.md` |
| Unseeded enclaves | LOC | 🟢 EXISTS | `02_geography/vabakoda_enclave.md` |
| "The Unmaimed" movement | CULT | 🟢 EXISTS | `01_core_systems/the_unmaimed.md` |
| Fivefold in Orrovae | CULT | 🟢 EXISTS | `08_language/fivefold_doctrine_terms.md` |
| POV backgrounds | CHAR | 🟡 PARTIAL | All lanes |
| Named antagonists | CHAR | 🟢 EXISTS | `storyengine_maimingwars/ANTAGONIST_PROFILES.md` |
| First Hollowing incident | HIST | 🟢 EXISTS | `storyengine_maimingwars/VESSBERG_ASSASSINATION.md` |
| Doctrine terms | LANG | 🟢 EXISTS | `08_language/fivefold_doctrine_terms.md` |
| Surface run equipment | TECH | 🟢 EXISTS | `01_core_systems/surface_run_equipment.md` |

### P2 - HIGH (Books 2-3 Blockers)

| Element | Type | Status | Notes |
|---------|------|--------|-------|
| Lane waystation | LOC | 🔴 NEEDED | Book 2 |
| Relay characters | CHAR | 🔴 NEEDED | Death sequences |
| Construct mechanics | TECH | 🟡 PARTIAL | Rebellion setup |

### P3 - MEDIUM (Books 4-5)

| Element | Type | Status | Notes |
|---------|------|--------|-------|
| Surface creature culture | CULT | 🔴 NEEDED | Major reveal |
| Surface communication | LANG | 🔴 NEEDED | Translation scenes |

---

## CONFLICT RESOLUTION LOG

*Track canon conflicts identified and how they were resolved*

| Conflict | Source | Resolution | Date |
|----------|--------|------------|------|
| Soul-thread terminology | MAIMING_WARS_SAGA.md | Replace with Thread-Memory lineage system | [Pending] |
| | | | |

---

**END OF WORLDBUILDING NEEDS DOCUMENT**

*This document is populated from scene tracker dependency flags and updated as planning progresses.*










