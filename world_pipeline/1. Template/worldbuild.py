"""
worldbuilding.py — Worldbuilder v1.1

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

Key behavior update:
- ALWAYS creates a NEW run folder inside --out_root (default points at your drive path)

Usage:
  python worldbuilding.py
  python worldbuilding.py --seed 42
  python worldbuilding.py --config config.json
  python worldbuilding.py --out_root "I:\My Drive\Worldbuilding\world_pipeline\1. template"
  python worldbuilding.py --run_name run_custom_001
"""

from __future__ import annotations

import argparse
import json
import math
import os
import random
from dataclasses import dataclass, asdict, field
from datetime import date, datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# ----------------------------
# Data model
# ----------------------------

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
    polity_id: Optional[str]  # None means cross-border
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
    receipts: List[str]  # why it exists / what makes it plausible

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

# ----------------------------
# Utilities
# ----------------------------

SEASONS = ["Thaw", "Bloom", "Highsun", "Harvest", "Sootfall", "Deepfrost"]

def clamp(v: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, v))

def dist(a: Tuple[float, float], b: Tuple[float, float]) -> float:
    return math.hypot(a[0] - b[0], a[1] - b[1])

def weighted_choice(rng: random.Random, items: List[Tuple[str, float]]) -> str:
    total = sum(w for _, w in items)
    x = rng.random() * total
    acc = 0.0
    for item, w in items:
        acc += w
        if x <= acc:
            return item
    return items[-1][0]

# Simple pseudo-phonotactics name generator
ON = ["b","br","d","dr","g","gr","k","kr","m","n","p","pr","r","s","t","tr","v","z","sh","ch","th","sk","st","vr"]
NUC = ["a","e","i","o","u","ae","ai","ea","ei","ia","io","oa","ou","ui"]
COD = ["n","m","r","s","th","k","l","nd","st","sh","rk","rt","rn","ld","lm","nt"]

def make_name(rng: random.Random, syllables: int = 2, cap: bool = True) -> str:
    parts = []
    for _ in range(syllables):
        on = rng.choice(ON)
        nu = rng.choice(NUC)
        co = rng.choice(COD) if rng.random() < 0.7 else ""
        parts.append(on + nu + co)
    name = "".join(parts).replace("aa","a").replace("ee","e").replace("ii","i").replace("oo","o").replace("uu","u")
    return name.capitalize() if cap else name

