
# Series/Saga Structure Template

## Purpose

This document governs multi-installment narrative structures (trilogies, quartets, sagas). It extends the single-story structure rules to longer arcs while maintaining voice consistency per default.md.

---

# PART ONE: SERIES FOUNDATION

## 1.1 Series Identity

### Core Documentation

| Element                     | Description                             |
| --------------------------- | --------------------------------------- |
| **Series Title**      |                                         |
| **Installment Count** | (trilogy, quartet, five-book, ongoing)  |
| **Structure Type**    | (arc-based, episodic, hybrid)           |
| **Genre**             |                                         |
| **Medium**            | (novel, novella collection, screenplay) |

### Series Premise

One paragraph capturing the entire series arc. This should answer:

- What world/situation?
- What central conflict spans all installments?
- What's at stake across the full arc?

### Series-Level Thematic Question

The overarching question the series explores. Each installment should approach this question from a different angle.

Example: "Can individuals change systems built on corruption, or do the systems change them?"

### Philosophical/Economic Throughlines

Per worldbuilding requirements, identify which concepts thread through the series:

- [ ] Information asymmetry
- [ ] Sunk cost fallacy
- [ ] Moral hazard
- [ ] Adverse selection
- [ ] Signaling theory
- [ ] Loss aversion
- [ ] Opportunity cost
- [ ] Other: _______________

Track which installment emphasizes which concept.

---

## 1.4 Theoretical Framework Application
<!-- METADATA
category: series_foundation
applies_to: all_installments
dependencies: [1.1_series_identity, worldbuilding]
output_format: table
-->

### Concept-to-Plot Integration

Economic and philosophical concepts must drive character decisions and plot reversals, not just decorate the world. Each concept should create meaningful story pressure.

| Concept | Definition | Series Application | Book 1 | Book 2 | Book 3 |
|---------|------------|-------------------|--------|--------|--------|
| Sunk cost fallacy | Refusing to abandon failed investment despite mounting costs | Protagonist can't quit quest despite evidence of futility | Introduce: Character commits to path | Escalate: Cost becomes unbearable | Pay off: Must choose to persist or abandon |
| Information asymmetry | One party knows more than another, enabling exploitation | Antagonist withholds true cost of magic/technology | Hidden: Antagonist operates with hidden knowledge | Partial reveal: Protagonist suspects deception | Full reveal: Truth exposed, alters stakes |
| Loss aversion | Fear of losing what you have outweighs desire for gain | Character refuses risky action that could save more | Setup: Character protects status quo | Test: Opportunity requires risk | Crisis: Must risk loss for greater good |

### Integration Rules

- Each declared concept must drive at least one major plot decision per book
- Concepts should be dramatized through character action and consequences, never explained in dialogue
- At least one concept should be the direct *cause* of a major reversal or crisis
- Concepts can layer: sunk cost + loss aversion = character trapped by their own psychology
- Track concept application in scene cards: "This scene dramatizes [concept]"

### Validation Checklist

- [ ] Each concept has concrete story application, not just world flavor
- [ ] Protagonist makes at least one decision driven by declared concept
- [ ] Antagonist's strategy reflects at least one declared concept
- [ ] Concept creates meaningful stakes (consequences matter to characters)
- [ ] Concepts visible in action, not exposition

---

## 1.2 Series Arc Architecture
<!-- METADATA
category: series_foundation
applies_to: series_structure
dependencies: [1.1_series_identity]
output_format: mapping_table
-->

### Arc-to-Installment Mapping

The series functions as a macro-story with each installment serving as an act:

| Series Length       | Structure Model | Installment Functions                                                          |
| ------------------- | --------------- | ------------------------------------------------------------------------------ |
| **Trilogy**   | Three-act       | Book 1: Setup/Complication, Book 2: Confrontation/Reversal, Book 3: Resolution |
| **Quartet**   | Four-act        | Book 1: Setup, Book 2: Complication, Book 3: Crisis, Book 4: Resolution        |
| **Five-book** | Five-part       | Each book = one part per story structure rules                                 |
| **Longer**    | Nested arcs     | Map sub-trilogies or quartets within larger structure                          |

### Series Beat Sheet

| Beat                 | Location                              | Function                                  | Description | Example/Template |
| -------------------- | ------------------------------------- | ----------------------------------------- | ----------- | ---------------- |
| Series Hook          | Book 1, Part 1                        | Establish world and central tension       | What image/event introduces the world? What question does it raise? | "Protagonist discovers evidence of systemic corruption; raises question: how deep does this go?" |
| Series Question      | Book 1, Part 3                        | Pose the overarching thematic question    | What philosophical/moral question will the series explore? | "Can one person change a corrupt system without becoming corrupt themselves?" |
| False Victory/Defeat | Mid-series                            | Apparent resolution that's incomplete     | What seems resolved but isn't? What new problem emerges? | "Antagonist defeated, but their methods have infected protagonist" |
| Dark Night           | Penultimate book or final book Part 4 | Maximum despair, all seems lost           | What makes victory seem impossible? What has protagonist lost? | "Protagonist's allies dead/turned, last refuge destroyed, hope extinguished" |
| Series Climax        | Final book, Part 5                    | Thematic question answered through action | What choice/action answers the thematic question? | "Protagonist chooses principle over victory, accepts cost" |
| Series Resolution    | Final book, ending                    | New status quo, resonance                 | What has changed? What final image echoes the opening? | "World unchanged but protagonist transformed; final image mirrors opening with new meaning" |

### Tension Architecture Across Series

Map intended tension levels:

```
Book 1: ████████░░ (High tension, partial resolution)
Book 2: ██████████ (Escalation, major reversal, tension maintained)
Book 3: ████████████ (Maximum stakes, cathartic resolution)
```

