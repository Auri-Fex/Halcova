


import argparse
import dataclasses
import datetime as dt
import hashlib
import json
import math
import os
import random
import re
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# ============================================================
# CONFIG — change this if you ever move the pipeline directory
# ============================================================

PIPELINE_DIR = Path(r"I:\My Drive\Worldbuilding\world_pipeline")

# ============================================================
# Helpers
# ============================================================

VOWELS = set("aeiouy")
SEASONS = ["Thaw", "Bloom", "Highsun", "Harvest", "Sootfall", "Deepfrost"]

def clamp(v: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, v))

def slugify_keep_readable(name: str) -> str:
    name = name.strip()
    name = re.sub(r'[<>:"/\\|?*]', "", name)  # Windows illegal chars
    name = re.sub(r"\s+", " ", name).strip()
    return name[:80] if len(name) > 80 else name

def safe_filename(name: str) -> str:
    name = slugify_keep_readable(name)
    return re.sub(r"[^\w\s\-\.,']", "", name).strip() or "World"

def ensure_unique_dir(base: Path) -> Path:
    if not base.exists():
        base.mkdir(parents=True, exist_ok=True)
        return base
    # If folder exists, create suffix __2, __3, ...
    i = 2
    while True:
        candidate = Path(str(base) + f"__{i}")
        if not candidate.exists():
            candidate.mkdir(parents=True, exist_ok=True)
            return candidate
        i += 1

def stable_hash_int(s: str, mod: int) -> int:
    h = hashlib.sha256(s.encode("utf-8")).hexdigest()
    return int(h[:16], 16) % mod

def dist(a: Tuple[float, float], b: Tuple[float, float]) -> float:
    return math.hypot(a[0] - b[0], a[1] - b[1])

def pick(rng: random.Random, items: List[str]) -> str:
    return items[rng.randrange(len(items))]

def weighted_choice(rng: random.Random, items: List[Tuple[str, float]]) -> str:
    total = sum(w for _, w in items)
    x = rng.random() * total
    acc = 0.0
    for item, w in items:
        acc += w
        if x <= acc:
            return item
    return items[-1][0]

def dedupe_preserve(xs: List[str]) -> List[str]:
    seen = set()
    out = []
    for x in xs:
        if x not in seen:
            out.append(x)
            seen.add(x)
    return out

# ============================================================
# Data model
# ============================================================

@dataclass
class Planet:
    name: str
    gravity_g: float
    day_hours: float
    year_days: int
    axial_tilt_deg: float
    notes: List[str] = field(default_factory=list)

@dataclass
class Region:
    id: str
    name: str
    biome: str
    hazards: List[str]
    resources: List[str]
    notes: List[str] = field(default_factory=list)

@dataclass
class Settlement:
    id: str
    name: str
    kind: str  # hamlet, village, town, city, fort, port
    population: int
    region_id: str
    x: float
    y: float
    tags: List[str] = field(default_factory=list)

@dataclass
class Route:
    a: str
    b: str
    km: float
    mode: str  # road, river, sea
    risk: str  # low, medium, high

@dataclass
class Polity:
    id: str
    name: str
    capital_id: str
    government: str
    ideology: List[str]
    population: int
    army_pct: float
    treasury_index: float
    exports: List[str]
    imports: List[str]
    laws: List[str]
    institutions: List[str]
    notes: List[str] = field(default_factory=list)

@dataclass
class Faction:
    id: str
    name: str
    polity_id: Optional[str]  # None for cross-border
    type: str
    goals: List[str]
    methods: List[str]
    resources: List[str]
    enemies: List[str]
    allies: List[str]
    hooks: List[str]

@dataclass
class MagicSystem:
    presence: str  # none, rare, common
    hardness: str  # soft, medium, hard
    inputs: List[str]
    outputs: List[str]
    costs: List[str]
    failure_modes: List[str]
    countermeasures: List[str]
    second_order_effects: List[str]
    notes: List[str] = field(default_factory=list)

@dataclass
class Event:
    id: str
    year: int
    season: str
    title: str
    cause_ids: List[str]
    agents: List[str]
    consequences: List[str]

