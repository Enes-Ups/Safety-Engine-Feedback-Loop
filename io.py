import json
from pathlib import Path

config_path = Path(__file__).parent / "upsonic_configs.json"
with open(config_path, "r") as f:
    config = json.load(f)

inputs = config.get("input_schema", {}).get("inputs", {})
outputs = config.get("output_schema", {})