# Norbela Wiki Consolidation Master Plan
## Converting All Existing Files to Wikipedia-Style Pages

---

## CONSOLIDATION STRATEGY

### Source Files Inventory

Based on your existing structure:

```
norbela/
├── World_Arcane_Oil_Combined.md
├── conlang_lexicon.json
└── world/
    ├── overview.md
    ├── world_bible.md
    ├── geography/
    │   └── geography_maps.md
    ├── cities/
    │   ├── cities_settlements.md
    │   └── city_layouts_compendium.md
    ├── technology/
    │   ├── technology.md
    │   ├── tech_history_1500_1900.md
    │   └── technology_catalog/
    │       └── technology_catalog.md
    ├── religion/
    │   └── religion_spirituality.md
    ├── economics/
    │   └── economics.md
    ├── factions/
    │   └── factions_organizations.md
    ├── legal/
    │   └── legal_systems.md
    ├── social/
    │   └── social_structures.md
    ├── society/
    │   └── character_relationships.md
    └── conlang/
        └── naming_conventions/
            └── name_charter.md
```

---

## CONVERSION MAP

### PLANETARY Category (6 pages)

**1. World Overview** ✓ CREATED
- Source: `world/overview.md` (primary)
- Status: Sample already created
- Macro Tags: PLANETARY, LORE
- Content: Physical characteristics, climate, basic geography

**2. Celestial Mechanics** ⚠️ TO CREATE
- Source: Extract from `world/overview.md` (locked sections)
- Macro Tags: PLANETARY
- Content: Rotation, orbit, gravity, astronomical parameters
- **CRITICAL GAP**: Needs exact values for rotation period, year length

**3. Climate and Biomes** ⚠️ TO CREATE
- Source: Extract from `world/overview.md` (climate section)
- Macro Tags: PLANETARY, GEOGRAPHY
- Content: Biomes, temperature ranges, weather patterns, seasonal cycles

**4. Moon and Ring System** ⚠️ TO CREATE
- Source: Extract from `world/overview.md` (moon/ring sections)
- Macro Tags: PLANETARY, LORE, MAGIC
- Content: Moon details, eruptions, ring composition, magical rain

**5. Natural Phenomena** ⚠️ TO CREATE
- Source: Extract from `world/overview.md` (auroras, phenomena)
- Macro Tags: PLANETARY
- Content: Auroras, crystal formations, unique features

**6. Finyak Substrate** ⚠️ TO CREATE
- Source: `world/overview.md` + `World_Arcane_Oil_Combined.md`
- Macro Tags: PLANETARY, MAGIC
- Content: Geological source of magic, distribution, depletion

---

### MAGIC Category (8 pages)

**1. Magic System Overview** ⚠️ TO CREATE
- Source: `world/overview.md` + `World_Arcane_Oil_Combined.md`
- Macro Tags: MAGIC
- Content: Core principles, how magic works, fundamental rules

**2. Magical Creatures Catalog** ✓ SAMPLE CREATED
- Source: `world/overview.md` (creature sections)
- Macro Tags: MAGIC, ECONOMICS
- Status: 5 species detailed, needs 15+ more
- Content: All magical creatures, biology, oil properties

**3. Shyak Extraction** ⚠️ TO CREATE
- Source: `World_Arcane_Oil_Combined.md`
- Macro Tags: MAGIC, ECONOMICS, TECHNOLOGY
- Content: Harvesting methods, refinement, sustainability

**4. Magical Physics** ⚠️ TO CREATE
- Source: `world/overview.md` (magical feedback sections)
- Macro Tags: MAGIC, TECHNOLOGY
- Content: Entropy, resonance cascades, conservation principles

**5. Alternative Fuels** ⚠️ TO CREATE
- Source: `world/overview.md` + `technology.md`
- Macro Tags: MAGIC, TECHNOLOGY, ECONOMICS
- Content: Fauxil, slagcells, bonewire - specifications and risks