def nearest_neighbor_graph(nodes: Dict[str, Tuple[float, float]], rng: random.Random) -> List[Tuple[str, str]]:
    """Connected graph via Prim-ish MST, then add a few redundant edges."""
    ids = list(nodes.keys())
    if not ids:
        return []
    start = ids[0]
    visited = {start}
    edges: List[Tuple[str, str]] = []

    while len(visited) < len(ids):
        best = None
        best_d = 1e18
        for u in visited:
            for v in ids:
                if v in visited:
                    continue
                d = dist(nodes[u], nodes[v])
                if d < best_d:
                    best_d = d
                    best = (u, v)
        edges.append(best)  # type: ignore[arg-type]
        visited.add(best[1])  # type: ignore[index]

    extra = max(1, len(ids) // 5)
    for _ in range(extra):
        u = rng.choice(ids)
        candidates = sorted(
            [(dist(nodes[u], nodes[v]), v) for v in ids if v != u],
            key=lambda x: x[0]
        )[:4]
        v = rng.choice([c[1] for c in candidates])
        if (u, v) not in edges and (v, u) not in edges:
            edges.append((u, v))
    return edges

def dijkstra(adj: Dict[str, List[Tuple[str, float]]], src: str) -> Dict[str, float]:
    import heapq
    INF = 1e18
    dist_map = {k: INF for k in adj.keys()}
    dist_map[src] = 0.0
    pq = [(0.0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d != dist_map[u]:
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist_map[v]:
                dist_map[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist_map

def travel_days(km: float, mode: str) -> float:
    # Writer-plausible defaults (not a physics lecture)
    speed_km_per_day = {"road": 28.0, "river": 45.0, "sea": 110.0}
    return km / speed_km_per_day.get(mode, 28.0)

# ----------------------------
# Survey defaults → config
# ----------------------------

def default_config(seed: Optional[int] = None) -> Dict:
    return {
        "seed": seed if seed is not None else random.randint(1, 1_000_000),
        "tone": "grounded-dark",
        "realism_target": "high",             # high or pulp
        "scale": "continent",                 # continent or region
        "story_type": "political-intrigue",
        "tech_level": "late-medieval",
        "magic_presence": "rare",             # none, rare, common
        "magic_hardness": "hard",             # soft, medium, hard
        "themes": ["scarcity", "institutional-rot", "moral-tradeoffs", "duty-vs-love"],
        "no_go": ["prophecy-solves-everything", "free-energy-magic", "omniscient-gods"],
        "inspirations": ["ports-and-chokepoints", "winter-pressure", "guild-law", "border-marches"],
    }

# ----------------------------
# Generation
# ----------------------------

def gen_planet(rng: random.Random, cfg: Dict) -> Planet:
    name = make_name(rng, 3)
    realism = cfg.get("realism_target", "high")

    if realism == "high":
        g = clamp(rng.gauss(1.02, 0.08), 0.85, 1.25)
        day = clamp(rng.gauss(24.5, 2.0), 18.0, 34.0)
        year = int(clamp(rng.gauss(360, 30), 280, 520))
        tilt = clamp(rng.gauss(22, 6), 5, 35)
    else:
        g = clamp(rng.gauss(1.1, 0.2), 0.6, 1.6)
        day = clamp(rng.gauss(26, 6), 12, 60)
        year = int(clamp(rng.gauss(420, 80), 180, 900))
        tilt = clamp(rng.gauss(28, 10), 0, 60)

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

def gen_regions(rng: random.Random, cfg: Dict) -> Dict[str, Region]:
    biomes = ["temperate-coast", "steppe-marches", "wet-highlands", "river-delta", "cold-north", "dry-basin", "forest-belt"]
    hazards_pool = ["banditry", "storm-surge", "flooding", "late-frost", "blight", "salt-winds", "rockslide", "sea-raiders", "fever-marsh"]

    base = rng.randint(5, 7) if cfg.get("scale") in ("continent", "large-region") else rng.randint(3, 5)
    regions: Dict[str, Region] = {}

    for i in range(base):
        rid = f"R{i+1}"
        name = make_name(rng, 2) + " Reach"
        biome = rng.choice(biomes)
        hazards = rng.sample(hazards_pool, k=rng.randint(2, 3))
        regions[rid] = Region(id=rid, name=name, biome=biome, hazards=hazards, resources=[], notes=[])

    return regions

def gen_settlements(rng: random.Random, cfg: Dict, regions: Dict[str, Region]) -> Dict[str, Settlement]:
    n = rng.randint(14, 22) if cfg.get("scale") == "continent" else rng.randint(8, 14)
    kinds = [("hamlet", 0.18), ("village", 0.27), ("town", 0.28), ("city", 0.16), ("fort", 0.06), ("port", 0.05)]

    settlements: Dict[str, Settlement] = {}
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

        region_id = rng.choice(list(regions.keys()))
        x, y = rng.random() * 100.0, rng.random() * 100.0
        name = make_name(rng, 2)

        tags: List[str] = []
        if kind == "port":
            tags.append("coastal")
        if rng.random() < 0.18:
            tags.append("holy-site")
        if rng.random() < 0.16:
            tags.append("guild-stronghold")

        settlements[sid] = Settlement(
            id=sid, name=name, kind=kind, population=pop, region_id=region_id, x=x, y=y, tags=tags
        )

    return settlements

def gen_routes(rng: random.Random, settlements: Dict[str, Settlement], regions: Dict[str, Region]) -> List[Route]:
    nodes = {sid: (s.x, s.y) for sid, s in settlements.items()}
    edges = nearest_neighbor_graph(nodes, rng)

    routes: List[Route] = []
    risk_levels = [("low", 0.45), ("medium", 0.40), ("high", 0.15)]

    for a, b in edges:
        sa, sb = settlements[a], settlements[b]
        km = dist((sa.x, sa.y), (sb.x, sb.y)) * 12.0  # scale factor

        # mode heuristic
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
    resources: List[str]
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

    inst_pool = ["harbor office", "grain bureau", "guild tribunal", "border watch", "sanctuary clinics", "roadwardens", "mint commission"]

    polities: Dict[str, Polity] = {}
    for i, cap_id in enumerate(capitals):
        pid = f"P{i+1}"
        name = make_name(rng, 2) + " Dominion"
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

        exports = sorted(rng.sample(list(available), k=min(len(available), rng.randint(2, 4)))) if available else ["labor"]
        needs = [r for r in resources if r not in available]
        imports = sorted(rng.sample(needs, k=min(len(needs), rng.randint(2, 4)))) if needs else ["luxury-goods"]

        laws = rng.sample(law_pool, k=3)
        inst = rng.sample(inst_pool, k=3)

        notes = [
            f"Capital is {settlements[cap_id].name}; legitimacy flows through {government.replace('-', ' ')} procedure.",
            f"Exports emphasize {', '.join(exports)}; imports rely on {', '.join(imports)}."
        ]

        polities[pid] = Polity(
            id=pid,
            name=name,
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

def gen_factions(rng: random.Random, polities: Dict[str, Polity], resources: List[str]) -> Dict[str, Faction]:
    ftypes = ["guild", "church-order", "intelligence-office", "rebel-cell", "noble-house", "mercenary-banner", "smugglers"]
    goal_pool = [
        "control tariffs", "break a monopoly", "protect pilgrims", "overthrow a regent", "legalize a banned rite",
        "secure grain reserves", "end conscription abuse", "corner the salt trade", "rewrite succession law"
    ]
    method_pool = ["bribery", "blackmail", "public charity", "targeted violence", "bureaucratic sabotage", "propaganda", "trade embargo", "strike action"]

    factions: Dict[str, Faction] = {}
    idx = 1

    for pid in list(polities.keys()):
        for _ in range(rng.randint(2, 3)):
            fid = f"F{idx}"
            idx += 1
            name = make_name(rng, 2) + " " + rng.choice(["Accord", "Cabal", "Ledger", "Host", "Covenant", "Office", "Banner"])
            ftype = rng.choice(ftypes)
            goals = rng.sample(goal_pool, k=2)
            methods = rng.sample(method_pool, k=3)
            res = rng.sample(resources, k=2) + [ftype]
            hooks = [
                f"A stamped receipt proves {name} funds a 'charity' that is actually a pipeline for {methods[0]}.",
                f"A missing crate of {rng.choice(resources)} vanished on a route that {name} 'audits'."
            ]
            factions[fid] = Faction(
                id=fid, name=name, polity_id=pid, type=ftype,
                goals=goals, methods=methods, resources=res,
                enemies=[], allies=[], hooks=hooks
            )

    # One cross-border faction
    fid = f"F{idx}"
    name = make_name(rng, 2) + " " + rng.choice(["Circuit", "Concord", "Undertide", "Else-Rail"])
    factions[fid] = Faction(
        id=fid, name=name, polity_id=None, type=rng.choice(ftypes),
        goals=["profit from conflict", "control a chokepoint archive"],
        methods=["forged stamps", "bribed roadwardens", "selective arson"],
        resources=[rng.choice(resources), "maps", "false seals"],
        enemies=[], allies=[], hooks=[
            "Their courier carries two identical stamps — one real, one boneglass counterfeit.",
            "They can prove your ancestry — and they can also erase it."
        ]
    )

    # Light linking for allies/enemies (not deep simulation yet)
    fids = list(factions.keys())
    for f in factions.values():
        others = [x for x in fids if x != f.id]
        rng.shuffle(others)
        f.allies = others[:rng.randint(0, 2)]
        # pick a slice (could be empty)
        start = rng.randint(2, 3)
        end = rng.randint(4, 6)
        f.enemies = others[start:end]

    return factions

def gen_magic(rng: random.Random, cfg: Dict) -> MagicSystem:
    presence = cfg.get("magic_presence", "rare")
    hardness = cfg.get("magic_hardness", "hard")

    if presence == "none":
        return MagicSystem(
            presence="none",
            hardness=hardness,
            inputs=[],
            outputs=[],
            costs=[],
            failure_modes=[],
            countermeasures=[],
            second_order_effects=[],
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
        presence=presence,
        hardness=hardness,
        inputs=inputs,
        outputs=outputs,
        costs=costs,
        failure_modes=failure,
        countermeasures=counters,
        second_order_effects=effects,
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

    # root events
    roots = rng.randint(4, 7)
    for i in range(roots):
        title, _, cons = rng.choice(templates)
        eid = f"E{i+1}"
        year = start_year + int((i / roots) * (abs(start_year)))
        season = rng.choice(SEASONS)
        agents = rng.sample(polity_names, k=min(len(polity_names), rng.randint(1, 2)))
        consequences = [rng.choice(cons), f"{rng.choice(resources)} prices move for a decade"]
        events.append(Event(id=eid, year=year, season=season, title=title, cause_ids=[], agents=agents, consequences=consequences))

    # downstream events with causes
    for i in range(roots, n):
        title, _, cons = rng.choice(templates)
        eid = f"E{i+1}"
        cause = rng.choice(events)

        year = int(clamp(rng.gauss(cause.year + rng.randint(2, 18), 12), start_year, end_year))
        season = rng.choice(SEASONS)
        agents = rng.sample(polity_names, k=min(len(polity_names), rng.randint(1, 3)))
        consequences = [rng.choice(cons), rng.choice(cons), f"Receipts tighten in {rng.choice(agents)} courts"]

        cause_ids = [cause.id]
        if rng.random() < 0.35:
            cause2 = rng.choice(events)
            if (cause2.year, SEASONS.index(cause2.season)) <= (year, SEASONS.index(season)) and cause2.id != cause.id:
                cause_ids.append(cause2.id)

        events.append(Event(id=eid, year=year, season=season, title=title, cause_ids=cause_ids, agents=agents, consequences=consequences))

    events.sort(key=lambda e: (e.year, SEASONS.index(e.season)))
    return events

def gen_conflicts(rng: random.Random, polities: Dict[str, Polity], magic: MagicSystem, resources: List[str]) -> List[Conflict]:
    pol = list(polities.values())
    rng.shuffle(pol)
    n = rng.randint(3, 6)

    conflicts: List[Conflict] = []
    for i in range(n):
        a = rng.choice(pol).name
        b = rng.choice(pol).name
        while b == a:
            b = rng.choice(pol).name

        res = rng.choice(resources)
        stakes = [
            f"Control of {res} flow through a chokepoint",
            "Winter reserves and the legitimacy that follows",
            "Whether courts accept truth-rites without counter-seals" if magic.presence != "none" else "Whether courts accept guild receipts as law"
        ]
        escalation = [
            "Tariffs rise; caravans reroute; black markets bloom.",
            "Border watch expands; exemptions become bribes.",
            "A public trial becomes a proxy war; assassins follow the stamps."
        ]
        receipts = [
            f"{a} depends on importing {res} and can't stomach another price spike.",
            f"{b} needs revenue — treasury pressure is real, not a vibe.",
            "Enforcement capacity exists: roadwardens and harbor offices can actually collect, so laws matter."
        ]
        conflicts.append(Conflict(
            id=f"C{i+1}",
            title=f"The {res.capitalize()} Pressure",
            parties=[a, b],
            stakes=stakes,
            escalation=escalation,
            receipts=receipts
        ))

    return conflicts

def gen_storykit(rng: random.Random, cfg: Dict, settlements: Dict[str, Settlement], polities: Dict[str, Polity]) -> StoryKit:
    tone = cfg.get("tone", "grounded-dark")
    story_type = cfg.get("story_type", "political-intrigue")
    themes = cfg.get("themes", [])

    places = [s.name for s in settlements.values() if s.kind in ("city", "port", "fort", "town")]
    rng.shuffle(places)
    default_scenes = places[:10]

    hook_templates = [
        "A sealed ledger page surfaces — it proves {pol} lied about {thing}.",
        "A winter convoy goes missing; the stamped exemptions are too clean.",
        "A witness recants after a truth-rite; someone is gaming the counter-seals.",
        "A port quarantine is declared; the real reason is {thing}.",
        "A fort commander sells road passes to fund {thing}.",
        "A relic lease is forged; it implicates a person tied to {pol}.",
        "A guild tribunal demands proof nobody can legally obtain."
    ]
    things = ["grain reserves", "succession law", "smuggling routes", "a secret tax ledger", "a forbidden rite", "a counterfeit seal workshop"]

    polys = list(polities.values())
    hooks: List[str] = []
    for _ in range(20):
        t = rng.choice(hook_templates)
        pol = rng.choice(polys).name
        thing = rng.choice(things)
        hooks.append(t.format(pol=pol, thing=thing))

    dont_break = [
        "Travel times: caravans take days, not hours; distance is a weapon.",
        "Institutions collect receipts: proof beats reputation; paperwork is power.",
        "Scarcity has political consequences (prices, riots, rationing, treaties).",
        "Magic (if present) has costs and countermeasures; it doesn't handwave logistics."
    ]

    return StoryKit(
        themes=themes,
        tone=tone,
        story_type=story_type,
        default_scene_locations=default_scenes,
        hooks=hooks,
        dont_break=dont_break
    )

def compile_world(cfg: Dict) -> World:
    seed = int(cfg.get("seed", random.randint(1, 1_000_000)))
    rng = random.Random(seed)

    planet = gen_planet(rng, cfg)
    regions = gen_regions(rng, cfg)
    settlements = gen_settlements(rng, cfg, regions)
    routes = gen_routes(rng, settlements, regions)
    resources = gen_resources(rng, regions)
    polities = gen_polities(rng, cfg, settlements, regions, resources)
    factions = gen_factions(rng, polities, resources)
    magic = gen_magic(rng, cfg)
    timeline = gen_timeline(rng, cfg, polities, resources)
    conflicts = gen_conflicts(rng, polities, magic, resources)
    story = gen_storykit(rng, cfg, settlements, polities)

    receipts = [
        "Every major claim is backed by a concrete driver: terrain, travel time, scarcity, enforcement, or institutional incentives.",
        "Routes form a connected graph; chokepoints are intentionally exploited by polities and factions.",
        "Timeline events carry causes and lingering consequences; nothing 'just happens'."
    ]

    return World(
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
        conflicts=conflicts,
        story=story,
        receipts=receipts
    )

# ----------------------------
# Validation & repair
# ----------------------------

@dataclass
class ValidationIssue:
    severity: str  # error, warn
    code: str
    message: str
    where: Optional[str] = None
    suggestion: Optional[str] = None

def build_adj(routes: List[Route], all_nodes: Optional[List[str]] = None) -> Dict[str, List[Tuple[str, float]]]:
    adj: Dict[str, List[Tuple[str, float]]] = {}
    if all_nodes:
        for n in all_nodes:
            adj.setdefault(n, [])
    for r in routes:
        adj.setdefault(r.a, []).append((r.b, r.km))
        adj.setdefault(r.b, []).append((r.a, r.km))
    return adj

def validate(world: World) -> Tuple[float, List[ValidationIssue]]:
    issues: List[ValidationIssue] = []
    score = 1.0

    # Connectivity
    all_sids = list(world.settlements.keys())
    adj = build_adj(world.routes, all_sids)
    if all_sids:
        d0 = dijkstra(adj, all_sids[0])
        disconnected = [sid for sid in all_sids if d0.get(sid, 1e18) >= 1e17]
        if disconnected:
            issues.append(ValidationIssue(
                severity="error",
                code="DISCONNECTED_MAP",
                message=f"{len(disconnected)} settlements are disconnected from the route network.",
                where="routes",
                suggestion="Add routes to connect isolated nodes."
            ))
            score -= 0.35

    # City logistics sanity
    route_count = {sid: 0 for sid in all_sids}
    sea_or_river = {sid: 0 for sid in all_sids}
    for r in world.routes:
        route_count[r.a] += 1
        route_count[r.b] += 1
        if r.mode in ("sea", "river"):
            sea_or_river[r.a] += 1
            sea_or_river[r.b] += 1

    for s in world.settlements.values():
        if s.population >= 20000 and s.kind in ("city", "port"):
            if route_count.get(s.id, 0) < 2:
                issues.append(ValidationIssue(
                    severity="error",
                    code="CITY_ISOLATED",
                    message=f"{s.name} ({s.population}) lacks sufficient routes for its size.",
                    where=s.id,
                    suggestion="Add another route to the nearest trade node or make it a port with a sea lane."
                ))
                score -= 0.12
            if ("coastal" not in s.tags) and sea_or_river.get(s.id, 0) == 0:
                issues.append(ValidationIssue(
                    severity="warn",
                    code="CITY_NO_CHEAP_BULK",
                    message=f"{s.name} is large but lacks river/sea bulk transport links.",
                    where=s.id,
                    suggestion="Add a river lane/canal note or reduce population."
                ))
                score -= 0.03

    # Army percentage sanity (soft check)
    for p in world.polities.values():
        if p.army_pct > 0.16:
            issues.append(ValidationIssue(
                severity="warn",
                code="ARMY_TOO_HIGH",
                message=f"{p.name} army_pct={p.army_pct:.3f} is high for sustained readiness.",
                where=p.id,
                suggestion="Lower standing army; add levy rules or mercenary contracts."
            ))
            score -= 0.03

    # Food logic proxy: every polity must export grain OR import grain
    for p in world.polities.values():
        if "grain" not in p.exports and "grain" not in p.imports:
            issues.append(ValidationIssue(
                severity="error",
                code="NO_GRAIN_PATH",
                message=f"{p.name} neither exports nor imports grain — food logic missing.",
                where=p.id,
                suggestion="Add grain to imports or ensure a grain-producing region lies in the polity."
            ))
            score -= 0.18

    # Timeline causality validity: causes exist and are not in the future
    events_by_id = {e.id: e for e in world.timeline}
    for e in world.timeline:
        for cid in e.cause_ids:
            if cid not in events_by_id:
                issues.append(ValidationIssue(
                    severity="error",
                    code="MISSING_CAUSE",
                    message=f"{e.id} references missing cause {cid}.",
                    where=e.id,
                    suggestion="Rewire event causes to existing earlier events."
                ))
                score -= 0.08
            else:
                ce = events_by_id[cid]
                if (ce.year, SEASONS.index(ce.season)) > (e.year, SEASONS.index(e.season)):
                    issues.append(ValidationIssue(
                        severity="error",
                        code="FUTURE_CAUSE",
                        message=f"{e.id} has cause {cid} set in the future.",
                        where=e.id,
                        suggestion="Rewire causes so they precede the event."
                    ))
                    score -= 0.12

    # Magic second-order effects: if magic exists, describe it
    if world.magic.presence != "none" and not world.magic.second_order_effects:
        issues.append(ValidationIssue(
            severity="warn",
            code="MAGIC_NO_SECOND_ORDER",
            message="Magic exists but no second-order institutional effects are described.",
            where="magic",
            suggestion="Add court/insurance/labor effects so magic doesn't handwave logistics."
        ))
        score -= 0.04

    score = max(0.0, min(1.0, score))
    return score, issues

def repair(world: World, issues: List[ValidationIssue]) -> World:
    """Cheap repairs. Not a full simulation. Goal: remove obvious contradictions."""
    w = world
    rng = random.Random(w.seed + 99991)

    by_id = w.settlements

    def add_route(a: str, b: str, mode: str = "road"):
        sa, sb = by_id[a], by_id[b]
        km = math.hypot(sa.x - sb.x, sa.y - sb.y) * 12.0
        w.routes.append(Route(a=a, b=b, km=float(f"{km:.1f}"), mode=mode, risk="medium"))

    for issue in issues:
        if issue.code == "CITY_ISOLATED" and issue.where in by_id:
            s = by_id[issue.where]
            candidates = [(math.hypot(s.x - t.x, s.y - t.y), t.id) for t in by_id.values() if t.id != s.id]
            candidates.sort()
            if candidates:
                add_route(s.id, candidates[0][1], mode="road")

        elif issue.code == "NO_GRAIN_PATH" and issue.where in w.polities:
            p = w.polities[issue.where]
            if "grain" not in p.imports:
                p.imports.append("grain")

        elif issue.code == "DISCONNECTED_MAP":
            # Connect each isolated settlement to its nearest neighbor
            adj = build_adj(w.routes, list(by_id.keys()))
            sids = list(by_id.keys())
            if sids:
                d0 = dijkstra(adj, sids[0])
                isolated = [sid for sid in sids if d0.get(sid, 1e18) >= 1e17]
                for sid in isolated:
                    s = by_id[sid]
                    candidates = [(math.hypot(s.x - t.x, s.y - t.y), t.id) for t in by_id.values() if t.id != s.id]
                    candidates.sort()
                    if candidates:
                        add_route(s.id, candidates[0][1], mode="road")

        elif issue.code in ("MISSING_CAUSE", "FUTURE_CAUSE"):
            # Rewire causality: keep only earlier causes; if none, assign an earlier one (unless it's the first/root event)
            by_eid = {e.id: e for e in w.timeline}
            ordered = sorted(w.timeline, key=lambda e: (e.year, SEASONS.index(e.season)))
            for e in ordered:
                filtered: List[str] = []
                for cid in e.cause_ids:
                    ce = by_eid.get(cid)
                    if ce is None:
                        continue
                    if (ce.year, SEASONS.index(ce.season)) <= (e.year, SEASONS.index(e.season)):
                        filtered.append(cid)

                if not filtered and e.id != ordered[0].id:
                    earlier = [x for x in ordered if (x.year, SEASONS.index(x.season)) <= (e.year, SEASONS.index(e.season)) and x.id != e.id]
                    if earlier:
                        filtered = [earlier[max(0, len(earlier)//2)].id]  # stable-ish choice

                e.cause_ids = filtered

    return w

def compile_with_repair(cfg: Dict, target_score: float = 0.93, max_iters: int = 25) -> Tuple[World, float, List[ValidationIssue]]:
    world = compile_world(cfg)
    last_score = 0.0
    last_issues: List[ValidationIssue] = []

    for _ in range(max_iters):
        score, issues = validate(world)
        last_score, last_issues = score, issues
        hard_errors = [i for i in issues if i.severity == "error"]
        if score >= target_score and not hard_errors:
            return world, score, issues
        world = repair(world, issues)

    return world, last_score, last_issues

# ----------------------------
# Export
# ----------------------------

def md_table(rows: List[List[str]]) -> str:
    if not rows:
        return ""
    header = rows[0]
    out = ["| " + " | ".join(header) + " |", "| " + " | ".join(["---"] * len(header)) + " |"]
    for r in rows[1:]:
        out.append("| " + " | ".join(r) + " |")
    return "\n".join(out)

def export_markdown(world: World, score: float, issues: List[ValidationIssue]) -> str:
    p = world.planet
    cfg = world.config

    # travel-time graph (days)
    adj_days: Dict[str, List[Tuple[str, float]]] = {sid: [] for sid in world.settlements.keys()}
    for r in world.routes:
        days = travel_days(r.km, r.mode)
        adj_days[r.a].append((r.b, days))
        adj_days[r.b].append((r.a, days))

    def shortest_days(a: str, b: str) -> float:
        import heapq
        INF = 1e18
        dist_map = {k: INF for k in adj_days.keys()}
        dist_map[a] = 0.0
        pq = [(0.0, a)]
        while pq:
            d, u = heapq.heappop(pq)
            if u == b:
                return d
            if d != dist_map[u]:
                continue
            for v, w in adj_days[u]:
                nd = d + w
                if nd < dist_map[v]:
                    dist_map[v] = nd
                    heapq.heappush(pq, (nd, v))
        return INF

    pols = list(world.polities.values())
    cap_rows = [["From/To"] + [world.settlements[p.capital_id].name for p in pols]]
    for pa in pols:
        row = [world.settlements[pa.capital_id].name]
        for pb in pols:
            d = shortest_days(pa.capital_id, pb.capital_id)
            row.append("—" if d >= 1e17 else f"{d:.1f}d")
        cap_rows.append(row)

    pol_rows = [["Polity", "Govt", "Pop", "Army%", "Exports", "Imports", "Capital"]]
    for po in pols:
        pol_rows.append([
            po.name,
            po.government.replace("-", " "),
            f"{po.population:,}",
            f"{po.army_pct * 100:.1f}%",
            ", ".join(po.exports),
            ", ".join(po.imports),
            world.settlements[po.capital_id].name
        ])

    tops = sorted(world.settlements.values(), key=lambda s: s.population, reverse=True)[:10]
    set_rows = [["Settlement", "Kind", "Pop", "Region", "Tags"]]
    for s in tops:
        set_rows.append([s.name, s.kind, f"{s.population:,}", world.regions[s.region_id].name, ", ".join(s.tags) if s.tags else "—"])

    err = [i for i in issues if i.severity == "error"]
    warn = [i for i in issues if i.severity == "warn"]

    conflict_md: List[str] = []
    for c in world.conflicts:
        conflict_md.append(f"### {c.title}\n")
        conflict_md.append(f"**Parties:** {', '.join(c.parties)}\n")
        conflict_md.append("**Stakes:**\n" + "\n".join([f"- {x}" for x in c.stakes]) + "\n")
        conflict_md.append("**Escalation path:**\n" + "\n".join([f"- {x}" for x in c.escalation]) + "\n")
        conflict_md.append("**Receipts (why this is plausible):**\n" + "\n".join([f"- {x}" for x in c.receipts]) + "\n")

    recent = sorted(world.timeline, key=lambda e: (e.year, SEASONS.index(e.season)), reverse=True)[:18]
    time_rows = [["Year", "Season", "Event", "Causes", "Consequences (selection)"]]
    for e in reversed(recent):
        causes = ", ".join(e.cause_ids) if e.cause_ids else "—"
        cons = "; ".join(e.consequences[:2])
        time_rows.append([str(e.year), e.season, e.title, causes, cons])

    md = f"""# World Compendium — {p.name}

**Build:** seed={world.seed} • coherence_score={score:.3f} • generated_on={date.today().isoformat()}

## 1) One-Page Pitch

This is a **{cfg.get('tone','')}** {cfg.get('scale','')} setting tuned for **{cfg.get('story_type','')}** stories.
It is built to be writable immediately: travel times matter, scarcity creates politics, institutions have enforcement, and every major claim has a receipt.

**Primary themes:** {", ".join(world.story.themes) if world.story.themes else "—"}

## 2) Physical Laws and Calendar

- **Gravity:** ~{p.gravity_g:.2f}g
- **Day:** {p.day_hours:.1f} hours
- **Year:** {p.year_days} days
- **Axial tilt:** {p.axial_tilt_deg:.1f}°

Notes:
{chr(10).join([f"- {n}" for n in p.notes])}

## 3) Regions

{chr(10).join([f"### {r.name}{chr(10)}**Biome:** {r.biome}{chr(10)}**Hazards:** {', '.join(r.hazards)}{chr(10)}**Key resources:** {', '.join(r.resources) if r.resources else '—'}{chr(10)}" for r in world.regions.values()])}

## 4) Major Settlements (top 10 by population)

{md_table(set_rows)}

## 5) Polities and Power

{md_table(pol_rows)}

### Capital Travel Times (days, along routes)

{md_table(cap_rows)}

## 6) Institutions, Laws, and Daily Enforcement

This world runs on receipts — stamps, witness marks, charters, permits, and audits. That paperwork is not flavor; it is the primary weapon.

Key receipts and checks that appear on page:
{chr(10).join([f"- {x}" for x in world.receipts])}

## 7) Magic / Tech Rules

**Presence:** {world.magic.presence} • **Hardness:** {world.magic.hardness}

**Inputs:** {", ".join(world.magic.inputs) if world.magic.inputs else "—"}
**Outputs:** {", ".join(world.magic.outputs) if world.magic.outputs else "—"}

**Costs:**
{chr(10).join([f"- {x}" for x in world.magic.costs]) if world.magic.costs else "- —"}

**Failure modes:**
{chr(10).join([f"- {x}" for x in world.magic.failure_modes]) if world.magic.failure_modes else "- —"}

**Countermeasures (why magic doesn’t dominate):**
{chr(10).join([f"- {x}" for x in world.magic.countermeasures]) if world.magic.countermeasures else "- —"}

**Second-order effects (how the world changes):**
{chr(10).join([f"- {x}" for x in world.magic.second_order_effects]) if world.magic.second_order_effects else "- —"}

## 8) Factions

{chr(10).join([f"### {f.name}{chr(10)}**Type:** {f.type}{chr(10)}**Aligned polity:** {world.polities[f.polity_id].name if f.polity_id else 'Cross-border'}{chr(10)}**Goals:** {', '.join(f.goals)}{chr(10)}**Methods:** {', '.join(f.methods)}{chr(10)}**Hooks:**{chr(10)}- {f.hooks[0]}{chr(10)}- {f.hooks[1] if len(f.hooks)>1 else ''}{chr(10)}" for f in world.factions.values()])}

## 9) Active Conflicts

{chr(10).join(conflict_md)}

## 10) Recent History (for immediate plotting)

{md_table(time_rows)}

## 11) Story Toolkit

**Default scene locations (ready for chapter 1):**
{chr(10).join([f"- {x}" for x in world.story.default_scene_locations])}

**20 Hooks:**
{chr(10).join([f"- {h}" for h in world.story.hooks])}

**Don’t break these invariants:**
{chr(10).join([f"- {x}" for x in world.story.dont_break])}

## 12) Coherence Report

**Score:** {score:.3f}

**Hard errors:** {len(err)} • **Warnings:** {len(warn)}

{chr(10).join([f"- [{i.severity.upper()}] {i.code}: {i.message}" + (f" (suggestion: {i.suggestion})" if i.suggestion else "") for i in issues]) if issues else "No issues. World is internally coherent by current validators."}
"""
    return md

def export_graphviz_dot(world: World) -> str:
    lines = ["graph world {", "  overlap=false;", "  splines=true;"]
    for s in world.settlements.values():
        label = f"{s.name}\\n{s.kind} ({s.population})"
        lines.append(f'  {s.id} [label="{label}"];')
    for r in world.routes:
        lines.append(f'  {r.a} -- {r.b} [label="{r.mode} {r.km:.0f}km"];')
    lines.append("}")
    return "\n".join(lines)

def export_pdf(md_text: str, pdf_path: str) -> bool:
    """Very naive Markdown-to-PDF: headings + paragraphs + simple tables."""
    try:
        from reportlab.lib.pagesizes import LETTER
        from reportlab.lib.styles import getSampleStyleSheet
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
        from reportlab.lib.units import inch
        from reportlab.lib import colors
    except Exception:
        return False

    styles = getSampleStyleSheet()
    h1 = styles["Heading1"]
    h2 = styles["Heading2"]
    h3 = styles["Heading3"]
    body = styles["BodyText"]
    body.spaceAfter = 8

    doc = SimpleDocTemplate(pdf_path, pagesize=LETTER, rightMargin=54, leftMargin=54, topMargin=54, bottomMargin=54)
    story = []
    lines = md_text.splitlines()
    i = 0

    def parse_table(start: int):
        table_lines = []
        j = start
        while j < len(lines) and lines[j].strip().startswith("|"):
            table_lines.append(lines[j].strip())
            j += 1
        if len(table_lines) < 2:
            return None, start

        rows = []
        for tl in table_lines:
            parts = [p.strip() for p in tl.strip("|").split("|")]
            rows.append(parts)

        # remove separator row
        if len(rows) >= 2 and all(set(x) <= set("-:") for x in rows[1]):
            rows = [rows[0]] + rows[2:]
        return rows, j

    while i < len(lines):
        line = lines[i].rstrip()
        if line.startswith("# "):
            story.append(Paragraph(line[2:], h1))
            story.append(Spacer(1, 0.18 * inch))
            i += 1
            continue
        if line.startswith("## "):
            story.append(Paragraph(line[3:], h2))
            story.append(Spacer(1, 0.12 * inch))
            i += 1
            continue
        if line.startswith("### "):
            story.append(Paragraph(line[4:], h3))
            story.append(Spacer(1, 0.08 * inch))
            i += 1
            continue

        if line.strip().startswith("|"):
            rows, ni = parse_table(i)
            if rows:
                t = Table(rows, hAlign="LEFT")
                t.setStyle(TableStyle([
                    ("FONT", (0, 0), (-1, 0), "Helvetica-Bold"),
                    ("BACKGROUND", (0, 0), (-1, 0), colors.whitesmoke),
                    ("GRID", (0, 0), (-1, -1), 0.25, colors.grey),
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("FONTSIZE", (0, 0), (-1, -1), 8),
                    ("LEFTPADDING", (0, 0), (-1, -1), 4),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                ]))
                story.append(t)
                story.append(Spacer(1, 0.12 * inch))
                i = ni
                continue

        if line.strip() == "":
            i += 1
            continue

        safe = line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        if safe.count("**") >= 2:
            safe = safe.replace("**", "<b>", 1).replace("**", "</b>", 1)
        story.append(Paragraph(safe, body))
        i += 1

    doc.build(story)
    return True

def export_canon_json(world: World) -> Dict:
    return asdict(world)

# ----------------------------
# CLI (with always-new run folder)
# ----------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", type=str, default=None, help="Path to config.json (optional).")
    ap.add_argument(
        "--out_root",
        type=str,
        default=r"I:\My Drive\Worldbuilding\world_pipeline\1. Template",
        help="Root folder where a NEW run folder is created every run."
    )
    ap.add_argument(
        "--run_name",
        type=str,
        default=None,
        help="Optional run folder name. If omitted, uses timestamp+seed."
    )
    ap.add_argument("--seed", type=int, default=None, help="Override seed.")
    ap.add_argument("--target_score", type=float, default=0.93, help="Minimum coherence score target (0..1).")
    ap.add_argument("--max_repair_iters", type=int, default=25, help="Max validator/repair iterations.")
    args = ap.parse_args()

    cfg = default_config(args.seed)
    if args.config:
        with open(args.config, "r", encoding="utf-8") as f:
            user_cfg = json.load(f)
        cfg.update(user_cfg)
        if args.seed is not None:
            cfg["seed"] = args.seed

    world, score, issues = compile_with_repair(cfg, target_score=args.target_score, max_iters=args.max_repair_iters)

    out_root = Path(args.out_root)
    out_root.mkdir(parents=True, exist_ok=True)

    if args.run_name:
        run_folder = out_root / args.run_name
        # If you explicitly name it, we still enforce "new folder" by refusing collisions.
        run_folder.mkdir(parents=True, exist_ok=False)
    else:
        # Auto unique run folder
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        run_folder = out_root / f"run_{ts}_seed{world.seed}"
        run_folder.mkdir(parents=True, exist_ok=False)

    md = export_markdown(world, score, issues)
    (run_folder / "world_bible.md").write_text(md, encoding="utf-8")

    (run_folder / "canon.json").write_text(
        json.dumps(export_canon_json(world), ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

    (run_folder / "map_graph.dot").write_text(export_graphviz_dot(world), encoding="utf-8")

    pdf_ok = export_pdf(md, str(run_folder / "world_bible.pdf"))

    print(f"Run folder: {run_folder}")
    print(f"Wrote: {run_folder / 'world_bible.md'}")
    print(f"Wrote: {run_folder / 'canon.json'}")
    print(f"Wrote: {run_folder / 'map_graph.dot'}")
    if pdf_ok:
        print(f"Wrote: {run_folder / 'world_bible.pdf'}")
    else:
        print("Skipped PDF export (reportlab not installed).")
    print(f"Coherence score: {score:.3f}  (issues: {len(issues)})")

if __name__ == "__main__":
    main()
