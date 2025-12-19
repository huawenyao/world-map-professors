#!/usr/bin/env python3
"""数据管理脚本（不依赖 wp 命令）。

用途：
- validate: 校验 data 目录（schema + 引用 + 质量门禁）
- catalog: 生成 data/_catalog（entities/links/stats）
- report: 输出覆盖率摘要（基于 catalog/stats）
- scaffold-scenarios: 从 CSV 种子生成场景 YAML 骨架

示例：
  python3 scripts/manage_data.py validate --data-dir data
  python3 scripts/manage_data.py validate --data-dir data --strict-refs --strict-quality
  python3 scripts/manage_data.py catalog --data-dir data
  python3 scripts/manage_data.py scaffold-scenarios seeds/scenario_seed.csv --data-dir data
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from world_professors.services.catalog import CatalogBuilder
from world_professors.services.scaffold import Scaffold
from world_professors.services.validator import DataValidator


def _p(path: str | None, default: Path) -> Path:
    return Path(path) if path is not None else default


def cmd_validate(args: argparse.Namespace) -> int:
    data_dir = _p(args.data_dir, Path("data"))
    v = DataValidator(data_dir)
    summary = v.validate(strict_refs=args.strict_refs, strict_quality=args.strict_quality)

    # 简单文本输出（脚本场景）
    for msg in summary.errors + summary.warnings:
        sev = "ERROR" if msg.severity == "error" else "WARN"
        try:
            rel = msg.file_path.relative_to(data_dir)
        except Exception:
            rel = msg.file_path
        print(f"[{sev}] {msg.code} {rel}: {msg.message}")

    print(
        f"\nChecked: {summary.checked_files} files | "
        f"Errors: {len(summary.errors)} | Warnings: {len(summary.warnings)}"
    )
    return 0 if summary.ok else 1


def cmd_catalog(args: argparse.Namespace) -> int:
    data_dir = _p(args.data_dir, Path("data"))
    output_dir = Path(args.output_dir) if args.output_dir else None
    paths = CatalogBuilder(data_dir).build(output_dir=output_dir)
    print(f"✅ catalog 生成完成: {paths.root}")
    print(f"- entities: {paths.entities}")
    print(f"- links:    {paths.links}")
    print(f"- stats:    {paths.stats}")
    return 0


def cmd_report(args: argparse.Namespace) -> int:
    data_dir = _p(args.data_dir, Path("data"))
    paths = CatalogBuilder(data_dir).build()
    stats = json.loads(paths.stats.read_text(encoding="utf-8"))
    print(json.dumps(stats, ensure_ascii=False, indent=2))
    return 0


def cmd_scaffold_scenarios(args: argparse.Namespace) -> int:
    data_dir = _p(args.data_dir, Path("data"))
    seed_csv = Path(args.seed_csv)
    created = Scaffold(data_dir).scaffold_scenarios_from_csv(seed_csv, overwrite=args.overwrite)
    print(f"✅ 生成 {len(created)} 个场景文件")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="manage_data.py")
    sub = parser.add_subparsers(dest="command", required=True)

    p_validate = sub.add_parser("validate", help="校验 data 目录")
    p_validate.add_argument("--data-dir", default=None, help="数据目录（默认 data）")
    p_validate.add_argument("--strict-refs", action="store_true", help="引用缺失视为错误")
    p_validate.add_argument("--strict-quality", action="store_true", help="质量门禁视为错误")
    p_validate.set_defaults(func=cmd_validate)

    p_catalog = sub.add_parser("catalog", help="生成 data/_catalog")
    p_catalog.add_argument("--data-dir", default=None, help="数据目录（默认 data）")
    p_catalog.add_argument("--output-dir", default=None, help="输出目录（默认 data/_catalog）")
    p_catalog.set_defaults(func=cmd_catalog)

    p_report = sub.add_parser("report", help="输出覆盖率摘要（JSON）")
    p_report.add_argument("--data-dir", default=None, help="数据目录（默认 data）")
    p_report.set_defaults(func=cmd_report)

    p_scaffold = sub.add_parser("scaffold-scenarios", help="从 seed CSV 生成场景骨架")
    p_scaffold.add_argument("seed_csv", help="CSV 路径")
    p_scaffold.add_argument("--data-dir", default=None, help="数据目录（默认 data）")
    p_scaffold.add_argument("--overwrite", action="store_true", help="覆盖已存在文件")
    p_scaffold.set_defaults(func=cmd_scaffold_scenarios)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return int(args.func(args))


if __name__ == "__main__":
    sys.exit(main())

