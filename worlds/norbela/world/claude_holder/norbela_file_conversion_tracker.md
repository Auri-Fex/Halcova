# Norbela File Conversion Tracker
## Complete Consolidation and Wiki Conversion Plan

---

## Source Files Identified

### Current Structure (Your Drive)
```
I:\My Drive\Worldbuilding\norbela\
├── World_Arcane_Oil_Combined.md
├── conlang_lexicon.json
├── world/
│   ├── overview.md ✓ (MASSIVE - needs splitting)
│   ├── world_bible.md (stub - needs expansion)
│   ├── story (excluded - story file)
│   ├── society/character_relationships.md
│   ├── geography/geography_maps.md ✓
│   ├── technology/
│   │   ├── tech_history_1500_1900.md
│   │   ├── technology.md ✓
│   ├── religion/religion_spirituality.md
│   ├── economics/economics.md
│   ├── factions/factions_organizations.md ✓
│   ├── cities/
│   │   ├── cities_settlements.md ✓
│   │   ├── city_layouts_compendium.md
│   ├── legal/legal_systems.md
│   ├── social/social_structures.md
│   ├── technology_catalog/technology_catalog.md
│   └── conlang/naming_conventions/name_charter.md
└── stories/ (entire directory excluded)
```

---

## Conversion Plan by Macro Category

### PLANETARY (6-8 wiki pages)

**Source**: world/overview.md (sections)

**Target Pages**:
1. ✓ `planetary/world_overview.md` 
   - Sources: overview.md (intro, core principles)
   - Macro: [PLANETARY, LORE]
   - Status: SAMPLE CREATED

2. `planetary/celestial_mechanics.md`
   - Sources: overview.md (rotation, orbit, planetary parameters)
   - Macro: [PLANETARY]
   - Content: Exact specs for rotation period, year length, axial tilt, orbit
   - NEEDS: Final decisions on exact values

3. `planetary/moon_ring_system.md`
   - Sources: overview.md (moon eruptions, ring origins)
   - Macro: [PLANETARY, MAGIC]
   - Content: Moon volc

anism, ring formation, magical rain
   - NEEDS: Moon name, exact orbital period

4. `planetary/climate_biomes.md`
   - Sources: overview.md (climate section, biomes section)
   - Macro: [PLANETARY, GEOGRAPHY]
   - Content: Iceworld details, all biome types, seasonal cycles

5. `planetary/blaysol_blue_sun.md`
   - Sources: overview.md (Blaysol section)
   - Macro: [PLANETARY, SOCIETY]
   - Content: Blue sun effects, visual aesthetics, cultural impact

6. `planetary/finyak_substrate.md`
   - Sources: overview.md (finyak sections), World_Arcane_Oil_Combined.md
   - Macro: [PLANETARY, MAGIC]
   - Content: Geological magic source, distribution, depletion

7. `planetary/natural_phenomena.md`
   - Sources: overview.md (auroras, crystals, unique features)
   - Macro: [PLANETARY]
   - Content: Auroras, crystal formations, gravity anomalies, unique world aspects

8. `planetary/entropy_dead_zones.md`
   - Sources: overview.md, geography_maps.md
   - Macro: [PLANETARY, MAGIC, LORE]
   - Content: Shisolak wastes, expansion, effects, Central Tavanor dead zone

---

### MAGIC (8-10 wiki pages)

**Sources**: overview.md, World_Arcane_Oil_Combined.md

**Target Pages**:
1. `magic/magic_system_overview.md`
   - Sources: overview.md (magic sections)
   - Macro: [MAGIC]
   - Content: Core principles, how magic works, limitations

2. ✓ `magic/creatures_catalog.md`
   - Sources: overview.md (creatures), World_Arcane_Oil_Combined.md
   - Macro: [MAGIC, ECONOMICS, PLANETARY]
   - Status: SAMPLE CREATED (needs 15+ more species)

3. `magic/finyak_mechanics.md`
   - Sources: overview.md, World_Arcane_Oil_Combined.md (finyak sections)
   - Macro: [MAGIC, PLANETARY]
   - Content: How finyak works, measurement, distribution

4. `magic/shyak_extraction.md`
   - Sources: overview.md (extraction sections), World_Arcane_Oil_Combined.md
   - Macro: [MAGIC, ECONOMICS, TECHNOLOGY]
   - Content: Harvesting methods, refinement, regulation

