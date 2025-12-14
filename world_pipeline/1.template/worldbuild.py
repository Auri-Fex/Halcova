<FULL SCRIPT FROM USER'S LATEST MESSAGE>
        },
    }

# ----------------------------
# Output directory logic
# ----------------------------
def get_output_dir(planet_name: str) -> Path:
    """Create and return the output directory for the generated world."""
    base_dir = Path(__file__).parent.parent / "world_pipeline"
    folder_name = slugify(planet_name)
    output_dir = base_dir / folder_name
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir



##############################
# Minimal NAMING_PROFILES dict
##############################
NAMING_PROFILES = {
    "slavic_soft": {
        "templates": ["CVCV", "CVCCV", "CVVCV"],
        "digraphs": ["ch", "sh", "zh", "ts", "dz", "kh", "ph", "th"],
        "consonants": list("bcdfghjklmnpqrstvwxyz"),
        "vowels": list("aeiouy"),
    },
    # Add more profiles as needed
}


# ----------------------------
# NameForge class definition (moved up)
# ----------------------------
class NameForge:
    def __init__(self, world_seed: int, cfg: Dict, registry: Dict[str, str]):
        self.world_seed = world_seed
        self.cfg = cfg.get("naming", {})
        self.profile_name = self.cfg.get("profile", "slavic_soft")
        if self.profile_name not in NAMING_PROFILES:
            self.profile_name = "slavic_soft"
        self.profile = NAMING_PROFILES[self.profile_name]
        self.max_cluster = int(self.cfg.get("max_cluster", 2))
        self.min_vowel_spacing = int(self.cfg.get("min_vowel_spacing", 4))
        self.semantic_names = bool(self.cfg.get("semantic_names", True))
        self.use_dialects = bool(self.cfg.get("dialects", True))
        self.entity_syllables = self.cfg.get("entity_syllables", {
            "planet": [3, 4],
            "region": [2, 3],
            "settlement": [2, 3],
            "polity": [2, 4],
            "faction": [2, 4],
        })
        self.registry = registry

    def name(self, entity: str, key: str, meaning: Optional[List[str]] = None,
             region_id: Optional[str] = None, polity_id: Optional[str] = None) -> str:
        reg_key = f"{entity}:{key}"
        if reg_key in self.registry:
            return self.registry[reg_key]

        rng = random.Random(self.world_seed)
        # For simplicity, just return a dummy name for now
        name = f"{entity}_{key}"
        self.registry[reg_key] = name
        return name

# ----------------------------
# Generator function definitions (moved up)
# ----------------------------
def gen_planet(rng: random.Random, cfg: Dict, namer: NameForge) -> Planet:
    realism = cfg.get("realism_target", "high")
    if realism == "high":
        g = clamp(rng.gauss(1.02, 0.08), 0.85, 1.25)
        day = clamp(rng.gauss(24.0, 2.0), 18.0, 34.0)
        year = int(clamp(rng.gauss(360, 30), 280, 380))
        tilt = clamp(rng.gauss(22, 6), 5, 35)
    else:
        g = clamp(rng.gauss(1.1, 0.2), 0.6, 1.6)
        day = clamp(rng.gauss(26, 6), 12, 60)
        year = int(clamp(rng.gauss(420, 80), 180, 900))
        tilt = clamp(rng.gauss(28, 10), 0, 60)

    name = namer.name("planet", "world", ["reach"])
    notes = [
        f"Day length is {day:.1f} hours; watch schedules and night travel rules matter.",
        f"Year length is {year} days; seasonal taxes and supply cycles are explicit.",
        f"Gravity ~{g:.2f}g; load limits and fatigue show up in logistics.",
    ]
    return Planet(
        name=name,
        gravity_g=float(f"{g:.2f}"),
        day_hours=float(f"{day:.1f}"),
        year_days=year,
        axial_tilt_deg=float(f"{tilt:.1f}"),
        notes=notes
    )

def gen_regions(rng: random.Random, cfg: Dict, namer: NameForge) -> Dict[str, Region]:
    # ...existing code...
    pass

def gen_settlements(rng: random.Random, cfg: Dict, regions: Dict[str, Region], namer: NameForge) -> Dict[str, Settlement]:
    # ...existing code...
    pass

def gen_routes(rng: random.Random, settlements: Dict[str, Settlement], regions: Dict[str, Region]) -> List[Route]:
    # ...existing code...
    pass

def gen_resources(rng: random.Random, regions: Dict[str, Region]) -> List[str]:
    # ...existing code...
    pass

def gen_polities(rng: random.Random, cfg: Dict, settlements: Dict[str, Settlement], regions: Dict[str, Region], resources: List[str], namer: NameForge) -> Dict[str, Polity]:
    # ...existing code...
    pass

def gen_factions(rng: random.Random, polities: Dict[str, Polity], resources: List[str], namer: NameForge) -> Dict[str, Faction]:
    # ...existing code...
    pass

def gen_magic(rng: random.Random, cfg: Dict) -> MagicSystem:
    # ...existing code...
    pass

def gen_timeline(rng: random.Random, cfg: Dict, polities: Dict[str, Polity], resources: List[str]) -> List[Event]:
    # ...existing code...
    pass

