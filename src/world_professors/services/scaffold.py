"""Scaffolding helpers for bootstrapping data at scale."""

from __future__ import annotations

import csv
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

import yaml


@dataclass(frozen=True)
class ScenarioSeedRow:
    industry: str  # e.g. "finance"
    scenario_slug: str  # e.g. "wealth-mgmt"
    id: str  # e.g. "scn-fin-wealth-mgmt"
    name: str  # Chinese or English name
    description: str
    sub_industry: str | None = None
    priority: str | None = None
    source: str | None = None


def _now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


class Scaffold:
    def __init__(self, data_dir: Path) -> None:
        self.data_dir = Path(data_dir)

    def scaffold_scenarios_from_csv(self, seed_csv: Path, *, overwrite: bool = False) -> list[Path]:
        """Generate scenario YAMLs from a CSV seed file.

        CSV header (minimum):
            industry,scenario_slug,id,name,description
        Optional:
            sub_industry,priority,source
        """
        seed_csv = Path(seed_csv)
        created: list[Path] = []

        with open(seed_csv, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                seed = ScenarioSeedRow(
                    industry=(row.get("industry") or "").strip(),
                    scenario_slug=(row.get("scenario_slug") or "").strip(),
                    id=(row.get("id") or "").strip(),
                    name=(row.get("name") or "").strip(),
                    description=(row.get("description") or "").strip(),
                    sub_industry=(row.get("sub_industry") or "").strip() or None,
                    priority=(row.get("priority") or "").strip() or None,
                    source=(row.get("source") or "").strip() or None,
                )
                if not seed.industry or not seed.scenario_slug or not seed.id:
                    continue

                out_dir = self.data_dir / "scenarios" / seed.industry
                out_dir.mkdir(parents=True, exist_ok=True)
                out_path = out_dir / f"{seed.scenario_slug}.yaml"

                if out_path.exists() and not overwrite:
                    continue

                doc = {
                    "id": seed.id,
                    "name": seed.name,
                    "industry": seed.industry,
                    "sub_industry": seed.sub_industry,
                    "description": seed.description,
                    "value_flow": [],
                    "key_metrics": [],
                    "traditional_pain_points": [],
                    "ai_opportunities": [],
                    "tags": [],
                    "related_scenarios": [],
                    "metadata": {
                        "created_at": _now_iso(),
                        "updated_at": _now_iso(),
                        "author": "scaffold",
                        "version": "0.1",
                        "schema_version": "1.0",
                        "source": seed.source or "seed",
                        "priority": seed.priority or "P2",
                        "review_status": "draft",
                    },
                }

                with open(out_path, "w", encoding="utf-8") as wf:
                    yaml.safe_dump(doc, wf, allow_unicode=True, sort_keys=False)
                created.append(out_path)

        return created