**6. Entropy Phenomena** ⚠️ TO CREATE
- Source: `world/overview.md` + `geography_maps.md`
- Macro Tags: MAGIC, PLANETARY, LORE
- Content: Dead zones, shisolak, shibak, expansion, effects

**7. Symbiotic Microfauna** ⚠️ TO CREATE
- Source: `World_Arcane_Oil_Combined.md`
- Macro Tags: MAGIC
- Content: Biology of magic production, microbe role

**8. Conservation and Ethics** ⚠️ TO CREATE
- Source: `world/overview.md` (sentience/ethics sections)
- Macro Tags: MAGIC, SOCIETY, POLITICS
- Content: Creature sentience, rights debates, conservation efforts

---

### GEOGRAPHY Category (12+ pages)

**1. Continents Overview** ⚠️ TO CREATE
- Source: `geography_maps.md`
- Macro Tags: GEOGRAPHY, PLANETARY
- Content: All five continents at a glance

**2. Tavanor** ⚠️ TO CREATE
- Source: `geography_maps.md` (Tavanor section)
- Macro Tags: GEOGRAPHY, POLITICS
- Content: Detailed regional profile

**3. Sulenor** ⚠️ TO CREATE
- Source: `geography_maps.md` (Sulenor section)
- Macro Tags: GEOGRAPHY, POLITICS
- Content: Volcanic regions, industrial zones

**4. Eshtor** ⚠️ TO CREATE
- Source: `geography_maps.md` (Eshtor section)
- Macro Tags: GEOGRAPHY, POLITICS
- Content: Forests, conservation zones

**5. Vashor** ⚠️ TO CREATE
- Source: `geography_maps.md` (Vashor section)
- Macro Tags: GEOGRAPHY, POLITICS
- Content: Frozen wastes, mysterious north

**6. Konor** ⚠️ TO CREATE
- Source: `geography_maps.md` (Konor section)
- Macro Tags: GEOGRAPHY, POLITICS
- Content: Dying desert, entropy crisis

**7. Cities Major** ⚠️ TO CREATE
- Source: `cities_settlements.md`
- Macro Tags: GEOGRAPHY, SOCIETY
- Content: 15+ major cities detailed

**8. Settlements Minor** ⚠️ TO CREATE
- Source: `cities_settlements.md` (extract minor settlements)
- Macro Tags: GEOGRAPHY
- Content: Towns, outposts, villages

**9. Travel Infrastructure** ⚠️ TO CREATE
- Source: `geography_maps.md` (travel times section)
- Macro Tags: GEOGRAPHY, TECHNOLOGY
- Content: Roads, rail, routes, travel times

**10. Natural Wonders** ⚠️ TO CREATE
- Source: `world/overview.md` (unique features)
- Macro Tags: GEOGRAPHY, PLANETARY
- Content: Crystal ranges, rivers, plateaus, etc.

**11. Dead Zone Maps** ⚠️ TO CREATE
- Source: `geography_maps.md` (dangerous zones)
- Macro Tags: GEOGRAPHY, MAGIC
- Content: Entropy zones, expansion patterns

**12. City Layouts** ⚠️ TO CREATE
- Source: `city_layouts_compendium.md`
- Macro Tags: GEOGRAPHY, SOCIETY, REFERENCE
- Content: Detailed city maps and districts

---

### LORE Category (6+ pages)

**1. History: Ancient** ⚠️ TO CREATE
- Source: NEW CONTENT NEEDED
- Macro Tags: LORE
- Content: Pre-1500 history, origins, ancient civilizations
- **CRITICAL GAP**: This doesn't exist yet

**2. History: 1500-1780** ⚠️ TO CREATE
- Source: `tech_history_1500_1900.md` (extract pre-1780)
- Macro Tags: LORE, TECHNOLOGY
- Content: Pre-industrial magical adoption

**3. History: 1780-1880** ⚠️ TO CREATE
- Source: `world/overview.md` + `tech_history_1500_1900.md`
- Macro Tags: LORE, TECHNOLOGY, POLITICS
- Content: Industrial revolution, arcane age

