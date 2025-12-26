# Norbela Wiki Implementation Quick-Start Guide

## What You Have Now

1. **Complete Consolidation Plan** (CONSOLIDATION_MASTER_PLAN.md)
   - Maps all 110+ wiki pages
   - Shows which existing files become which pages
   - Identifies gaps and new content needed
   
2. **Sample Wiki Pages** (3 complete examples)
   - World Overview (PLANETARY)
   - Magical Creatures Catalog (MAGIC)
   - Shalen-Mor (CHARACTERS)

3. **Macro Category Templates** (12 landing pages)
   - Structure for your website homepage
   - Each category's index page

4. **Complete Worldbuilding Plan** (path to 100%)
   - What's missing and needs creation
   - Estimated time and priorities

---

## Recommended Implementation Path

### Option A: Do It Yourself (Systematic)

**Week 1-2: Foundation Setup**
1. Create directory structure on your Google Drive:
   ```
   norbela/wiki/
   ├── planetary/
   ├── lore/
   ├── society/
   ├── politics/
   ├── geography/
   ├── magic/
   ├── technology/
   ├── economics/
   ├── religion/
   ├── characters/
   ├── language/
   └── reference/
   ```

2. Start with PLANETARY category (6 pages):
   - Copy `world/overview.md` content
   - Split into sections per consolidation plan
   - Add frontmatter tags to each
   - Use sample pages as templates

**Week 3-4: Core Content**
3. Convert MAGIC category (8 pages)
4. Convert GEOGRAPHY continents (6 pages)

**Week 5-6: Characters and Places**
5. Create character pages (10+ pages)
6. Create city pages (from cities_settlements.md)

**Week 7-10: Remaining Categories**
7. Work through TECHNOLOGY, SOCIETY, POLITICS, etc.
8. Fill gaps with new content as you go

**Week 11-12: Integration**
9. Add cross-references between pages
10. Build indexes and reference tools

### Option B: Batch Conversion (Faster but Less Refined)

**Strategy**: Convert existing files quickly, refine later

For each existing file:
1. Copy content
2. Add frontmatter with macro tags
3. Split long files into logical pages
4. Save in appropriate category folder
5. Note gaps for later filling

**Time savings**: ~40-50 hours
**Trade-off**: Less polish, more editing needed later

### Option C: Hybrid (Recommended)

**Phase 1** (2 weeks): Convert all existing content
- Use templates to add frontmatter
- Don't worry about perfect organization
- Get everything into wiki format

**Phase 2** (2 weeks): Fill critical gaps
- Planetary parameters
- Magical creatures
- Character dossiers
- Historical timeline

**Phase 3** (4 weeks): Expand and deepen
- Add missing sections
- Expand thin content
- Create new pages

**Phase 4** (2 weeks): Integration and polish
- Cross-link everything
- Build indexes
- Add plot hooks
- Final consistency check

**Total time**: 10 weeks at 10-15 hrs/week

---

## Tools You Can Use

### Manual Conversion Checklist

For each file you convert:
- [ ] Add frontmatter (title, tags, status, etc.)
- [ ] Write quick summary sentence
- [ ] Create table of contents
- [ ] Split into logical sections with headers
- [ ] Add "In the World" section (cultural/regional context)
- [ ] Add "Story Integration" section (plot hooks)
- [ ] Add "Related Topics" links
- [ ] Add metadata footer
- [ ] Save in correct category folder

### Automated Tagging Helper

Based on content, add these macro tags:

**PLANETARY**: Physical world, climate, geography basics, celestial mechanics
**LORE**: History, mythology, past events, ancient knowledge
**SOCIETY**: Culture, daily life, customs, social structures
**POLITICS**: Government, power, factions, conflicts
**GEOGRAPHY**: Specific places, regions, cities, natural features
**MAGIC**: Creatures, finyak, shyak, magical systems
**TECHNOLOGY**: Devices, engineering, infrastructure
**ECONOMICS**: Trade, currency, resources, industries
**RELIGION**: Faiths, beliefs, spiritual practices
**CHARACTERS**: People, biographies, relationships
**LANGUAGE**: Conlang, linguistics, naming
**REFERENCE**: Tools, indexes, quick guides

### Quick Frontmatter Template

```markdown
---
title: "[Page Title]"
macro_tags: 
  - PRIMARY_TAG
  - SECONDARY_TAG
region_tags:
  - [Region if applicable]
era_tags:
  - [Era if applicable]
status: [Complete | In Progress | Stub]
word_count: [Approximate]
last_updated: YYYY-MM-DD
related_pages:
  - /category/page1
  - /category/page2
source_files:
  - original_file.md
---

# [Title]

> **Quick Summary**: One sentence overview

**In this article:**
- Section 1
- Section 2

[CONTENT HERE]

---

## In the World
[Cultural/regional/historical context]

---

## Story Integration
[Plot hooks and narrative uses]

---

## Related Topics
- [[Link to page 1]]
- [[Link to page 2]]

---

## Metadata
**Status**: [status]
**Last Updated**: [date]
```

---

## Priority Conversion Order

### Tier 1: Foundation (Do First)
1. World Overview (PLANETARY) ✓ DONE
2. Celestial Mechanics (PLANETARY)
3. Climate Biomes (PLANETARY)
4. Magic System Overview (MAGIC)
5. Creatures Catalog (MAGIC) ✓ DONE

