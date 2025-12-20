"""World Professors CLI (`wp`)."""

from __future__ import annotations

from pathlib import Path

import typer
from rich.console import Console
from rich.table import Table

from world_professors.config.settings import settings
from world_professors.services.catalog import CatalogBuilder
from world_professors.services.scaffold import Scaffold
from world_professors.services.validator import DataValidator

app = typer.Typer(no_args_is_help=True)
console = Console()


@app.command("validate")
def validate(
    data_dir: Path | None = typer.Option(
        None, "--data-dir", help="数据目录（默认使用 settings.data_dir）"
    ),
    strict_refs: bool = typer.Option(
        False, "--strict-refs", help="把引用缺失当作错误（默认仅 warning）"
    ),
    strict_quality: bool = typer.Option(
        False, "--strict-quality", help="把质量门禁当作错误（默认仅 warning）"
    ),
) -> None:
    """校验 data 目录（schema + 引用 + 质量门禁）。"""
    dd = data_dir or settings.data_dir
    validator = DataValidator(dd)
    summary = validator.validate(strict_refs=strict_refs, strict_quality=strict_quality)

    table = Table(title="Data Validation")
    table.add_column("Severity", style="magenta")
    table.add_column("Code", style="cyan")
    table.add_column("File", style="green")
    table.add_column("Message", style="white")

    for msg in summary.errors + summary.warnings:
        sev = "ERROR" if msg.severity == "error" else "WARN"
        try:
            rel = msg.file_path.relative_to(dd)
        except Exception:
            rel = msg.file_path
        table.add_row(sev, msg.code, str(rel), msg.message)

    console.print(table)
    console.print(
        f"\nChecked: {summary.checked_files} files | "
        f"Errors: {len(summary.errors)} | Warnings: {len(summary.warnings)}"
    )

    if len(summary.errors) > 0:
        raise typer.Exit(code=1)


@app.command("catalog")
def catalog(
    data_dir: Path | None = typer.Option(
        None, "--data-dir", help="数据目录（默认使用 settings.data_dir）"
    ),
    output_dir: Path | None = typer.Option(
        None, "--output-dir", help="输出目录（默认 data/_catalog）"
    ),
) -> None:
    """生成 data/_catalog（entities/links/stats）。"""
    dd = data_dir or settings.data_dir
    builder = CatalogBuilder(dd)
    paths = builder.build(output_dir=output_dir)
    console.print(f"✅ 生成完成: {paths.root}")
    console.print(f"- entities: {paths.entities}")
    console.print(f"- links:    {paths.links}")
    console.print(f"- stats:    {paths.stats}")


@app.command("report")
def report(
    data_dir: Path | None = typer.Option(
        None, "--data-dir", help="数据目录（默认使用 settings.data_dir）"
    ),
) -> None:
    """输出覆盖率摘要（基于 catalog/validator）。"""
    dd = data_dir or settings.data_dir
    builder = CatalogBuilder(dd)
    paths = builder.build()
    console.print(f"✅ stats: {paths.stats}")


@app.command("scaffold-scenarios")
def scaffold_scenarios(
    seed_csv: Path = typer.Argument(..., help="场景种子 CSV 路径"),
    data_dir: Path | None = typer.Option(
        None, "--data-dir", help="数据目录（默认使用 settings.data_dir）"
    ),
    overwrite: bool = typer.Option(False, "--overwrite", help="覆盖已存在的文件"),
) -> None:
    """从 CSV 种子批量生成场景 YAML 骨架。"""
    dd = data_dir or settings.data_dir
    scaffold = Scaffold(dd)
    created = scaffold.scaffold_scenarios_from_csv(seed_csv, overwrite=overwrite)
    console.print(f"✅ 生成 {len(created)} 个场景文件")


if __name__ == "__main__":
    app()