@dataclass
class Conflict:
    id: str
    title: str
    parties: List[str]
    stakes: List[str]
    escalation: List[str]
    receipts: List[str]

@dataclass
class StoryKit:
    themes: List[str]
    tone: str
    story_type: str
    default_scene_locations: List[str]
    hooks: List[str]
    dont_break: List[str] = field(default_factory=list)

@dataclass
class World:
    seed: int
    config: Dict
    planet: Planet
    regions: Dict[str, Region]
    settlements: Dict[str, Settlement]
    routes: List[Route]
    polities: Dict[str, Polity]
    factions: Dict[str, Faction]
    magic: MagicSystem
    timeline: List[Event]
    conflicts: List[Conflict]
    story: StoryKit
    receipts: List[str] = field(default_factory=list)
    name_registry: Dict[str, str] = field(default_factory=dict)
    coherence_score: float = 0.0
    warnings: List[str] = field(default_factory=list)
    hard_errors: List[str] = field(default_factory=list)

# ============================================================
# NameForge — pronounceable + deterministic + language-ish
# ============================================================

@dataclass
class NameProfile:
    name: str
    # phoneme-ish chunks
    onsets: List[str]
    nuclei: List[str]
    codas: List[str]
    # constraints
    max_consonant_run: int = 2
    min_vowel_rate: float = 0.30   # vowels / total chars
    max_len: int = 12
    min_len: int = 4
    banned_starts: Tuple[str, ...] = ("ng", "pt", "bn", "rtz")
    banned_ends: Tuple[str, ...] = ("hh", "jj", "vv", "qq")

def build_profiles() -> List[NameProfile]:
    # These aren't literal language models; they're *phonotactic moods* inspired by
    # real inventories (Celtic-ish / Slavic-ish / Romance-ish) without copying a language.
    celtic = NameProfile(
        name="celtic-ish",
        onsets=["b","br","c","ch","cr","d","dr","f","g","gr","h","k","l","m","n","p","pr","r","s","sh","t","tr","v"],
        nuclei=["a","e","i","o","u","ae","ai","ea","eo","ia","io","oa","ui"],
        codas=["n","r","l","s","th","nd","rn","rd","ll","ss","ch","g","m","t","d"],
        max_consonant_run=2,
        min_vowel_rate=0.33,
        max_len=11,
        min_len=4,
    )
    slavic = NameProfile(
        name="slavic-ish",
        onsets=["b","br","v","vr","d","dr","z","zh","k","kr","m","n","p","pr","r","s","sk","st","t","tr","ch"],
        nuclei=["a","e","i","o","u","y","ia","io","ei","oy"],
        codas=["n","v","k","t","d","r","s","sk","st","ch","v","m","z"],
        max_consonant_run=2,
        min_vowel_rate=0.30,
        max_len=12,
        min_len=4,
        banned_starts=("ng","pt","bn"),
    )
    romance = NameProfile(
        name="romance-ish",
        onsets=["b","c","ch","d","f","g","gr","l","m","n","p","pr","r","s","t","v"],
        nuclei=["a","e","i","o","u","ia","io","ea","eo","ou","au"],
        codas=["n","r","l","s","t","d","m","v"],
        max_consonant_run=2,
        min_vowel_rate=0.35,
        max_len=12,
        min_len=4,
    )
    return [celtic, slavic, romance]

def vowel_rate(s: str) -> float:
    if not s:
        return 0.0
    v = sum(1 for ch in s.lower() if ch in VOWELS)
    return v / len(s)

def max_consonant_run(s: str) -> int:
    best = 0
    cur = 0
    for ch in s.lower():
        if ch.isalpha() and ch not in VOWELS:
            cur += 1
            best = max(best, cur)
        else:
            cur = 0
    return best

def pronounceable(s: str, profile: NameProfile) -> bool:
    s2 = s.lower()
    if len(s2) < profile.min_len or len(s2) > profile.max_len:
        return False
    if any(s2.startswith(b) for b in profile.banned_starts):
        return False
    if any(s2.endswith(b) for b in profile.banned_ends):
        return False
    if max_consonant_run(s2) > profile.max_consonant_run:
        return False
    if vowel_rate(s2) < profile.min_vowel_rate:
        return False
    # avoid triple same letter
    if re.search(r"(.)\1\1", s2):
        return False
    return True

