Worldbuilder v1 (Python)

This is a small "world compiler" that:
- Generates a coherent setting with geography, polities, factions, history, conflicts, and story hooks
- Runs validators (connectivity, city logistics, food logic, timeline causality, etc.)
- Repairs basic errors
- Exports a ghostwriter-ready world bible (Markdown + optional PDF), plus canon.json

Quick start:
  python worldbuild.py --out ./out

Optional:
  python worldbuild.py --seed 42 --out ./out
  python worldbuild.py --config ./config.json --out ./out

Outputs:
  out/world_bible.md
  out/world_bible.pdf (if reportlab is installed)
  out/canon.json
  out/map_graph.dot (Graphviz)

Render the dot file (Graphviz):
  dot -Tpng map_graph.dot -o map_graph.png