5. `magic/magical_physics.md`
   - Sources: overview.md (magical physics section)
   - Macro: [MAGIC, TECHNOLOGY]
   - Content: Entropy, resonance, conservation, competing theories

6. `magic/alternative_fuels.md`
   - Sources: overview.md (fauxil, slagcells, bonewire)
   - Macro: [MAGIC, TECHNOLOGY, ECONOMICS]
   - Content: All alternatives, production, risks, uses

7. `magic/symbiotic_microfauna.md`
   - Sources: World_Arcane_Oil_Combined.md
   - Macro: [MAGIC, PLANETARY]
   - Content: Biology of magic production, microbe-host relationship

8. `magic/entropy_phenomena.md`
   - Sources: overview.md (shisolak, shibak, entropy storms)
   - Macro: [MAGIC, PLANETARY]
   - Content: Dead zones, overcharge zones, magical disasters

9. `magic/creature_ethics.md`
   - Sources: overview.md (sentience and ethics section)
   - Macro: [MAGIC, SOCIETY, POLITICS]
   - Content: Sentience spectrum, legal debates, conservation movements

10. `magic/pollution_byproducts.md`
    - Sources: overview.md (pollution sections)
    - Macro: [MAGIC, TECHNOLOGY, SOCIETY]
    - Content: Magical waste, environmental effects, cleanup

---

### GEOGRAPHY (15-20 wiki pages)

**Sources**: geography_maps.md, cities_settlements.md, overview.md

**Target Pages**:

**Continental Overview**:
1. `geography/continents_overview.md`
   - Sources: geography_maps.md, overview.md
   - Macro: [GEOGRAPHY, PLANETARY]
   - Content: All 5 continents summary, oceans, islands

**Individual Continents** (5 pages):
2. `geography/tavanor.md`
   - Sources: geography_maps.md (Tavanor section)
   - Macro: [GEOGRAPHY, POLITICS]
   - Content: Full continental detail, resources, regions

3. `geography/sulenor.md`
   - Sources: geography_maps.md
   - Macro: [GEOGRAPHY, POLITICS, ECONOMICS]
   
4. `geography/eshtor.md`
   - Sources: geography_maps.md
   - Macro: [GEOGRAPHY, POLITICS, MAGIC]

5. `geography/vashor.md`
   - Sources: geography_maps.md
   - Macro: [GEOGRAPHY, LORE]

6. `geography/konor.md`
   - Sources: geography_maps.md
   - Macro: [GEOGRAPHY, LORE, MAGIC]

**Cities** (split into tiers):
7. `geography/cities_capital.md`
   - Sources: cities_settlements.md (Kalen-Sheloth)
   - Macro: [GEOGRAPHY, POLITICS, SOCIETY]

8. `geography/cities_major.md`
   - Sources: cities_settlements.md (major cities)
   - Macro: [GEOGRAPHY, SOCIETY]
   - Content: 10-15 major cities with full details

9. `geography/settlements_minor.md`
   - Sources: cities_settlements.md (minor settlements)
   - Macro: [GEOGRAPHY]
   - Content: 30-50 towns, outposts, villages

**Infrastructure**:
10. `geography/travel_infrastructure.md`
    - Sources: geography_maps.md (travel times), cities
    - Macro: [GEOGRAPHY, TECHNOLOGY]
    - Content: Roads, rail, routes, travel times

11. `geography/natural_wonders.md`
    - Sources: overview.md (Stanyak Ral, Blayresh, etc.)
    - Macro: [GEOGRAPHY, PLANETARY]
    - Content: All unique geographical features

---

### TECHNOLOGY (8-10 wiki pages)

**Sources**: technology.md, tech_history_1500_1900.md, technology_catalog.md

**Target Pages**:
1. `technology/technology_overview.md`
   - Sources: technology.md (principles section)
   - Macro: [TECHNOLOGY]
   - Content: How arcane tech works, limitations, baseline tech level

2. `technology/device_catalog.md`
   - Sources: technology.md (devices), technology_catalog.md
   - Macro: [TECHNOLOGY, ECONOMICS]
   - Content: 100+ devices organized by category

3. `technology/communication.md`
   - Sources: technology.md (communication section)
   - Macro: [TECHNOLOGY, SOCIETY]
   - Content: Message stones, scrying, telegraph