class NameForge:
    def __init__(self, world_seed: int, registry: Dict[str, str], profiles: List[NameProfile]):
        self.world_seed = world_seed
        self.registry = registry
        self.profiles = profiles

    def _rng_for(self, key: str) -> random.Random:
        # deterministic RNG per key
        h = hashlib.sha256(f"{self.world_seed}::{key}".encode("utf-8")).hexdigest()
        seed_int = int(h[:16], 16)
        return random.Random(seed_int)

    def get(self, key: str, style: str = "auto", cap: bool = True) -> str:
        # key: stable ID like "planet:core", "region:R1", "settlement:S4", "faction:F2", etc.
        if key in self.registry:
            return self.registry[key]

        rng = self._rng_for(key)

        if style == "auto":
            profile = rng.choice(self.profiles)
        else:
            profile = next((p for p in self.profiles if p.name == style), rng.choice(self.profiles))

        # generate syllables
        for _ in range(400):
            syl = rng.randint(2, 4)
            parts = []
            for _i in range(syl):
                onset = rng.choice(profile.onsets)
                nuc = rng.choice(profile.nuclei)
                coda = rng.choice(profile.codas) if rng.random() < 0.7 else ""
                parts.append(onset + nuc + coda)
            candidate = "".join(parts)
            if pronounceable(candidate, profile):
                result = candidate.capitalize() if cap else candidate
                self.registry[key] = result
                return result
        # fallback
        result = "Xyloxis" if cap else "xyloxis"
        self.registry[key] = result
        return result

# =================== MAIN BLOCK AT END ===================


