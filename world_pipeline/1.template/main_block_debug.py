# Place main block at the very end, after all definitions
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
    print(f"[DEBUG] Loaded {len(profiles)} name profiles.")
    name_registry = {}
    namer = NameForge(seed, name_registry, profiles)
    print(f"[DEBUG] NameForge initialized.")
    # Generate a planet name
    planet_name = namer.get("planet:core")
    print(f"[DEBUG] Generated planet name: '{planet_name}'")
    output_dir_path = PIPELINE_DIR / safe_filename(planet_name)
    print(f"[DEBUG] Intended output directory: {output_dir_path}")
    # Create output directory
    out_dir = ensure_unique_dir(output_dir_path)
    print(f"[DEBUG] Output directory created: {out_dir}")
    # Write a simple world_bible.md as proof of generation
    try:
        with open(out_dir / "world_bible.md", "w", encoding="utf-8") as f:
            f.write(f"# {planet_name} World Bible\n\n")
            f.write(f"Seed: {seed}\n")
            f.write(f"Generated at: {dt.datetime.now().isoformat()}\n")
        print(f"[DEBUG] world_bible.md written successfully.")
    except Exception as e:
        print(f"[DEBUG] Failed to write world_bible.md: {e}")
    print(f"World generated: {planet_name}\nOutput folder: {out_dir}")
