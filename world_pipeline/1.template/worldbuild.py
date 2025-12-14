from __future__ import annotations
# ============================================================
# Main execution block
# ============================================================

if __name__ == "__main__":
    import sys
    seed = random.randint(1, 1_000_000)
    if len(sys.argv) > 1:
        try:
            seed = int(sys.argv[1])
        except Exception:
            pass
    profiles = build_profiles()
    name_registry = {}
    namer = NameForge(seed, name_registry, profiles)
    # Generate a planet name
    planet_name = namer.get("planet:core")
    # Create output directory
    out_dir = ensure_unique_dir(PIPELINE_DIR / safe_filename(planet_name))
    # Write a simple world_bible.md as proof of generation
    with open(out_dir / "world_bible.md", "w", encoding="utf-8") as f:
        f.write(f"# {planet_name} World Bible\n\n")
        f.write(f"Seed: {seed}\n")
        f.write(f"Generated at: {dt.datetime.now().isoformat()}\n")
    print(f"World generated: {planet_name}\nOutput folder: {out_dir}")
"""
Worldbuilder v2.0 — Ghostwriter-ready world compendium + stable NameForge

Outputs (in a folder named after the world):
- world_bible.md              (polished compendium)
- canon.json                  (full structured data + name registry)
- map_graph.dot               (route graph for visualization)
- naming.py                   (CLI + helper to generate consistent new names later)
- build_meta.json             (seed, timestamps, coherence scores)

Hard requirements implemented:
- Output folder is created under:
    I:\\My Drive\\Worldbuilding\\world_pipeline\\<WorldName>
- Folder name is the generated world name (safe-cleaned). If exists -> suffix __2, __3...
- Naming is deterministic per world + key, and registry is persisted for expansions.
- Pronounceability gate + language-ish profiles (phoneme sets inspired by real languages).



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
    """
    Keep it human-readable for folder names, not aggressive URL slugging.
    - trims
    - removes forbidden Windows path characters
    - collapses whitespace
    """
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
    """
    These aren't literal language models; they're *phonotactic moods* inspired by
    real inventories (Celtic-ish / Slavic-ish / Romance-ish) without copying a language.
    """
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
        """
        key: stable ID like "planet:core", "region:R1", "settlement:S4", "faction:F2", etc.
        """
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