if __name__ == "__main__":
    print("[DEBUG] Script main block reached.")
    import sys
    seed = random.randint(1, 1_000_000)
    print(f"[DEBUG] Using seed: {seed}")
    if len(sys.argv) > 1:
        try:
            seed = int(sys.argv[1])
            print(f"[DEBUG] Overriding seed from argv: {seed}")
        except Exception as e:
            print(f"[DEBUG] Failed to parse seed from argv: {e}")
    profiles = build_profiles()
    name_registry = {}
    namer = NameForge(seed, name_registry, profiles)
    rng = random.Random(seed)

    # Advanced planet generation
    planet_name = namer.get("planet:core")
    planet_desc = f"{planet_name} is a world of extremes, with ancient ruins, shifting climates, and a sky dominated by {rng.choice(['two moons', 'a crimson sun', 'perpetual auroras', 'a shattered ring'])}."
    planet = Planet(
        name=planet_name,
        gravity_g=round(rng.uniform(0.7, 1.3), 2),
        day_hours=rng.choice([22, 24, 26]),
        year_days=rng.choice([360, 400, 420]),
        axial_tilt_deg=rng.choice([23.5, 25, 28]),
        notes=[planet_desc]
    )

    # Regions with relationships and lore
    region_biomes = ["forest", "mountain", "plains", "desert", "coast", "swamp", "tundra"]
    region_features = [
        "ancient standing stones", "forbidden library", "volcanic springs", "crystal caves",
        "haunted battlefield", "living forest", "sunken city", "sky-piercing spire"
    ]
    regions = {}
    region_lore = {}
    for i in range(3):
        region_id = f"R{i+1}"
        region_name = namer.get(f"region:{region_id}")
        biome = rng.choice(region_biomes)
        feature = rng.choice(region_features)
        lore = f"{region_name} is known for its {feature} and {biome} landscape. Legends speak of {rng.choice(['lost gods', 'ancient wars', 'hidden treasures', 'cursed bloodlines'])} here."
        regions[region_id] = Region(
            id=region_id,
            name=region_name,
            biome=biome,
            hazards=[rng.choice(["bandits", "storms", "monsters", "famine", "plague", "arcane fallout"])],
            resources=[rng.choice(["iron", "grain", "timber", "salt", "crystal", "herbs"])],
            notes=[lore]
        )
        region_lore[region_id] = lore

    # Region relationships
    region_rel = []
    region_ids = list(regions.keys())
    for i in range(len(region_ids)):
        a, b = region_ids[i], region_ids[(i+1)%len(region_ids)]
        rel = rng.choice(["trade", "rivalry", "ancient feud", "seasonal alliance"])
        region_rel.append(f"{regions[a].name} and {regions[b].name} have a history of {rel}.")

    # Settlements with purpose
    settlements = {}
    settlement_purposes = ["trade hub", "defensive outpost", "pilgrimage site", "arcane academy", "mining town", "port city"]
    for i in range(6):
        region_id = rng.choice(region_ids)
        settlement_id = f"S{i+1}"
        settlement_name = namer.get(f"settlement:{settlement_id}")
        kind = rng.choice(["village", "town", "city", "fort"])
        purpose = rng.choice(settlement_purposes)
        settlements[settlement_id] = Settlement(
            id=settlement_id,
            name=settlement_name,
            kind=kind,
            population=rng.randint(500, 20000),
            region_id=region_id,
            x=rng.uniform(0, 100),
            y=rng.uniform(0, 100),
            tags=[purpose]
        )

    # Polities with alliances/conflicts
    polity_names = [namer.get(f"polity:P{i+1}") for i in range(2)]
    polities = {}
    for i, polity_name in enumerate(polity_names):
        pol_id = f"P{i+1}"
        controlled_settlements = [s.id for s in settlements.values() if int(s.id[1:]) % 2 == i]
        polities[pol_id] = Polity(
            id=pol_id,
            name=polity_name,
            capital_id=controlled_settlements[0] if controlled_settlements else list(settlements.keys())[0],
            government=rng.choice(["monarchy", "republic", "theocracy", "council"]),
            ideology=[rng.choice(["tradition", "progress", "faith", "order", "freedom"])],
            population=sum(settlements[sid].population for sid in controlled_settlements),
            army_pct=round(rng.uniform(0.03, 0.12), 2),
            treasury_index=round(rng.uniform(0.5, 2.0), 2),
            exports=[rng.choice(["grain", "iron", "timber", "arcane relics"])],
            imports=[rng.choice(["salt", "herbs", "crystal", "livestock"])],
            laws=[rng.choice(["trial by ordeal", "open markets", "arcane registration", "hereditary rule"])],
            institutions=[rng.choice(["council", "academy", "guild", "temple"])],
            notes=[f"Controls settlements: {', '.join(controlled_settlements)}"]
        )

    polity_rel = f"{polity_names[0]} and {polity_names[1]} are currently in a state of {rng.choice(['tense peace', 'open conflict', 'secret alliance', 'trade war'])}."

    # Factions
    factions = {}
    for i in range(2):
        fac_id = f"F{i+1}"
        fac_name = namer.get(f"faction:{fac_id}")
        factions[fac_id] = Faction(
            id=fac_id,
            name=fac_name,
            polity_id=f"P{(i%2)+1}",
            type=rng.choice(["guild", "cult", "mercenary band", "secret society"]),
            goals=[rng.choice(["control trade", "uncover lost magic", "overthrow rulers", "spread faith"])],
            methods=[rng.choice(["espionage", "bribery", "ritual", "force"]), rng.choice(["infiltration", "propaganda", "blackmail", "duels"])],
            resources=[rng.choice(["ancient texts", "hidden gold", "loyal agents", "forbidden spells"])],
            enemies=[namer.get(f"faction:F{2 if i==0 else 1}")],
            allies=[],
            hooks=[f"Rumored to be behind the {rng.choice(['disappearance of a noble', 'recent plague', 'arcane explosion', 'failed coup'])}."]
        )

    # Magic system with cultural role
    magic = MagicSystem(
        presence=rng.choice(["rare", "common", "ubiquitous"]),
        hardness=rng.choice(["soft", "medium", "hard"]),
        inputs=[rng.choice(["mana", "blood", "song", "memory"])],
        outputs=[rng.choice(["healing", "fire", "divination", "flight", "transformation"])],
        costs=[rng.choice(["fatigue", "madness", "aging", "debt"])],
        failure_modes=[rng.choice(["backfire", "mutation", "summoning", "memory loss"])],
        countermeasures=[rng.choice(["wards", "rituals", "iron", "oaths"])],
        second_order_effects=[rng.choice(["social stratification", "magical pollution", "political upheaval"])],
        notes=[f"Magic is {rng.choice(['regulated by the state', 'taboo in some regions', 'central to daily life', 'a source of fear'])}."]
    )

    # Timeline/history with causes and consequences
    timeline = []
    for i in range(3):
        event_id = f"E{i+1}"
        year = 1000 + i*37
        season = rng.choice(SEASONS)
        title = rng.choice([
            f"The {rng.choice(['Great', 'Last', 'Hidden'])} War of {planet_name}",
            f"Discovery of the {rng.choice(['Crystal Spire', 'Forbidden Library', 'Sunken City'])}",
            f"The Plague of {rng.choice([region.name for region in regions.values()])}"
        ])
        timeline.append(Event(
            id=event_id,
            year=year,
            season=season,
            title=title,
            cause_ids=[rng.choice(list(factions.keys()))],
            agents=[rng.choice(list(polities.values())).name],
            consequences=[rng.choice(["famine", "migration", "magical boom", "dynastic change"])]
        ))

    # Story kit with narrative hooks
    story = StoryKit(
        themes=[rng.choice(["adventure", "mystery", "betrayal", "redemption", "exploration"])],
        tone=rng.choice(["epic", "dark", "hopeful", "tragic"]),
        story_type=rng.choice(["quest", "conspiracy", "war saga", "coming of age"]),
        default_scene_locations=[region.name for region in regions.values()],
        hooks=[f"A {rng.choice(['lost artifact', 'forbidden ritual', 'missing heir', 'ancient prophecy'])} is at the heart of the unfolding events."],
        dont_break=["internal logic", "character motivation"]
    )

    # Assemble world
    world = World(
        seed=seed,
        config={},
        planet=planet,
        regions=regions,
        settlements=settlements,
        routes=[],
        polities=polities,
        factions=factions,
        magic=magic,
        timeline=timeline,
        conflicts=[],
        story=story,
        receipts=[],
        name_registry=name_registry,
        coherence_score=1.0,
        warnings=[],
        hard_errors=[]
    )

    # Output
    output_dir_path = PIPELINE_DIR / safe_filename(planet_name)
    out_dir = ensure_unique_dir(output_dir_path)
    try:
        with open(out_dir / "world_bible.md", "w", encoding="utf-8") as f:
            f.write(f"# {planet_name} World Bible\n\n")
            f.write(f"Seed: {seed}\n")
            f.write(f"Generated at: {dt.datetime.now().isoformat()}\n\n")
            f.write(f"## Planet Overview\n{planet_desc}\n\n")
            f.write(f"### Physical Parameters\nGravity: {planet.gravity_g}g\nDay: {planet.day_hours}h\nYear: {planet.year_days} days\nAxial Tilt: {planet.axial_tilt_deg}°\n\n")
            f.write(f"## Regions\n")
            for region in regions.values():
                f.write(f"### {region.name}\nBiome: {region.biome}\nHazards: {', '.join(region.hazards)}\nResources: {', '.join(region.resources)}\nLore: {region.notes[0]}\n\n")
            f.write(f"### Region Relationships\n")
            for rel in region_rel:
                f.write(f"- {rel}\n")
            f.write(f"\n## Settlements\n")
            for settlement in settlements.values():
                f.write(f"### {settlement.name}\nType: {settlement.kind}\nPopulation: {settlement.population}\nRegion: {regions[settlement.region_id].name}\nPurpose: {', '.join(settlement.tags)}\nLocation: ({settlement.x:.1f}, {settlement.y:.1f})\n\n")
            f.write(f"## Polities\n")
            for polity in polities.values():
                f.write(f"### {polity.name}\nType: {polity.government}\nIdeology: {', '.join(polity.ideology)}\nCapital: {settlements[polity.capital_id].name}\nPopulation: {polity.population}\nArmy: {int(polity.army_pct*100)}%\nTreasury Index: {polity.treasury_index}\nExports: {', '.join(polity.exports)}\nImports: {', '.join(polity.imports)}\nLaws: {', '.join(polity.laws)}\nInstitutions: {', '.join(polity.institutions)}\nNotes: {', '.join(polity.notes)}\n\n")
            f.write(f"### Polity Relationships\n- {polity_rel}\n\n")
            f.write(f"## Factions\n")
            for faction in factions.values():
                f.write(f"### {faction.name}\nType: {faction.type}\nPolity: {polities[faction.polity_id].name}\nGoals: {', '.join(faction.goals)}\nMethods: {', '.join(faction.methods)}\nResources: {', '.join(faction.resources)}\nEnemies: {', '.join(faction.enemies)}\nHooks: {', '.join(faction.hooks)}\n\n")
            f.write(f"## Magic System\nPresence: {magic.presence}\nHardness: {magic.hardness}\nInputs: {', '.join(magic.inputs)}\nOutputs: {', '.join(magic.outputs)}\nCosts: {', '.join(magic.costs)}\nFailure Modes: {', '.join(magic.failure_modes)}\nCountermeasures: {', '.join(magic.countermeasures)}\nSecond Order Effects: {', '.join(magic.second_order_effects)}\nNotes: {', '.join(magic.notes)}\n\n")
            f.write(f"## Timeline\n")
            for event in timeline:
                f.write(f"### {event.title}\nYear: {event.year} {event.season}\nAgents: {', '.join(event.agents)}\nCauses: {', '.join(event.cause_ids)}\nConsequences: {', '.join(event.consequences)}\n\n")
            f.write(f"## Story Kit\nThemes: {', '.join(story.themes)}\nTone: {story.tone}\nType: {story.story_type}\nLocations: {', '.join(story.default_scene_locations)}\nHooks: {', '.join(story.hooks)}\nDon't break: {', '.join(story.dont_break)}\n\n")
        print(f"[DEBUG] world_bible.md written successfully.")
    except Exception as e:
        print(f"[DEBUG] Failed to write world_bible.md: {e}")
    print(f"World generated: {planet_name}\nOutput folder: {out_dir}")