# ----------------------------
# Main execution block (single, at end of file)
# ----------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Worldbuilder: Generate a world compendium.")
    parser.add_argument("--seed", type=int, default=None, help="Random seed for reproducibility.")
    args = parser.parse_args()

    # Config and seed
    cfg = default_config(args.seed)
    seed = cfg["seed"]
    rng = random.Random(seed)
    name_registry = {}
    namer = NameForge(seed, cfg, name_registry)

    # Generate world
    planet = gen_planet(rng, cfg, namer)
    regions = gen_regions(rng, cfg, namer)
    settlements = gen_settlements(rng, cfg, regions, namer)
    routes = gen_routes(rng, settlements, regions)
    resources = gen_resources(rng, regions)
    polities = gen_polities(rng, cfg, settlements, regions, resources, namer)
    factions = gen_factions(rng, polities, resources, namer)
    magic = gen_magic(rng, cfg)
    timeline = gen_timeline(rng, cfg, polities, resources)
    # (conflicts, story, etc. can be added as needed)

    # Compose world object
    world = World(
        seed=seed,
        config=cfg,
        planet=planet,
        regions=regions,
        settlements=settlements,
        routes=routes,
        polities=polities,
        factions=factions,
        magic=magic,
        timeline=timeline,
        conflicts=[],
        story=StoryKit(
            themes=cfg.get("themes", []),
            tone=cfg.get("tone", ""),
            story_type=cfg.get("story_type", ""),
            default_scene_locations=[],
            hooks=[],
        ),
        receipts=[],
        name_registry=name_registry,
    )

    # Create output directory
    output_dir = get_output_dir(planet.name)

    # Write outputs
    with open(output_dir / "world_bible.md", "w", encoding="utf-8") as f:
        f.write(f"# {planet.name} World Bible\n\n")
        f.write(f"## Planetary Data\n{planet}\n\n")
        # (Add more sections as needed)

    with open(output_dir / "canon.json", "w", encoding="utf-8") as f:
        json.dump(asdict(world), f, indent=2, ensure_ascii=False)

    print(f"World generated: {planet.name}\nOutput folder: {output_dir}")

"""
Worldbuilder v1.3 — NameForge + World-Named Folders

Generates a ghostwriter-ready world compendium with:
- planet + calendar
- regions, settlements, routes (connected graph)
- polities + trade baskets + institutions/laws
- factions
- magic system (optional) with costs + countermeasures + second-order effects
- causal-ish timeline
- active conflicts + story hooks
- validators + basic repair loop
- exports: world_bible.md, world_bible.pdf (optional), canon.json, map_graph.dot

Key behavior:
- Output folder is named after the generated planet/world (slugified),
  and created directly under the world_pipeline folder (one level up from this script's folder by default).
"""

import argparse
import json
import math
import random
import hashlib

from dataclasses import dataclass, asdict, field
from datetime import date
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# ----------------------------
# Output directory logic
# ----------------------------
def get_output_dir(planet_name: str) -> Path:
    """Create and return the output directory for the generated world."""
    base_dir = Path(__file__).parent.parent / "world_pipeline"
    folder_name = slugify(planet_name)
    output_dir = base_dir / folder_name
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir


# ----------------------------
# Output directory logic
# ----------------------------
def get_output_dir(planet_name: str) -> Path:
    """Create and return the output directory for the generated world."""
    base_dir = Path(__file__).parent.parent / "world_pipeline"
    folder_name = slugify(planet_name)
    output_dir = base_dir / folder_name
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir

# ----------------------------
# Main execution block
# ----------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Worldbuilder: Generate a world compendium.")
    parser.add_argument("--seed", type=int, default=None, help="Random seed for reproducibility.")
    args = parser.parse_args()

    # Config and seed
    cfg = default_config(args.seed)
    seed = cfg["seed"]
    rng = random.Random(seed)
    name_registry = {}
    namer = NameForge(seed, cfg, name_registry)

    # Generate world
    planet = gen_planet(rng, cfg, namer)
    regions = gen_regions(rng, cfg, namer)
    settlements = gen_settlements(rng, cfg, regions, namer)
    routes = gen_routes(rng, settlements, regions)
    resources = gen_resources(rng, regions)
    polities = gen_polities(rng, cfg, settlements, regions, resources, namer)
    factions = gen_factions(rng, polities, resources, namer)
    magic = gen_magic(rng, cfg)
    timeline = gen_timeline(rng, cfg, polities, resources)
    # (conflicts, story, etc. can be added as needed)

    # Compose world object
    world = World(
        seed=seed,
        config=cfg,
        planet=planet,
        regions=regions,
        settlements=settlements,
        routes=routes,
        polities=polities,
        factions=factions,
        magic=magic,
        timeline=timeline,
        conflicts=[],
        story=StoryKit(
            themes=cfg.get("themes", []),
            tone=cfg.get("tone", ""),
            story_type=cfg.get("story_type", ""),
            default_scene_locations=[],
            hooks=[],
        ),
        receipts=[],
        name_registry=name_registry,
    )

    # Create output directory
    output_dir = get_output_dir(planet.name)

    # Write outputs
    with open(output_dir / "world_bible.md", "w", encoding="utf-8") as f:
        f.write(f"# {planet.name} World Bible\n\n")
        f.write(f"## Planetary Data\n{planet}\n\n")
        # (Add more sections as needed)

    with open(output_dir / "canon.json", "w", encoding="utf-8") as f:
        json.dump(asdict(world), f, indent=2, ensure_ascii=False)

    print(f"World generated: {planet.name}\nOutput folder: {output_dir}")



