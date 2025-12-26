# Norbela Wiki Reorganization & Consolidation Plan
## Wikipedia-Style Pages with Macro Tag System

---

## I. MACRO TAG TAXONOMY

### Primary Categories (Website Landing Pages)

1. **PLANETARY** - Physical world, celestial mechanics, natural phenomena
2. **LORE** - History, mythology, legends, major events
3. **SOCIETY** - Culture, daily life, social structures, customs
4. **POLITICS** - Government, factions, conflicts, power structures
5. **GEOGRAPHY** - Locations, regions, settlements, natural features
6. **MAGIC** - Magical systems, creatures, finyak, arcane mechanics
7. **TECHNOLOGY** - Devices, inventions, engineering, infrastructure
8. **ECONOMICS** - Trade, currency, resources, industries
9. **RELIGION** - Faiths, spiritual practices, beliefs, institutions
10. **CHARACTERS** - Major figures, biographies, relationships
11. **LANGUAGE** - Conlang, naming conventions, linguistics
12. **REFERENCE** - Quick guides, tables, tools, indexes

### Secondary Tags (For Cross-Referencing)
- Era: Ancient, Pre-Industrial, Industrial, Current
- Region: Tavanor, Sulenor, Eshtor, Vashor, Konor
- Tone: Hard-R, Body-Horror, Political, Economic, Environmental
- Caste: Upper, Middle, Lower, Outcasts
- Faction: Council, Barons, Rebels, Criminals, Religious

---

## II. CONSOLIDATED FILE STRUCTURE