import argparse
import dataclasses
import datetime as dt
import hashlib
import json
import math
import os
import random
import re
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import argparse
import dataclasses
import datetime as dt
import hashlib
import json
import math
import os
import random
import re
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Dict, List, Optional, Tuple


# ...existing code...


# ...existing code...
r"""
Worldbuilder v2.0 — Ghostwriter-ready world compendium + stable NameForge

Outputs (in a folder named after the world):
- world_bible.md              (polished compendium)
- canon.json                  (full structured data + name registry)
- map_graph.dot               (route graph for visualization)
- naming.py                   (CLI + helper to generate consistent new names later)
- build_meta.json             (seed, timestamps, coherence scores)

Hard requirements implemented:
- Output folder is created under:
    I:\My Drive\Worldbuilding\world_pipeline\<WorldName>
- Folder name is the generated world name (safe-cleaned). If exists -> suffix __2, __3...
- Naming is deterministic per world + key, and registry is persisted for expansions.
- Pronounceability gate + language-ish profiles (phoneme sets inspired by real languages).
"""


import argparse
import dataclasses
import datetime as dt
import hashlib
import json
import math
import os
import random
import re
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# ============================================================
# CONFIG — change this if you ever move the pipeline directory
# ============================================================

PIPELINE_DIR = Path(r"I:\My Drive\Worldbuilding\world_pipeline")

