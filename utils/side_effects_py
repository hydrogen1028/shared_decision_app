import json
from pathlib import Path

SIDE_EFFECTS_FILE = Path("data/side_effects.json")

def load_common_side_effects():
    if SIDE_EFFECTS_FILE.exists():
        with open(SIDE_EFFECTS_FILE, "r") as f:
            return json.load(f)
    return []

def save_common_side_effect(effect):
    effects = load_common_side_effects()
    if effect not in effects:
        effects.append(effect)
        with open(SIDE_EFFECTS_FILE, "w") as f:
            json.dump(sorted(effects), f, indent=2)
