# Patch for worldbuild.py
# - Save output to a new world folder in world_pipeline for each run
# - Ensure all references use '1.template' (not '1. template' or '1._template')
# - Add output directory logic at the end of the script

import argparse
import json
import math
import random
import hashlib
from dataclasses import dataclass, asdict, field
from datetime import date, datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import shutil
import os

# ...existing code...

def get_unique_world_output_dir(base_dir: Path) -> Path:
    base_dir = Path(base_dir)
    base_dir.mkdir(parents=True, exist_ok=True)
    i = 1
    while True:
        candidate = base_dir / f"world_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{i}"
        if not candidate.exists():
            candidate.mkdir()
            return candidate
        i += 1

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Worldbuilder v1.2 — NameForge edition")
    parser.add_argument('--out', type=str, default=None, help='Output directory for world files')
    parser.add_argument('--seed', type=int, default=None, help='Random seed for reproducibility')
    parser.add_argument('--config', type=str, default=None, help='Optional config file')
    args = parser.parse_args()

    # Determine output directory
    world_pipeline_dir = Path(__file__).parent.parent
    if args.out:
        out_dir = Path(args.out)
        if not out_dir.is_absolute():
            out_dir = world_pipeline_dir / args.out
        out_dir.mkdir(parents=True, exist_ok=True)
    else:
        out_dir = get_unique_world_output_dir(world_pipeline_dir)

    # ...existing world generation logic...
    # Example: save a dummy file to show output
    with open(out_dir / "world_bible.md", "w", encoding="utf-8") as f:
        f.write("# Example World Bible\n\nWorld generated successfully.")

    print(f"World files saved to: {out_dir}")
