Here’s the full system, pulled together and cleaned up into one coherent write-up.

---

# Core Premise

Magic in this world behaves **like programming**, but expressed in mystical terms rather than literal code.

* **Sources** are metaphysical realities, like remote services or cosmic “APIs.”
* **Artifacts** are routes and adapters that let you safely reach those Sources.
* **Spells** are structured instructions that call one or more Sources with specific parameters.
* **Casters** are programmers: their power is not just in raw energy, but in how well they *understand, structure, and maintain* their magic.

Everything we’ve locked in builds on this.

---

# 1. The Magic Stack

### 1.1. Sources (Metaphysical Services)

Sources are fundamental metaphysical domains: not gods, but cosmic services that embody some aspect of reality.

Examples we’ve defined:

* **Ember Deep** – heat, combustion, hunger, burning transformation.
* **Still Archive** – memory, records, static snapshots, preservation.
* **Sky Loom** – distance, height, storms, wide perspective, messages.
* **Silent Ledger** – balance, debt, consequence, oaths, cause-and-effect.

Sources:

* Don’t live in physical space, but in **concept-space**.
* Are accessed by knowing their **address** (how to point your will at them).
* Enforce a **protocol** (rules of engagement, etiquette, constraints).

They are the underlying “CPU” of the magic system.

---

### 1.2. Artifacts (Routes, Adapters, Wrappers)

Artifacts are the physical or semi-physical tools that make working with Sources practical:

1. **Keys (Address-cachers)**

   * Store the addressing ritual for a specific Source.
   * Example: a charred wand keyed to Ember Deep.

2. **Channels (Conduits)**

   * Limit flow and shape how much power can pass safely.
   * Example: a copper bracer that grounds Sky Loom’s lightning.

3. **Wrappers (Prebuilt spells)**

   * Bundle Source + pattern + constraints into a reusable “macro.”
   * Example: a ring that always creates a standard Silent Ledger oath-binding.

4. **Adapters (Cross-Source combiners)**

   * Designed to interface multiple Sources together.
   * Example: a glass lens that can channel Sky Loom (vision) and Still Archive (snapshot) for surveillance.

Artifacts encode:

* The **address** of one or more Sources.
* Some or all of the **protocol** (expected structure, safe defaults, built-in costs/limits).

---

### 1.3. Spells (Calls / Programs)

A spell is a **structured call** to one or more Sources, usually expressed as ritual language + gesture + symbolic setup.

Every non-trivial spell conceptually specifies:

1. **Source(s)** – Which metaphysical service(s) you’re calling.
2. **Address** – How you align yourself / the artifact / the ritual to reach them.
3. **Target** – What the spell acts upon.
4. **Scope** – How big, how far, how many.
5. **Duration / Termination Condition** – When it stops or why.
6. **Cost / Payment** – What you offer (fuel, fatigue, memories, time, vows, etc.).
7. **Safety Constraints** – Max intensity, fallback conditions, safe failure modes (if the caster is skilled enough).

Under the hood, it’s like:

```python
source.call(
    target=...,
    scope=...,
    duration=...,
    cost=...,
    safety=...
)
```

—but the caster experiences it as a ritual, invocation, and shaped intent.

---

### 1.4. Casters (Programmers)

Casters differ not just in how much power they can channel, but in:

* How well they understand **Sources** and their limitations.
* How flexible and safe their **spell patterns** are.
* How well they can **debug, maintain, and design** magical systems.

Growth is less “bigger spell = higher level” and more:

> “I can now construct, test, and maintain more complex, subtle, and reliable magic.”

---

# 2. The Address + Protocol Model of Sources

We locked in that Sources are accessed via **Address** + **Protocol**.

### 2.1. Address (Concept-Space Location)

Each Source is located in concept-space and has a “coordinate”:

* Not numbers, but a specific combination of:

  * **Sigils**
  * **Materials or conditions**
  * **Postures and internal mental states**
  * **Names / titles / invocations**

Example: Ember Deep’s address might involve:

* Charred marks in a circle.
* The smell of smoke.
* An elevated heartbeat (symbolizing urgency and hunger).
* The whispered name of a long-dead star.

### 2.2. Protocol (How You Must Ask)

Even if you “hit” the Source, it only responds if the request conforms to its internal rules.

Each Source has:

* **Accepted structure**:

  * Must specify a target.
  * Must limit scope or the Source will refuse or lash out.
* **Etiquette / taboos**:

  * Sky Loom hates lies in the greeting.
  * Silent Ledger demands explicit terms and collateral.
* **Cost preferences**:

  * Ember Deep likes consumption (fuel, calories, memories).
  * Still Archive likes forgotten moments as payment.
  * Sky Loom likes orientation/sense of direction as a tithe.
  * Silent Ledger takes pledged collateral.

Break protocol → you get errors, misfires, or twisted interpretations.

---

# 3. Example Sources (Locked-In Behavior)

Short versions of the four we’ve been using:

### 3.1. Ember Deep