```
/norbela/
├── /planetary/
│   ├── world_overview.md          [PLANETARY, LORE]
│   ├── celestial_mechanics.md     [PLANETARY]
│   ├── climate_biomes.md          [PLANETARY, GEOGRAPHY]
│   ├── moon_ring_system.md        [PLANETARY, LORE]
│   └── natural_phenomena.md       [PLANETARY]
│
├── /lore/
│   ├── history_ancient.md         [LORE]
│   ├── history_1500_1780.md       [LORE, SOCIETY]
│   ├── history_1780_1880.md       [LORE, TECHNOLOGY, POLITICS]
│   ├── major_events.md            [LORE, POLITICS]
│   └── mythology_legends.md       [LORE, RELIGION]
│
├── /geography/
│   ├── continents_overview.md     [GEOGRAPHY, PLANETARY]
│   ├── tavanor.md                 [GEOGRAPHY, POLITICS]
│   ├── sulenor.md                 [GEOGRAPHY, POLITICS]
│   ├── eshtor.md                  [GEOGRAPHY, POLITICS]
│   ├── vashor.md                  [GEOGRAPHY, POLITICS]
│   ├── konor.md                   [GEOGRAPHY, POLITICS]
│   ├── cities_major.md            [GEOGRAPHY, SOCIETY]
│   ├── settlements_minor.md       [GEOGRAPHY]
│   ├── natural_wonders.md         [GEOGRAPHY, PLANETARY]
│   └── travel_infrastructure.md   [GEOGRAPHY, TECHNOLOGY]
│
├── /magic/
│   ├── magic_system_overview.md   [MAGIC]
│   ├── finyak_substrate.md        [MAGIC, PLANETARY]
│   ├── magical_physics.md         [MAGIC, TECHNOLOGY]
│   ├── creatures_catalog.md       [MAGIC, ECONOMICS]
│   ├── shyak_extraction.md        [MAGIC, ECONOMICS, TECHNOLOGY]
│   ├── alternative_fuels.md       [MAGIC, TECHNOLOGY, ECONOMICS]
│   └── entropy_phenomena.md       [MAGIC, PLANETARY, LORE]
│
├── /technology/
│   ├── technology_overview.md     [TECHNOLOGY]
│   ├── device_catalog.md          [TECHNOLOGY, ECONOMICS]
│   ├── manufacturing.md           [TECHNOLOGY, ECONOMICS, SOCIETY]
│   ├── weaponry.md                [TECHNOLOGY, POLITICS]
│   ├── medicine_healing.md        [TECHNOLOGY, SOCIETY]
│   ├── communication.md           [TECHNOLOGY, SOCIETY]
│   ├── transportation.md          [TECHNOLOGY, GEOGRAPHY]
│   └── forbidden_tech.md          [TECHNOLOGY, POLITICS, LORE]
│
├── /society/
│   ├── social_structures.md       [SOCIETY, POLITICS]
│   ├── caste_system.md            [SOCIETY, ECONOMICS]
│   ├── daily_life_upper.md        [SOCIETY, ECONOMICS]
│   ├── daily_life_middle.md       [SOCIETY]
│   ├── daily_life_lower.md        [SOCIETY, ECONOMICS]
│   ├── culture_arts.md            [SOCIETY, LORE]
│   ├── customs_traditions.md      [SOCIETY, RELIGION]
│   ├── festivals_calendar.md      [SOCIETY, RELIGION, PLANETARY]
│   ├── education.md               [SOCIETY, TECHNOLOGY]
│   └── family_relationships.md    [SOCIETY]
│
├── /politics/
│   ├── government_systems.md      [POLITICS]
│   ├── baron_council.md           [POLITICS, CHARACTERS]
│   ├── legal_systems.md           [POLITICS, SOCIETY]
│   ├── law_enforcement.md         [POLITICS, SOCIETY]
│   ├── military.md                [POLITICS, TECHNOLOGY]
│   ├── diplomacy_espionage.md     [POLITICS]
│   └── conflicts_wars.md          [POLITICS, LORE]
│
├── /economics/
│   ├── economics_overview.md      [ECONOMICS]
│   ├── shyak_economy.md           [ECONOMICS, MAGIC, POLITICS]
│   ├── industries.md              [ECONOMICS, TECHNOLOGY]
│   ├── trade_commerce.md          [ECONOMICS, GEOGRAPHY]
│   ├── currency_finance.md        [ECONOMICS, SOCIETY]
│   ├── labor_systems.md           [ECONOMICS, SOCIETY, POLITICS]
│   └── black_markets.md           [ECONOMICS, POLITICS]
│
├── /religion/
│   ├── religion_overview.md       [RELIGION, SOCIETY]
│   ├── faiths_denominations.md    [RELIGION, LORE]
│   ├── inquisition.md             [RELIGION, POLITICS]
│   ├── clergy_institutions.md     [RELIGION, SOCIETY]
│   ├── rituals_practices.md       [RELIGION, SOCIETY]
│   └── theology_philosophy.md     [RELIGION, LORE]
│
├── /factions/
│   ├── factions_overview.md       [POLITICS, SOCIETY]
│   ├── barons_houses.md           [POLITICS, CHARACTERS]
│   ├── rebels_resistance.md       [POLITICS, SOCIETY]
│   ├── criminals_underground.md   [POLITICS, ECONOMICS]
│   ├── guilds_orders.md           [SOCIETY, ECONOMICS]
│   ├── religious_groups.md        [RELIGION, POLITICS]
│   └── civic_organizations.md     [SOCIETY, POLITICS]
│
├── /characters/
│   ├── characters_major.md        [CHARACTERS, POLITICS]
│   ├── shalen_mor.md              [CHARACTERS, POLITICS]
│   ├── telvor_shin.md             [CHARACTERS, TECHNOLOGY]
│   ├── koresh_val.md              [CHARACTERS, POLITICS]
│   ├── velasha_nen.md             [CHARACTERS, POLITICS]
│   ├── meshira_tal.md             [CHARACTERS, POLITICS]
│   ├── morshan.md                 [CHARACTERS, POLITICS]
│   ├── nethvor.md                 [CHARACTERS, POLITICS]
│   ├── telumesh.md                [CHARACTERS, LORE]
│   ├── vonder_shin.md             [CHARACTERS, RELIGION]
│   └── supporting_cast.md         [CHARACTERS]
│
├── /language/
│   ├── conlang_overview.md        [LANGUAGE, LORE]
│   ├── lexicon.md                 [LANGUAGE, REFERENCE]
│   ├── grammar_syntax.md          [LANGUAGE, REFERENCE]
│   ├── naming_conventions.md      [LANGUAGE, SOCIETY]
│   ├── dialects_variations.md     [LANGUAGE, GEOGRAPHY]
│   └── writing_systems.md         [LANGUAGE, SOCIETY]
│
└── /reference/
    ├── quick_reference.md         [REFERENCE]
    ├── timeline_master.md         [REFERENCE, LORE]
    ├── glossary.md                [REFERENCE]
    ├── index_master.md            [REFERENCE]
    ├── plot_hooks.md              [REFERENCE]
    ├── gm_tools.md                [REFERENCE]
    └── style_guide.md             [REFERENCE]
```

