#!/usr/bin/env python3
"""Validate YAML template files against Pydantic models."""

import sys
from pathlib import Path

import yaml

from world_professors.models import Capability, Role, Scenario


def validate_template(template_path: Path, model_class: type) -> bool:
    """Validate a YAML template file against a Pydantic model.

    Args:
        template_path: Path to the YAML template file
        model_class: Pydantic model class to validate against

    Returns:
        True if validation succeeds, False otherwise
    """
    print(f"\n{'='*60}")
    print(f"验证模板: {template_path.name}")
    print(f"模型类: {model_class.__name__}")
    print(f"{'='*60}")

    try:
        # 读取 YAML 文件
        with open(template_path, encoding="utf-8") as f:
            data = yaml.safe_load(f)

        # 验证数据
        instance = model_class.model_validate(data)

        print("✅ 验证通过!")
        print(f"   ID: {instance.id}")
        print(f"   名称: {instance.name}")

        return True

    except Exception as e:
        print("❌ 验证失败!")
        print(f"   错误: {e}")
        return False


def main() -> None:
    """Validate all template files."""
    templates_dir = Path("data/templates")

    if not templates_dir.exists():
        print(f"❌ 模板目录不存在: {templates_dir}")
        sys.exit(1)

    templates = {
        "scenario-template.yaml": Scenario,
        "role-template.yaml": Role,
        "capability-template.yaml": Capability,
    }

    results = []

    for filename, model_class in templates.items():
        template_path = templates_dir / filename

        if not template_path.exists():
            print(f"❌ 模板文件不存在: {filename}")
            results.append(False)
            continue

        success = validate_template(template_path, model_class)
        results.append(success)

    # 汇总结果
    print(f"\n{'='*60}")
    print("验证结果汇总")
    print(f"{'='*60}")
    print(f"总计: {len(results)} 个模板")
    print(f"✅ 通过: {sum(results)} 个")
    print(f"❌ 失败: {len(results) - sum(results)} 个")

    if all(results):
        print("\n🎉 所有模板验证通过!")
        sys.exit(0)
    else:
        print("\n⚠️  部分模板验证失败,请检查!")
        sys.exit(1)


if __name__ == "__main__":
    main()