# ----------------------------
# Utilities
# ----------------------------

SEASONS = ["Thaw", "Bloom", "Highsun", "Harvest", "Sootfall", "Deepfrost"]

VOWELS = set("aeiouy")

def clamp(v: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, v))

def dist(a: Tuple[float, float], b: Tuple[float, float]) -> float:
    return math.hypot(a[0] - b[0], a[1] - b[1])

def weighted_choice(rng: random.Random, items: List[Tuple[str, float]]) -> str:
    pass  # ...existing code...
# ----------------------------
# Output directory logic
# ----------------------------
def get_output_dir(planet_name: str) -> Path:
    """Create and return the output directory for the generated world."""
    base_dir = Path(__file__).parent.parent / "world_pipeline"
    folder_name = slugify(planet_name)
    output_dir = base_dir / folder_name
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir

# ----------------------------
# Main execution block
# ----------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Worldbuilder: Generate a world compendium.")
    parser.add_argument("--seed", type=int, default=None, help="Random seed for reproducibility.")
    args = parser.parse_args()

    # Config and seed
    cfg = default_config(args.seed)
    seed = cfg["seed"]
    rng = random.Random(seed)
    name_registry = {}
    namer = NameForge(seed, cfg, name_registry)

    # Generate world
    planet = gen_planet(rng, cfg, namer)
    regions = gen_regions(rng, cfg, namer)
    settlements = gen_settlements(rng, cfg, regions, namer)
    routes = gen_routes(rng, settlements, regions)
    resources = gen_resources(rng, regions)
    polities = gen_polities(rng, cfg, settlements, regions, resources, namer)
    factions = gen_factions(rng, polities, resources, namer)
    magic = gen_magic(rng, cfg)
    timeline = gen_timeline(rng, cfg, polities, resources)
    # (conflicts, story, etc. can be added as needed)

    # Compose world object
    world = World(
        seed=seed,
        config=cfg,
        planet=planet,
        regions=regions,
        settlements=settlements,
        routes=routes,
        polities=polities,
        factions=factions,
        magic=magic,
        timeline=timeline,
        conflicts=[],
        story=StoryKit(
            themes=cfg.get("themes", []),
            tone=cfg.get("tone", ""),
            story_type=cfg.get("story_type", ""),
            default_scene_locations=[],
            hooks=[],
        ),
        receipts=[],
        name_registry=name_registry,
    )

    # Create output directory
    output_dir = get_output_dir(planet.name)

    # Write outputs
    with open(output_dir / "world_bible.md", "w", encoding="utf-8") as f:
        f.write(f"# {planet.name} World Bible\n\n")
        f.write(f"## Planetary Data\n{planet}\n\n")
        # (Add more sections as needed)

    with open(output_dir / "canon.json", "w", encoding="utf-8") as f:
        json.dump(asdict(world), f, indent=2, ensure_ascii=False)

    print(f"World generated: {planet.name}\nOutput folder: {output_dir}")

    # ----------------------------
    # Main execution block
    # ----------------------------
    if __name__ == "__main__":
        parser = argparse.ArgumentParser(description="Worldbuilder: Generate a world compendium.")
        parser.add_argument("--seed", type=int, default=None, help="Random seed for reproducibility.")
        args = parser.parse_args()

        # Config and seed
        cfg = default_config(args.seed)
        seed = cfg["seed"]
        rng = random.Random(seed)
        name_registry = {}
        namer = NameForge(seed, cfg, name_registry)

        # Generate world
        planet = gen_planet(rng, cfg, namer)
        regions = gen_regions(rng, cfg, namer)
        settlements = gen_settlements(rng, cfg, regions, namer)
        routes = gen_routes(rng, settlements, regions)
        resources = gen_resources(rng, regions)
        polities = gen_polities(rng, cfg, settlements, regions, resources, namer)
        factions = gen_factions(rng, polities, resources, namer)
        magic = gen_magic(rng, cfg)
        timeline = gen_timeline(rng, cfg, polities, resources)
        # (conflicts, story, etc. can be added as needed)

        # Compose world object
        world = World(
            seed=seed,
            config=cfg,
            planet=planet,
            regions=regions,
            settlements=settlements,
            routes=routes,
            polities=polities,
            factions=factions,
            magic=magic,
            timeline=timeline,
            conflicts=[],
            story=StoryKit(
                themes=cfg.get("themes", []),
                tone=cfg.get("tone", ""),
                story_type=cfg.get("story_type", ""),
                default_scene_locations=[],
                hooks=[],
            ),
            receipts=[],
            name_registry=name_registry,
        )

        # Create output directory
        output_dir = get_output_dir(planet.name)

        # Write outputs
        with open(output_dir / "world_bible.md", "w", encoding="utf-8") as f:
            f.write(f"# {planet.name} World Bible\n\n")
            f.write(f"## Planetary Data\n{planet}\n\n")
            # (Add more sections as needed)

        with open(output_dir / "canon.json", "w", encoding="utf-8") as f:
            json.dump(asdict(world), f, indent=2, ensure_ascii=False)

        print(f"World generated: {planet.name}\nOutput folder: {output_dir}")