# ============================================================
# Helpers
# ============================================================

VOWELS = set("aeiouy")
SEASONS = ["Thaw", "Bloom", "Highsun", "Harvest", "Sootfall", "Deepfrost"]

def clamp(v: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, v))

def slugify_keep_readable(name: str) -> str:
    name = name.strip()
    name = re.sub(r'[<>:"/\\|?*]', "", name)  # Windows illegal chars
    name = re.sub(r"\s+", " ", name).strip()
    return name[:80] if len(name) > 80 else name

def safe_filename(name: str) -> str:
    name = slugify_keep_readable(name)
    return re.sub(r"[^\w\s\-\.,']", "", name).strip() or "World"

def ensure_unique_dir(base: Path) -> Path:
    if not base.exists():
        base.mkdir(parents=True, exist_ok=True)
        return base
    # If folder exists, create suffix __2, __3, ...
    i = 2
    while True:
        candidate = Path(str(base) + f"__{i}")
        if not candidate.exists():
            candidate.mkdir(parents=True, exist_ok=True)
            return candidate
        i += 1

def stable_hash_int(s: str, mod: int) -> int:
    h = hashlib.sha256(s.encode("utf-8")).hexdigest()
    return int(h[:16], 16) % mod

def dist(a: Tuple[float, float], b: Tuple[float, float]) -> float:
    return math.hypot(a[0] - b[0], a[1] - b[1])