4. `technology/transportation.md`
   - Sources: technology.md (transport section)
   - Macro: [TECHNOLOGY, GEOGRAPHY]
   - Content: Carriages, rail, skyships

5. `technology/weaponry.md`
   - Sources: technology.md (weapons section)
   - Macro: [TECHNOLOGY, POLITICS]
   - Content: Firearms, cannons, blades, explosives

6. `technology/medicine_healing.md`
   - Sources: technology.md (medicine section)
   - Macro: [TECHNOLOGY, SOCIETY]
   - Content: Surgery, regeneration, life extension

7. `technology/industry_manufacturing.md`
   - Sources: technology.md (industry section)
   - Macro: [TECHNOLOGY, ECONOMICS]
   - Content: Factories, forges, automation

8. `technology/forbidden_technology.md`
   - Sources: technology.md (forbidden section)
   - Macro: [TECHNOLOGY, POLITICS, LORE]
   - Content: Entropy weapons, necromancy, corruption programs

9. `technology/device_failures.md`
   - Sources: technology.md (failures section)
   - Macro: [TECHNOLOGY, SOCIETY]
   - Content: Accidents, explosions, common failures

10. `technology/tech_evolution.md`
    - Sources: tech_history_1500_1900.md
    - Macro: [TECHNOLOGY, LORE]
    - Content: 1780s-1880s innovation timeline

---

### SOCIETY (8-10 wiki pages)

**Sources**: social_structures.md, factions_organizations.md, overview.md, cities

**Target Pages**:
1. `society/social_structures.md`
   - Sources: social_structures.md
   - Macro: [SOCIETY, POLITICS]
   - Content: Caste system, class divisions

2. `society/daily_life_upper.md`
   - Sources: cities, overview.md (culture sections)
   - Macro: [SOCIETY, ECONOMICS]
   - Content: Elite lifestyle, luxury, access

3. `society/daily_life_middle.md`
   - Sources: cities, inferred
   - Macro: [SOCIETY]
   - Content: Middle caste experience

4. `society/daily_life_lower.md`
   - Sources: cities, technology.md (underclass sections)
   - Macro: [SOCIETY, ECONOMICS]
   - Content: Underclass survival, hardships

5. `society/culture_arts.md`
   - Sources: overview.md (culture), cities (smog theaters, etc.)
   - Macro: [SOCIETY, LORE]
   - Content: Music, art, literature, theater

6. `society/customs_traditions.md`
   - Sources: overview.md (rituals), cities
   - Macro: [SOCIETY, RELIGION]
   - Content: Festivals, rituals, social customs

7. `society/food_cuisine.md`
   - Sources: cities (cantina scripts, street stews)
   - Macro: [SOCIETY]
   - Content: Food by class, dining customs

8. `society/fashion_clothing.md`
   - Sources: overview.md (fashion), cities
   - Macro: [SOCIETY, ECONOMICS]
   - Content: Clothing by class and region

9. `society/education.md`
   - Sources: factions (collegia), cities
   - Macro: [SOCIETY, TECHNOLOGY]
   - Content: Schools, apprenticeships, access by class

10. `society/civic_organizations.md`
    - Sources: factions_organizations.md (civic section)
    - Macro: [SOCIETY, POLITICS]
    - Content: Water wardens, burial societies, tenement watches

---

### POLITICS (8-10 wiki pages)

**Sources**: geography_maps.md (barons), factions_organizations.md, legal_systems.md

**Target Pages**:
1. `politics/government_systems.md`
   - Sources: Inferred from baron structure, geography
   - Macro: [POLITICS]
   - Content: How government actually works

2. `politics/baron_council.md`
   - Sources: geography_maps.md, character info
   - Macro: [POLITICS, CHARACTERS]
   - Content: Council structure, voting, power dynamics

3. `politics/legal_systems.md`
   - Sources: legal_systems.md
   - Macro: [POLITICS, SOCIETY]
   - Content: Laws, courts, enforcement

4. `politics/law_enforcement.md`
   - Sources: cities (guards), factions
   - Macro: [POLITICS, SOCIETY]
   - Content: City Guard, Council Peacekeepers, Inquisition

5. `politics/military.md`
   - Sources: geography (baron forces), weaponry
   - Macro: [POLITICS, TECHNOLOGY]
   - Content: Military structure, forces, capabilities