SEMANTIC_MORPHEMES = {
    "river": ["riv", "ran", "dun", "mor"],
    "ford": ["vad", "vad", "vad", "ford"],
    "hill": ["col", "mon", "bryn"],
    "marsh": ["fen", "mor", "sog"],
    "forest": ["sil", "bosc", "lis"],
    "coast": ["mar", "cost", "port"],
    "port": ["port", "har", "mar"],
    "fort": ["gar", "kast", "tor"],
    "market": ["merk", "baz", "sal"],
    "stone": ["kar", "ston", "skal"],
    "salt": ["sal", "hal", "mor"],
    "iron": ["fer", "irn", "stal"],
    "horses": ["hip", "ros", "cab"],
    "temple": ["templ", "san", "kir"],
    "league": ["lig", "kon", "kom"],
    "reach": ["riv", "march", "step"],
}

PIPELINE_OUTCOMES = {
    "bribery": "quiet bribe routes",
    "blackmail": "blackmail dossiers",
    "public charity": "patronage lists",
    "targeted violence": "hired knives",
    "bureaucratic sabotage": "buried permits",
    "propaganda": "pamphlet presses",
    "trade embargo": "choked trade ledgers",
    "strike action": "coordinated walkouts",
}

def is_vowel(ch: str) -> bool:
    return ch.lower() in VOWELS

def pronounceable(s: str, max_cluster: int, min_vowel_spacing: int, forbid: List[str]) -> bool:
    cluster = 0
    last_vowel_idx = -999
    for i, ch in enumerate(s.lower()):
        if ch.isalpha() and not is_vowel(ch):
            cluster += 1
            if cluster > max_cluster:
                return False
        else:
            cluster = 0
            last_vowel_idx = i
        if i - last_vowel_idx >= min_vowel_spacing:
            return False
    lower = s.lower()
    for bad in forbid:
        if bad in lower:
            return False
    return True

class NameForge:
    def __init__(self, world_seed: int, cfg: Dict, registry: Dict[str, str]):
        self.world_seed = world_seed
        self.cfg = cfg.get("naming", {})
        self.profile_name = self.cfg.get("profile", "slavic_soft")
        if self.profile_name not in NAMING_PROFILES:
            self.profile_name = "slavic_soft"
        self.profile = NAMING_PROFILES[self.profile_name]
        self.max_cluster = int(self.cfg.get("max_cluster", 2))
        self.min_vowel_spacing = int(self.cfg.get("min_vowel_spacing", 4))
        self.semantic_names = bool(self.cfg.get("semantic_names", True))
        self.use_dialects = bool(self.cfg.get("dialects", True))
        self.entity_syllables = self.cfg.get("entity_syllables", {
            "planet": [3, 4],
            "region": [2, 3],
            "settlement": [2, 3],
            "polity": [2, 4],
            "faction": [2, 4],
        })
        self.registry = registry

    def _rng_for(self, entity: str, key: str, meaning: Optional[List[str]]) -> random.Random:
        payload = f"{self.world_seed}|{self.profile_name}|{entity}|{key}|{','.join(sorted(meaning or []))}"
        h = hashlib.sha256(payload.encode("utf-8")).hexdigest()
        seed = int(h[:16], 16)
        return random.Random(seed)

    def _base_syllable(self, rng: random.Random) -> str:
        p = self.profile
        tmpl = rng.choice(p["templates"])
        s = ""
        i = 0
        while i < len(tmpl):
            t = tmpl[i]
            if t == "C":
                if rng.random() < 0.25 and p["digraphs"]:
                    s += rng.choice(p["digraphs"])
                else:
                    s += rng.choice(p["consonants"])
            elif t == "V":
                s += rng.choice(p["vowels"])
            else:
                s += t
            i += 1
        return s

    def _apply_dialect(self, text: str, region_id: Optional[str], polity_id: Optional[str]) -> str:
        if not self.use_dialects:
            return text
        key = region_id or polity_id
        if not key:
            return text
        h = hashlib.sha256(f"dialect|{key}".encode("utf-8")).hexdigest()
        code = int(h[:2], 16) % 3
        s = text

        if code == 0:
            s = s.replace("ar", "air")
            s = s.replace("or", "oar")
        elif code == 1:
            out = []
            for i, ch in enumerate(s):
                if ch.lower() in "td" and i > 0 and is_vowel(s[i - 1]):
                    out.append(ch + "h")
                else:
                    out.append(ch)
            s = "".join(out)
        elif code == 2:
            s = s.replace("th", "t").replace("dh", "d").replace("hh", "h")

        return s

    def _pick_morphemes(self, rng: random.Random, meaning: Optional[List[str]], syllable_range: Tuple[int, int]) -> List[str]:
        if not self.semantic_names or not meaning:
            n = rng.randint(syllable_range[0], syllable_range[1])
            return [self._base_syllable(rng) for _ in range(n)]

        chunks: List[str] = []
        for tag in meaning:
            forms = SEMANTIC_MORPHEMES.get(tag)
            if forms:
                chunks.append(rng.choice(forms))
        if not chunks:
            n = rng.randint(syllable_range[0], syllable_range[1])
            return [self._base_syllable(rng) for _ in range(n)]

        if rng.random() < 0.55:
            chunks.insert(0, self._base_syllable(rng))
        return chunks

    def _shape_name(self, raw: str, rng: random.Random) -> str:
        if len(raw) > 10:
            raw = raw[:10]
        if rng.random() < 0.7 and self.profile["nice_endings"]:
            end = rng.choice(self.profile["nice_endings"])
            if not raw.endswith(end):
                raw = raw + end
        for rep in ["aa", "ee", "ii", "oo", "uu"]:
            while rep in raw:
                raw = raw.replace(rep, rep[0])
        return raw.capitalize()

    def name(self, entity: str, key: str, meaning: Optional[List[str]] = None,
             region_id: Optional[str] = None, polity_id: Optional[str] = None) -> str:
        reg_key = f"{entity}:{key}"
        if reg_key in self.registry:
            return self.registry[reg_key]

        rng = self._rng_for(entity, key, meaning)
        syllable_range = self.entity_syllables.get(entity, [2, 3])
        lo, hi = int(syllable_range[0]), int(syllable_range[1])

        max_cluster = self.max_cluster
        min_vowel_spacing = self.min_vowel_spacing
        forbid = self.profile["forbid"]

        for _ in range(32):
            chunks = self._pick_morphemes(rng, meaning, (lo, hi))
            raw = "".join(chunks)
            raw = self._apply_dialect(raw, region_id, polity_id)
            cand = self._shape_name(raw, rng)

            key_stripped = "".join(ch.lower() for ch in cand if ch.isalpha())
            if not pronounceable(key_stripped, max_cluster, min_vowel_spacing, forbid):
                continue

            if cand in self.registry.values():
                continue

            self.registry[reg_key] = cand
            return cand

        cand = self._shape_name("".join(self._pick_morphemes(rng, None, (lo, hi))), rng)
        self.registry[reg_key] = cand
        return cand