---

## III. WIKIPEDIA-STYLE PAGE TEMPLATE

Every page should follow this structure:

```markdown
---
title: [Page Title]
macro_tags: [PRIMARY, SECONDARY, TERTIARY]
region_tags: [if applicable]
era_tags: [if applicable]
last_updated: YYYY-MM-DD
status: [Complete | In Progress | Stub]
related_pages: [list of related wiki pages]
---

# [Page Title]

> **Quick Summary**: One-sentence description for quick reference

**In this article:**
- [Section 1]
- [Section 2]
- [Section 3]

---

## Overview
[2-3 paragraph introduction providing context and scope]

---

## [Main Sections]
### [Subsection]
[Content with internal links to related pages]

### [Subsection]
[Content]

---

## In the World
### Cultural Impact
[How this affects daily life, culture, society]

### Regional Variations
[How this differs by region, if applicable]

### Historical Context
[How this developed over time]

---

## Story Integration
### Narrative Uses
[How GMs/writers can use this]

### Plot Hooks
- Hook 1
- Hook 2
- Hook 3

### Key Scenes
[Suggested scene types involving this topic]

---

## Related Topics
### See Also
- [[Related Page 1]]
- [[Related Page 2]]
- [[Related Page 3]]

### Further Reading
- [[Deep Dive Document]]
- [[Technical Specifications]]

---

## References
### Source Documents
- Original file: [filename]
- Consolidated from: [list]

### Canonical Sources
- [Primary source documents]

---

## Metadata
**Status**: [Complete/In Progress/Stub]
**Last Updated**: [Date]
**Contributors**: [If tracking]
**Word Count**: [Approximate]

---

*[Footer with navigation: Previous | Index | Next]*
```

---

## IV. CURRENT FILE CONSOLIDATION MAP

### Files to Consolidate → New Wiki Pages

#### PLANETARY
- `world/overview.md` + relevant sections → `planetary/world_overview.md`
- Create new: `planetary/celestial_mechanics.md` (rotation, year, orbit)
- Create new: `planetary/moon_ring_system.md`
- Extract climate from overview → `planetary/climate_biomes.md`

#### GEOGRAPHY
- `world/geography/geography_maps.md` → Split into:
  - `geography/continents_overview.md`
  - `geography/tavanor.md` through `geography/konor.md` (5 files)
- `world/cities/cities_settlements.md` → Split into:
  - `geography/cities_major.md`
  - `geography/settlements_minor.md`
- `world/cities/city_layouts_compendium.md` → Merge into cities_major.md

#### MAGIC
- `World_Arcane_Oil_Combined.md` + sections from overview → Split into:
  - `magic/magic_system_overview.md`
  - `magic/finyak_substrate.md`
  - `magic/magical_physics.md`
  - `magic/creatures_catalog.md`
  - `magic/shyak_extraction.md`
  - `magic/alternative_fuels.md`
  - `magic/entropy_phenomena.md`

#### TECHNOLOGY
- `world/technology/technology.md` → Split into:
  - `technology/technology_overview.md`
  - `technology/device_catalog.md`
  - `technology/weaponry.md`
  - `technology/medicine_healing.md`
  - `technology/communication.md`
  - `technology/transportation.md`
  - `technology/forbidden_tech.md`