**4. Major Events** ⚠️ TO CREATE
- Source: Extract from multiple files
- Macro Tags: LORE, POLITICS
- Content: Second Cascade, key turning points

**5. Mythology and Legends** ⚠️ TO CREATE
- Source: Extract from `world/overview.md` + `religion_spirituality.md`
- Macro Tags: LORE, RELIGION
- Content: Cultural myths, creature legends

**6. Timeline Master** ⚠️ TO CREATE
- Source: Compiled from all sources
- Macro Tags: LORE, REFERENCE
- Content: Complete chronology with dates

---

### TECHNOLOGY Category (8 pages)

**1. Technology Overview** ⚠️ TO CREATE
- Source: `technology.md` (principles section)
- Macro Tags: TECHNOLOGY
- Content: Core principles, limitations, capabilities

**2. Device Catalog** ⚠️ TO CREATE
- Source: `technology.md` + `technology_catalog.md`
- Macro Tags: TECHNOLOGY, ECONOMICS
- Content: 100+ specific devices detailed

**3. Manufacturing** ⚠️ TO CREATE
- Source: `technology.md` (industrial section)
- Macro Tags: TECHNOLOGY, ECONOMICS, SOCIETY
- Content: Production processes, factories

**4. Weaponry** ⚠️ TO CREATE
- Source: `technology.md` (weaponry section)
- Macro Tags: TECHNOLOGY, POLITICS
- Content: Firearms, cannons, forbidden weapons

**5. Medicine and Healing** ⚠️ TO CREATE
- Source: `technology.md` (medicine section)
- Macro Tags: TECHNOLOGY, SOCIETY
- Content: Surgery, regeneration, devices

**6. Communication** ⚠️ TO CREATE
- Source: `technology.md` (communication section)
- Macro Tags: TECHNOLOGY, SOCIETY
- Content: Message stones, scrying, telegraph

**7. Transportation** ⚠️ TO CREATE
- Source: `technology.md` (transportation section)
- Macro Tags: TECHNOLOGY, GEOGRAPHY
- Content: Carriages, rail, skyships

**8. Forbidden Technology** ⚠️ TO CREATE
- Source: `technology.md` (forbidden tech section)
- Macro Tags: TECHNOLOGY, POLITICS, LORE
- Content: Illegal devices, experiments, risks

---

### SOCIETY Category (8+ pages)

**1. Social Structures** ⚠️ TO CREATE
- Source: `social_structures.md`
- Macro Tags: SOCIETY, POLITICS
- Content: Caste system, hierarchy, mobility

**2. Caste System** ⚠️ TO CREATE
- Source: Extract from `social_structures.md`
- Macro Tags: SOCIETY, ECONOMICS
- Content: Upper/Middle/Lower castes, outcasts

**3. Daily Life: Upper Caste** ⚠️ TO CREATE
- Source: Extract from multiple files
- Macro Tags: SOCIETY, ECONOMICS
- Content: Housing, food, leisure, routines

**4. Daily Life: Middle Caste** ⚠️ TO CREATE
- Source: NEW CONTENT NEEDED (currently sparse)
- Macro Tags: SOCIETY
- Content: Struggles, aspirations, daily reality

**5. Daily Life: Lower Caste** ⚠️ TO CREATE
- Source: Extract from multiple files
- Macro Tags: SOCIETY, ECONOMICS
- Content: Survival, hardship, resistance

**6. Culture and Arts** ⚠️ TO CREATE
- Source: NEW CONTENT NEEDED
- Macro Tags: SOCIETY, LORE
- Content: Music, literature, visual arts

**7. Customs and Traditions** ⚠️ TO CREATE
- Source: Extract from `world/overview.md`
- Macro Tags: SOCIETY, RELIGION
- Content: Rituals, taboos, social norms