# ----------------------------
# Survey defaults → config
# ----------------------------

def default_config(seed: Optional[int] = None) -> Dict:
    return {
        "seed": seed if seed is not None else random.randint(1, 1_000_000),
        "tone": "grounded-dark",
        "realism_target": "high",
        "scale": "continent",
        "story_type": "political-intrigue",
        "tech_level": "late-medieval",
        "magic_presence": "rare",
        "magic_hardness": "hard",
        "themes": ["scarcity", "institutional-rot", "moral-tradeoffs", "duty-vs-love"],
        "no_go": ["prophecy-solves-everything", "free-energy-magic", "omniscient-gods"],
        "inspirations": ["ports-and-chokepoints", "winter-pressure", "guild-law", "border-marches"],
        "naming": {
            "profile": "slavic_soft",
            "max_cluster": 2,
            "min_vowel_spacing": 4,
            "entity_syllables": {
                "planet": [3, 4],
                "region": [2, 3],
                "settlement": [2, 3],
                "polity": [2, 4],
                "faction": [2, 4]
            },
            "semantic_names": True,
            "dialects": True
        },
    }

# ----------------------------
# Generation
# ----------------------------

def gen_planet(rng: random.Random, cfg: Dict, namer: NameForge) -> Planet:
    realism = cfg.get("realism_target", "high")
    if realism == "high":
        g = clamp(rng.gauss(1.02, 0.08), 0.85, 1.25)
        day = clamp(rng.gauss(24.0, 2.0), 18.0, 34.0)
        year = int(clamp(rng.gauss(360, 30), 280, 380))
        tilt = clamp(rng.gauss(22, 6), 5, 35)
    else:
        g = clamp(rng.gauss(1.1, 0.2), 0.6, 1.6)
        day = clamp(rng.gauss(26, 6), 12, 60)
        year = int(clamp(rng.gauss(420, 80), 180, 900))
        tilt = clamp(rng.gauss(28, 10), 0, 60)

    name = namer.name("planet", "world", ["reach"])
    notes = [
        f"Day length is {day:.1f} hours; watch schedules and night travel rules matter.",
        f"Year length is {year} days; seasonal taxes and supply cycles are explicit.",
        f"Gravity ~{g:.2f}g; load limits and fatigue show up in logistics.",
    ]
    return Planet(
        name=name,
        gravity_g=float(f"{g:.2f}"),
        day_hours=float(f"{day:.1f}"),
        year_days=year,
        axial_tilt_deg=float(f"{tilt:.1f}"),
        notes=notes
    )

def gen_regions(rng: random.Random, cfg: Dict, namer: NameForge) -> Dict[str, Region]:
    biomes = ["temperate-coast", "steppe-marches", "wet-highlands", "river-delta", "cold-north", "dry-basin", "forest-belt"]
    hazards_pool = ["banditry", "storm-surge", "flooding", "late-frost", "blight", "salt-winds", "rockslide", "sea-raiders", "fever-marsh"]

    base = rng.randint(5, 7) if cfg.get("scale") in ("continent", "large-region") else rng.randint(3, 5)
    regions: Dict[str, Region] = {}

    for i in range(base):
        rid = f"R{i+1}"
        biome = rng.choice(biomes)
        meaning: List[str] = []
        if "coast" in biome:
            meaning = ["coast", "reach"]
        elif "river" in biome:
            meaning = ["river", "reach"]
        elif "steppe" in biome or "basin" in biome:
            meaning = ["reach"]
        elif "forest" in biome:
            meaning = ["forest", "reach"]
        elif "cold" in biome:
            meaning = ["hill", "reach"]
        name = namer.name("region", rid, meaning)
        hazards = rng.sample(hazards_pool, k=rng.randint(2, 3))
        regions[rid] = Region(id=rid, name=f"{name} Reach", biome=biome, hazards=hazards, resources=[], notes=[])

    return regions

