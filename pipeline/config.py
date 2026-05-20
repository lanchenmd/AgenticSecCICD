import yaml
from pathlib import Path
from typing import Any


def load_config(config_name: str) -> dict[str, Any]:
    config_dir = Path(__file__).parent.parent / "config"
    config_path = config_dir / f"{config_name}.yaml"

    with open(config_path) as f:
        return yaml.safe_load(f)