def pick(rng: random.Random, items: List[str]) -> str:
    return items[rng.randrange(len(items))]

def weighted_choice(rng: random.Random, items: List[Tuple[str, float]]) -> str:
    total = sum(w for _, w in items)
    x = rng.random() * total
    acc = 0.0
    for item, w in items:
        acc += w
        if x <= acc:
            return item
    return items[-1][0]

def dedupe_preserve(xs: List[str]) -> List[str]:
    seen = set()
    out = []
    for x in xs:
        if x not in seen:
            out.append(x)
            seen.add(x)
    return out

# ============================================================
# Data model
# ============================================================

@dataclass
class Planet:
    name: str
    gravity_g: float
    day_hours: float
    year_days: int
    axial_tilt_deg: float
    notes: List[str] = field(default_factory=list)

@dataclass
class Region:
    id: str
    name: str
    biome: str
    hazards: List[str]
    resources: List[str]
    notes: List[str] = field(default_factory=list)

@dataclass
class Settlement:
    id: str
    name: str
    kind: str  # hamlet, village, town, city, fort, port
    population: int
    region_id: str
    x: float
    y: float
    tags: List[str] = field(default_factory=list)

@dataclass
class Route:
    a: str
    b: str
    km: float
    mode: str  # road, river, sea
    risk: str  # low, medium, high

@dataclass
class Polity:
    id: str
    name: str
    capital_id: str
    government: str
    ideology: List[str]
    population: int
    army_pct: float
    treasury_index: float
    exports: List[str]
    imports: List[str]
    laws: List[str]
    institutions: List[str]
    notes: List[str] = field(default_factory=list)

@dataclass
class Faction:
    id: str
    name: str
    polity_id: Optional[str]  # None for cross-border
    type: str
    goals: List[str]
    methods: List[str]
    resources: List[str]
    enemies: List[str]
    allies: List[str]
    hooks: List[str]

@dataclass
class MagicSystem:
    presence: str  # none, rare, common
    hardness: str  # soft, medium, hard
    inputs: List[str]
    outputs: List[str]
    costs: List[str]
    failure_modes: List[str]
    countermeasures: List[str]
    second_order_effects: List[str]
    notes: List[str] = field(default_factory=list)

@dataclass
class Event:
    id: str
    year: int
    season: str
    title: str
    cause_ids: List[str]
    agents: List[str]
    consequences: List[str]

@dataclass
class Conflict:
    id: str
    title: str
    parties: List[str]
    stakes: List[str]
    escalation: List[str]
    receipts: List[str]

@dataclass
class StoryKit:
    themes: List[str]
    tone: str
    story_type: str
    default_scene_locations: List[str]
    hooks: List[str]
    dont_break: List[str] = field(default_factory=list)

@dataclass
class World:
    seed: int
    config: Dict
    planet: Planet
    regions: Dict[str, Region]
    settlements: Dict[str, Settlement]
    routes: List[Route]
    polities: Dict[str, Polity]
    factions: Dict[str, Faction]
    magic: MagicSystem
    timeline: List[Event]
    conflicts: List[Conflict]
    story: StoryKit
    receipts: List[str] = field(default_factory=list)
    name_registry: Dict[str, str] = field(default_factory=dict)
    coherence_score: float = 0.0
    warnings: List[str] = field(default_factory=list)
    hard_errors: List[str] = field(default_factory=list)

# ============================================================
# NameForge — pronounceable + deterministic + language-ish
# ============================================================

@dataclass
class NameProfile:
    name: str
    # phoneme-ish chunks
    onsets: List[str]
    nuclei: List[str]
    codas: List[str]
    # constraints
    max_consonant_run: int = 2
    min_vowel_rate: float = 0.30   # vowels / total chars
    max_len: int = 12
    min_len: int = 4
    banned_starts: Tuple[str, ...] = ("ng", "pt", "bn", "rtz")
    banned_ends: Tuple[str, ...] = ("hh", "jj", "vv", "qq")