def gen_settlements(rng: random.Random, cfg: Dict, regions: Dict[str, Region], namer: NameForge) -> Dict[str, Settlement]:
    n = rng.randint(14, 22) if cfg.get("scale") == "continent" else rng.randint(8, 14)
    kinds = [("hamlet", 0.18), ("village", 0.27), ("town", 0.28), ("city", 0.16), ("fort", 0.06), ("port", 0.05)]

    settlements: Dict[str, Settlement] = {}
    region_ids = list(regions.keys())

    for i in range(n):
        sid = f"S{i+1}"
        kind = weighted_choice(rng, kinds)
        if kind == "hamlet":
            pop = int(clamp(rng.gauss(120, 60), 40, 350))
        elif kind == "village":
            pop = int(clamp(rng.gauss(550, 250), 180, 1400))
        elif kind == "town":
            pop = int(clamp(rng.gauss(4500, 1800), 1600, 9000))
        elif kind == "city":
            pop = int(clamp(rng.gauss(24000, 9000), 12000, 60000))
        elif kind == "fort":
            pop = int(clamp(rng.gauss(900, 450), 250, 2800))
        else:  # port
            pop = int(clamp(rng.gauss(14000, 6000), 6000, 42000))

        region_id = rng.choice(region_ids)
        x, y = rng.random() * 100.0, rng.random() * 100.0

        meaning: List[str] = []
        if kind == "port":
            meaning = ["port", "coast"]
        elif kind == "fort":
            meaning = ["fort"]
        elif kind in ("town", "city"):
            meaning = ["market"]
        name = namer.name("settlement", sid, meaning, region_id=region_id)

        tags: List[str] = []
        if kind == "port":
            tags.append("coastal")
        if rng.random() < 0.18:
            tags.append("holy-site")
        if rng.random() < 0.16:
            tags.append("guild-stronghold")

        settlements[sid] = Settlement(
            id=sid, name=name, kind=kind, population=pop,
            region_id=region_id, x=x, y=y, tags=tags
        )

    return settlements

def gen_routes(rng: random.Random, settlements: Dict[str, Settlement], regions: Dict[str, Region]) -> List[Route]:
    nodes = {sid: (s.x, s.y) for sid, s in settlements.items()}
    edges = nearest_neighbor_graph(nodes, rng)
    routes: List[Route] = []
    risk_levels = [("low", 0.45), ("medium", 0.40), ("high", 0.15)]

    for a, b in edges:
        sa, sb = settlements[a], settlements[b]
        km = dist((sa.x, sa.y), (sb.x, sb.y)) * 12.0

        if "coastal" in sa.tags and "coastal" in sb.tags and km > 220:
            mode = "sea"
        else:
            mode = "road"

        if (regions[sa.region_id].biome in ("river-delta", "wet-highlands")
            and regions[sb.region_id].biome in ("river-delta", "wet-highlands")
            and rng.random() < 0.25):
            mode = "river"

        risk = weighted_choice(rng, risk_levels)
        routes.append(Route(a=a, b=b, km=float(f"{km:.1f}"), mode=mode, risk=risk))

    return routes

def gen_resources(rng: random.Random, regions: Dict[str, Region]) -> List[str]:
    pool = [
        "grain", "salt", "iron", "timber", "wool", "stone", "fish", "horses", "amber",
        "spices", "copper", "glass-sand", "dye-moss", "flax", "coal", "silver", "wine"
    ]
    must = ["grain", "salt", "timber", "iron"]
    rest = [p for p in pool if p not in must]
    rng.shuffle(rest)
    picked = must + rest[:rng.randint(5, 7)]

    for r in regions.values():
        r.resources = []

    for res in picked:
        targets = rng.sample(list(regions.keys()), k=1 if rng.random() < 0.7 else 2)
        for rid in targets:
            if res not in regions[rid].resources:
                regions[rid].resources.append(res)

    fallback_res = "subsistence-grain"
    for r in regions.values():
        if not r.resources:
            r.resources.append(fallback_res)
            if fallback_res not in picked:
                picked.append(fallback_res)

    return picked

def pick_capital(rng: random.Random, settlements: Dict[str, Settlement]) -> str:
    cands: List[Tuple[str, float]] = []
    for s in settlements.values():
        w = 1.0
        if s.kind in ("city", "port"):
            w = 4.0
        elif s.kind == "town":
            w = 2.0
        elif s.kind == "fort":
            w = 1.5
        cands.append((s.id, w))
    return weighted_choice(rng, cands)

def assign_polity_membership(settlements: Dict[str, Settlement], capitals: List[str]) -> Dict[str, str]:
    cap_xy = {cid: (settlements[cid].x, settlements[cid].y) for cid in capitals}
    membership: Dict[str, str] = {}
    for sid, s in settlements.items():
        best = None
        best_d = 1e18
        for cid, xy in cap_xy.items():
            d = dist((s.x, s.y), xy)
            if d < best_d:
                best_d = d
                best = cid
        membership[sid] = best  # type: ignore[assignment]
    return membership