### Tier 2: Core Content (Do Second)
6. Five continent pages (GEOGRAPHY)
7. Major cities (GEOGRAPHY)
8. Nine baron characters (CHARACTERS)
9. Technology overview (TECHNOLOGY)
10. History timeline (LORE)

### Tier 3: Depth (Do Third)
11. Society and culture pages
12. Economic systems
13. Religion and factions
14. Language and conlang

### Tier 4: Integration (Do Last)
15. Reference tools
16. Indexes
17. Cross-linking
18. Plot hook database

---

## Specific File Conversions

### Your Current Files → Wiki Pages

**World_Arcane_Oil_Combined.md** splits into:
- `/magic/magic_system_overview.md`
- `/magic/shyak_extraction.md`
- `/magic/magical_physics.md`
- `/magic/symbiotic_microfauna.md`
- `/economics/shyak_economy.md`

**geography_maps.md** splits into:
- `/geography/continents_overview.md`
- `/geography/tavanor.md`
- `/geography/sulenor.md`
- `/geography/eshtor.md`
- `/geography/vashor.md`
- `/geography/konor.md`
- `/geography/dead_zones.md`
- `/geography/travel_infrastructure.md`

**cities_settlements.md** splits into:
- `/geography/cities_major.md`
- `/geography/settlements_minor.md`
- Plus individual city pages if desired

**technology.md** splits into:
- `/technology/technology_overview.md`
- `/technology/device_catalog.md`
- `/technology/weaponry.md`
- `/technology/medicine_healing.md`
- `/technology/communication.md`
- `/technology/transportation.md`
- `/technology/forbidden_tech.md`

**factions_organizations.md** splits into:
- `/factions/factions_overview.md`
- `/factions/barons_houses.md`
- `/factions/rebels_resistance.md`
- `/factions/criminals_underground.md`
- `/factions/guilds_orders.md`
- `/factions/civic_organizations.md`

**etc.** (see CONSOLIDATION_MASTER_PLAN for full map)

---

## Quality Checklist

Before considering a page "complete":
- [ ] Has proper frontmatter with all tags
- [ ] Quick summary is clear and accurate
- [ ] Main content is well-organized
- [ ] "In the World" adds cultural context
- [ ] "Story Integration" has 3-5 plot hooks
- [ ] Related links work and are relevant
- [ ] No contradictions with other pages
- [ ] Conlang terms used correctly
- [ ] Appropriate tone (dark, hard-R where relevant)
- [ ] 1500-5000 words for major topics
- [ ] 500-1500 for minor topics

---

## Website Implementation

### Landing Page Structure

Each macro category needs:
1. **Header** - Category name and icon
2. **Quick Facts** - 6-8 key statistics
3. **Browse Topics** - 3-4 subsections with links
4. **Related Categories** - Cross-links
5. **Featured Content** - Popular articles

See `macro_category_landing_pages.md` for templates.

### Navigation System

**Global Nav** (on every page):
```
[HOME] [PLANETARY] [LORE] [SOCIETY] [POLITICS] [GEOGRAPHY] 
[MAGIC] [TECHNOLOGY] [ECONOMICS] [RELIGION] [CHARACTERS] 
[LANGUAGE] [REFERENCE]
```

**Breadcrumb** (on every page):
```
Home > CATEGORY > Current Page
```

**Page Links** (wiki-style):
```
[[Page Title]] → links to /category/page_title
```

---

## Next Steps

### Immediate (This Week)
1. **Review** consolidation plan
2. **Decide** on exact planetary parameters (rotation, year)
3. **Choose** implementation path (A, B, or C)
4. **Start** with 5-10 pages from Tier 1

### Short-Term (Next Month)
5. **Convert** all existing files to wiki format
6. **Fill** critical gaps (creatures, history, characters)
7. **Build** directory structure
8. **Create** indexes

### Long-Term (Next 3 Months)
9. **Expand** all categories to full depth
10. **Cross-link** everything
11. **Polish** and edit
12. **Deploy** to website

---

## Help Available

If you want me to:
- **Convert specific files** - Share the file and I'll convert it
- **Create missing content** - Tell me which gap to fill
- **Build indexes** - I can generate from existing pages
- **Check consistency** - I can audit for contradictions
- **Write new pages** - Specify topic and I'll create

Just let me know which part you want help with next!

---

## Time Estimates

**Per Page** (average):
- Convert existing content: 30-60 minutes
- Create new content: 1-3 hours
- Polish and cross-link: 15-30 minutes

**Total Project**:
- 60 pages (existing content): 30-60 hours
- 50 pages (new content): 50-150 hours
- Integration: 20-30 hours
- **Grand Total**: 100-240 hours

**At 10 hours/week**: 10-24 weeks (2.5-6 months)
**At 20 hours/week**: 5-12 weeks (1.25-3 months)

---

## Success Metrics

You'll know you're done when:
- [ ] All 110+ pages exist
- [ ] No major contradictions
- [ ] All tags properly assigned
- [ ] Cross-links functional
- [ ] Indexes complete
- [ ] Can answer any question quickly
- [ ] New writers can onboard in 4-6 hours
- [ ] Website structure ready to deploy

---

**Ready to start? Pick your first 5 pages and let's convert them!**