**8. Festivals and Calendar** ⚠️ TO CREATE
- Source: Extract from `world/overview.md`
- Macro Tags: SOCIETY, RELIGION, PLANETARY
- Content: Annual celebrations, calendar system

**9. Education** ⚠️ TO CREATE
- Source: Extract from multiple files
- Macro Tags: SOCIETY, TECHNOLOGY
- Content: Schools, apprenticeships, literacy

**10. Family and Relationships** ⚠️ TO CREATE
- Source: `character_relationships.md`
- Macro Tags: SOCIETY
- Content: Marriage, kinship, social bonds

---

### POLITICS Category (8 pages)

**1. Government Systems** ⚠️ TO CREATE
- Source: Extract from multiple files
- Macro Tags: POLITICS
- Content: Baron Council structure, voting, authority

**2. Baron Council** ⚠️ TO CREATE
- Source: Extract from geography, characters
- Macro Tags: POLITICS, CHARACTERS
- Content: Nine seats, power dynamics, conflicts

**3. Legal Systems** ⚠️ TO CREATE
- Source: `legal_systems.md`
- Macro Tags: POLITICS, SOCIETY
- Content: Laws, courts, justice, punishment

**4. Law Enforcement** ⚠️ TO CREATE
- Source: Extract from cities, legal files
- Macro Tags: POLITICS, SOCIETY
- Content: Guards, enforcement, corruption

**5. Military** ⚠️ TO CREATE
- Source: Extract from technology, politics
- Macro Tags: POLITICS, TECHNOLOGY
- Content: Forces, organization, warfare

**6. Diplomacy and Espionage** ⚠️ TO CREATE
- Source: Extract from character, faction files
- Macro Tags: POLITICS
- Content: International relations, spy networks

**7. Conflicts and Wars** ⚠️ TO CREATE
- Source: Extract from geography, lore
- Macro Tags: POLITICS, LORE
- Content: Active conflicts, historical wars

**8. Succession Crisis** ⚠️ TO CREATE
- Source: Extract from characters, politics
- Macro Tags: POLITICS, LORE, CHARACTERS
- Content: Current crisis, implications

---

### ECONOMICS Category (6 pages)

**1. Economics Overview** ⚠️ TO CREATE
- Source: `economics.md`
- Macro Tags: ECONOMICS
- Content: System structure, principles

**2. Shyak Economy** ⚠️ TO CREATE
- Source: `economics.md` + magic files
- Macro Tags: ECONOMICS, MAGIC, POLITICS
- Content: Oil markets, pricing, control

**3. Industries** ⚠️ TO CREATE
- Source: `economics.md` + technology files
- Macro Tags: ECONOMICS, TECHNOLOGY
- Content: Non-shyak industries, manufacturing

**4. Trade and Commerce** ⚠️ TO CREATE
- Source: `economics.md` + geography files
- Macro Tags: ECONOMICS, GEOGRAPHY
- Content: Routes, merchants, guilds

**5. Currency and Finance** ⚠️ TO CREATE
- Source: `economics.md`
- Macro Tags: ECONOMICS, SOCIETY
- Content: Money, banking, wealth distribution

**6. Labor Systems** ⚠️ TO CREATE
- Source: `economics.md` + society files
- Macro Tags: ECONOMICS, SOCIETY, POLITICS
- Content: Employment, slavery, unions

**7. Black Markets** ⚠️ TO CREATE
- Source: `economics.md` + faction files
- Macro Tags: ECONOMICS, POLITICS
- Content: Illegal trade, smuggling, counterfeits

---

### RELIGION Category (6 pages)

**1. Religion Overview** ⚠️ TO CREATE
- Source: `religion_spirituality.md`
- Macro Tags: RELIGION, SOCIETY
- Content: Belief systems, major faiths

**2. Faiths and Denominations** ⚠️ TO CREATE
- Source: `religion_spirituality.md`
- Macro Tags: RELIGION, LORE
- Content: Different belief systems, conflicts

**3. The Inquisition** ⚠️ TO CREATE
- Source: `religion_spirituality.md` + politics
- Macro Tags: RELIGION, POLITICS
- Content: Organization, power, persecution