- `world/technology/tech_history_1500_1900.md` → Integrate into lore/history files
- `world/technology_catalog/technology_catalog.md` → Merge into device_catalog.md

#### SOCIETY
- `world/social/social_structures.md` → `society/social_structures.md`
- `world/society/character_relationships.md` → Extract to characters/ and society/
- Create new files for daily life, culture, customs, etc.

#### POLITICS
- Extract from geography, society files → Create politics/ structure

#### ECONOMICS
- `world/economics/economics.md` + magic economy sections → Split into economics/ files

#### RELIGION
- `world/religion/religion_spirituality.md` → Split into religion/ files

#### FACTIONS
- `world/factions/factions_organizations.md` → Split into factions/ files

#### LEGAL
- `world/legal/legal_systems.md` → `politics/legal_systems.md`

#### CHARACTERS
- Extract all character content → Create individual character pages

#### LANGUAGE
- `conlang_lexicon.json` → `language/lexicon.md`
- `world/conlang/naming_conventions/name_charter.md` → `language/naming_conventions.md`
- Create new grammar, dialect files

#### LORE
- Extract historical content from all files → Create history files
- Create mythology/legends file
- Create major events file

---

## V. IMPLEMENTATION PHASES

### Phase 1: Foundation (Week 1)
**Tasks**:
1. Create directory structure
2. Create templates for each macro category
3. Build master index framework
4. Set up cross-referencing system

**Deliverables**:
- Empty directory structure
- 12 category-specific templates
- Index skeleton

---

### Phase 2: Consolidation (Weeks 2-4)
**Tasks**:
1. Process existing files by macro category
2. Extract and reorganize content
3. Write new overview pages
4. Add macro tags to all pages

**Deliverables**:
- 50-60 consolidated wiki pages
- All existing content reorganized
- Proper tagging system in place

---

### Phase 3: Gap Filling (Weeks 5-8)
**Tasks**:
1. Identify missing pages (stubs)
2. Write new content for gaps
3. Expand thin sections
4. Add missing creatures, devices, etc.

**Deliverables**:
- All critical gaps filled
- 80-100 complete wiki pages
- No major stubs remaining

---

### Phase 4: Integration (Weeks 9-10)
**Tasks**:
1. Add cross-references between all pages
2. Build comprehensive indexes
3. Create navigation systems
4. Verify consistency

**Deliverables**:
- Fully linked wiki
- Master indexes
- Navigation aids
- Consistency verified

---

### Phase 5: Polish (Weeks 11-12)
**Tasks**:
1. Add "In the World" sections to all pages
2. Create plot hooks for every page
3. Build GM tools and references
4. Final editing pass

**Deliverables**:
- Production-ready wiki
- 100+ complete pages
- Full reference system
- Style guide compliance

---

## VI. WEBSITE STRUCTURE

### Landing Pages (Macro Categories)

#### Example: PLANETARY Landing Page
```
PLANETARY
=========

The physical world of Norbela, its celestial mechanics, 
climate, and natural phenomena.

Quick Facts:
- Planet diameter: 75% of Earth
- Gravity: 0.56g
- Rotation: 45 hours
- Orbit: 450 local days (20,250 standard hours)
- Climate: Iceworld

Browse Topics:
┌─────────────────────────────────────┐
│ • World Overview                    │
│ • Celestial Mechanics               │
│ • Climate & Biomes                  │
│ • Moon & Ring System                │
│ • Natural Phenomena                 │
│ • Finyak Substrate                  │
└─────────────────────────────────────┘

Related Categories: GEOGRAPHY, MAGIC, LORE
```

### Navigation System
```
Global Nav:
[PLANETARY] [LORE] [SOCIETY] [POLITICS] [GEOGRAPHY] 
[MAGIC] [TECHNOLOGY] [ECONOMICS] [RELIGION] 
[CHARACTERS] [LANGUAGE] [REFERENCE]

Page Nav:
Breadcrumb: Home > MAGIC > Creatures Catalog > Shyalev

Side Nav:
- Overview
- Main Content Sections
- In the World
- Story Integration
- Related Topics
```