def build_profiles() -> List[NameProfile]:
    # These aren't literal language models; they're *phonotactic moods* inspired by
    # real inventories (Celtic-ish / Slavic-ish / Romance-ish) without copying a language.
    celtic = NameProfile(
        name="celtic-ish",
        onsets=["b","br","c","ch","cr","d","dr","f","g","gr","h","k","l","m","n","p","pr","r","s","sh","t","tr","v"],
        nuclei=["a","e","i","o","u","ae","ai","ea","eo","ia","io","oa","ui"],
        codas=["n","r","l","s","th","nd","rn","rd","ll","ss","ch","g","m","t","d"],
        max_consonant_run=2,
        min_vowel_rate=0.33,
        max_len=11,
        min_len=4,
    )
    slavic = NameProfile(
        name="slavic-ish",
        onsets=["b","br","v","vr","d","dr","z","zh","k","kr","m","n","p","pr","r","s","sk","st","t","tr","ch"],
        nuclei=["a","e","i","o","u","y","ia","io","ei","oy"],
        codas=["n","v","k","t","d","r","s","sk","st","ch","v","m","z"],
        max_consonant_run=2,
        min_vowel_rate=0.30,
        max_len=12,
        min_len=4,
        banned_starts=("ng","pt","bn"),
    )
    romance = NameProfile(
        name="romance-ish",
        onsets=["b","c","ch","d","f","g","gr","l","m","n","p","pr","r","s","t","v"],
        nuclei=["a","e","i","o","u","ia","io","ea","eo","ou","au"],
        codas=["n","r","l","s","t","d","m","v"],
        max_consonant_run=2,
        min_vowel_rate=0.35,
        max_len=12,
        min_len=4,
    )
    return [celtic, slavic, romance]

def vowel_rate(s: str) -> float:
    if not s:
        return 0.0
    v = sum(1 for ch in s.lower() if ch in VOWELS)
    return v / len(s)

def max_consonant_run(s: str) -> int:
    best = 0
    cur = 0
    for ch in s.lower():
        if ch.isalpha() and ch not in VOWELS:
            cur += 1
            best = max(best, cur)
        else:
            cur = 0
    return best

def pronounceable(s: str, profile: NameProfile) -> bool:
    s2 = s.lower()
    if len(s2) < profile.min_len or len(s2) > profile.max_len:
        return False
    if any(s2.startswith(b) for b in profile.banned_starts):
        return False
    if any(s2.endswith(b) for b in profile.banned_ends):
        return False
    if max_consonant_run(s2) > profile.max_consonant_run:
        return False
    if vowel_rate(s2) < profile.min_vowel_rate:
        return False
    # avoid triple same letter
    if re.search(r"(.)\1\1", s2):
        return False
    return True

class NameForge:
    def __init__(self, world_seed: int, registry: Dict[str, str], profiles: List[NameProfile]):
        self.world_seed = world_seed
        self.registry = registry
        self.profiles = profiles

    def _rng_for(self, key: str) -> random.Random:
        # deterministic RNG per key
        h = hashlib.sha256(f"{self.world_seed}::{key}".encode("utf-8")).hexdigest()
        seed_int = int(h[:16], 16)
        return random.Random(seed_int)

    def get(self, key: str, style: str = "auto", cap: bool = True) -> str:
        # key: stable ID like "planet:core", "region:R1", "settlement:S4", "faction:F2", etc.
        if key in self.registry:
            return self.registry[key]

        rng = self._rng_for(key)

        if style == "auto":
            profile = rng.choice(self.profiles)
        else:
            profile = next((p for p in self.profiles if p.name == style), rng.choice(self.profiles))

        # generate syllables
        for _ in range(400):
            syl = rng.randint(2, 4)
            parts = []
            for _i in range(syl):
                onset = rng.choice(profile.onsets)
                nuc = rng.choice(profile.nuclei)
                coda = rng.choice(profile.codas) if rng.random() < 0.7 else ""
                parts.append(onset + nuc + coda)