**4. Clergy and Institutions** ⚠️ TO CREATE
- Source: `religion_spirituality.md`
- Macro Tags: RELIGION, SOCIETY
- Content: Priests, temples, hierarchy

**5. Rituals and Practices** ⚠️ TO CREATE
- Source: `religion_spirituality.md` + society
- Macro Tags: RELIGION, SOCIETY
- Content: Ceremonies, worship, traditions

**6. Theology and Philosophy** ⚠️ TO CREATE
- Source: `religion_spirituality.md`
- Macro Tags: RELIGION, LORE
- Content: Beliefs about magic, entropy, afterlife

---

### FACTIONS Category (7 pages)

**1. Factions Overview** ⚠️ TO CREATE
- Source: `factions_organizations.md`
- Macro Tags: POLITICS, SOCIETY
- Content: All major groups at a glance

**2. Barons and Houses** ⚠️ TO CREATE
- Source: Extract from factions, characters
- Macro Tags: POLITICS, CHARACTERS
- Content: Noble families, territories

**3. Rebels and Resistance** ⚠️ TO CREATE
- Source: `factions_organizations.md` (Morshan section)
- Macro Tags: POLITICS, SOCIETY
- Content: Breakers, other rebel groups

**4. Criminals and Underground** ⚠️ TO CREATE
- Source: `factions_organizations.md` (Nethvor section)
- Macro Tags: POLITICS, ECONOMICS
- Content: Nethvor-Shadows, crime networks

**5. Guilds and Orders** ⚠️ TO CREATE
- Source: `factions_organizations.md`
- Macro Tags: SOCIETY, ECONOMICS
- Content: Trade guilds, professional orders

**6. Religious Groups** ⚠️ TO CREATE
- Source: `religion_spirituality.md` + factions
- Macro Tags: RELIGION, POLITICS
- Content: Church factions, cults

**7. Civic Organizations** ⚠️ TO CREATE
- Source: `factions_organizations.md`
- Macro Tags: SOCIETY, POLITICS
- Content: Community groups, services

---

### CHARACTERS Category (10+ pages)

**1. Characters Major** ⚠️ TO CREATE
- Source: Compiled from all character mentions
- Macro Tags: CHARACTERS, POLITICS
- Content: Index of all major characters

**2. Shalen-Mor** ✓ SAMPLE CREATED
- Source: Extracted from multiple files
- Macro Tags: CHARACTERS, POLITICS
- Status: Complete sample

**3-10. Individual Baron Pages** ⚠️ TO CREATE
- Telvor-Shin, Koresh-Val, Velasha-Nen, Meshira-Tal, Telumesh, Threnok-Gash, Soryn-Kesh, Vonder-Shin
- Sources: Extract from all files
- Macro Tags: CHARACTERS, POLITICS
- Content: Full character dossiers

**11-13. Revolutionary Leaders** ⚠️ TO CREATE
- Morshan, Keshiel, Moreth-Kiren
- Sources: Extract from faction files
- Macro Tags: CHARACTERS, POLITICS

**14. Nethvor** ⚠️ TO CREATE
- Source: Faction files
- Macro Tags: CHARACTERS, POLITICS

**15. Supporting Cast** ⚠️ TO CREATE
- Source: NEW CONTENT NEEDED
- Macro Tags: CHARACTERS
- Content: 20-30 secondary characters

---

### LANGUAGE Category (6 pages)

**1. Conlang Overview** ⚠️ TO CREATE
- Source: `world/overview.md` (conlang note)
- Macro Tags: LANGUAGE, LORE
- Content: Language structure, philosophy

**2. Lexicon** ⚠️ TO CREATE
- Source: `conlang_lexicon.json`
- Macro Tags: LANGUAGE, REFERENCE
- Content: Complete vocabulary (currently minimal)

