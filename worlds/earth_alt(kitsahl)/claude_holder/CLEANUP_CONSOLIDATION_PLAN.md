---
title: CLEANUP & CONSOLIDATION PLAN
tags: [organization, cleanup, plan]
created: 2025-12-24
status: ACTION_REQUIRED
---

# EARTH_ALT(KITSAHL) FOLDER CLEANUP & CONSOLIDATION

## CURRENT STATUS

**Total Files**: ~50+ files across 14 folders
**Completed**: 3 new files with correct naming
**Remaining**: ~47 files need name corrections + consolidation

---

## PHASE 1: NAME CORRECTIONS ⚠️ CRITICAL

### High Priority Files (Reference Kitsahl frequently)

✅ places/kitsahl_region_expansion.md - DONE
✅ systems/bureau_preemptive_justice.md - DONE  
✅ systems/greymouth_resonance_trust.md - DONE (needs rename to kitsahl_resonance_trust.md)

❌ places/greymouth_overview.md.gdoc - **UPDATE + RENAME TO kitsahl_overview.md**
❌ places/admiralty_heights.md.gdoc
❌ places/crown_square.md.gdoc
❌ places/the_tangles.md.gdoc
❌ places/foundry_row.md.gdoc
❌ places/tidemark.md.gdoc
❌ places/regional_context.md.gdoc

### Find-Replace List:
```
"Greymouth" → "Kitsahl"
"Graymouth" → "Kitsahl"  
"Grey Bay" → "Kitsahl Bay"
"Fort Grey" → "Fort Kitsahl"
"Greymouth Resonance Trust" → "Kitsahl Resonance Trust"
"Kitsahl Territory" → "New Albion" (when referring to territory)
```

---

## PHASE 2: CONSOLIDATE DUPLICATES

### Identified Duplicates:
- mechanics/oracle_mechanics.md.gdoc + mechanics/04_oracle_mechanics.md.gdoc
- status/BUILD_STATUS.md.gdoc + status/_BUILD_STATUS.md.gdoc  
- social_structures/01_racial_hierarchy.md + social_structures/04_racial_hierarchy.md
- Possibly: people/class_tiers.md.gdoc vs social_structures/01_five_tier_system.md

**Action**: Compare, merge best content, delete redundant

---

## PHASE 3: RECOMMENDED NEW STRUCTURE

```
earth_alt(kitsahl)/claude_holder/
├── README.md ← CREATE
├── QUICK_REFERENCE.md ← CREATE
│
├── 01_core_canon/
│   ├── timelines/ (from root)
│   ├── history/ (from root)
│   └── guides/ (from root)
│
├── 02_geography/
│   ├── kitsahl_city/ (from places/)
│   └── new_albion_territory/
│
├── 03_systems/
│   ├── oracle_mechanics.md
│   ├── alchemy_system.md
│   ├── bureau_preemptive_justice.md
│   └── kitsahl_resonance_trust.md
│
├── 04_economy/ (keep as-is)
├── 05_social_structures/ (keep as-is)
├── 06_language/ (keep as-is)
├── 07_people/
│
└── _meta/
    ├── build_status.md
    ├── expansion_plan.md
    └── correction_guides/
```

---

## IMPLEMENTATION PRIORITY

**DO TODAY**:
1. Rename systems/greymouth_resonance_trust.md → kitsahl_resonance_trust.md
2. Update all places/ files with name corrections
3. Consolidate BUILD_STATUS files
4. Consolidate oracle_mechanics files

**DO THIS WEEK**:  
5. Name corrections in economy/ and mechanics/
6. Create master README.md
7. Create QUICK_REFERENCE.md

**WHEN TIME PERMITS**:
8. Full folder reorganization
9. Delete desktop.ini files
10. Archive deprecated content

---

## QUESTIONS FOR YOU

Before I proceed with automation:

1. **Folder reorganization**: Do you want the simplified structure above, or keep current 14-folder setup?

2. **File format**: Keep .gdoc files or convert everything to .md for consistency?

3. **Duplicates**: For oracle_mechanics, BUILD_STATUS, class_tiers - which versions should I keep?

4. **Automation**: Should I proceed with automated name corrections across all files now?

---

*Goal: Transform scattered files into organized worldbuilding bible ready for wiki import or story writing.*