def gen_polities(
    rng: random.Random,
    cfg: Dict,
    settlements: Dict[str, Settlement],
    regions: Dict[str, Region],
    resources: List[str],
    namer: NameForge
) -> Dict[str, Polity]:
    k = rng.randint(3, 5) if cfg.get("scale") == "continent" else rng.randint(2, 3)

    capitals: List[str] = []
    used: set[str] = set()
    while len(capitals) < k:
        c = pick_capital(rng, settlements)
        if c not in used:
            capitals.append(c)
            used.add(c)

    membership = assign_polity_membership(settlements, capitals)

    govs = ["crowned-council", "merchant-republic", "temple-compact", "military-duchy", "charter-league"]
    ide_pool = ["order", "honor", "profit", "piety", "unity", "purity", "tradition", "reform", "autonomy", "mercy"]

    law_pool = [
        "Proof beats reputation in court; receipts and witnesses decide.",
        "Port tariffs fund winter grain reserves — audited by a rival office.",
        "Guild charters grant monopoly only with public quotas.",
        "Conscription limited to one season in three — exemptions must be stamped.",
        "Debt labor is legal only with a written sunset date and a witness mark.",
        "Relics may not be sold — only leased via temple bond."
    ]

    inst_pool = [
        "harbor office", "grain bureau", "guild tribunal",
        "border watch", "sanctuary clinics", "roadwardens", "mint commission"
    ]

    polities: Dict[str, Polity] = {}
    for i, cap_id in enumerate(capitals):
        pid = f"P{i+1}"
        government = rng.choice(govs)
        ideology = rng.sample(ide_pool, k=3)

        member_ids = [sid for sid, cap in membership.items() if cap == cap_id]
        pop = sum(settlements[sid].population for sid in member_ids)

        base_army = rng.uniform(0.02, 0.09) if government != "military-duchy" else rng.uniform(0.06, 0.14)
        army_pct = float(f"{base_army:.3f}")
        treasury = float(f"{rng.uniform(0.6, 1.4):.2f}")

        regs = {settlements[sid].region_id for sid in member_ids}
        available = set()
        for rid in regs:
            available |= set(regions[rid].resources)

        exports = sorted(
            rng.sample(list(available), k=min(len(available), rng.randint(2, 4)))
        ) if available else ["labor"]
        needs = [r for r in resources if r not in available]
        imports = sorted(
            rng.sample(needs, k=min(len(needs), rng.randint(2, 4)))
        ) if needs else ["luxury-goods"]

        name_meaning: List[str] = []
        if government in ("merchant-republic", "charter-league"):
            name_meaning = ["league"]
        elif "temple" in government:
            name_meaning = ["temple"]
        name = namer.name("polity", pid, name_meaning)

        laws = rng.sample(law_pool, k=3)
        inst = rng.sample(inst_pool, k=3)

        notes = [
            f"Capital is {settlements[cap_id].name}; legitimacy flows through {government.replace('-', ' ')} procedure.",
            f"Exports emphasize {', '.join(exports)}; imports rely on {', '.join(imports)}."
        ]

        polities[pid] = Polity(
            id=pid,
            name=f"{name} Dominion",
            capital_id=cap_id,
            government=government,
            ideology=ideology,
            population=pop,
            army_pct=army_pct,
            treasury_index=treasury,
            exports=exports,
            imports=imports,
            laws=laws,
            institutions=inst,
            notes=notes
        )

    return polities

def gen_factions(rng: random.Random, polities: Dict[str, Polity], resources: List[str], namer: NameForge) -> Dict[str, Faction]:
    ftypes = ["guild", "church-order", "intelligence-office", "rebel-cell", "noble-house", "mercenary-banner", "smugglers"]
    goal_pool = [
        "control tariffs", "break a monopoly", "protect pilgrims", "overthrow a regent", "legalize a banned rite",
        "secure grain reserves", "end conscription abuse", "corner the salt trade", "rewrite succession law"
    ]
    method_pool = ["bribery", "blackmail", "public charity", "targeted violence",
                   "bureaucratic sabotage", "propaganda", "trade embargo", "strike action"]

    def hook_for(name: str, method: str, res: str) -> List[str]:
        pipe = PIPELINE_OUTCOMES.get(method, "shadow operations")
        return [
            f"A stamped receipt proves {name} funds a 'charity' that is actually a pipeline for {pipe}.",
            f"A missing crate of {res} vanished on a route that {name} 'audits'."
        ]

    factions: Dict[str, Faction] = {}
    idx = 1

    polity_ids = list(polities.keys())
    for pid in polity_ids:
        for _ in range(random.randint(2, 3)):
            fid = f"F{idx}"
            idx += 1
            base = namer.name("faction", fid, ["market"])
            suffix = rng.choice(["Accord", "Cabal", "Ledger", "Host", "Covenant", "Office", "Banner"])
            name = f"{base} {suffix}"
            ftype = rng.choice(ftypes)
            goals = rng.sample(goal_pool, k=2)
            methods = rng.sample(method_pool, k=3)
            res = rng.sample(resources, k=2) + [ftype]
            hooks = hook_for(name, methods[0], rng.choice(resources))
            factions[fid] = Faction(
                id=fid, name=name, polity_id=pid, type=ftype,
                goals=goals, methods=methods, resources=res,
                enemies=[], allies=[], hooks=hooks
            )

    fid = f"F{idx}"
    base = namer.name("faction", fid, ["market"])
    suffix = random.choice(["Circuit", "Concord", "Undertide", "Else-Rail"])
    name = f"{base} {suffix}"
    factions[fid] = Faction(
        id=fid, name=name, polity_id=None, type=random.choice(ftypes),
        goals=["profit from conflict", "control a chokepoint archive"],
        methods=["forged stamps", "bribed roadwardens", "selective arson"],
        resources=[random.choice(resources), "maps", "false seals"],
        enemies=[], allies=[], hooks=[
            "Their courier carries two identical stamps — one real, one boneglass counterfeit.",
            "They can prove your ancestry — and they can also erase it."
        ]
    )

    fids = list(factions.keys())
    for f in factions.values():
        others = [x for x in fids if x != f.id]
        random.shuffle(others)
        f.allies = others[:random.randint(0, 2)]
        start = random.randint(2, 3)
        end = random.randint(4, 6)
        f.enemies = others[start:end]

    return factions