**3. Grammar and Syntax** ⚠️ TO CREATE
- Source: NEW CONTENT NEEDED
- Macro Tags: LANGUAGE, REFERENCE
- Content: Rules, structure, usage

**4. Naming Conventions** ⚠️ TO CREATE
- Source: `name_charter.md`
- Macro Tags: LANGUAGE, SOCIETY
- Content: How names work, meaning-based system

**5. Dialects and Variations** ⚠️ TO CREATE
- Source: NEW CONTENT NEEDED
- Macro Tags: LANGUAGE, GEOGRAPHY
- Content: Regional differences

**6. Writing Systems** ⚠️ TO CREATE
- Source: NEW CONTENT NEEDED
- Macro Tags: LANGUAGE, SOCIETY
- Content: Scripts, literacy, documentation

---

### REFERENCE Category (8 pages)

**1. Quick Reference** ⚠️ TO CREATE
- Source: Compiled
- Macro Tags: REFERENCE
- Content: One-page summaries of everything

**2. Timeline Master** ⚠️ TO CREATE
- Source: All historical content
- Macro Tags: REFERENCE, LORE
- Content: Complete chronology

**3. Glossary** ⚠️ TO CREATE
- Source: All files
- Macro Tags: REFERENCE
- Content: Terms, definitions, quick lookups

**4. Master Index** ⚠️ TO CREATE
- Source: All pages
- Macro Tags: REFERENCE
- Content: Alphabetical index of everything

**5. Plot Hooks Database** ⚠️ TO CREATE
- Source: Extract from all pages
- Macro Tags: REFERENCE
- Content: 100+ ready-to-use hooks

**6. GM Tools** ⚠️ TO CREATE
- Source: NEW CONTENT
- Macro Tags: REFERENCE
- Content: Generators, tables, calculators

**7. Style Guide** ⚠️ TO CREATE
- Source: This project
- Macro Tags: REFERENCE
- Content: How to maintain consistency

**8. Conversion Tables** ⚠️ TO CREATE
- Source: All technical data
- Macro Tags: REFERENCE
- Content: Measurements, costs, conversions

---

## PRIORITY CONVERSION ORDER

### Phase 1: Foundation (Weeks 1-2)
1. PLANETARY (6 pages) - Defines the world
2. MAGIC (8 pages) - Core system
3. GEOGRAPHY: Continents (6 pages) - Basic locations

### Phase 2: People and Places (Weeks 3-4)
4. CHARACTERS: Major (10 pages) - Key figures
5. GEOGRAPHY: Cities (6 pages) - Detailed locations
6. LORE: History (6 pages) - Timeline foundation

### Phase 3: Systems (Weeks 5-6)
7. TECHNOLOGY (8 pages) - How world works
8. SOCIETY (8 pages) - How people live
9. POLITICS (8 pages) - Power structures

### Phase 4: Details (Weeks 7-8)
10. ECONOMICS (6 pages) - Resource systems
11. RELIGION (6 pages) - Beliefs and institutions
12. FACTIONS (7 pages) - Organizations

### Phase 5: Integration (Weeks 9-10)
13. LANGUAGE (6 pages) - Communication
14. REFERENCE (8 pages) - Tools and indexes
15. Cross-linking and polish

---

## STATUS SUMMARY

**Total Wiki Pages Planned**: ~110 pages

**Current Status**:
- ✓ Complete: 3 pages (samples)
- ⚠️ To Create: ~107 pages
- 📝 Source exists: ~60 pages
- 🆕 New content needed: ~50 pages

**Estimated Work**:
- Conversion (existing content): 60 hours
- Creation (new content): 50 hours
- Integration/polish: 20 hours
- **Total: 130 hours**

---

## NEXT IMMEDIATE STEPS

1. **Create directory structure** in outputs
2. **Begin PLANETARY conversion** (6 pages from existing content)
3. **Continue with MAGIC** (8 pages, mostly existing)
4. **Build GEOGRAPHY** (continent pages from existing)
5. **Systematic progression** through all categories

Would you like me to start the actual conversion now?