* **Domain:** Heat, combustion, hunger, transforming through burning.
* **Loves:** Clear fuel, bounded requests.
* **Hates:** Being asked to create from nothing or to preserve without change.
* **Typical payments:** Burned offerings, caloric drain, emotional exhaustion, sacrificed memories or options.

### 3.2. Still Archive

* **Domain:** Memory, snapshots, preserved states.
* **Loves:** Precision and clarity.
* **Hates:** Vague requests; cannot record what the caster has never truly perceived.
* **Typical payments:** Sacrificed memories, willingness to forget or freeze parts of oneself.

### 3.3. Sky Loom

* **Domain:** Distance, height, storms, signals, wide awareness.
* **Loves:** Clear vectors/directions, honest initial greeting.
* **Hates:** Initial lies or confusion in orientation.
* **Typical payments:** Disorientation, lost sense of direction, vertigo, or “skewed perspective” later.

### 3.4. Silent Ledger

* **Domain:** Balances, debt, oaths, consequences.
* **Loves:** Explicit, possible contracts with clear terms.
* **Hates:** Impossible contracts, contradictory clauses.
* **Typical payments:** Collateral items or conditions held “in escrow” until contracts resolve.

---

# 4. Magical “Languages” / Traditions

Different spellcasting cultures are essentially different **frontends** to the same underlying Sources.

We mapped them to coding paradigms:

### 4.1. Pythonic Tradition (“Readable Charms”)

* High-level, expressive, humane.
* Focus on **clear intent** and **sensible defaults**.
* Easy to write, fast to improvise, moderate reliability.
* Effects are “spelled out” in natural, structured language.

Example: A safe warming charm using Ember Deep with bounded temperature and a clear stop condition.

### 4.2. Deep Geometry (C++-Style Tradition)

* Low-level, extremely explicit.
* Uses dense **geometric arrays**, runes, and spatial relationships.
* Strongly typed: every line encodes exact Source facet, target type, and constraints.
* High prep time, high precision, capable of massive and efficient workings.

Example: A forge circle that heats metal to a specified temperature range, with feedback loops and venting into a heat sink.

### 4.3. Ritecraft / Statistical Tradition (R-Style)

* Designed for **large sets**, populations, and trends.
* Works over **arrays of names, locations, omens**, etc.
* Optimizes outcomes at the level of groups, cities, campaigns.
* Quirky scoping rules; can cause subtle, unexpected side-effects if not well-contained.

Example: A rite that nudges weather patterns to favor a region over a season, or improves the survival odds of a battalion at the cost of another.

All call the same Sources; they just structure and optimize the requests differently.

---

# 5. Data Structures & Integrity in Magic

To make this feel like real programming, we explicitly treat **magical state** as structured data.

### 5.1. Magical Data Structures

Casters eventually work not just on single things, but structures:

* **Scalar**: One object or person (a single enchanted sword, one target).
* **List / Array**: Many similar targets (every soldier in a unit, every door in the palace).
* **Map / Dictionary**: Key→value relationships:

  * True name → current location.
  * Oath → penalty.
* **Graph**: Networks of relationships:

  * Webs of debt, loyalty, conspiracy, bloodline ties.

As casters advance, they stop thinking “cast on this one thing” and start thinking “define the set, define the relations.”

### 5.2. Integrity Rules (Invariants)

Pseudo-systems and complex rituals obey **integrity constraints**, like database or type invariants:

* “No oath exists without a signer.”
* “No two living souls share the same True Name.”
* “Every recorded debt references a valid person or archived record.”
* “This ward must always log a passage if and only if someone crosses the line.”

When these invariants are violated:

* Pseudo-sources become unstable.
* Sources react with glitches:

  * Ember Deep leaks out of bounds.
  * Still Archive holds contradictory records.
  * Silent Ledger spawns paradoxical or dangling debts.

Certain mages specialize in maintaining and repairing these structures—basically arcane DBAs / system administrators.

---

# 6. Pseudo-Sources (Advanced Constructs)

At higher levels, casters can create **pseudo-sources**:

> Structured, local, constrained magical entities built on top of real Sources.

They are **not new fundamental realities**; they’re “powered by” or “backed by” one or more Sources.

### 6.1. Bound Subdomains

A **sub-slice** of a Source with very specific rules.

Example: **The Forgeheart**

* Anchored to Ember Deep.
* Only handles heat for forging metal within safe ranges.
* Has clear invariants:

  * Max temperature.
  * Safe shutoff when metal reaches a certain expansion.
  * Fixed payment source (fatigue of nearby smiths).

To use it, smiths address the Forgeheart instead of Ember Deep directly. Internally, it routes calls to Ember with tightly controlled parameters.

### 6.2. Synthetic Stores (Magical Databases)

Long-lived pseudo-sources focused on **state**, not raw effect.

Example: **The Census Engine**

* Uses Still Archive + Silent Ledger.
* Stores:

  * Citizens, oaths, incidents, debts, statuses.