6. `politics/diplomacy_espionage.md`
   - Sources: Nethvor info, baron relationships
   - Macro: [POLITICS, CHARACTERS]
   - Content: Intelligence networks, negotiations

7. `politics/conflicts_wars.md`
   - Sources: geography_maps.md (Extraction Wars, siege)
   - Macro: [POLITICS, LORE]
   - Content: Active conflicts, war causes

8. `politics/factions_overview.md`
   - Sources: factions_organizations.md
   - Macro: [POLITICS, SOCIETY]
   - Content: All major faction summary

9. `politics/rebels_resistance.md`
   - Sources: factions (Morshan-Breakers, etc.)
   - Macro: [POLITICS, SOCIETY]
   - Content: Revolutionary groups, methods

10. `politics/criminals_underground.md`
    - Sources: factions (Nethvor-Shadows, Blue Lanterns, etc.)
    - Macro: [POLITICS, ECONOMICS]
    - Content: Criminal networks, black markets

---

### ECONOMICS (6-8 wiki pages)

**Sources**: economics.md, overview.md (economy sections), factions

**Target Pages**:
1. `economics/economics_overview.md`
   - Sources: economics.md, overview.md
   - Macro: [ECONOMICS]
   - Content: Economic systems, principles

2. `economics/shyak_economy.md`
   - Sources: economics.md, overview.md (oil economy)
   - Macro: [ECONOMICS, MAGIC, POLITICS]
   - Content: Oil markets, pricing, futures

3. `economics/industries.md`
   - Sources: economics.md, technology.md
   - Macro: [ECONOMICS, TECHNOLOGY]
   - Content: Non-shyak industries, manufacturing

4. `economics/trade_commerce.md`
   - Sources: cities, geography (trade routes)
   - Macro: [ECONOMICS, GEOGRAPHY]
   - Content: Trade networks, merchant systems

5. `economics/currency_finance.md`
   - Sources: cities (GS currency), economics
   - Macro: [ECONOMICS, SOCIETY]
   - Content: Money, banking, investment

6. `economics/labor_systems.md`
   - Sources: economics.md, society, factions (guilds)
   - Macro: [ECONOMICS, SOCIETY, POLITICS]
   - Content: Guilds, unions, slavery, unemployment

7. `economics/black_markets.md`
   - Sources: overview.md, factions (criminal networks)
   - Macro: [ECONOMICS, POLITICS]
   - Content: Illegal trade, counterfeit, smuggling

8. `economics/class_inequality.md`
   - Sources: technology.md, society, economics
   - Macro: [ECONOMICS, SOCIETY]
   - Content: Wealth distribution, access disparities

---

### RELIGION (4-6 wiki pages)

**Sources**: religion_spirituality.md, factions

**Target Pages**:
1. `religion/religion_overview.md`
   - Sources: religion_spirituality.md
   - Macro: [RELIGION, SOCIETY]
   - Content: Major faiths, spiritual landscape

2. `religion/faiths_denominations.md`
   - Sources: religion_spirituality.md
   - Macro: [RELIGION, LORE]
   - Content: All belief systems

3. `religion/inquisition.md`
   - Sources: cities (siege), factions
   - Macro: [RELIGION, POLITICS]
   - Content: Religious enforcement, persecution

4. `religion/clergy_institutions.md`
   - Sources: religion_spirituality.md, factions
   - Macro: [RELIGION, SOCIETY]
   - Content: Religious orders, priests

5. `religion/rituals_practices.md`
   - Sources: overview.md (aurora rituals), religion
   - Macro: [RELIGION, SOCIETY]
   - Content: Ceremonies, observances

6. `religion/theology_philosophy.md`
   - Sources: religion_spirituality.md
   - Macro: [RELIGION, LORE]
   - Content: Religious thought, debates

---

### FACTIONS (Already well-organized)

**Sources**: factions_organizations.md

**Target Pages**:
1. `factions/guilds_orders.md`
   - Sources: factions (Guild section)
   - Macro: [SOCIETY, ECONOMICS]

2. `factions/criminals.md`
   - Sources: factions (Criminal section)
   - Macro: [POLITICS, ECONOMICS]

3. `factions/schools_learned.md`
   - Sources: factions (Schools section)
   - Macro: [SOCIETY, LORE]

---