---

## VII. METADATA SCHEMA

### Standard Frontmatter
```yaml
---
title: "Page Title"
macro_tags: 
  - PRIMARY
  - SECONDARY
region_tags:
  - Tavanor
  - Sulenor
era_tags:
  - Current
  - Industrial
tone_tags:
  - Hard-R
  - Body-Horror
caste_tags:
  - All
  - Upper
status: Complete
word_count: 3500
last_updated: 2024-12-20
related_pages:
  - link/to/page1
  - link/to/page2
source_files:
  - original/file1.md
  - original/file2.md
---
```

---

## VIII. QUALITY STANDARDS

### Every Wiki Page Must Have:
- [ ] Frontmatter with complete metadata
- [ ] Quick summary (1 sentence)
- [ ] Table of contents
- [ ] Overview section (2-3 paragraphs)
- [ ] Main content sections with headers
- [ ] "In the World" section (cultural/regional/historical context)
- [ ] "Story Integration" section (narrative uses, plot hooks)
- [ ] "Related Topics" section (see also links)
- [ ] References section (source documents)
- [ ] Metadata footer

### Content Standards:
- No contradictions with other pages
- Internal consistency
- Proper use of conlang terms
- Cross-references where appropriate
- Appropriate tone (dark, hard-R where relevant)
- 1500-5000 words (major topics)
- 500-1500 words (minor topics)
- 100-500 words (stubs, to be expanded)

---

## IX. CROSS-REFERENCING SYSTEM

### Link Types:
- `[[Direct Link]]` - To another wiki page
- `[[Link|Display Text]]` - Custom display
- `[External](URL)` - To outside resources
- `{{Template:Name}}` - For reusable content blocks

### Standard Cross-Reference Sections:
Every page should link to:
- Parent category page
- Related pages in same category
- Related pages in other categories
- Character pages (if relevant)
- Location pages (if relevant)
- Technology/magic pages (if relevant)

---

## X. TOOLS & UTILITIES NEEDED

### Create These Reference Tools:
1. **Master Index** - Alphabetical list of all pages
2. **Timeline Index** - All pages by historical era
3. **Geographic Index** - All pages by region
4. **Character Index** - All pages by character involvement
5. **Quick Reference Sheets** - One-page summaries
6. **Plot Hook Generator** - Searchable database
7. **Name Generator** - Using conlang rules
8. **Consistency Checker** - Find contradictions
9. **Link Validator** - Verify all internal links
10. **Tag Browser** - Filter pages by tags

---

## XI. NEXT IMMEDIATE STEPS

1. **Review & Approve Structure**
   - Confirm macro tag categories
   - Approve file organization
   - Verify page template

2. **Create First Pages** (Proof of Concept)
   - Write 3-5 sample pages using template
   - Test cross-referencing
   - Verify metadata system

3. **Build Consolidation Scripts** (If Needed)
   - Automate content extraction
   - Tag assignment helpers
   - Link conversion tools

4. **Begin Systematic Conversion**
   - Start with PLANETARY category
   - Move to MAGIC
   - Then GEOGRAPHY
   - Continue through all categories

---

## XII. SUCCESS METRICS

The reorganization is complete when:
- [ ] All existing content consolidated
- [ ] All pages use standard template
- [ ] All pages properly tagged
- [ ] All critical gaps filled
- [ ] All cross-references working
- [ ] All macro landing pages complete
- [ ] Master indexes built
- [ ] Navigation system functional
- [ ] Style guide followed consistently
- [ ] No orphaned content

---

## TIMELINE ESTIMATE

- **Phase 1** (Foundation): 1 week
- **Phase 2** (Consolidation): 3 weeks
- **Phase 3** (Gap Filling): 4 weeks
- **Phase 4** (Integration): 2 weeks
- **Phase 5** (Polish): 2 weeks

**Total: 12 weeks at 10-15 hours/week = 120-180 hours**

This includes both consolidation AND completing the world to 100%.

---

Would you like me to start with creating the first batch of sample wiki pages to demonstrate the format?