**Rule**: No installment should end with lower tension than it started (except final book's resolution).

---

## 1.3 Triptych-Specific Structure
<!-- METADATA
category: series_foundation
applies_to: three_story_arcs
dependencies: [1.2_series_arc]
output_format: table
-->

### When to Use Triptych vs. Standard Trilogy

Choose the appropriate structure based on narrative intent:

**Use Triptych Structure if:**
- Each story can stand alone with complete character arc
- Stories share world/theme but may have different protagonists
- Emphasis on reread value and recontextualization
- Final story reframes/reinterprets events of first two
- Reader understanding deepens retroactively
- Stories are connected but not strictly sequential

**Use Standard Trilogy if:**
- Same protagonist throughout all three books
- Continuous plot thread (reader can't skip Book 2)
- Linear escalation of conflict
- Final book is climax/resolution, not recontextualization
- Each book ends on unresolved tension
- Character arc spans all three books continuously

**Hybrid Approach:**
- Each book has complete arc BUT contributes to larger arc
- Same protagonist but each book could be read alone
- Combines standalone satisfaction with series payoff

For three-story arcs (like Fonváros Triptych), additional requirements:

### Triptych Functions

| Story                 | Structural Role                                            | Emotional Register             | Ending Type                                 |
| --------------------- | ---------------------------------------------------------- | ------------------------------ | ------------------------------------------- |
| **Story One**   | Establish world, introduce corruption, protagonist awakens | Discovery → Disillusionment   | Open (questions raised)                     |
| **Story Two**   | Deepen stakes, show system's cost, complicate morality     | Tension → Moral complexity    | Complicated (partial victory, new problems) |
| **Story Three** | Force choice, pay off setups, resolve or transform         | Crisis → Catharsis or Tragedy | Closed (but resonant)                       |

### Triptych Linking Requirements

- Each story must be readable standalone (complete arc)
- Each story must deepen understanding of previous stories on reread
- At least one character, location, or object must appear in all three
- The thematic question must be approached from three distinct angles
- Final story must recontextualize events of first two

### Triptych Handoff Tracking

| Element                | Story 1 | Story 2 | Story 3 |
| ---------------------- | ------- | ------- | ------- |
| Protagonist            |         |         |         |
| Setting                |         |         |         |
| Time Period            |         |         |         |
| Central Relationship   |         |         |         |
| Antagonist Evolution   |         |         |         |
| Thread Carried Forward |         |         |         |
| Thread Resolved        |         |         |         |

---

# PART TWO: CHARACTER SYSTEMS

## 2.1 POV Architecture
<!-- METADATA
category: character_systems
applies_to: all_installments
dependencies: [1.2_series_arc, 2.2_character_arcs]
output_format: table
-->

### POV Structure Types

- **Fixed**: Same POV throughout series
- **Rotating**: Multiple POVs, consistent across series
- **Expanding**: New POVs added as series progresses
- **Contracting**: POVs removed (death, resolution) as series narrows
- **Lane-based**: Distinct narrative lanes that converge

### POV Rules for This Series

Document specific rules:

- How many POV characters per installment?
- Can POV characters die? (See death rules below)
- When can new POVs be introduced?
- Must all POVs appear in every installment?

### POV Death Rules

**The Irony Requirement**: When a POV character dies, the death must carry narrative irony—a gap between expectation and outcome that amplifies meaning.

Types of death irony:

- **Dramatic irony**: Reader knows something character doesn't
- **Situational irony**: Death contradicts character's defining trait/goal
- **Cosmic irony**: Fate/world punishes character for virtues
- **Tragic irony**: Character's strength becomes their undoing

**Death must not be**:

- Random (unless randomness is thematically essential)
- Shock-value without resonance
- Convenient plot solution
- Punishment for reader-sympathetic choices

### POV Tracking Table

| Character | POV in Book 1 | POV in Book 2 | POV in Book 3 | Status | Death (if applicable) |
| --------- | ------------- | ------------- | ------------- | ------ | --------------------- |
|           |               |               |               |        |                       |

### AI Prompt Template: POV Structure Planning

```
I am planning a [trilogy/quartet/triptych] with [number] POV characters.
My POV structure type is [fixed/rotating/expanding/contracting/lane-based].
The protagonist is [name], whose arc is [summary].

Help me determine:
1. Which additional POVs are needed to tell this story effectively
2. When each POV should be introduced (which book/part)
3. Which POVs (if any) can die and when, applying the irony requirement
4. How to maintain voice differentiation across [X] books
5. Whether all POVs need to appear in every installment

Series context: [brief premise and central conflict]
Thematic focus: [main thematic question]
```

---

## 2.2 Character Arc Mapping

### Protagonist Evolution Across Series

| Aspect           | Book 1 Start | Book 1 End | Book 2 End | Book 3 End |
| ---------------- | ------------ | ---------- | ---------- | ---------- |
| Core Want        | What they consciously pursue | Achieved/evolved? | New want or deeper understanding | Final state: transformed want |
| Core Need        | What they actually need (often unconscious) | Glimpsed? | Partially understood | Achieved or tragically missed |
| Core Flaw        | Character weakness that causes problems | Challenged | Persists but complicated | Overcome, accepted, or fatal |
| Core Strength    | Character asset that helps/hinders | Proven useful | Becomes liability or deepens | Tempered by experience |
| Key Relationship | Most important connection | Formed/strained | Tested/broken | Resolved/transformed |
| Worldview        | How they see reality | Naive certainty | Shattered/complicated | New understanding (wisdom or despair) |

**Example Row (Want):**
| Core Want | "Wants to prove themselves worthy" | "Proven to others but not to self" | "No longer seeks external validation" | "Accepts self, no longer needs proof" |

### Character Introduction/Exit Schedule

| Character | Introduced     | Function | Arc Complete   | Exit (if any) |
| --------- | -------------- | -------- | -------------- | ------------- |
|           | Book _, Part _ |          | Book _, Part _ |               |

### Relationship Evolution Tracking

Track key relationships across the series:

| Relationship | Book 1 State | Book 2 State | Book 3 State | Arc |
| ------------ | ------------ | ------------ | ------------ | --- |
|              |              |              |              |     |

---

## 2.3 Antagonist Architecture

### Antagonist Types Across Series

- **Series Antagonist**: The overarching opposition (person, system, force)
- **Installment Antagonists**: Book-specific opposition
- **Evolving Antagonist**: Antagonist who changes role across series
- **Revealed Antagonist**: True antagonist hidden until later installment

### Antagonist Escalation Requirements

**Rule**: Antagonist threat must escalate across installments. Each book's antagonist should be more dangerous, more personal, or more thematically complex than the last.

| Book | Antagonist | Threat Type | Action Taken | Stakes |
| ---- | ---------- | ----------- | ------------ | ------ |
| 1    |            |             |              |        |
| 2    |            |             |              |        |
| 3    |            |             |              |        |

### Antagonist Action Requirements

Per story structure rules, antagonists must ACT in every installment they appear. Track actions, consequences, and protagonist responses to ensure active opposition.

| Antagonist | Book | Action Taken | Consequence (immediate impact) | Protagonist Response | Escalation Factor |
|------------|------|--------------|-------------------------------|---------------------|------------------|
| [Name] | 1 | Destroys protagonist's safe house | Protagonist loses key ally, resources | Goes underground, seeks new allies | Trust network compromised |
| [Name] | 2 | Corrupts protagonist's mentor | Mentor becomes liability/enemy | Protagonist isolated, questions judgment | Personal betrayal |
| [Name] | 3 | Forces impossible choice | Protagonist must sacrifice principle or person | Makes choice, bears cost | Stakes become existential |

### Antagonist Action Validation

- [ ] Every antagonist acts at least once per book they appear in
- [ ] Each action has concrete consequences that affect protagonist
- [ ] Protagonist must respond to each antagonist action (even if response is inaction)
- [ ] Antagonist threat escalates across installments (more dangerous, more personal, or more complex)
- [ ] At least one antagonist action forces protagonist into moral dilemma

### Original Tracking Table (for simpler tracking)

Use this for quick reference; use expanded table above for detailed planning.

| Antagonist | Book 1 Actions | Book 2 Actions | Book 3 Actions |
| ---------- | -------------- | -------------- | -------------- |
|            |                |                |                |

---

# PART THREE: NARRATIVE THREADING

## 3.1 Setup/Payoff Engineering
<!-- METADATA
category: narrative_threading
applies_to: all_installments
dependencies: [1.2_series_arc, 2.2_character_arcs]
output_format: table
-->

### Series-Level Setups

Setups planted in early installments that pay off later:

| Setup | Planted (Book/Part) | Type | Payoff (Book/Part) | Satisfaction Target |
| ----- | ------------------- | ---- | ------------------ | ------------------- |
|       |                     |      |                    |                     |

**Setup Types**:

- Object (physical item)
- Information (fact, secret)
- Relationship (connection established)
- Ability (skill, trait)
- Pattern (recurring element)
- Thematic (idea seeded)

### Payoff Timing Rules

- Minor setups: Pay off within same book
- Medium setups: Pay off within next book
- Major setups: Can span entire series, but must be recalled before payoff
- Series-defining setups: Planted in Book 1, paid off in final book

### Retroactive Enhancement

Elements in early books that gain meaning on reread after later books:

| Element | Original Context | Enhanced Meaning | Book That Recontextualizes |
| ------- | ---------------- | ---------------- | -------------------------- |
|         |                  |                  |                            |

### Setup/Payoff Validation Rules

- [ ] Every setup has a payoff location identified
- [ ] No payoff occurs before its setup (chronological check)
- [ ] No setup pays off more than one book later without a callback/reminder
- [ ] Major setups pay off in climactic moments (Part 5 or final book)
- [ ] Series-defining setups planted in Book 1 have clear payoff in final book
- [ ] At least one setup per book creates "I knew it!" reader satisfaction
- [ ] At least one setup per book creates "I didn't see that coming!" surprise

---

## 3.2 Motif Discipline
<!-- METADATA
category: narrative_threading
applies_to: all_installments
dependencies: [3.1_setup_payoff, default.md]
output_format: table
-->

### Series Motifs

Motifs that thread through all installments:

| Motif | Book 1 Appearance | Book 2 Evolution | Book 3 Payoff |
| ----- | ----------------- | ---------------- | ------------- |
|       |                   |                  |               |

### Motif Rules

- Each declared motif must appear in each installment
- Motif meaning should evolve/deepen across the series
- At least one motif should crystallize in the series' final image
- Motifs should connect to thematic content (not just decoration)

### Installment-Specific Motifs

Motifs unique to individual books (may connect to series motifs):

| Book | Unique Motif | Function | Connection to Series Motifs |
| ---- | ------------ | -------- | --------------------------- |
| 1    |              |          |                             |
| 2    |              |          |                             |
| 3    |              |          |                             |

### AI Prompt Template: Motif Planning

```
I am planning motifs for my [trilogy/saga] with the following elements:

Series themes: [list main themes]
Setting: [brief description]
Protagonist's journey: [arc summary]
Key emotional tones: [e.g., melancholy, dread, hope]

Help me:
1. Identify 2-4 series-spanning motifs that connect to these themes
2. Suggest how each motif can appear in each installment
3. Show how motif meaning should evolve across the series
4. Recommend one motif to crystallize in the final image
5. Identify installment-specific motifs that support series motifs

Consider sensory motifs (objects, images), conceptual motifs (phrases, ideas), and symbolic motifs (colors, weather, animals).
```

---

## 3.3 Subplot Management
<!-- METADATA
category: narrative_threading
applies_to: all_installments
dependencies: [1.2_series_arc, 2.2_character_arcs]
output_format: table
-->

### Series-Spanning Subplots

Subplots that carry across multiple installments:

| Subplot | Function | Book 1 | Book 2 | Book 3 | Resolution |
| ------- | -------- | ------ | ------ | ------ | ---------- |
|         |          |        |        |        |            |

**Subplot Functions**:

- Mirror (reflects main theme from different angle)
- Contrast (shows alternative approach/outcome)
- Complicate (creates obstacles or competing demands)
- Deepen (reveals character through different context)
- Connect (links installments)

### Subplot Resolution Rules

- A subplot introduced must be resolved (even if "resolution" is deliberate ambiguity)
- Series-spanning subplots must advance in each installment they appear
- No subplot should disappear for an entire installment without justification
- Subplots should intersect with main plot at least once per book

### Thread Handoff Table

What carries from each book to the next:

| From Book 1 to Book 2 | From Book 2 to Book 3 |
| --------------------- | --------------------- |
|                       |                       |

---

## 3.4 Theme Evolution
<!-- METADATA
category: narrative_threading
applies_to: all_installments
dependencies: [1.1_series_identity, 3.1_setup_payoff]
output_format: table
-->

### Thematic Progression

How the central thematic question evolves:

| Book | Thematic Focus | Question Posed | Answer Suggested | Complication Added |
| ---- | -------------- | -------------- | ---------------- | ------------------ |
| 1    |                |                |                  |                    |
| 2    |                |                |                  |                    |
| 3    |                |                |                  |                    |

### Thematic Argument Structure

The series should function as an argument:

- **Book 1**: Thesis (initial position or question)
- **Book 2**: Antithesis (complication, counterargument, or reversal)
- **Book 3**: Synthesis (resolution that incorporates complexity)

### Theme Expression Rules

Per default.md, theme must be expressed through:

- Character action and consequence
- Dramatized conflict
- Motif evolution
- Final image resonance

NOT through:

- Character speeches explaining theme
- Narrator editorializing
- Convenient moral lessons

### AI Prompt Template: Thematic Development

```
My series explores the thematic question: [central question]

Series premise: [brief summary]
Protagonist's arc: [journey]
Antagonist represents: [what they embody]

Help me structure thematic development:

Book 1 - Thesis:
- What initial position/question should be posed?
- How should protagonist approach this naively or with certainty?
- What events challenge this initial position?

Book 2 - Antithesis:
- What complication/counterargument emerges?
- How does protagonist's understanding deepen or fracture?
- What reversal forces reconsideration of Book 1's "answer"?

Book 3 - Synthesis:
- How can the resolution incorporate complexity from both positions?
- What action (not speech) demonstrates the nuanced answer?
- How does final image express this thematic synthesis?

Ensure theme is expressed through character action, dramatized conflict, and motif evolution—never through exposition.
```

---

## 3.5 Foreshadowing & Misdirection Architecture
<!-- METADATA
category: narrative_threading
applies_to: all_installments
dependencies: [3.1_setup_payoff, 3.2_motif_discipline]
output_format: table
-->

Foreshadowing is a core element of the narrative style. Scenes are seeded with subtle and pointed hints—some true, some false—to reward rereading, hide meaning in plain sight, and create suspense through playful misdirection.

### Foreshadowing Types and Tracking

| Type | Book Planted | Part/Scene | Element/Detail | True/False | Payoff/Reveal Location | Reader Should Notice? |
|------|--------------|------------|----------------|------------|------------------------|----------------------|
| True clue | Book 1 | Part 2, Scene 3 | Character mentions "blood debt" | True | Book 3, Part 4 | Subtle - only on reread |
| Red herring | Book 1 | Part 3, Scene 7 | Suspicious object suggests false motive | False | Dispelled Book 2, Part 5 | Obvious - meant to mislead |
| Dramatic irony | Book 2 | Part 1, Scene 2 | Reader knows secret, character doesn't | True | Character learns Book 3, Part 2 | Explicit - reader aware |
| Symbolic foreshadowing | Book 1 | Part 1, Scene 1 | Weather/imagery hints at ending | True | Crystallizes in final scene | Unconscious - felt not noticed |
| False flag | Book 2 | Part 3, Scene 5 | Character seems to be traitor | False | Revealed innocent Book 2, Part 5 | Deliberate - test reader assumptions |

### Foreshadowing Rules

**True Foreshadowing Must:**
- Be "hidden in plain sight" (obvious in retrospect, subtle on first read)
- Connect to character psychology or world logic (not arbitrary)
- Gain new meaning when recontextualized by later events
- Appear natural in context (not obviously planted)
- Reward attentive readers without punishing casual readers

**False Foreshadowing Must:**
- Feel plausible enough to mislead
- Be based on reasonable assumptions (not cheap tricks)
- Serve thematic or character purpose beyond mere surprise
- Be dispelled clearly (not just forgotten)
- Create "I should have known" feeling when revealed as misdirection

### Misdirection Requirements

- At least **one major red herring per installment**
- At least **two true clues** planted early that pay off late (series-spanning)
- At least **one moment of dramatic irony** per book (reader knows more than character)
- Final book must **recontextualize at least three elements** from earlier books

### Foreshadowing Integration Checklist

- [ ] Foreshadowing woven into sensory description (not exposition)
- [ ] False and true foreshadowing balanced (not all red herrings)
- [ ] Character psychology determines what details they notice
- [ ] Motifs serve as foreshadowing vehicles
- [ ] At least one foreshadowing element appears in opening of Book 1 and closing of final book
- [ ] Reread value: early scenes gain new significance after series completion

### AI Prompt Template: Foreshadowing Planning

```
I am planning foreshadowing for my [trilogy/quartet/saga].
My series centers on [brief premise].
The major reversal/revelation is: [key plot turn].

Help me:
1. Identify 3-5 true clues I can plant in Book 1 that pay off in later books
2. Design 2-3 red herrings that mislead readers toward false conclusions
3. Determine which clues should be obvious vs. subtle
4. Create moments of dramatic irony where reader knows more than protagonist
5. Plan how final book recontextualizes early details

Key thematic elements: [themes]
Protagonist's arc: [brief summary]
Antagonist's hidden motivation: [if applicable]
```

---

# PART FOUR: READER EXPERIENCE

## 4.1 Reader Question Management
<!-- METADATA
category: reader_experience
applies_to: all_installments
dependencies: [1.2_series_arc, 3.4_theme_evolution]
output_format: table
-->

### The Question Engine Across Series

What questions drive reader through each installment:

| Book | Opening Question | Midpoint Question | Closing Question (carried forward) |
| ---- | ---------------- | ----------------- | ---------------------------------- |
| 1    |                  |                   |                                    |
| 2    |                  |                   |                                    |
| 3    |                  |                   |                                    |

### Question Rules

- Each book must answer its opening question (at least partially)
- Each book must raise new questions
- Series-level questions should become more urgent, not less
- Final book must answer the series-level question (even if answer is complex)

---

## 4.2 Emotional Journey Mapping
<!-- METADATA
category: reader_experience
applies_to: all_installments
dependencies: [1.2_series_arc, 2.2_character_arcs]
output_format: emotional_map
-->

### Series Emotional Arc

Map intended reader emotional experience:

| Book | Part 1 | Part 2 | Part 3 | Part 4 | Part 5 | Overall |
| ---- | ------ | ------ | ------ | ------ | ------ | ------- |
| 1    |        |        |        |        |        |         |
| 2    |        |        |        |        |        |         |
| 3    |        |        |        |        |        |         |

Use emotional descriptors: curiosity, dread, hope, despair, tension, relief, satisfaction, devastation, catharsis, resonance, etc.

### Emotional Pacing Rules

- Don't sustain single emotional register across entire book
- Provide relief beats even in dark narratives
- Earn catharsis through sufficient buildup
- Final book's ending should provide emotional closure even if plot remains somewhat open

---

## 4.3 Satisfaction Engineering
<!-- METADATA
category: reader_experience
applies_to: all_installments
dependencies: [3.1_setup_payoff, 3.5_foreshadowing]
output_format: table
-->

### Satisfaction Markers Across Series

Plan specific moments of reader satisfaction:

| Type                                          | Book 1 | Book 2 | Book 3 |
| --------------------------------------------- | ------ | ------ | ------ |
| "I knew it" (suspicion confirmed)             |        |        |        |
| "I didn't see that coming" (earned surprise)  |        |        |        |
| "Finally" (character does what reader wanted) |        |        |        |
| "No, don't" (dreaded choice made)             |        |        |        |
| Callback reward (early detail matters)        |        |        |        |
| Character growth visible                      |        |        |        |

### Series-End Satisfaction Requirements

The final installment must provide:

- [ ] Resolution of central conflict
- [ ] Completion of protagonist's character arc
- [ ] Payoff of major series-level setups
- [ ] Thematic crystallization
- [ ] Emotional catharsis appropriate to genre
- [ ] Final image that resonates with series opening

---

## 4.4 Resonance Engineering
<!-- METADATA
category: reader_experience
applies_to: series_ending
dependencies: [1.2_series_arc, 3.2_motif_discipline, 3.4_theme_evolution]
output_format: table
-->

The series ending must create resonance—a sense of completion that echoes the beginning while showing transformation. This requires deliberate architectural planning.

### Resonance Requirements

The final installment's ending must achieve:

1. **Image Echo**: Final scene image echoes series opening (transformed)
2. **Motif Crystallization**: At least one series motif appears in new context
3. **Thematic Answer**: Series question answered (even if complexly)
4. **Emotional Closure**: POV character's emotional arc complete
5. **Transformation Visible**: Change is demonstrated through contrast with beginning

### Resonance Tracking

| Element | Series Opening (Book 1, Part 1) | Series Closing (Final Book, Part 5) | Transformation |
|---------|--------------------------------|-------------------------------------|----------------|
| **Image** | What literal image/scene opens the series? | What literal image/scene closes the series? | How does the same/similar image now mean something different? |
| **Example** | "Protagonist stands at city gates, looking in" | "Protagonist stands at city gates, looking out" | "Once seeking entry/belonging, now leaving/transformed" |
| **Motif** | First appearance of key motif | Final appearance of key motif | How has its meaning evolved? |
| **Example** | "Mirror shows protagonist's face - doesn't recognize self" | "Mirror shows protagonist's face - finally recognizes self" | "Journey from alienation to self-knowledge" |
| **Question** | What question is posed? | What answer is offered? | What complexity/wisdom was gained? |
| **Example** | "Can I change the system?" | "I changed, system remains - but that matters" | "Individual transformation vs. systemic change" |
| **Emotion** | What does protagonist feel? | What does protagonist feel? | How has emotional capacity/understanding shifted? |
| **Example** | "Fear, confusion, determination" | "Acceptance, clarity, melancholy hope" | "From naive determination to wise acceptance" |

### Resonance Design Worksheet

Complete before drafting final installment:

**Series Opening Scene:**
- Location:
- POV character's physical position:
- Key sensory details:
- Emotional register:
- What protagonist wants:
- What protagonist doesn't yet know:

**Series Closing Scene:**
- Location: [same/similar/contrasting?]
- POV character's physical position:
- Key sensory details: [which echo opening?]
- Emotional register: [how transformed?]
- What protagonist has learned:
- What protagonist has sacrificed:
- What new understanding:

**Resonance Checklist:**
- [ ] Final scene location relates to opening (same place, symbolic parallel, or meaningful contrast)
- [ ] At least one sensory detail from opening reappears transformed
- [ ] Protagonist's final action mirrors/inverts opening action
- [ ] At least one motif crystallizes in final image
- [ ] Closing line echoes opening thematically (not literally)
- [ ] Reader can "feel" the journey's weight in final image
- [ ] Ending avoids explaining its own symbolism (show, don't tell)

### AI Prompt Template: Resonance Engineering

```
I am designing the resonant ending for my [trilogy/saga].

Series opening scene:
- Location: [where]
- Image: [what we see]
- Protagonist state: [emotional/physical]
- Key motif introduced: [what]

Series arc:
- Protagonist's journey: [brief summary]
- Central question: [thematic question]
- Key transformations: [what changed]

Help me design a closing scene that:
1. Echoes the opening image with transformation
2. Crystallizes [motif name] in new context
3. Answers the central question through image/action, not explanation
4. Provides emotional closure while honoring complexity
5. Creates "full circle" feeling without being repetitive

What specific images, actions, or sensory details should appear in the final scene?
```

---

## 4.5 Reader Experience Diagnostics
<!-- METADATA
category: reader_experience
applies_to: revision
dependencies: [4.1_question_management, 4.2_emotional_journey, 4.3_satisfaction_engineering]
output_format: diagnostic_table
-->

When reader experience fails, use this diagnostic tool to identify and fix structural issues.

### Common Failure Patterns

| Symptom | Likely Cause | Diagnostic Questions | Fix |
|---------|--------------|---------------------|-----|
| "Middle book feels static" | Stakes didn't escalate; protagonist passive | Does antagonist ACT in Book 2? Does protagonist make choices with consequences? | Add antagonist action forcing protagonist choice; raise personal stakes |
| "Ending felt abrupt" | Insufficient emotional buildup | Map emotional beats in Part 4-5: does tension build? Is catharsis earned? | Add physical stakes in Part 4; extend Part 5 emotional processing |
| "Lost thread between books" | No handoff elements | Check: what questions carry forward? What relationships continue? | Ensure 2-3 threads explicitly carry forward; end on unresolved question |
| "Character feels different" | Voice drift | Compare dialogue in Book 1 vs. current: same speech patterns? | Reread previous dialogue; verify sentence length, word choice, verbal tics |
| "Don't care about stakes" | Stakes not personal enough | Are consequences abstract or concrete? Do they threaten what character loves? | Make stakes personal; threaten relationships, identity, or core values |
| "Saw it coming" | Foreshadowing too obvious | Is reversal telegraphed? Are alternatives presented? | Add red herrings; make "correct" interpretation seem unlikely |
| "That came out of nowhere" | Insufficient setup | Is reversal seeded? Does it follow from established rules/character? | Plant setup earlier; add callback before payoff |
| "Why should I read Book 3?" | Book 2 didn't raise new questions | Check Book 2 ending: what's unresolved? What new problem emerged? | Complicate resolution; reveal new layer of threat or mystery |
| "Protagonist is annoying" | Flaw without growth or growth without flaw | Does protagonist learn? Do they still have edge/complexity? | Balance growth with consistent flaw; show progress AND setback |
| "Pacing drags" | Too much setup, not enough action | Setup-to-payoff ratio: is setup justified by payoff? | Cut redundant setup; accelerate payoff; add active opposition |
| "Ending was too neat" | All conflicts resolved cleanly | Real cost? Messy consequences? Unresolved complexity? | Add bittersweet element; show price of victory; honor complexity |
| "Ending was too bleak" | No hope/transformation visible | Does protagonist grow? Is sacrifice meaningful? Any light? | Show transformation earned through suffering; add moment of grace |

### Diagnostic Workflow

**When feedback indicates problem:**

1. **Identify symptom** from table above (or describe in similar terms)
2. **Ask diagnostic questions** to pinpoint root cause
3. **Check dependencies**: Does problem originate in earlier section?
   - Character problem → Check 2.2 (character arcs)
   - Stakes problem → Check 1.2 (series arc), 2.3 (antagonist)
   - Pacing problem → Check 3.1 (setup/payoff), 4.1 (questions)
   - Satisfaction problem → Check 3.5 (foreshadowing), 4.3 (satisfaction engineering)
4. **Apply fix** from table
5. **Verify fix** addresses root cause, not just symptom

### Prevention Checklist

Use during drafting to avoid common failures:

- [ ] Each installment raises questions for next installment
- [ ] Antagonist acts in every installment (forces protagonist response)
- [ ] Stakes escalate and become more personal across series
- [ ] Protagonist makes choices (not just reacts) in every installment
- [ ] Voice consistency checked by rereading previous installment's dialogue
- [ ] Emotional register varies within each installment (not monotone)
- [ ] Major reversals have setup planted at least one part earlier
- [ ] Endings balance resolution with ongoing tension (except final book)

---

# PART FIVE: CRAFT CONSISTENCY

## 5.1 Voice Maintenance Across Series
<!-- METADATA
category: craft_consistency
applies_to: all_installments
dependencies: [default.md]
output_format: checklist
-->

### Voice Anchors

Per default.md, maintain across all installments:

- Sentence variation keyed to emotional intensity
- Deep POV consistency
- Sensory immersion (3+ senses per scene, non-visual included)
- Dark humor integration (2-3 moments per story minimum)
- Character voice differentiation

### Voice Drift Prevention

After drafting each installment:

- [ ] Reread previous installment's opening and closing
- [ ] Check sentence rhythm patterns match
- [ ] Verify POV depth consistent
- [ ] Confirm dark humor ratio maintained
- [ ] Ensure returning characters sound like themselves

---

## 5.2 Continuity Management
<!-- METADATA
category: craft_consistency
applies_to: all_installments
dependencies: [all_character_and_world_sections]
output_format: tracking_table
-->

### Continuity Categories

- **Hard continuity**: Facts that cannot change (character deaths, world rules, established history)
- **Soft continuity**: Details that should be consistent but can be quietly adjusted
- **Retconnable**: Elements deliberately left vague for flexibility

### Continuity Tracking

| Category    | Element | Established (Book/Part) | Notes |
| ----------- | ------- | ----------------------- | ----- |
| Hard        |         |                         |       |
| Soft        |         |                         |       |
| Retconnable |         |                         |       |

### Continuity Red Flags

- Character knowing information they shouldn't yet have
- Timeline contradictions
- World rule violations
- Character voice inconsistency
- Relationship status errors

---

## 5.3 Naming and Language Consistency
<!-- METADATA
category: craft_consistency
applies_to: all_installments
dependencies: [conlang_document, naming_conventions]
output_format: tracking_table
-->

### Conlang Application

Per naming conventions document:

- All character names follow conlang derivation rules
- Place names follow established patterns
- New terms introduced must be derived through full process
- Maintain pronunciation guide consistency

### Naming Tracking

| Character | Full Name | Common Address | First Appearance |
| --------- | --------- | -------------- | ---------------- |
|           |           |                |                  |

---

## 5.4 Craft Consistency Requirements
<!-- METADATA
category: craft_consistency
applies_to: all_installments
dependencies: [default.md, 5.1_voice_maintenance]
output_format: checklist
-->

These requirements derive from default.md and must be maintained across all installments. They define the voice and are non-negotiable.

### Dark Humor Integration

**Requirement**: At least **2-3 moments of dark humor per installment** (minimum).

Dark humor is not optional—it's counterpoint to grimness and reveals character intelligence and worldview.

**Types of Dark Humor:**
- Sardonic observation of hypocrisy or absurdity
- Gallows humor in the face of danger
- Bitter callbacks to earlier moments
- Understatement in extreme situations
- Self-aware acknowledgment of hopelessness

**Placement Strategy:**
- Most effective in tense moments (gallows humor as coping mechanism)
- Can emerge from POV character's internal voice or dialogue
- Cynical characters should have sardonic observations
- Even earnest characters can recognize absurdity

**Per-Installment Tracking:**

| Book | Dark Humor Moments | Location (Part, Scene) | Type | Character Source |
|------|-------------------|----------------------|------|------------------|
| 1 | Minimum 2-3 | | | |
| 2 | Minimum 2-3 | | | |
| 3 | Minimum 2-3 | | | |

**Red Flag**: If draft is relentlessly earnest throughout, add dark humor beats in revision pass.

---

### Sensory Immersion Requirements

**Requirement**: Every scene must engage **at least 3 senses**, with **at least one being non-visual**.

**Sensory Checklist:**
- **Visual**: Default sense; use but don't over-rely
- **Auditory**: Background noise, voice quality, silence
- **Olfactory**: Powerful for memory and atmosphere
- **Tactile**: Texture, temperature, pressure, pain
- **Gustatory**: Taste of air, food, fear (metallic), etc.
- **Proprioception**: Body awareness, weight, balance, muscle state

**Bodies in Space:**
Characters must exist as physical bodies, not floating consciousnesses:
- Where is their weight?
- What are their hands doing?
- How does their body respond to emotion? (clenched jaw, shallow breath, tight shoulders)
- What physical sensations accompany the scene's emotional content?

**Environmental Character:**
Settings should feel distinct through sensory signature:
- A temple feels different from a kitchen feels different from a slum
- Establish sensory baseline, then use deviation for emphasis
- Sensory details should reflect POV character's attention and psychology

**Per-Scene Audit** (sample scenes per installment):

| Book | Part | Scene | Visual | Auditory | Olfactory | Tactile | Gustatory | Proprioception | Total Senses | Pass? |
|------|------|-------|--------|----------|-----------|---------|-----------|---------------|--------------|-------|
| | | | Y | Y | N | Y | N | N | 3 | Y |

**Validation**: After drafting each installment, audit 10-15 random scenes. If >20% fail (fewer than 3 senses), revision required.

---

### Deep POV Maintenance

**Requirement**: Every scene must maintain consistent deep POV. Reader should feel embedded in character's consciousness.

**Interiority Checkpoints** (each scene requires minimum):
- **1-2 moments of raw emotional reaction** (not observation, not analysis—felt experience)
- **Physical sensation grounding** (body awareness: breath, heartbeat, muscle tension, temperature)
- **Thought patterns** that reflect character's specific psychology

**Common Deep POV Failures to Avoid:**
- **Telling emotions from outside**: "She was angry" → Show through sensation, thought, action
- **Camera-eye narration**: "She sat at the table and ate breakfast" → Filter through experience
- **Disappearing interiority during dialogue**: Maintain internal reaction, don't let scenes become transcripts
- **Placeholder vagueness**: Avoid "something" as emotional descriptor ("something like anger")—name it or describe specifically

**POV Temperature Tracking:**

Track emotional temperature across scenes. Should escalate across story arc, not remain at single register.

| Book | Part 1 Temp | Part 2 Temp | Part 3 Temp | Part 4 Temp | Part 5 Temp | Escalation? |
|------|------------|------------|------------|------------|------------|-------------|
| 1 | Curiosity | Unease | Dread | Fear | Partial relief | Y |
| 2 | | | | | | |
| 3 | | | | | | |

**Validation Checklist:**
- [ ] Each scene has at least one moment of raw emotional interiority
- [ ] Each scene grounds emotion in physical sensation
- [ ] Dialogue scenes maintain character's internal processing
- [ ] POV character's psychology visible in what they notice
- [ ] Emotional temperature varies across parts (not monotone)

---

### Sentence Variation & Rhythm

**Requirement**: Sentence structure must vary based on emotional intensity and pacing needs.

**Length Calibration by Emotional State:**
- **High tension/action/shock**: Short. Fragmented. Punchy. Subject-verb. No subordinate clauses.
- **Introspection/philosophy**: Longer, multi-clause sentences that wind through thought
- **Neutral narration**: Medium length, varied attack

**Sentence Opener Variation:**

Avoid repetitive subject-verb patterns. In any given paragraph, vary openers:
- Participial phrases: "Watching her father's hands, she understood..."
- Environmental/sensory: "The smell of lavender hit her first."
- Fragments: "Three generations. The lie went deeper than she'd known."
- Inverted structure: "Into the dark she went."
- Dependent clauses: "When the door opened, everything changed."

**Red Flag**: If three consecutive sentences begin with character name or pronoun + verb, restructure.

**Rhythm Markers:**
- Use fragments for emphasis, especially after longer passages
- Strategic paragraph breaks create beats—single-sentence paragraph hits harder
- Em-dashes should be rare (2-3 per scene maximum); don't use as crutch

**Per-Installment Check:**
- [ ] High-tension scenes use short, punchy sentences
- [ ] Introspective scenes use longer, winding sentences
- [ ] No more than 2 consecutive sentences with same opener pattern
- [ ] Fragments used strategically (not accidentally)
- [ ] Single-sentence paragraphs used for emphasis (not overused)

---

### Dialogue Voice Consistency

**Requirement**: Dialogue must reveal character through voice, not just convey information. Returning characters must sound like themselves across installments.

**Voice Differentiation** (establish for each speaking character):
- **Sentence length tendency** (terse vs. flowing)
- **Vocabulary register** (formal/educated vs. colloquial/working class)
- **Speech patterns** (interrupts self? speaks in questions? uses qualifiers?)
- **Characteristic phrases or verbal tics**

**Voice Consistency Test**: Cover dialogue tags. Can you identify speaker from voice alone? If not, revise.

**Class and Regional Markers:**
- Social class should be audible in speech patterns
- Regional origin should influence vocabulary and idiom
- Education level affects sentence complexity and word choice
- Profession shapes metaphor and reference

**Dialogue Rhythm:**
- Avoid characters speaking in complete, articulate paragraphs (especially in conflict)
- Include pauses, interruptions, unfinished thoughts
- Action beats between lines show physical subtext
- Silence is dialogue—mark what characters *don't* say

**Returning Character Tracking:**

| Character | Speech Pattern | Vocabulary Register | Verbal Tic/Phrase | Book 1 Sample | Book 2 Check | Book 3 Check |
|-----------|---------------|-------------------|------------------|---------------|--------------|-------------|
| | | | | | Consistent? | Consistent? |

**Validation Process:**
- [ ] Before drafting new installment, reread previous installment's dialogue for returning characters
- [ ] Create "voice sheet" for each returning character with sample dialogue
- [ ] During revision, verify speech patterns match established voice
- [ ] Check: Does character's class/education/region remain consistent?

---

### Show vs. Tell for Major Revelations

**Requirement**: Major revelations and reversals must be **dramatized**, not explained through dialogue.

**The Dramatization Requirement:**

When a character learns something crucial:
- **Show them discovering it** through action/observation when possible
- If another character must explain, interrupt with reaction, doubt, physical response
- **Never let exposition run longer than 3-4 sentences** without POV character responding

**Reversal Staging:**

The midpoint reversal (and other major turns) should:
- Have **visual/physical component** reader can "see"
- Create **immediate emotional impact** shown through POV character
- **Raise questions** rather than answer everything
- **Change character's behavior/posture/thought pattern** immediately after

**Avoiding the Exposition Dump:**

When information must be conveyed:
- Break into **dialogue exchange**, not monologue
- Have POV character **actively processing** (agreeing, doubting, connecting)
- Include **physical business** (movement, gesture, environmental interaction)
- Leave **some information for reader to infer**

**Per-Installment Tracking:**

| Book | Major Revelation | Delivery Method | Dramatized? | Immediate Impact Shown? |
|------|-----------------|----------------|-------------|-------------------------|
| 1 | [What is revealed] | [Action/dialogue/discovery] | Y/N | [How POV character reacts physically/emotionally] |
| 2 | | | | |
| 3 | | | | |

**Red Flags:**
- Character explains plot for more than 4 sentences uninterrupted
- POV character learns crucial information "off-screen"
- Revelation has no immediate physical/emotional consequences
- Reader told what happened rather than shown the moment

---

### Craft Consistency Master Checklist

Use after completing each installment:

- [ ] **Dark humor**: Minimum 2-3 moments present and tracked
- [ ] **Sensory immersion**: 10-15 random scenes audited; >80% have 3+ senses with 1+ non-visual
- [ ] **Deep POV**: Every scene has interiority checkpoint (emotion + physical sensation + psychology)
- [ ] **Sentence variation**: Rhythm matches emotional intensity; opener patterns varied
- [ ] **Dialogue voice**: Returning characters sound like themselves (voice sheet verified)
- [ ] **Show vs. tell**: Major revelations dramatized with immediate impact
- [ ] **Overall voice**: Matches previous installment (reread opening/closing of previous book)

**If any checklist item fails**, revision required before proceeding to next installment.

---

# PART SIX: INSTALLMENT BREAKDOWN
<!-- METADATA
category: installment_planning
applies_to: individual_books
dependencies: [all_previous_sections]
output_format: per_book_template
-->

## Template for Each Installment

Repeat this section for each book in the series:

### Book [N]: [Title]

**Structural Role**: [Setup/Confrontation/Resolution per series arc]

**Protagonist(s)**:
**POV Character(s)**:
**Antagonist(s)**:

**Central Conflict (this book)**:
**Thematic Focus (this book)**:
**Economic/Philosophical Concept Emphasized**:

**Five-Part Structure**:

| Part | %   | Beat | Description |
| ---- | --- | ---- | ----------- |
| 1    | 20% |      |             |
| 2    | 20% |      |             |
| 3    | 20% |      |             |
| 4    | 20% |      |             |
| 5    | 20% |      |             |

**Setups Planted**:

| Setup | Type | Intended Payoff |
| ----- | ---- | --------------- |
|       |      |                 |

**Payoffs Delivered**:

| From Book | Setup | How Paid Off |
| --------- | ----- | ------------ |
|           |       |              |

**Threads Carried Forward**:
------------------------

**Motif Appearances**:

| Series Motif | Appearance/Evolution |
| ------------ | -------------------- |
|              |                      |

**Reader Questions**:

- Opening:
- Closing (carried forward):

**Emotional Arc**: [One sentence]

**Ending Type**: [Resolved/Open/Cliffhanger/Complicated]

### AI Prompt Template: Installment Planning

```
I am planning Book [N] of my [trilogy/quartet/saga].

Series context:
- Overall premise: [brief summary]
- Series thematic question: [question]
- This book's structural role: [Setup/Confrontation/Resolution]

Previous installments:
- Book [N-1] ended with: [brief summary]
- Threads carrying forward: [list]
- Unresolved questions: [list]

This book should:
- Central conflict: [what's at stake]
- Protagonist arc: [where they start → where they end]
- Thematic focus: [specific angle on series question]
- Antagonist role: [what they do in this book]

Help me:
1. Structure five-part breakdown with key beats per part
2. Identify setups to plant (with intended payoff timing)
3. Identify payoffs to deliver from previous books
4. Determine motif appearances and evolution
5. Plan reader questions (opening question, closing question carried forward)
6. Design emotional arc across the five parts
7. Ensure this book escalates stakes from previous installment
8. Create satisfying ending that's [resolved/open/cliffhanger/complicated]
```

---

# PART SEVEN: SERIES DEVELOPMENT WORKFLOW
<!-- METADATA
category: workflow
applies_to: all_phases
dependencies: [all_previous_sections]
output_format: phased_checklist
-->

This workflow replaces traditional checklists with phase-based triggers that clarify **when** to apply each requirement.

---

## PHASE 1: Series Planning
**Trigger**: Before writing any installment

### Foundation Setup
- [ ] Series-level thematic question articulated (Section 1.1)
- [ ] Series arc architecture mapped (Section 1.2)
- [ ] Theoretical framework identified and integrated (Section 1.4)
- [ ] Structure type chosen (trilogy/triptych/quartet) with reasoning (Section 1.3)
- [ ] Series beat sheet complete with examples (Section 1.2)

### Character Architecture
- [ ] Character arcs mapped across all installments (Section 2.2)
- [ ] POV structure determined (Section 2.1)
- [ ] POV death rules established (if applicable) (Section 2.1)
- [ ] Antagonist escalation planned (Section 2.3)
- [ ] Antagonist actions scheduled with consequences (Section 2.3)

### Narrative Infrastructure
- [ ] Major series-spanning setups identified with intended payoffs (Section 3.1)
- [ ] Setup/payoff timing rules applied (Section 3.1)
- [ ] Series motifs declared (minimum 2-3) (Section 3.2)
- [ ] Foreshadowing architecture planned (true clues + red herrings) (Section 3.5)
- [ ] Resonance elements identified (opening/closing image relationship) (Section 4.4)

### Reader Experience Design
- [ ] Question engine mapped across series (Section 4.1)
- [ ] Emotional arc per installment sketched (Section 4.2)
- [ ] Satisfaction markers planned (Section 4.3)
- [ ] Series-end resonance requirements articulated (Section 4.4)

**Output**: Complete series structure document with all planning sections filled.

---

## PHASE 2: Installment Setup
**Trigger**: Before drafting each book

### Continuity Review
- [ ] Previous installment's opening and closing reread (Section 5.1)
- [ ] Previous installment's threads reviewed (what continues? what resolves?) (Section 3.3)
- [ ] Continuity document updated with new elements (Section 5.2)
- [ ] Returning characters' dialogue reviewed (voice refresh) (Section 5.4)

### Installment Planning
- [ ] This book's structural role in series clarified (Setup/Confrontation/Resolution) (Section 1.2)
- [ ] Five-part structure for this book outlined (Part 6)
- [ ] New setups planned with payoff timing identified (Section 3.1)
- [ ] Payoffs scheduled for setups from previous books (Section 3.1)
- [ ] This book's motif appearances planned (Section 3.2)
- [ ] This book's foreshadowing elements identified (Section 3.5)

### Character Preparation
- [ ] Character arcs for this installment reviewed (where they start/end) (Section 2.2)
- [ ] POV structure for this book confirmed (Section 2.1)
- [ ] Antagonist actions for this book detailed (Section 2.3)
- [ ] Voice anchors reviewed (sensory, POV depth, dark humor, sentence rhythm) (Section 5.1)

### Craft Setup
- [ ] Dark humor minimum identified (2-3 moments) (Section 5.4)
- [ ] Sensory immersion requirements noted (3+ senses per scene) (Section 5.4)
- [ ] Major revelations identified for dramatization (Section 5.4)
- [ ] Emotional temperature progression planned (Section 5.4)

**Output**: Installment-specific outline ready for drafting.

---

## PHASE 3: Installment Drafting
**Triggers**: During active writing

### After Completing Part 1
- [ ] Voice consistency spot-check: compare opening to previous book's opening (Section 5.1)
- [ ] Deep POV verified: interiority checkpoints present (Section 5.4)
- [ ] Sensory immersion audit: 5 random scenes checked for 3+ senses (Section 5.4)
- [ ] Series hook or callback present (Section 1.2)

### At Midpoint (After Part 3)
- [ ] Setup/payoff ratio check: are setups justified by payoffs? (Section 3.1)
- [ ] Antagonist has acted at least once (Section 2.3)
- [ ] Protagonist has made choices (not just reacted) (Section 2.2)
- [ ] Dark humor: at least 1 moment present so far (Section 5.4)
- [ ] Motifs: declared motifs have appeared (Section 3.2)
- [ ] Emotional arc progressing (not monotone) (Section 5.4)

### After Part 4 (Before Final Part)
- [ ] Tension at maximum (Dark Night achieved) (Section 1.2)
- [ ] All threads identified for resolution or handoff (Section 3.3)
- [ ] Major revelation dramatized (not exposition-dumped) (Section 5.4)
- [ ] Reader questions managed: old answered, new raised (Section 4.1)

### After Completing Draft
- [ ] Full sensory audit: 10-15 random scenes (>80% must pass 3+ senses) (Section 5.4)
- [ ] Dark humor minimum met (2-3 moments) (Section 5.4)
- [ ] Sentence variation check: rhythm matches intensity (Section 5.4)

**Output**: Complete installment draft ready for revision.

---

## PHASE 4: Installment Revision
**Trigger**: After draft complete, before finalization

### Setup/Payoff Audit
- [ ] All declared setups either paid off or explicitly carried forward (Section 3.1)
- [ ] Setup/payoff validation rules applied (Section 3.1)
- [ ] No payoffs occur before their setups (chronological check) (Section 3.1)
- [ ] Major setups have callbacks before payoff if spanning books (Section 3.1)

### Thread Management
- [ ] All active subplots advanced or resolved (Section 3.3)
- [ ] Thread handoff clear: what carries to next book? (Section 3.3)
- [ ] No subplot disappeared without justification (Section 3.3)

### Character Arc Verification
- [ ] Character arcs progressed per map (Section 2.2)
- [ ] Protagonist evolution visible through contrast (Section 2.2)
- [ ] Antagonist threat escalated from previous book (Section 2.3)
- [ ] POV characters maintain voice consistency (Section 5.4)

### Craft Polish
- [ ] Voice consistency verified (reread previous installment for comparison) (Section 5.1)
- [ ] Deep POV maintained throughout (no camera-eye narration) (Section 5.4)
- [ ] Dialogue voices consistent for returning characters (Section 5.4)
- [ ] Major revelations dramatized with immediate impact (Section 5.4)

### Motif & Theme
- [ ] Motifs appeared and evolved per plan (Section 3.2)
- [ ] Thematic question advanced (Section 3.4)
- [ ] Theme expressed through action, not speeches (Section 3.4)

### Reader Experience
- [ ] Reader questions managed: old answered, new raised (Section 4.1)
- [ ] Emotional arc achieved per design (Section 4.2)
- [ ] Satisfaction markers hit (Section 4.3)
- [ ] Connection to next installment seeded (or series closure if final) (Section 4.4)

### Continuity Check
- [ ] Continuity errors caught (Section 5.2)
- [ ] Hard continuity facts verified against previous books (Section 5.2)
- [ ] Character knowledge appropriate (no premature information) (Section 5.2)

**Output**: Revised installment ready for finalization.

---

## PHASE 5: Series Completion
**Trigger**: After final installment drafted

### Series-Level Payoffs
- [ ] All series-level setups paid off (Section 3.1)
- [ ] Central thematic question answered (even if complexly) (Section 3.4)
- [ ] All character arcs complete (Section 2.2)
- [ ] All major subplots resolved (Section 3.3)

### Resonance Achievement
- [ ] Series motifs crystallized in final image (Section 3.2, 4.4)
- [ ] Final scene echoes series opening with transformation (Section 4.4)
- [ ] Resonance tracking complete (image, motif, question, emotion) (Section 4.4)
- [ ] Emotional catharsis achieved (Section 4.2)
- [ ] Ending provides closure while honoring complexity (Section 4.3)

### Foreshadowing Payoff
- [ ] True clues paid off (Section 3.5)
- [ ] Red herrings resolved/dispelled (Section 3.5)
- [ ] Early details gain new meaning on reread (Section 3.1)
- [ ] Final book recontextualizes previous books (Section 3.5)

### Craft Verification
- [ ] Voice consistent across all installments (Section 5.1)
- [ ] All craft requirements met in final installment (Section 5.4)
- [ ] Final scene dramatized (not explained) (Section 5.4)

### Series Integrity Check
- [ ] Triptych requirements met (if applicable) (Section 1.3)
- [ ] Tension architecture achieved per design (Section 1.2)
- [ ] Theoretical concepts integrated meaningfully (Section 1.4)
- [ ] Antagonist escalation complete (Section 2.3)

**Output**: Complete series ready for publication.

---

## Emergency Diagnostics
**Trigger**: When something feels wrong or feedback indicates problem

### Use Diagnostic Tools
1. Identify symptom using **Section 4.5: Reader Experience Diagnostics**
2. Apply diagnostic questions to pinpoint root cause
3. Check dependencies (character? stakes? pacing? satisfaction?)
4. Apply fix from diagnostic table
5. Verify fix addresses root cause, not just symptom

### Common Emergency Fixes
- **Static middle book** → Add antagonist action forcing choice (Section 2.3)
- **Voice drift** → Reread previous dialogue; rebuild voice sheet (Section 5.4)
- **Lost threads** → Check handoff table; make threads explicit (Section 3.3)
- **Abrupt ending** → Extend Part 5 emotional processing (Section 4.2, 4.4)
- **Stakes don't matter** → Make personal, threaten what character loves (Section 2.3)

---

## Workflow Quick Reference

| Phase | When | Key Actions | Output |
|-------|------|-------------|--------|
| 1. Series Planning | Before any writing | Map full series arc, characters, setups, motifs | Complete structure document |
| 2. Installment Setup | Before each book | Review previous, plan this book, refresh continuity | Installment outline |
| 3. Installment Drafting | During writing | Check at Part 1, midpoint, Part 4, completion | Complete draft |
| 4. Installment Revision | After draft | Audit setups, threads, arcs, craft, continuity | Revised installment |
| 5. Series Completion | After final book | Verify all payoffs, resonance, closure | Complete series |
| Emergency | When problems arise | Use diagnostics, identify root cause, fix | Problem resolved |

---

# APPENDICES

## A. Glossary of Key Terms
<!-- METADATA
category: reference
applies_to: documentation
output_format: definitions
-->

**Arc**: The trajectory of change a character undergoes across the story; can be positive (growth), negative (corruption), or flat (world changes around them).

**Beat**: A specific story moment or turning point; can refer to emotional beats (shifts in feeling), plot beats (events), or structural beats (key moments like midpoint reversal).

**Callback**: A reference to an earlier story element that gains new significance; rewards reader memory and creates cohesion.

**Crystallization**: When a motif or theme reaches its fullest, clearest expression, usually in the climax or resolution.

**Dark Humor**: Humor derived from grim, morbid, or absurd situations; serves as tonal counterpoint and reveals character psychology.

**Deep POV**: Point-of-view technique where reader is embedded in character's consciousness; filters all narration through character's perception, thoughts, and emotions.

**Dramatization**: Showing events unfold through action and scene rather than summarizing or explaining; "show don't tell."

**Escalation**: Progressive increase in stakes, danger, or complexity across the narrative; essential for maintaining tension.

**Foreshadowing**: Planting hints or clues about future events; can be true (accurate) or false (red herrings for misdirection).

**Handoff**: Elements (questions, relationships, threads) that carry from one installment to the next; creates continuity.

**Interiority**: The internal experience of a character; thoughts, feelings, sensations rendered on the page.

**Irony** (Dramatic): When reader knows something character doesn't; creates tension and engagement.

**Irony** (Situational): When outcome contradicts expectations in meaningful way; often used for character deaths.

**Motif**: A recurring element (object, image, phrase, symbol) that carries thematic significance; meaning should evolve across story.

**Payoff**: The fulfillment or resolution of a setup; creates reader satisfaction when executed well.

**POV** (Point of View): The perspective from which story is told; can be first-person, third-person limited, third-person omniscient, etc.

**Red Herring**: False clue or misleading information designed to misdirect reader; must be plausible to work.

**Resonance**: The sense that ending meaningfully connects to beginning, creating feeling of completion and transformation.

**Reversal**: A major turning point where situation changes significantly; often involves new information or perspective.

**Setup**: An element planted early that will pay off later; can be object, information, relationship, ability, or pattern.

**Stakes**: What characters stand to gain or lose; personal stakes are more powerful than abstract ones.

**Subplot**: Secondary plot thread that runs parallel to main plot; should mirror, contrast, complicate, or deepen main themes.

**Throughline**: An element that continues across entire series; can be character, relationship, question, or theme.

**Tracking Table**: Organizational tool for monitoring how elements (setups, motifs, character arcs) develop across installments.

**Triptych**: Three-story structure where each story stands alone but gains meaning from the others; final story recontextualizes previous ones.

**Voice**: The distinctive style and personality of narration; includes word choice, sentence rhythm, tone, and character-specific patterns.

**Voice Drift**: When character's distinctive speech patterns or narrative voice becomes inconsistent across installments.

---

## B. Adaptation Notes

Space for considering other medium adaptations:

- Visual requirements
- Pacing adjustments for screen
- POV translation challenges
- Episode/season breakdown potential

## B. Marketing Considerations

- Release strategy
- Series positioning
- Comparable titles
- Hook for each installment

## C. Feedback and Revision Log

| Date | Feedback Source | Issue Identified | Resolution | Installment Affected |
| ---- | --------------- | ---------------- | ---------- | -------------------- |
|      |                 |                  |            |                      |