def gen_magic(rng: random.Random, cfg: Dict) -> MagicSystem:
    presence = cfg.get("magic_presence", "rare")
    hardness = cfg.get("magic_hardness", "hard")

    if presence == "none":
        return MagicSystem(
            presence="none", hardness=hardness,
            inputs=[], outputs=[], costs=[], failure_modes=[],
            countermeasures=[], second_order_effects=[],
            notes=["No verified magic; belief still shapes politics."]
        )

    inputs = ["rare reagents", "oaths spoken to witnesses", "glyphwork on boneglass", "blood-warm catalysts"] if hardness != "soft" else ["belief", "ritual", "sacrifice"]
    outputs = ["short-range warding", "truth-pressure in testimony", "localized distortion of sound/light", "binding a minor spirit into a tool"]
    costs = ["migraine debt", "scar tissue in the caster's hands", "collateral binding (someone else inherits a cost)", "legal liability (licensed only)"]
    failure = ["ward inversion", "false-positive truth reads", "runaway binding", "ritual backlash onto witnesses"]
    counters = ["seal-paste nulling", "iron-gall inks that resist glyphwork", "oath-auditors and receipts", "salt-thread boundaries"]
    effects = [
        "Courts demand receipts: a truth-rite is admissible only with witness marks and counter-seals.",
        "Insurance markets exist for licensed casters; premiums spike in flood season.",
        "Smuggling uses counterfeit seals and forced witnesses — creating a black market in testimony."
    ]
    notes = ["Magic is procedural and expensive; its biggest impact is institutional, not flashy combat."]

    return MagicSystem(
        presence=presence, hardness=hardness,
        inputs=inputs, outputs=outputs,
        costs=costs, failure_modes=failure,
        countermeasures=counters, second_order_effects=effects,
        notes=notes
    )

def gen_timeline(rng: random.Random, cfg: Dict, polities: Dict[str, Polity], resources: List[str]) -> List[Event]:
    start_year = -rng.randint(160, 260)
    end_year = 0
    n = rng.randint(55, 85) if cfg.get("scale") == "continent" else rng.randint(35, 55)

    templates = [
        ("Grain Shortage", ["blight", "late-frost", "war requisitions"], ["rationing stamps", "food riots", "new tariffs"]),
        ("Succession Crisis", ["sudden death", "forged lineage", "temple refusal"], ["border raids", "new regent law", "purges"]),
        ("Trade War", ["tariff hike", "seized caravan", "harbor blockade"], ["price spike", "smuggling boom", "treaty court"]),
        ("Flood Year", ["river overrun", "storm surge", "dam failure"], ["relocation", "new levee office", "disease wave"]),
        ("Border Campaign", ["raider season", "ideological split", "mercenary contract"], ["fort expansion", "debt taxes", "missing veterans"]),
        ("Relic Scandal", ["temple audit", "fake seals", "stolen relic"], ["public trial", "new seal standards", "assassination attempt"]),
    ]

    polity_names = [p.name for p in polities.values()]
    events: List[Event] = []

    roots = rng.randint(4, 7)
    for i in range(roots):
        title, _, cons = rng.choice(templates)
        eid = f"E{i+1}"
        year = start_year + int((i / max(1, roots - 1)) * (abs(start_year)))
        season = rng.choice(SEASONS)
        agents = rng.sample(polity_names, k=min(len(polity_names), rng.randint(1, 2)))
        c1 = rng.choice(cons)
        c2 = rng.choice(cons)
        if c2 == c1:
            c2 = rng.choice([x for x in cons if x != c1] or [c1])
        consequences = [c1, c2, f"{rng.choice(resources)} prices move for a decade"]
        events.append(Event(id=eid, year=year, season=season, title=title, cause_ids=[], agents=agents, consequences=consequences))

    for i in range(roots, n):
        title, _, cons = rng.choice(templates)
        eid = f"E{i+1}"
        cause = rng.choice(events)
        year = int(clamp(rng.gauss(cause.year + rng.randint(2, 18), 12), start_year, end_year))
        season = rng.choice(SEASONS)
        agents = rng.sample(polity_names, k=min(len(polity_names), rng.randint(1, 3)))
        c1 = rng.choice(cons)
        c2 = rng.choice(cons)
        if c2 == c1:
            c2 = rng.choice([x for x in cons if x != c1] or [c1])
