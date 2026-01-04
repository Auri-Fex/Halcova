
# Coding-Type Magic: Advanced Magic System Design

## Table of Contents
1. [Making it Feel Like Advanced Programming](#making-it-feel-like-really-advanced-programming)
2. [Making it Entertaining for Non-Programmers](#making-it-entertaining-for-non-programmers)
3. [Abstract & Compositional Sources](#abstract--compositional-sources-advanced-magic-system-design)
4. [Combat Magic as Aspect Manipulation](#combat-magic-as-aspect-manipulation)
5. [Magical Languages as Paradigms](#magical-languages-as-paradigms)
6. [Five-Tier Caster Progression](#five-tier-caster-progression-updated-for-aspects-behaviors-and-languages)

---

## Introduction

This document explores a magic system inspired by advanced programming concepts, blending technical depth with narrative clarity. It is structured for both worldbuilders and writers who want a system that is cinematic, logical, and accessible.

---


## Making it Feel Like *Really* Advanced Programming

You already have:

* Sources as services
* Modes (streaming, artifact, pseudo-source)
* Pseudo-sources with schemas/invariants
* A skill ladder

To get “senior engineer / architect” feeling, add **high-level software concepts** as *in-world magical practices*, not CS jargon.


### A. Higher-Order Magic (Functions that Take Functions)

Programming idea: functions that take other functions, or return them.

In-world:

* Spells that **modify other spells** rather than acting on people/things.
* Example: a “Limiter Weave” that can be laid over any fire-working to clamp its max size and auto-shutoff conditions.

Everyone knows it as:

> “Throw the Cloak of Restraint over any Ember-working, and it can’t spill past ten paces.”

Under the hood: it’s basically a wrapper / decorator.

Readers just see:
“Ah, she’s slapping the safety-cloak on that crazy ritual before it kills everyone.”

---


### B. Generics & Polymorphism (One Pattern, Many Types)

Programming idea: one function works with many types as long as they satisfy some interface.

In-world:

* A pattern like “bind oath between two parties” that works for:

  * Human ↔ human
  * Human ↔ city
  * Human ↔ pseudo-source
* As long as each can present a “Name”, “Will”, and “Stake”.

You show this by:

* Having the same **oath-ritual** used:

  * For a marriage,
  * For a guild charter,
  * For plugging a new pseudo-source into the city’s grid.

Readers get:
“This is a universal binding rite—it works on everything.”

You get your polymorphism itch scratched.

---


### C. Concurrency & Race Conditions

Programming idea: simultaneous processes interacting in weird ways.

In-world:

* Duels between mages where the conflict isn’t “bigger laser” but:

  * Whose ritual finishes first,
  * Whose ward hooks the Source first,
  * Whose conditions fire in what order.

Example drama beat:

* Two casters both lay claim to Sky Loom over a battlefield:

  * One trying to drop fog,
  * One trying to clear the sky.
* The sky shimmers between states; lightning arcs sideways; one side’s messages get scrambled.

You can literally describe:

> “The sky couldn’t decide what it was. Clouds half-spun and shredded, messages broke mid-flight. Somewhere above them, two different spell-threads were fighting over the same piece of Sky Loom.”

That’s a race condition, but no one has to know the word.

---


### D. Transactions & Rollbacks

Programming idea: “Do all of this or none of it” (ACID transactions).

In-world:

* Ledger-based rituals where **multiple changes** either:

  * All take effect, or
  * None do, and everything snaps back.

Example:

* A high-risk healing ritual that:

  * Draws life from three volunteers,
  * Channels it through Ember Deep,
  * Into a dying soldier.
* If *any* step fails, Ledger rolls back:

  * Everyone’s state reverts to pre-ritual.

Tension:

* They’re terrified of partial success because the cost would be horrific, so they depend on the Ledger’s all-or-nothing enforcement.

You can explicitly say:

> “If the contract failed, the Ledger would yank them all back to how they’d been before the circle was drawn—injuries, wounds, and all.”

That *feels* like database transactions, but reads like high-stakes ritual law.

---


### E. Version Control & Forks

Programming idea: Git, branching, merging.

In-world:

* Ritual traditions are **branches**:

  * “The Third Revision of the Fire Curtain Ward.”
* Old versions still exist, with known bugs.
* Radical mages “fork” a working:

  * New variant, new strengths, new horrible edge cases.

You show it with:

* Marginalia in grimoires: “Do *not* use the Second Revision unless you want the flames to cling.”
* Arguments in councils: “The Fifth School’s fork of Ember etiquette is why their city burned.”

Readers see:

* Magic evolving like competing doctrines.
  You get:
* Semantic versioning, diffs, merges, bugfixes.

---


### F. Testing & Staging

Programming idea: unit tests, staging environments.

In-world:

* **Sandbox pockets** (we already discussed) used not just for experiments, but as an institutional norm:

  * “No new ward goes live without a hundred passes in the pocket-city.”

Dramatic use:

* A character *skips* proper testing because they’re desperate—everyone knows it’s a terrible idea.
* Or they find that someone *faked* test results on a civic ward: magical Volkswagen emissions scandal.

Readers just see **“we tested this in a little fake world first”**—graspable, cool, and obviously advanced.

---


## Making it Entertaining for Non-Programmers

Now: how do you show all that without turning your book into a senior dev blog?

### A. Show consequences, not diagrams

When you want to flex how technical things are, **don’t** explain the whole mechanism. Show:

* The *setup* in 1–2 concrete details.
* The *failure* or *success* in a vivid, sensory way.
* One character’s reaction that hints at the deeper logic.

Example: integrity failure in a Census Engine.

Instead of:

> “The schema of the pseudo-source had broken its foreign key constraint…”

You write:

> The city-statue that housed the Census Engine began to stutter through names.
>
> “Jeral son of—error.
> Keth of—error.
> Unbound soul—error.”
>
> Marble tears bled from its eyes.
>
> “We’ve got dangling oaths,” Mara breathed. “Someone’s been deleting people without unbinding them.”

Non-programmers: “Creepy! People are being erased wrong.”
Programmers: “Oh god, dangling references in production.”

---

### B. Use character attitude as the hook

Let characters **argue about magic** the way devs argue about frameworks—but make it about personality and stakes.

Example:

> “You’re still using Third-Form Ember bindings?”
> “They’re stable.”
> “They’re *cowardly.* You lose half the throughput.”
> “Throughput doesn’t matter if the wall doesn’t fall down on your head, Sera.”

Readers don’t need to know the exact difference—they feel:

* Tradition vs innovation
* Safety vs performance
* Temperament of the casters

The tech flavor is in the *rhythm* of the argument.

---

### C. One sharp concept per scene

This system has a ton of cool knobs. On the page:

* **Do not** introduce more than one new “weird” magical concept per scene.
* Everything else in that scene should reuse something already familiar.

So a given scene might be:

* “This is the first time we see a sandbox pocket.”
* Or: “This is where we see an internal pseudo-source glitch.”
* Or: “This is the race-condition duel.”

But never all three, and never with a lecture. Anchor it in emotion:

* They’re testing in a sandbox because they’re scared of the real stakes.
* The pseudo-source glitch threatens someone’s child.
* The race-condition duel decides who dies first.

---

### D. Use visual, physical metaphors for abstract things

Whenever you want to communicate a gnarly software idea:

* Turn it into a **visual magical phenomenon**.

Examples:

* **Concurrency issue** → Two differently-colored spell-threads tangling mid-air, stuttering the sky.
* **Rollback** → Time stuttering back a few seconds, blood spattering back into wounds.
* **Data corruption** → Ghostly echoes of the wrong person walking through a ward, statues reciting contradictory names.

Then drop one line of explanation afterward, not before.

---

### E. Make “debugging” scenes mystery scenes

When a high-level caster inspects a broken ward or pseudo-source:

* Structure it like a **whodunit**:

  * Clues (weird glitches, partial failures).
  * Red herrings (wrong assumptions about the Source).
  * A reveal: “Oh, someone changed this clause; that’s why Ember’s leaking into the water grid.”

Non-programmers enjoy:

* The mystery,
* The detective work,
* The “aha!”

Programmers enjoy:

* That it’s literally a root-cause analysis.

---

### F. Give readers a simple mental model

Internally, you’ve got:

* Sources, addresses, protocols.
* Modes.
* Pseudo-sources, invariants, languages.

Readers just need a **simple, short story** you repeat in different flavors:

> “All magic is calling things bigger than you.
> You can do it raw (streaming), through tools (artifacts), or through engines people built earlier (pseudo-sources).
> Each way has different risks and prices.”

If you keep circling that sentence in new contexts, they’ll feel the depth without memorizing the API.

---

### G. Keep the tech 70% subtext, 30% text

Use the **rule of iceberg**:

* You know 100% of the structure.
* On the page, you show ~30%:

  * A bit of vocabulary,
  * Some consistent consequences,
  * Repeatable patterns.
* The remaining 70% is implied.

If beta readers say “this feels deep and consistent” **without** being able to recite how pseudo-sources work, you’ve nailed it.

---

If you want, I can:

* Draft a short scene where a high-level caster **debugs a failing pseudo-source** and we make it:

  * Readable as a magical mystery for non-programmers,
  * But secretly full of advanced-programming vibes (transactions, invariants, race conditions) for you.

---


# Abstract & Compositional Sources: Advanced Magic System Design

Right, cool pivot. Let’s peel Ember Deep back a layer and make the whole thing feel more abstract and compositional.

You’re basically saying:

> “I don’t want ‘Fire Source = fire.’
> I want abstract sources that, when *combined*, can *produce* fire, water-control, etc.
> And maybe the *control* aspect is what you can internalize as a personal pseudo-source.”

That absolutely works, and it actually makes the system feel *more* like advanced programming.

I’ll set this up as:

1. Two-layer model of Sources
2. How “fire” and “water control” emerge from combos
3. The “control Source” as what gets internalized
4. How this fits everything we’ve locked in

---

## 1. Two Layers of Sources

Instead of “Ember Deep = Fire,” we introduce a deeper layer:


### Layer 1 – Primal Aspects (Abstract Sources)

These are very abstract metaphysical currents. Each is a way reality *behaves*, not a concrete element.

Here’s a clean set you can work with:

1. **Substance** – “There is something here.”
   * All material/existential stuff: matter, energy, intangible “stuff.”
2. **Form** – “This is *shaped* like this.”
   * Structure, pattern, geometry, arrangement.
3. **Flow** – “This is *changing* like this.”
   * Motion, processes, transformations, rates.
4. **Bind** – “These things are *linked* like this.”
   * Control, constraints, cause/effect, obligations, ownership.
5. **Threshold** – “Here is a *boundary* between states/places.”
   * Inside/outside, life/death, allowed/forbidden, here/there.
6. **Echo** – “This *remembers* or *repeats*.”
   * Memory, repetition, resonance, patterns over time.
7. **Skew** – “This is *unbalanced*.”
   * Difference, gradients, tension, potential (like energy, charge, hunger).

These are the **real** Sources in a technical sense. They’re weird, conceptual, and combine like operators.

Most casters never talk about “Skew Source” and “Bind Source” by name; that’s advanced-nerd territory.

---


### Layer 2 – Domain Sources (What Most People Perceive)

“Ember Deep,” “Verdant Host,” “Sky Loom,” etc. are now:

> **Composite domains** built from Primal Aspects.

For example (illustrative, not rigid):

* **Ember Deep (fire/hunger)**
  ≈ Substance (combustible) + Form (flicker/outward spread) + Flow (rapid change) + Skew (high gradient) + Bind (to fuel).
* **Still Archive (memory)**
  ≈ Substance (record) + Form (snapshot) + Echo (repeatable pattern) + Threshold (freeze boundary at time t).
* **Sky Loom (distance/messages)**
  ≈ Form (spatial mapping) + Flow (propagation) + Threshold (nodes) + Bind (who sees what).
* **Silent Ledger (debt/oaths)**
  ≈ Bind (relations) + Echo (history) + Threshold (owe/paid) + Skew (imbalance).

So:

* **Novices** call Domain Sources (“Ember Deep, do fire stuff”).
* **Advanced casters** go one level deeper and use Primal Aspects directly, or recombine them into *new* domain-like behaviors.

That’s your “less obvious” part.

---

## 2. How Fire, Heat, and Water Control Come from Combinations

Now, effects become **recipes** of Aspects, not “I hit the Fire button.”


#### 2.1. Creating Fire / Heat

What is “fire” in this system?

* There is **Substance** → something present to burn.
* It has **Form** → a loose, dancing shape; surface flicker.
* It undergoes **Flow** → rapid, consuming change.
* It’s driven by **Skew** → a big imbalance (hot vs cold, fuel vs ash).
* There’s **Bind** to new things → it spreads where fuel + air are.

A “technical” caster doing a basic *heat* effect might think:

* I don’t want full-blown fire, just temperature change.
* So use: **Substance + Skew + Flow**, but keep **Form** and **Bind** constrained.

Ritual-wise (still readable):

> “Let the hidden difference wake within this iron,
>
> skewing heat toward its heart,
>
> changing only its softness, not its shape,
>
> and bind that change to this hammer’s rhythm alone.”

Under the hood that’s:

* Call **Substance** (target iron).
* Call **Skew** to create temperature gradient.
* Call **Flow** to convert gradient into internal change.
* Limit **Form** and **Bind** so no flame spreads.

If they wanted actual fire:

* They’d loosen Form and Bind (“everything nearby can catch”) and give Skew more headroom.

---


#### 2.2. Controlling Existing Water

Your idea:

> “To control water in an area, I connect the water source and call another source too—combine them.”

Perfect.

We don’t need a “Water Source.” We need a “Water Pattern” plus abstract Sources.

Think:

* Water is: Substance in the *liquid state* (we can treat that as a Form pattern for Substance).
* To control it, we need:
  * **Substance**: “select all liquid matter in this region that matches this pattern.”
  * **Form**: “reshape surface and volume like this.”
  * **Flow**: “move it along this path / with this speed.”
  * **Bind**: “obey my will / obey this rule-set until condition X.”

So a journeyman “water control” spell:

> “Substance, hear me:
>
> mark all that yields and flows as this river does within ten steps of where I stand.
>
> Form, gather that marked water into a single band;
>
> Flow, guide that band along my arm and out from my hand;
>
> Bind, hold to this pattern until my palm opens or stone bars its way.”

Notice:

* No “Water God.” Just Source calls to abstract behaviors.
* The caster’s understanding of **what water is** (yielding, cohesive, liquid) matters—a lot.

To a non-technical in-world mage, they might still *name* this combination something like “River’s Grasp.” But technically, it’s Substance + Form + Flow + Bind.

---

## 3. The “Control Source” as Personal Pseudo-Source

> “Perhaps the source that allows control is what can be moved into a pseudo personal source”

Yes. That’s a very clean distinction:

* **Substance/Form/Flow/Skew/etc.** are hard to internalize in any general way—they’re reality-level.
* But **Bind**—the aspect of **linking, constraining, controlling**—is the one that makes sense as a personal engine.


#### 3.1. What is Bind-as-Source?

Bind is:

* Cause/effect
* Ownership
* “Follow this rule”
* “You are linked to me / to this pattern”

If a mage internalizes a tiny subdomain of **Bind**, they become:

* **Exceptionally good at control**:
  * They can quickly attach or detach control links.
  * They can rewrite which rules local stuff follows, *within limits*.

But they *cannot* conjure new raw phenomena just from Bind—it’s an operator, not a substrate.

---


#### 3.2. What a Control Pseudo-Source Lets Them Do

A mage with personal Bind pseudo-source:

* Can **grab and redirect** existing effects more easily:
  * Take a wild fire someone else started and clamp its Form/Flow.
  * Take ambient water and reassign its Flow pattern.
  * Take someone’s spell and rebind its target mid-flight (dangerous as hell).
* Still needs **connection to relevant Aspects**:
  * They can’t control water in a vacuum where there’s no Substance match.
  * They can’t control fire if there’s no Skew+Flow+Substance combination forming flame.
* Has a **local, always-on control loop**:
  * They can apply small corrections without calling external Bind each time.

Technically:

* Their soul is now a **local controller** for Bind operations.
* Bigger controls still require full Bind Source calls.
* It’s like embedding the control-logic library locally, so small operations are cheap and instant.

---

## 4. How This Fits What We’ve Already Built

We don’t have to throw away Ember Deep, Verdant Host, etc. We just **re-interpret** them:

* They’re **high-level Domain Sources**: stable metaphysical regions built from Aspects.


#### 4.1. For Most People

* Farmers, hedge-witches, regular battle-mages:
  * Work with Domain Sources: Ember Deep for fire, Verdant Host for growth, etc.
  * It’s simpler: “Ember Deep = fire behaviors.”


#### 4.2. For Advanced Casters

* Learn that Ember Deep is really:
  * A “pre-written library” of specific Aspect combinations:
    * a family of Skew/Flow/Substance/Bind/Form recipes tuned for combustion.

They can:

* Use Ember Deep as-is for fast, reliable fire spells,
  **or**
* Instead call Aspects individually to build weird, new things:
  * Cold flame (Skew + Flow + Echo + Form, but with net heat absorb).
  * Non-burning light (Substance:photonic + Form + Skew, no combustion).
  * Water that flows uphill because they manipulate Threshold + Skew + Flow directly.

Which feels:

* Less like pressing an “element” button,
* More like composing primitives in code.

---

## 5. Programming Parallel (Because Of Course)

This maps beautifully to actual advanced programming:

* **Primal Aspects** = *very low-level, generic primitives* (like math operations, memory, references, control structures).
* **Domain Sources** = *libraries/frameworks* built on those primitives (like NumPy, a game engine, a physics engine).
* **Control pseudo-source (Bind-in-self)** =
  * Having your own local scheduler / event loop / control-flow utilities always resident.

Fire in vanilla way:

```python
# Domain Source call
ember_deep.cast_fireball(target, size="medium")
```

Fire from Aspects:

```python
# Aspect-level composition
heat_field = Skew.create_gradient(target, amount="high")
Flow.apply_change(heat_field, to=target_structure)
Form.allow_flicker(target_surface)
Bind.propagation_rules(target, neighbors, when="fuel_available")
```

Water control:

```python
water_set = Substance.select(region, state="liquid")
Form.reshape(water_set, shape="whip")
Flow.move_along_path(water_set, path=arm_to_target)
Bind.tie_to_intent(water_set, owner=caster, end_condition="open_palm or blocked")
```

Internal Bind pseudo-source:

```python
# Local control engine
caster.bind_engine.retarget_spell(incoming_spell, new_target)
```

You don’t show code in the novel, but you design with this mental model.

---

## 6. What This Buys You in Story Terms

* **Less obvious Sources**:
  * No “Fire God, Water God” cliché; everything is concept currents.
* **Elemental effects feel *engineered***:
  * The same system that makes fire can make laser-like heat, cold fire, weird plasma, etc.
* **Personal pseudo-source of control**:
  * Makes certain mages feel *qualitatively* different:
    * They are controllers, redirectors, surgeons of magic, not just bigger cannons.
* **Clear progression**:
  * Beginners use Domain Sources like black-box APIs.
  * Journeymen start mixing Domain Sources (“fire + ledger = burning contract marks”).
  * Advanced mages descend to Aspect-level composition:
    * New pseudo-sources.
    * New “elements” no one’s seen.

---

If you like this direction, next I can:

* Define a **small, named set of Domain Sources** explicitly in terms of Primal Aspects, so you’ve got a reference grid.
* Or focus on **one character** who’s a “control mage” (Bind-in-self pseudo-source) and show what they can and can’t do vs a classic “fire mage” who just uses Ember Deep.

---


# Combat Magic as Aspect Manipulation

Right now you’re thinking: “I want fire/water/earth/air-style action, but I don’t want the magic to *actually* be those dumbed-down elements.”

We can absolutely do that by making **combat magic = visible side-effect of Aspect manipulation.**
It can look like bending, but under the hood it’s deeper and rule-y enough to feel Sanderson-ish.

I’ll lay out:

1. A deeper “elemental” layer built from your Aspects
2. How a fight actually looks with this
3. The big, simple rules that make it Sanderson-ish

---

## 1. Elemental *Behaviors*, not Elemental Buckets

Instead of “Fire Source, Water Source,” define a small set of **Action Domains** – ways the world can *behave* – and build all flashy stuff from those.

Use your Aspects as the guts.

Let’s define 4–5 “combat elements” that are actually Aspect-combos:


#### A. Matter – Shape and Density of Stuff
*Aspects: Substance + Form*

What they can do:

* Solidify, soften, reshape things.
* Make stone flow like clay; make cloth rigid as steel.
* Compact air into a visible wall; hollow out stone.

Limits:

* Cannot create matter from nothing.
* Cannot change *what* something is (stone stays stone; you’re changing shape/packing, not transmuting species).

In terms of Aspects:

* They pull on **Substance** (“this stuff here”) and **Form** (“arrange it like this”).

---


#### B. Motion – Trajectories and Speed
*Aspects: Flow + Skew*

What they can do:

* Push/pull, throw, slow, stop.
* Redirect projectiles, alter gravity-like effects, accelerate themselves.

Limits:

* They can’t ignore mass/inertia; heavy stuff is still harder.
* They can’t get perfect stillness in a dynamic environment – something always twitches.

Aspects:

* **Flow** (“change over time”) + **Skew** (“difference / potential to move”).

---


#### C. Force / Pressure – Impacts and Blasts
*Aspects: Skew + Bind + Flow*

What they can do:

* Create shockwaves, concussive blasts, crushing pressure.
* Shields that absorb/redistribute force.

Limits:

* Need a gradient to work with: pressure difference, weight, opposing forces.
* The bigger the imbalance, the more dangerous if it snaps back.

Aspects:

* **Skew** (build up tension)
* **Bind** (hold it temporarily)
* **Flow** (release/have it propagate)

---


#### D. Heat / Phase – Temperature and State Changes
*Aspects: Skew + Flow + Threshold + Substance*

What they can do:

* Heat or chill, melt/freeze, boil/burn.
* Turn fog to rain, water to steam, rock to lava (with effort).

Limits:

* Can’t erase energy: cooling something must move heat somewhere.
* State changes take time and material cooperation (can’t melt a mountain in a second).

Aspects:

* **Skew** (temp gradient), **Flow** (movement of heat),
* **Threshold** (phase boundaries), **Substance** (what’s being changed).

---


#### E. Constraint – Barriers, Snares, Bindings
*Aspects: Bind + Threshold + Form*

What they can do:

* Hard-light cages, invisible trip-lines, “no-cross” wards.
* Pin a person in place, lock a spell mid-air, freeze an object’s movement.

Limits:

* Cannot bind what they cannot *define*.
* Must anchor to something: ground, wall, self, etc.

Aspects:

* **Bind** (who/what follows what rule),
* **Threshold** (inside/outside the constraint),
* **Form** (shape of the cage/line/field).

---

Now: **fire / water / air / earth** are just *special cases* of mixing these Domains with particular materials.

* Fire = Heat/Phase + Force + Motion acting on air/fuel.
* Earth control = Matter + Motion acting on dense solid Substance.
* Water control = Matter + Motion + Heat/Phase acting on fluid Substance.
* Air control = Matter + Motion + Force acting on diffuse Substance.

You get flashy, familiar visuals, but inside the system it’s always “I’m pushing Flow + Skew on Substance with this Form and Bind.”

---

## 2. How a Fight Actually Looks

Let’s take a mid-level combat caster who’s good at **Motion + Matter**, and show a fast, cinematic duel.

### Opening move: “Earth spike”

* They call **Matter**:
  * Select Substance: the flagstones.
  * Re-form into a spike.
* They call **Motion**:
  * Push that spike upward fast.

Visually: stone spears erupting from the floor.
In your internal model: `Substance.select(ground) → Form.rearrange(spike) → Flow.apply(upwards)`.

### Counter: “Soft ground, hard air”

Opponent with **Matter + Constraint**:

* Softens the floor under themselves:
  * Matter: decrease density / rigidity.
* Hardens the air in front as a shield:
  * Matter: compact air;
  * Constraint: Bind it into a stable wall.

So the spike rises into a patch of *thick mud* instead of their foot, and their “air wall” catches debris.

All the reader sees:

> Stone roared up from the floor. She sank—waist-high—in a blink, flagstone turning to sucking mud around her legs. The spear of stone punched through empty air and crumpled against something invisible an arm’s length from her face.

Behind the curtain, you’re tracking the Aspects.

### Mid-fight cleverness: Using Skew

Your Motion+Matter caster notices:

* The opponent keeps hardening air → building **Skew** between normal and compressed zones.

He deliberately attacks that:

* Control **Force/Pressure**:
  * Reach into the compressed air wall: feel the tension (Skew).
  * Release it sideways with Flow.

Boom: their *own* hard air explodes into a side-blast that knocks them over.

That’s peak Sanderson energy: using limitations and structure cleverly mid-fight.

---

## 3. Where “Deeper than Elements” Shows Up

Here’s how you make it *feel* deeper than “I shoot fire.”

### 3.1. Casters think in *behaviors*, not substances

* Rookie: “I throw rocks and make walls.”
* Journeyman: “I adjust density and motion of local matter; rocks are just convenient.”
* Advanced: “I don’t care what it is—if it’s Substance, I can reForm it and Flow it.”

So later, the same Matter+Motion mage:

* Solidifies **mist** into stepping platforms.
* Makes an enemy’s **cloak** rigid so they trip.
* Shreds **shadow** on the ground by treating it as a thin layer of altered Substance/Form.

Readers see consistent “power set,” but also evolution in cleverness.

---

### 3.2. Clear **laws** (Sanderson flavor)

A few simple rules you keep repeating:

1. **You can’t affect Aspects that aren’t there.**
   * No Substance? You can’t grab it.
   * No existing Skew? You can’t release a blast; you have to build it first.
2. **You can’t get something for nothing.**
   * Cooling one place heats another.
   * Strengthening one structure weakens or draws from something else.
3. **You’re bottlenecked by knowledge & definition.**
   * To bind, you must be able to *define* what you’re binding.
   * To change Form, you must understand the structure at least intuitively.

This keeps the system feeling like a Sanderson-style “puzzle box” rather than a vibe.

---

### 3.3. Action-oriented progression

Instead of just “more power,” fighters progress like this:

* **Novice Matter-mage:**
  * Simple shapes: walls, spikes, crude shields.
* **Journeyman:**
  * Complex, *moving* geometry: folding shields, shifting terrain, mobile platforms.
* **Senior:**
  * Aspect-level tricks:
    * Using Skew to pre-load tension in the arena then release when needed.
    * Using Threshold to flip terrain between solid/liquid states in patterns.

Same underlying Tools, more **tactical subtlety**.

---

## 4. Making It Feel Sanderson-y *and* Understandable

To keep non-nerds happy while still using all this:

* On the page, talk mostly in **Domain** language:
  * “She thinned the ground under him and thickened the air above.”
  * “He stole momentum from the arrow and dumped it into the stone behind him.”
* Use Aspect jargon **sparingly**, for:
  * Masters.
  * Training scenes.
  * Big “ohhhh that’s how it works” reveals.
* Lean on **limitations** for drama:
  * “The stone here is already hollow; I can’t pull more shape from it.”
  * “I’ve pushed all the heat into that one spot—if the binding breaks, it’ll go off like a bomb.”
* Let clever combos win fights, not bigger beams:
  * Redirecting enemy force,
  * Exploiting their built-up Skew,
  * Rebinding their Threshold mid-teleport, etc.

That’s very Sanderson: readers learn the rules bit by bit, then get rewarded when those rules are used in surprising, logical ways.

---

If you want, next we can:

* Pick **one Domain** (say Motion or Heat/Phase) and build a full “combat style” out of it: basic moves, advanced tricks, signature duels.
* Or sketch **three different casters**, each with a different Aspect specialty, and stage a three-way fight to stress-test the system.

---


# Magical Languages as Paradigms

They still make sense, but they “shift down a layer” now that we’ve gone full Aspects/Behaviors instead of “Fire Source go boom.”

Think of it like this:

* **Aspects** (Substance, Form, Flow, Bind, Threshold, Echo, Skew, etc.) = CPU instructions.
* **Elemental Behaviors** (Matter, Motion, Heat/Phase, Force/Pressure, Constraint) = standard libraries.
* **Languages** = different *casting paradigms* that talk to those libraries and Aspects in different ways.

Let’s expand the language options and show how each one fits this new structure.

---

## 1. Recap: What’s a “language” in-world?

A **language** = a magical tradition / discipline that has:

* Its own way of writing / speaking rituals
* Its own assumptions about **what you manipulate**:
  * Domain Sources vs Aspects vs pseudo-sources
* Its own strengths: speed, precision, scalability, etc.

Everyone is still talking to the *same* metaphysics underneath; they just “code” differently.

---


## 2. Language 1 – Vernacular Charms (Pythonic Style)

**High-level / readable / action-friendly.**

### What it is

* Everyday spoken charms + simple sigils.
* Casters mostly think in **Elemental Behaviors**:
  * “Harden the wall,” “pull that spear sideways,” “heat the lock until it warps.”
* Under the hood, the tradition has baked-in Aspect combos:
  * “Harden” = Matter (Substance+Form density)
  * “Pull” = Motion (Flow on position + Skew toward caster)
  * “Heat” = Heat/Phase (Skew+Flow+Threshold on temp)

### How it uses the system

* **Mostly calls Behavior-level “APIs”**, not raw Aspects.
* Often uses **artifact streaming**:
  * Wands, rings, staves that know how to translate “harden” into the right Aspect calls.
* Can still do **manual streaming** for flexible one-off effects.

### Strengths

* Fast to learn, fast to improvise.
* Great for **action scenes**:
  * One shouted phrase → a clear effect.
* Easy to show on-page with simple, punchy incantations.

### Weaknesses

* Less raw control over Aspects:
  * “Harden” always uses the standard density pattern. Want exotic materials? That’s harder.
* Harder to invent truly new effects; you’re remixing existing “verbs.”


### Action Feel

Your fight mage yelling:

> “Harden, here! Break, there! Pull, now!”

…and we know that’s:

* Constraint + Matter + Motion combos firing under the hood.

This language totally *works* with the new system. It’s just the “high-level API” layer over Aspects.

---


## 3. Language 2 – Glyphic Geometry (Deep Geometry / C++ Style)

**Low-level, precise, precomputed.**

### What it is

* Complex ritual diagrams, polygons, 3D arrays of sigils.
* Geometry spells out **Form, Threshold, and Bind** in painful detail:
  * Lines = Flow paths.
  * Angles = relative Skew limits.
  * Layers = Thresholds between states.

### How it uses the system

* Works at the **Aspect level**, but via geometry:
  * A narrow funnel shape = where Flow is allowed.
  * Thickened lines = where Substance should accumulate.
  * Nested circles = Thresholds inside Thresholds.
* Most often used with:
  * **StreamingArtifact** (huge built-in circles in a chamber).
  * **Pseudo-sources** (city wards, fortress engines) compiled from big diagrams.

### Strengths

* Insanely efficient and scalable:
  * Citywide wards,
  * Climate control engines,
  * Giant battlefield manipulations.
* Very predictable once set up: “compiled” magic.

### Weaknesses

* Slow to prepare.
* Error-prone: one bad angle → catastrophic misrouting of Flow or Skew.


### Action Feel

* Not for quick duels; more for:
  * “We’re standing in the middle of a giant sigil; they just activated the outer ring.”
  * Earth splitting in clean fractal lines, storm walls snapping into perfect hexagons.

Glyphic Geometry makes *perfect* sense with Aspects: it’s literally **Form + Threshold + Bind UI**.

---


## 4. Language 3 – Pattern Ritecraft (R-Style / Statistical)

**Data-heavy, large-scale, pattern-based.**

### What it is

* Rituals that work on **sets** rather than individuals:
  * Whole battalions, entire districts, bloodlines, seasons.
* Uses:
  * Repeated invocations, tally marks, chants, and symbolic “tables.”

### How it uses the system

* Heavy on:
  * **Echo** (past events, logs),
  * **Skew** (imbalances across a population),
  * Optional **Pattern** Aspect (if you choose to include it).
* Talks mostly to:
  * **Pseudo-sources** like Census Engines, Oath Engines, Weather Wards:
    * “Set morale of this cohort +10%.”
    * “Reduce disease incidence in these blocks.”
* Mode is often:
  * **Buffered + Pseudo-source**:
    * The ritual updates parameters on a city system which then acts continuously.

### Strengths

* Insane power at **population level**:
  * Nudge a war’s outcome by tweaking odds.
  * Shift the baseline luck of a whole neighborhood.

### Weaknesses

* Terrible for precise, one-off action:
  * You can’t discreetly snipe one guy with Pattern Ritecraft (or you can, but it’s wasteful and weird).
* Easy to introduce **bias** and weird side effects:
  * “We lowered crime but accidentally tanked innovation.”


### Action Feel

More “behind the curtain,” but you can have:

> The enemy army hit a stretch of road the ward had studied for twenty years.
>
> Statistically, half those horses should’ve kept their footing. Today, not one did.

Again: fits perfectly, because it’s just one way to orchestrate **Echo + Skew + Bind + Flow** on groups.

---


## 5. Language 4 – Aspect Calculus (Assembly / Functional)

**Super-nerd, very abstract, very powerful in small hands.**

### What it is

* A tradition that **names and manipulates Aspects directly**:
  * “Increase Skew between here and there.”
  * “Route Flow of this change along that Form.”
* Often spoken in very compact, technical phrases or even silent mental diagrams.

### How it uses the system

* Works **purely at the Aspect layer**, sometimes skipping Domain behaviors entirely.
* Example internal thinking:
  * “Don’t call ‘Fire’; call:
    * Skew(temperature) on Substance(air+fuel),
    * then Flow until Threshold(ignition).”
* Mode:
  * Usually **StreamingManual**, sometimes with tiny helper artifacts.
  * Advanced casters might have **BufferedInternal** pseudo-sources (like Bind engines).

### Strengths

* Extreme flexibility:
  * Can improvise effects no one’s ever seen because they’re building from primitives.
* Deep understanding of limitations:
  * They can see exactly where and why a rival’s spell is unstable.

### Weaknesses

* Hard to learn.
* Easy to break yourself:
  * Screw up Flow+Skew interplay, and you create runaway cascades or deadlocks.
* Very cognitively expensive in combat:
  * Most Aspect Calculus users rely on a few favorite “macros” for action scenes.


### Action Feel

For readers, you still show flashy effects.
But when they think, it sounds like:

> “He’d over-skewed the floor without providing Flow out. Idiot. All that tension had to go somewhere.”

This is the language that makes the system feel **deeply hard & technical** in a Sanderson-compatible way.

---


## 6. Language 5 – Contractual Logic (Rule / IFTTT / Prolog-ish)

**Rule-based, event-driven magic.**

### What it is

* Spells framed as explicit rules:
  * “IF anyone crosses this line WITHOUT this token, THEN apply constraint X and alert Y.”
* Lives on:
  * Wards,
  * Background enchantments,
  * Long-term oaths.

### How it uses the system

* Heavy on:
  * **Bind** (conditions & consequences),
  * **Threshold** (events & boundaries),
  * **Echo** (history of triggers).
* Often uses **Silent Ledger** and similar Domain Sources as the host.
* Mode:
  * Usually **Pseudo-source** (rule engines running continuously).
  * Also **ArtifactStreaming** for “smart items.”

### Strengths

* Perfect for automation:
  * Security,
  * Contracts,
  * “Always-on” protections.
* Very testable:
  * You can sandbox rules and see what they do.

### Weaknesses

* Static and brittle:
  * If your conditions don’t cover a weird edge-case, the magic will misbehave in very literal ways.
* Vulnerable to “lawyer mages”:
  * People who exploit logical loopholes.


### Action Feel

In fights:

* Rules pre-trigger:
  * You hit someone → a rule (“if caster is struck, then warp attacker’s footing”) fires.
* Clever characters **change rules mid-fight**:
  * Rebinding protections,
  * Trick an enemy into crossing a hidden threshold.

This meshes wonderfully with **Threshold + Bind** Aspects and gives you a lot of “Sanderson puzzle combat” possibilities.

---

## 7. Do These Languages Still Make Sense With Aspects & Modes?

Yes. They’re just different **views** on the same substrate:

* Vernacular Charms: Elemental Behaviors, high-level, action-driven → great POV magic for main characters.
* Glyphic Geometry: Infrastructure, wards, big systems → great backdrop & set-piece magic.
* Pattern Ritecraft: Societal-scale manipulation → great for politics, wars, large consequences.
* Aspect Calculus: Rare, deep specialists → great for mentors, villains, or late-arc growth.
* Contractual Logic: Background rules & oaths → great for treaties, curses, and clever rule exploits.

Each language naturally **favours certain modes**:

| Language          | Favored Mode(s)                                      |
| ----------------- | ---------------------------------------------------- |
| Vernacular Charms | StreamingManual, ArtifactStreaming                   |
| Glyphic Geometry  | ArtifactStreaming, Pseudo-source                     |
| Pattern Ritecraft | Pseudo-source (civic systems), Buffered              |
| Aspect Calculus   | StreamingManual, BufferedInternal                    |
| Contractual Logic | Pseudo-source, ArtifactStreaming (smart wards/items) |

But nothing stops a versatile mage from mixing them.

---

## 8. How to Use This in an Action-Oriented, Sanderson-ish Way

To keep it punchy and fun for non-programmers:

* **Frontstage**:
  * Show Vernacular Charms and Contractual Logic most often:
    * “He reversed the force on the spear.”
    * “The floor rune triggered when she crossed it.”
* **Midstage**:
  * Occasionally show a glimpse of Glyphic Geometry (massive circles, city wards) and Pattern Ritecraft (rituals affecting thousands).
* **Backstage / High-tier**:
  * Reveal Aspect Calculus in key mentor/villain/late-book moments:
    * “No, don’t call fire. Increase Skew here and give Flow nowhere to go but through his shield.”

That gives exactly the Sanderson feel:

* Clear, repeated rules.
* Increasingly clever uses.
* A sense that there’s *more* under the hood if you look.

---


# Five-Tier Caster Progression (Updated for Aspects, Behaviors, and Languages)


## Overview of What Changes

With our new setup, skill is really about:

* **Layer awareness**
  * Domain Behaviors (Matter, Motion, Heat/Phase, Force/Pressure, Constraint)
  * Underlying Aspects (Substance, Form, Flow, Bind, Threshold, Echo, Skew)
  * Pseudo-sources and civic systems
* **Language fluency**
  * Vernacular Charms (high-level)
  * Glyphic Geometry
  * Pattern Ritecraft
  * Contractual Logic
  * Aspect Calculus
* **Mode mastery**
  * Streaming manual
  * Artifact streaming
  * Buffered (artifact or internal)
  * Pseudo-source manipulation

The 5 tiers now map cleanly onto *how deep down the stack* a caster can work.

---


## Tier 1 – Charm User (Script User)

**Where they live in the stack:**

* **Behaviors only** (Matter/Motion/Heat/Constraint) as *named moves*.
* No real awareness of Aspects; they think in “harden, push, burn, block.”
* 90% Vernacular Charms, 10% “press button on artifact.”

**Languages / modes:**

* Language: **Vernacular Charms** only.
* Mode: mostly **Artifact Streaming** (“wand does the hard part”), with a bit of **Streaming Manual** for tiny effects.

**What they can do:**

* Use pre-taught moves in straight lines:
  * Harden this spot.
  * Pull that object.
  * Throw a simple fire-burst.
* Basic, canned combos:
  * Raise a stone wall, then harden it.
* Some param tweaks:
  * “Smaller wall, but quicker.”

**What they *don’t* get:**

* Why “harden” fails on fog but works on stone.
* Why their heating spell sometimes explodes when overused.
* Anything about pseudo-sources, Aspects, or civic systems.

---


## Tier 2 – Shaper (Junior / Parameter Tinkerer)

**Where they live in the stack:**

* **Behaviors plus a *hint* of Aspects.**
* They know:
  * Matter is really “shape + stuff.”
  * Motion is “change + imbalance.”

**Languages / modes:**

* Languages:
  * Solid in **Vernacular Charms**.
  * Beginning to dabble in simple **Contractual Logic** (“if I’m hit, do X”).
* Modes:
  * Comfortable with **Streaming Manual** for modest spells.
  * Still lean on **Artifact Streaming** for bigger effects.

**What they can do:**

* Tune Behavior parameters intentionally:
  * “Harden it *only* against arrows, not against sound.”
* Chain Behaviors smartly:
  * Soften the floor then push someone into it.
  * Pull heat out of metal and dump it into air instead of nowhere.
* Recognize “this is a Motion problem, not a Matter problem.”

**What they *don’t* get:**

* The full Aspect layer: they sense Skew and Flow as “tension” and “rush,” but can’t articulate it.
* They can’t design wards or pseudo-sources; they just use them.

---


## Tier 3 – Weaver (Journeyman / Spell Developer)

**Where they live in the stack:**

* Fully fluent in **Elemental Behaviors**.
* Consciously aware of some **Aspects**:
  * They can talk about Skew, Flow, Bind in simple terms.
* Beginning awareness of **pseudo-sources** as things that must be fed and maintained (but they don’t design them from scratch).

**Languages / modes:**

* Languages:
  * Fluent **Vernacular Charms**.
  * Functional **Contractual Logic** (simple wards & triggers).
  * At least literate in **Glyphic Geometry** (can read and tweak existing arrays).
* Modes:
  * Uses **all three**:
    * Streaming Manual for improvisation.
    * Artifact Streaming for reliable moves.
    * **Buffered artifacts** (pre-charged effects) for prepared fights.

**What they can do:**

* **Invent new “moves”** at the Behavior level:
  * A folding shield of Matter + Motion.
  * A “heat siphon” that moves temperature without combustion.
* Build small, localized pseudo-sources *from templates*:
  * A workshop Forge-knot that handles standard heating tasks.
* Use Aspect logic in combat:
  * “He built up Skew in that shield; if I relieve it sideways, it’ll slam him instead.”

**What they *don’t* get:**

* Writing brand-new glyphic systems from scratch (they tweak, they don’t architect).
* Aspect Calculus as a general language; they know a few “Aspect tricks” but not the whole discipline.
* Designing big civic pseudo-sources (gate engines, weather grids).

---


## Tier 4 – Systems Mage / Debugger

**Where they live in the stack:**

* Comfortable at **both**:
  * Domain Behaviors (for combat/action),
  * Aspect layer (for analysis and deep tweaks).
* They understand that:
  * Ember-like Domain Sources are just **precomposed Aspect bundles**.
  * Wards, engines, and pseudo-sources have **schemas and invariants**.

**Languages / modes:**

* Languages:
  * Strong in **Vernacular Charms** (for field work).
  * Fluent in **Glyphic Geometry**.
  * Competent in **Pattern Ritecraft** (group-level effects).
  * Proficient in **Contractual Logic** for complex wards/oaths.
  * Basic **Aspect Calculus** (can reason and occasionally cast with raw Aspects).
* Modes:
  * Heavy use of **Pseudo-sources** (civic systems, engines) and **Artifact Streaming**.
  * Still able to **Streaming Manual** + clever Aspect use in a pinch.
  * Can recharge / configure **BufferedInternal** pseudo-sources, even if they didn’t make them.

**What they can do:**

* Read, debug, and refactor:
  * City wards,
  * Long-lived oath engines,
  * Misbehaving pseudo-sources.
* Diagnose failures in Aspect terms:
  * “Too much Skew, no Flow path → explosive backfire.”
  * “Threshold is leaking; the boundary definition is fuzzy.”
* Safely patch and optimize:
  * Reduce cost,
  * Add proper Constraints,
  * Improve logging and rollback behavior.

**What they *don’t* (usually) do:**

* Invent whole new Domain Sources.
* Create brand-new languages/traditions.
* Rewrite the metaphysical “standard library” of Behaviors.
  Those are Tier 5 moves.

---


## Tier 5 – Architect / Aspect Theorist (Metaprogrammer)

**Where they live in the stack:**

* Most of their mental time is **at the Aspect and system level**:
  * How do Aspects compose?
  * What new Domain Behaviors can we define?
  * How do civic pseudo-sources, wards, and local engines all interact?

**Languages / modes:**

* Languages:
  * Mastery of **Glyphic Geometry** for infrastructure.
  * Deep **Pattern Ritecraft** for societal-scale nudges.
  * Full **Contractual Logic** for complex rule scaffolding.
  * Fluent **Aspect Calculus**: can think and cast directly in Aspects when needed.
  * Can design new **Vernacular Charms** and idioms that democratize their work.
* Modes:
  * Creates and maintains **pseudo-sources** (local engines, civic systems, experimental sandboxes).
  * Often hosts **BufferedInternal** control aspects (like personal Bind engines).
  * Uses Streaming Manual mostly to prototype; field-casting is rarely the bottleneck for them.

**What they can do:**

* Define **new Domain Behaviors**:
  * Invent a standardized “Shock” behavior that wraps Skew+Flow+Force in a safe pattern and then propagate it as a new charm set.
* Architect whole magical ecosystems:
  * A city’s fire grid (Matter + Heat + Constraint),
  * Its crime-oath engine (Bind + Threshold + Echo),
  * Its climate moderation system (Flow + Skew + Pattern of weather).
* Create or refine **languages** / traditions:
  * E.g., a battlefield shorthand dialect of Charms optimized for quick Aspect-safe combos.

**What they *worry about*:**

* Long-term system integrity:
  * Will this oath engine bias the law in subtle ways?
  * Will this climate ward overfit to the last decade and fail catastrophically?
* Global Aspects balance:
  * Too much Skew locked in one region,
  * Thresholds overloaded between worlds,
  * Echo saturated with bad states.

---


## How Progression Feels Now (High-Level)

---

## Summary

This document provides a comprehensive, modular, and technically robust framework for a magic system inspired by programming. It is designed to be both narratively rich and logically consistent, supporting a wide range of character arcs, magical traditions, and story structures.

From the POV of a character and reader, “levels” now read like this:

* **Tier 1 → 2:**
  * From “I know some moves” → “I understand how to tweak and chain moves.”
  * Fundamentally: learn **Behaviors** as composable tools instead of single tricks.
* **Tier 2 → 3:**
  * From tuning behaviors → designing **new techniques** and small engines.
  * Start to consciously recognize and exploit **Aspects** (Skew, Flow, Bind) in fights.
* **Tier 3 → 4:**
  * From designing single spells → understanding and maintaining **systems**.
  * They can reason about **pseudo-sources, wards, and civic magic**; become the ones others call when “the city’s magic is acting weird.”
* **Tier 4 → 5:**
  * From maintenance & optimization → **founding new paradigms**.
  * Create new Behaviors, traditions, pseudo-sources; redesign how a city or nation’s magic works at a fundamental layer.

Mechanically, nothing we added (Aspects, Behaviors, languages, pseudo-sources) breaks the ladder; it actually maps onto it very cleanly. The main tweak is *clarity*:

* Lower tiers: live at the **Behavior + Charm** level.
* Mid tiers: bridge **Behavior ↔ Aspect ↔ simple systems**.
* High tiers: operate at **Aspect + large systems + language design**.

---