* Enforces integrity:

  * No incident without a time and place.
  * Every oath is attached to people that exist.

It can:

* Answer complex queries.
* Trigger automatic consequences (alarms, flags, gentle nudges from Sources).

### 6.3. Sandboxes (Test Environments)

Small, sealed, simulated contexts used for **testing spells**.

* Built using Still Archive (snapshots), maybe Sky Loom for perspective.
* Casters copy patterns/entities into the sandbox and run new workings there.

If the sandbox’s boundaries leak, test magic bleeds into reality. Maintaining sandbox integrity is a high art.

### 6.4. Constraints on Pseudo-Sources

To avoid infinite absurd power:

1. They **introduce no new fundamental capabilities**, only structured wrappers.
2. They are always **backed by primary Sources**, who can cut them off or reclaim them.
3. They require **maintenance**—integrity auditing, recalibration, repairs.
4. They’re usually **local** (bounded to a place or artifact), not universally omnipresent.

---

# 7. Error Types (Magical Failure Modes)

We have a clear taxonomy of “errors,” which both keep magic hard and give you narrative hooks:

1. **Address Error (SourceNotFound)**

   * Wrong, partial, or corrupted address.
   * Effect: no response, or a weak/adjacent echo Source responding.

2. **Protocol Error (BadRequest / Forbidden)**

   * Hit the Source, but request violates etiquette or structure.
   * Effect: silence, or a twisted but rule-legal interpretation.

3. **Overflow (OverdrawError)**

   * Requested more power than the caster, artifact, or local reality can host.
   * Effect: backlash, burns, ruptured artifacts, environmental anomalies.

4. **Contractual Error (LedgerRebound)**

   * For Silent Ledger: impossible or unfair contract attempts.
   * Effect: the contract flips on the originator or escalates costs.

5. **Interference (RaceCondition)**

   * Multiple spells or casters hitting overlapping domains/sources in conflicting ways.
   * Effect: glitchy, merged, delayed, or oscillating outcomes.

6. **Integrity Error (Schema / Invariant Violation)**

   * For pseudo-sources: inconsistent or contradictory data/state.
   * Effect: ghost entries, lost people, paradoxical debts, broken wards.

---

# 8. Ability Tiers (5-Level Skill Ladder)

We compressed caster ability into 5 realistic skill tiers, aligned with programmer progression.

### Tier 1 – Script User

* Analog: beginner who can copy-paste working scripts.
* Uses pre-written spells as recipes.
* No real understanding of Sources, just “this charm makes fire.”
* Very limited ability to adapt spells; easily derailed by unusual conditions.

### Tier 2 – Junior Caster / Parameter Tinkerer

* Analog: junior dev who can modify function arguments and write simple scripts.
* Understands spells have **parameters** (size, duration, target, cost).
* Can safely tweak and recombine simple workings.
* Starting to think: “I am calling Ember Deep with these limits.”

### Tier 3 – Journeyman / Spell Developer

* Analog: solid mid-level dev.
* Writes their **own** spells using known patterns and Sources.
* Composes multiple Sources and artifacts into pipelines (detect → record → act).
* Uses simple **data structures** (lists, maps of targets).
* Embeds basic safety and fallback conditions.

### Tier 4 – Systems Mage / Debugger

* Analog: senior engineer / system maintainer.
* Reads, debugs, and refactors complex, legacy rituals and wards.
* Maintains and repairs pseudo-sources.
* Thinks in **interfaces**, **modules**, and **error types**.
* Works across multiple traditions (Pythonic, Deep Geometry, Ritecraft).

### Tier 5 – Architect / Metaprogrammer

* Analog: principal engineer / architect / language designer.
* Designs large-scale magical systems and pseudo-sources.
* Defines schemas, invariants, and long-term structures.
* Innovates new spell dialects or safer traditions.
* Thinks in **ecosystems**: interactions between many Sources, places, and generations of casters.

---

# 9. Growth Feels Like Learning to Code

Crucially, progression is not just “bigger fireball.”

Characters grow by:

* Moving from **rote recitation** → understanding parameters → designing patterns → maintaining systems → architecting structures.
* Learning to **abstract** (“this handshake with Ember Deep is reusable”).
* Learning to **debug** (“this ward fails because the Archive component logs too late”).
* Learning to **respect integrity** (“we must fix the oath schema before we add new bindings”).

By design:

* Mid-level casters can already do quite flashy effects.
* High-level casters are distinguished by:

  * Reliability
  * Scope (in space, time, complexity)
  * Subtlety
  * System design

Not raw destructive wattage.

---

This is the full, locked-in framework: Sources as metaphysical services; artifacts as routes and adapters; spells as structured calls; multiple “languages” of spellcraft; pseudo-sources as advanced constructs; explicit data structures and invariants; and a 5-tier skill ladder that mirrors real programming mastery.

Next step, if you want, we can:

* Turn this into an **in-world document** (academy curriculum, order manifesto).
* Or start **instantiating** it: build a specific city, school, or character whose story shows this system in action.