### CHARACTERS (10+ wiki pages)

**Sources**: Extract from geography_maps.md, character_relationships.md, overview

**Target Pages** (all individual character pages):
1. ✓ `characters/shalen_mor.md` (SAMPLE CREATED)
2. `characters/telvor_shin.md`
3. `characters/koresh_val.md`
4. `characters/velasha_nen.md`
5. `characters/meshira_tal.md`
6. `characters/telumesh.md`
7. `characters/morshan.md`
8. `characters/nethvor.md`
9. `characters/vonder_shin.md`
10. `characters/keshiel.md`
11. `characters/moreth_kiren.md`
12. `characters/supporting_cast.md`

---

### LANGUAGE (4-6 wiki pages)

**Sources**: conlang_lexicon.json, name_charter.md, overview.md (name key)

**Target Pages**:
1. `language/conlang_overview.md`
   - Sources: overview.md (conlang note), name_charter
   - Macro: [LANGUAGE, LORE]
   - Content: System overview, methodology

2. `language/lexicon.md`
   - Sources: conlang_lexicon.json, overview.md (name key)
   - Macro: [LANGUAGE, REFERENCE]
   - Content: Complete vocabulary organized

3. `language/naming_conventions.md`
   - Sources: overview.md (character examples), name_charter
   - Macro: [LANGUAGE, SOCIETY]
   - Content: How names work, personality-based system

4. `language/place_names.md`
   - Sources: overview.md (compound terms)
   - Macro: [LANGUAGE, GEOGRAPHY]
   - Content: Geographic naming patterns

5. `language/grammar_syntax.md`
   - Sources: name_charter (Turkish affixes, etc.)
   - Macro: [LANGUAGE, REFERENCE]
   - NEEDS: Full grammar documentation

6. `language/dialects.md`
   - Sources: NEEDS DEVELOPMENT
   - Macro: [LANGUAGE, GEOGRAPHY]
   - NEEDS: Regional variations

---

### LORE (6-8 wiki pages)

**Sources**: Extract from overview.md, tech_history, geography

**Target Pages**:
1. `lore/history_ancient.md`
   - Sources: NEEDS DEVELOPMENT (pre-1500)
   - Macro: [LORE]
   - CRITICAL GAP

2. `lore/history_1500_1780.md`
   - Sources: NEEDS DEVELOPMENT
   - Macro: [LORE, TECHNOLOGY]
   - CRITICAL GAP

3. `lore/history_1780_1880.md`
   - Sources: overview.md (Arcane Revolution), tech_history
   - Macro: [LORE, TECHNOLOGY, POLITICS]
   - Content: Industrial era, innovation timeline

4. `lore/major_events.md`
   - Sources: geography (Second Cascade), scattered
   - Macro: [LORE, POLITICS]
   - Content: Key historical moments

5. `lore/mythology_legends.md`
   - Sources: overview.md (Luminarchs as myth), scattered
   - Macro: [LORE, RELIGION]
   - NEEDS: Development

6. `lore/timeline_master.md`
   - Sources: Compile all dates
   - Macro: [LORE, REFERENCE]
   - Content: Complete chronology

7. `lore/arcane_punk_genre.md`
   - Sources: overview.md (Arcane Punk definition)
   - Macro: [LORE, REFERENCE]
   - Content: Genre conventions, themes

8. `lore/world_mysteries.md`
   - Sources: Luminarchs, Nethvor identity, etc.
   - Macro: [LORE]
   - Content: Unsolved questions, secrets

---

### REFERENCE (6-8 wiki pages)

**Target Pages**:
1. `reference/quick_reference.md`
   - Content: One-page cheat sheets
   - Macro: [REFERENCE]

2. `reference/glossary.md`
   - Content: All terms defined
   - Macro: [REFERENCE]

3. `reference/index_master.md`
   - Content: Alphabetical everything
   - Macro: [REFERENCE]

4. `reference/plot_hooks.md`
   - Content: 100+ story hooks
   - Macro: [REFERENCE]

5. `reference/gm_tools.md`
   - Content: Name generators, calculators
   - Macro: [REFERENCE]

6. `reference/style_guide.md`
   - Content: Writing conventions
   - Macro: [REFERENCE]

7. `reference/conversion_notes.md`
   - Content: Changes from old to new format
   - Macro: [REFERENCE]

---

