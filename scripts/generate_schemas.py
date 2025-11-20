#!/usr/bin/env python3
"""Generate JSON Schema files from Pydantic models."""

import json
from pathlib import Path

from world_professors.models import Capability, Role, Scenario


def main() -> None:
    """Generate JSON Schema files."""
    schemas_dir = Path("src/world_professors/schemas")
    schemas_dir.mkdir(parents=True, exist_ok=True)

    models = {
        "scenario": Scenario,
        "role": Role,
        "capability": Capability,
    }

    for name, model_class in models.items():
        schema = model_class.model_json_schema()
        output_path = schemas_dir / f"{name}-schema.json"

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(schema, f, indent=2, ensure_ascii=False)

        print(f"✅ Generated {output_path}")


if __name__ == "__main__":
    main()