## Conversion Priority Order

### PHASE 1: Foundation (Week 1) - HIGH PRIORITY
Create these first to establish structure:
1. All PLANETARY pages (8 pages)
2. Core MAGIC pages (magic system, creatures, extraction) (3-4 pages)
3. GEOGRAPHY continents overview (1 page)
4. Core LORE pages (timeline, 1780-1880 history) (2 pages)

**Deliverable**: World foundation established (14-15 pages)

### PHASE 2: Systems (Week 2) - HIGH PRIORITY
1. All TECHNOLOGY pages (10 pages)
2. All MAGIC pages (complete category) (6-7 pages)
3. ECONOMICS core pages (4-5 pages)
4. POLITICS core pages (4-5 pages)

**Deliverable**: Systems documented (24-27 pages)

### PHASE 3: Detail (Weeks 3-4) - MEDIUM PRIORITY
1. All individual GEOGRAPHY pages (continents, cities) (15 pages)
2. All SOCIETY pages (10 pages)
3. All individual CHARACTER pages (12 pages)
4. FACTIONS reorganization (3-4 pages)

**Deliverable**: Detail layer complete (40 pages)

### PHASE 4: Culture & Support (Week 5) - MEDIUM PRIORITY
1. All RELIGION pages (6 pages)
2. All LANGUAGE pages (6 pages)
3. Remaining LORE pages (5-6 pages)
4. POLITICS detail pages (remaining) (3-4 pages)

**Deliverable**: Cultural depth (20-22 pages)

### PHASE 5: Reference & Polish (Week 6) - LOW PRIORITY
1. All REFERENCE pages (8 pages)
2. Cross-linking all pages
3. Master indexes
4. Final consistency pass

**Deliverable**: Production-ready wiki (8 pages + integration)

---

## Total Page Count Estimate

- PLANETARY: 8 pages
- MAGIC: 10 pages
- GEOGRAPHY: 18 pages
- TECHNOLOGY: 10 pages
- SOCIETY: 10 pages
- POLITICS: 10 pages
- ECONOMICS: 8 pages
- RELIGION: 6 pages
- FACTIONS: 4 pages
- CHARACTERS: 12 pages
- LANGUAGE: 6 pages
- LORE: 8 pages
- REFERENCE: 8 pages

**TOTAL: ~118 wiki pages**

With 3 sample pages already created, **115 pages remaining**.

---

## Critical Gaps Requiring New Content

1. **Exact Planetary Parameters**: Rotation period, year length (2-3 hours work)
2. **Moon Details**: Name, orbit, specifications (2 hours)
3. **15+ Magical Creatures**: Complete catalog (8-10 hours)
4. **Pre-1780 History**: Ancient to pre-industrial (4-6 hours)
5. **1500-1780 History**: Development era (3-4 hours)
6. **30+ Minor Settlements**: Geographic completeness (6-8 hours)
7. **Aerial Creatures**: Currently missing (2-3 hours)
8. **Complete Lexicon**: Expand from current 17 entries (6-8 hours)
9. **Grammar Documentation**: Full conlang specs (4-5 hours)
10. **Mythology & Legends**: Cultural stories (3-4 hours)

**Total New Content**: 41-55 hours

---

## Success Metrics

Conversion complete when:
- ☐ All 118 wiki pages created
- ☐ All existing content migrated
- ☐ All pages properly tagged
- ☐ All critical gaps filled
- ☐ All pages cross-linked
- ☐ Master indexes built
- ☐ No orphaned content
- ☐ Style guide compliance
- ☐ Macro landing pages complete
- ☐ Website-ready structure

---

## Next Immediate Action

**CHOICE POINT**:

**Option A**: Continue with full automated conversion
- I systematically convert all 115 remaining pages
- Faster but you review after
- ~15-20 hours of my work

**Option B**: Category-by-category with review
- I complete PLANETARY (8 pages) first
- You review and approve
- Then move to next category
- Slower but you guide direction

**Option C**: Critical gaps first
- Define exact parameters
- Create missing creatures
- Write missing history
- Then convert existing
- Content complete, then organize

**RECOMMENDATION**: Option B - Complete PLANETARY category now, let you review, then continue.

This gives you:
- Complete foundation
- Template you can validate
- Clear sense of final product
- Ability to course-correct

---

Ready to proceed with PLANETARY category conversion?
