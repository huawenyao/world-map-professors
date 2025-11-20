# Tasks: Data Models Foundation

## Task Breakdown

本spec的实施分为6个主要阶段,共32个任务。

---

## Phase 1: 项目基础设施 (3 tasks)

### [ ] 1.1 初始化Python项目结构
**优先级**: P0 (必须)
**预计时间**: 2小时
**依赖**: 无

**子任务**:
- [ ] 创建项目根目录和基本结构
- [ ] 初始化Poetry项目 (`poetry init`)
- [ ] 配置 `pyproject.toml`
  - 项目元数据
  - 依赖声明
  - 开发工具配置 (ruff, black, mypy, pytest)
- [ ] 创建 `src/world_professors/` 主包
- [ ] 添加 `__init__.py` 和 `__version__.py`

**验收标准**:
- `poetry install` 成功执行
- 目录结构符合 structure.md 定义
- 可以 `import world_professors`

---

### [ ] 1.2 配置开发工具链
**优先级**: P0
**预计时间**: 1.5小时
**依赖**: 1.1

**子任务**:
- [ ] 配置 ruff (linting)
  - 创建 `pyproject.toml` 中的 `[tool.ruff]` 配置
  - 定义规则集
- [ ] 配置 black (formatting)
  - 行长度: 100
  - 其他格式化选项
- [ ] 配置 mypy (type checking)
  - 严格模式启用
  - 排除测试文件
- [ ] 配置 pytest
  - 测试目录: `tests/`
  - Coverage配置
- [ ] 创建 pre-commit hooks配置

**验收标准**:
- `poetry run ruff check src/` 无错误
- `poetry run black --check src/` 无错误
- `poetry run mypy src/` 无错误
- `poetry run pytest` 可执行(即使没有测试)

---

### [ ] 1.3 创建配置管理模块
**优先级**: P0
**预计时间**: 2小时
**依赖**: 1.1

**实施**:
创建 `src/world_professors/config/settings.py`:

```python
from pydantic_settings import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    # 数据目录
    data_dir: Path = Path("data")
    wiki_output_dir: Path = Path("wiki")

    # 日志配置
    log_level: str = "INFO"
    log_file: Path | None = None

    # API密钥(可选)
    openai_api_key: str | None = None
    anthropic_api_key: str | None = None

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
```

创建 `src/world_professors/config/constants.py`:
- 定义行业列表、能力类别等常量

**验收标准**:
- 可以导入 `from world_professors.config import settings`
- 读取 `.env` 文件(如存在)
- 默认值正确

---

## Phase 2: 核心数据模型 (8 tasks)

### [ ] 2.1 实现Base Model
**优先级**: P0
**预计时间**: 3小时
**依赖**: 1.1, 1.2

**实施**:
创建 `src/world_professors/models/base.py`:
- `Metadata` 模型
- `BaseEntity` 抽象基类
- 通用方法: `to_yaml()`, `to_dict()`, `display_name`

**验收标准**:
- 所有字段有类型注解
- Pydantic验证正常工作
- 单元测试覆盖率 > 90%

**测试文件**: `tests/unit/models/test_base.py`

---

### [ ] 2.2 实现Scenario Model
**优先级**: P0
**预计时间**: 4小时
**依赖**: 2.1

**实施**:
创建 `src/world_professors/models/taxonomy.py`:
- `ValueFlowStage` 嵌套模型
- `Scenario` 主模型
- 自定义验证器:
  - `validate_scenario_id`: ID格式检查
  - `no_self_reference`: 禁止自引用

**验收标准**:
- 所有必填字段和可选字段定义完整
- 验证器正确抛出异常
- 单元测试覆盖率 > 90%

**测试文件**: `tests/unit/models/test_taxonomy.py`

---

### [ ] 2.3 实现Role Model
**优先级**: P0
**预计时间**: 5小时
**依赖**: 2.1

**实施**:
创建 `src/world_professors/models/role.py`:
- 枚举类: `RoleType`, `CapabilityLevel`, `Priority`
- 嵌套模型: `RequiredCapability`, `Responsibilities`, `AITool`, `WorkflowStep`, `TransformationImpact`, `SalaryRange`
- `Role` 主模型
- 自定义验证器:
  - `validate_role_id`: ID格式检查
  - `validate_traditional_role`: ai-enhanced必填检查

**验收标准**:
- 所有字段定义完整
- 验证逻辑正确
- 单元测试覆盖率 > 90%

**测试文件**: `tests/unit/models/test_role.py`

---

### [ ] 2.4 实现Capability Model
**优先级**: P0
**预计时间**: 5小时
**依赖**: 2.1

**实施**:
创建 `src/world_professors/models/capability.py`:
- 枚举类: `CapabilityCategory`, `Transferability`, `AIImpact`
- 嵌套模型: `LevelDefinition`, `LearningResources`, `Milestone`, `LearningPath`, `TransferabilityProfile`
- `Capability` 主模型
- 自定义验证器:
  - `validate_capability_id`: ID格式检查
  - `validate_levels`: 至少两个等级
  - `no_self_reference`: 禁止自引用

**验收标准**:
- 所有字段定义完整
- 验证逻辑正确
- 单元测试覆盖率 > 90%

**测试文件**: `tests/unit/models/test_capability.py`

---

### [ ] 2.5 实现Practice Models
**优先级**: P1 (重要)
**预计时间**: 4小时
**依赖**: 2.1

**实施**:
创建 `src/world_professors/models/practice.py`:
- `AIPatternType` 枚举
- `AIPattern` 模型
- `ProcessState`, `ROI` 嵌套模型
- `TransformationCase` 模型

**验收标准**:
- 模型定义完整
- 单元测试覆盖率 > 80%

**测试文件**: `tests/unit/models/test_practice.py`

---

### [ ] 2.6 创建模型索引 (`__init__.py`)
**优先级**: P0
**预计时间**: 0.5小时
**依赖**: 2.1, 2.2, 2.3, 2.4, 2.5

**实施**:
创建 `src/world_professors/models/__init__.py`:

```python
from .base import BaseEntity, Metadata
from .taxonomy import Scenario, ValueFlowStage
from .role import (
    Role,
    RoleType,
    RequiredCapability,
    Responsibilities,
    # ... 其他导出
)
from .capability import (
    Capability,
    CapabilityCategory,
    LearningPath,
    # ... 其他导出
)
from .practice import AIPattern, TransformationCase

__all__ = [
    "BaseEntity",
    "Metadata",
    "Scenario",
    # ... 所有公开类
]
```

**验收标准**:
- 可以 `from world_professors.models import Scenario, Role, Capability`
- IDE自动补全正常

---

### [ ] 2.7 生成JSON Schema文件
**优先级**: P1
**预计时间**: 2小时
**依赖**: 2.2, 2.3, 2.4

**实施**:
创建 `scripts/generate_schemas.py`:
- 使用 `model.model_json_schema()` 生成
- 输出到 `src/world_professors/schemas/`
- 美化JSON格式(indent=2)

**验收标准**:
- 生成4个JSON Schema文件:
  - `scenario-schema.json`
  - `role-schema.json`
  - `capability-schema.json`
  - `practice-schema.json`
- Schema可被jsonschema库验证

---

### [ ] 2.8 创建YAML模板文件
**优先级**: P1
**预计时间**: 2小时
**依赖**: 2.2, 2.3, 2.4

**实施**:
创建模板目录 `data/templates/`:
- `scenario-template.yaml`
- `role-template.yaml`
- `capability-template.yaml`

每个模板包含:
- 所有必填字段(带说明注释)
- 常用可选字段(注释掉)
- 示例值

**验收标准**:
- 模板填写后可通过验证
- 注释清晰易懂

---

## Phase 3: 数据访问层 (5 tasks)

### [ ] 3.1 实现Base Repository
**优先级**: P0
**预计时间**: 3小时
**依赖**: 2.6

**实施**:
创建 `src/world_professors/repositories/base.py`:
- `BaseRepository[T]` 泛型类
- 方法: `load()`, `load_all()`, `save()`, `get_by_id()`
- YAML序列化/反序列化
- 错误处理

**验收标准**:
- 泛型类型正确
- 可以读写YAML文件
- 单元测试覆盖率 > 85%

**测试文件**: `tests/unit/repositories/test_base.py`

---

### [ ] 3.2 实现Scenario Repository
**优先级**: P0
**预计时间**: 2小时
**依赖**: 3.1, 2.2

**实施**:
创建 `src/world_professors/repositories/scenario_repo.py`:
- `ScenarioRepository(BaseRepository[Scenario])`
- `_build_index()`: 构建ID索引
- `get_by_id()`, `get_by_industry()`, `get_by_tags()`

**验收标准**:
- 查询方法正常工作
- 集成测试通过

**测试文件**: `tests/integration/test_scenario_repo.py`

---

### [ ] 3.3 实现Role Repository
**优先级**: P0
**预计时间**: 2.5小时
**依赖**: 3.1, 2.3

**实施**:
创建 `src/world_professors/repositories/role_repo.py`:
- `RoleRepository(BaseRepository[Role])`
- `get_by_scenario()`, `get_by_type()`, `get_by_industry()`

**验收标准**:
- 查询方法正常工作
- 集成测试通过

**测试文件**: `tests/integration/test_role_repo.py`

---

### [ ] 3.4 实现Capability Repository
**优先级**: P0
**预计时间**: 2.5小时
**依赖**: 3.1, 2.4

**实施**:
创建 `src/world_professors/repositories/capability_repo.py`:
- `CapabilityRepository(BaseRepository[Capability])`
- `get_by_category()`, `get_related()`, `get_prerequisites()`

**验收标准**:
- 查询方法正常工作
- 集成测试通过

**测试文件**: `tests/integration/test_capability_repo.py`

---

### [ ] 3.5 创建Repository工厂
**优先级**: P2 (可选)
**预计时间**: 1小时
**依赖**: 3.2, 3.3, 3.4

**实施**:
创建 `src/world_professors/repositories/__init__.py`:

```python
from pathlib import Path
from .scenario_repo import ScenarioRepository
from .role_repo import RoleRepository
from .capability_repo import CapabilityRepository

class RepositoryFactory:
    def __init__(self, data_dir: Path):
        self.data_dir = data_dir
        self._scenarios = None
        self._roles = None
        self._capabilities = None

    @property
    def scenarios(self) -> ScenarioRepository:
        if self._scenarios is None:
            self._scenarios = ScenarioRepository(self.data_dir)
        return self._scenarios

    # ... 其他repositories
```

**验收标准**:
- 单例模式正常工作
- 延迟加载生效

---

## Phase 4: 验证服务 (4 tasks)

### [ ] 4.1 实现核心验证服务
**优先级**: P0
**预计时间**: 4小时
**依赖**: 3.2, 3.3, 3.4

**实施**:
创建 `src/world_professors/services/validator.py`:
- `ValidationResult` 数据类
- `DataValidator` 类
- `validate_file()`: 验证单文件
- `validate_directory()`: 批量验证

**验收标准**:
- 返回详细的错误和警告
- 性能: 单文件验证 < 100ms
- 单元测试覆盖率 > 85%

**测试文件**: `tests/unit/services/test_validator.py`

---

### [ ] 4.2 实现引用完整性检查
**优先级**: P0
**预计时间**: 3小时
**依赖**: 4.1

**实施**:
在 `DataValidator` 中添加:
- `_validate_role_references()`: 检查scenario_ref和capability_id
- `_validate_scenario_references()`: 检查related_scenarios
- `_validate_capability_references()`: 检查prerequisites和related

**验收标准**:
- 所有引用错误被检测
- 友好的错误提示(包含行号)

---

### [ ] 4.3 实现循环依赖检测
**优先级**: P1
**预计时间**: 3小时
**依赖**: 4.1

**实施**:
创建 `src/world_professors/services/graph_utils.py`:
- `build_dependency_graph()`: 构建依赖图(NetworkX)
- `detect_cycles()`: DFS检测环
- 集成到 `DataValidator._check_circular_dependencies()`

**验收标准**:
- 正确检测简单环(A→B→A)
- 正确检测复杂环(A→B→C→A)
- 性能: 500节点图 < 1s

---

### [ ] 4.4 创建验证报告生成器
**优先级**: P1
**预计时间**: 2小时
**依赖**: 4.1

**实施**:
在 `DataValidator` 中添加:
- `generate_report()`: 生成验证报告(Markdown/HTML)
- 统计信息: 总文件数、通过率、错误分类

**验收标准**:
- 生成可读的Markdown报告
- 包含错误摘要和详情

---

## Phase 5: CLI工具 (6 tasks)

### [ ] 5.1 创建CLI应用框架
**优先级**: P0
**预计时间**: 2小时
**依赖**: 1.1

**实施**:
创建 `src/world_professors/cli/app.py`:

```python
import typer
from rich.console import Console

app = typer.Typer(
    name="wp",
    help="World Professors - AI时代数字角色维基百科工具集"
)
console = Console()

@app.command()
def version():
    """显示版本信息"""
    from world_professors import __version__
    console.print(f"world-professors version {__version__}")

if __name__ == "__main__":
    app()
```

在 `pyproject.toml` 中添加:
```toml
[tool.poetry.scripts]
wp = "world_professors.cli.app:app"
```

**验收标准**:
- `poetry run wp --help` 正常显示
- `poetry run wp version` 显示版本号

---

### [ ] 5.2 实现 validate 命令
**优先级**: P0
**预计时间**: 3小时
**依赖**: 5.1, 4.1

**实施**:
创建 `src/world_professors/cli/commands/validate.py`:
- `wp validate file <path>`: 验证单文件
- `wp validate directory <path>`: 批量验证
- Rich表格输出验证报告

**验收标准**:
- 命令正常执行
- 输出美观(Rich格式)
- 退出码正确(成功0,失败1)

---

### [ ] 5.3 实现 create 命令
**优先级**: P1
**预计时间**: 3小时
**依赖**: 5.1, 2.6

**实施**:
创建 `src/world_professors/cli/commands/create.py`:
- `wp create scenario`: 从模板创建场景
- `wp create role`: 从模板创建角色
- `wp create capability`: 从模板创建能力
- 交互式填写必填字段

**验收标准**:
- 创建的文件通过验证
- 交互式体验流畅

---

### [ ] 5.4 实现 explore 命令
**优先级**: P2
**预计时间**: 2小时
**依赖**: 5.1, 3.5

**实施**:
创建 `src/world_professors/cli/commands/explore.py`:
- `wp explore scenarios`: 浏览所有场景
- `wp explore roles --industry <industry>`: 浏览角色
- `wp explore capabilities --category <cat>`: 浏览能力
- Rich表格展示

**验收标准**:
- 数据展示完整
- 支持过滤和排序

---

### [ ] 5.5 实现 stats 命令
**优先级**: P2
**预计时间**: 2小时
**依赖**: 5.1, 3.5

**实施**:
创建 `src/world_professors/cli/commands/stats.py`:
- `wp stats`: 显示数据统计
  - 场景数量(按行业)
  - 角色数量(按类型)
  - 能力数量(按类别)
  - 覆盖率指标

**验收标准**:
- 统计数据准确
- 可视化展示(Rich图表)

---

### [ ] 5.6 完善CLI帮助文档
**优先级**: P1
**预计时间**: 1小时
**依赖**: 5.2, 5.3, 5.4, 5.5

**实施**:
- 为每个命令添加详细的 `--help` 文本
- 添加使用示例
- 创建 `docs/cli-reference.md`

**验收标准**:
- 每个命令的帮助信息清晰
- 包含示例用法

---

## Phase 6: 示例数据与文档 (6 tasks)

### [ ] 6.1 创建Scenario示例数据
**优先级**: P0
**预计时间**: 3小时
**依赖**: 2.2

**实施**:
创建至少2个完整的场景示例:
1. `data/taxonomy/scenarios/finance/wealth-management/scenario.yaml`
2. `data/taxonomy/scenarios/technology/software-development/scenario.yaml`

每个包含:
- 完整的必填字段
- 丰富的可选字段
- 真实的价值流定义

**验收标准**:
- 通过Schema验证
- 数据真实可信

---

### [ ] 6.2 创建Role示例数据
**优先级**: P0
**预计时间**: 4小时
**依赖**: 2.3, 6.1

**实施**:
为每个场景创建4种角色示例(traditional, ai-enhanced, emerging, ai-agent):
- `data/roles/by-industry/finance/wealth-management/traditional/wealth-advisor.yaml`
- `data/roles/by-industry/finance/wealth-management/ai-enhanced/ai-wealth-advisor.yaml`
- ... (共8个角色)

**验收标准**:
- 通过Schema和引用验证
- 职责分配合理
- AI工具真实存在

---

### [ ] 6.3 创建Capability示例数据
**优先级**: P0
**预计时间**: 4小时
**依赖**: 2.4

**实施**:
创建至少10个能力示例,覆盖4个类别:
- `data/capabilities/core-skills/cognitive/critical-thinking.yaml`
- `data/capabilities/core-skills/technical/ai-literacy/prompt-engineering.yaml`
- `data/capabilities/core-skills/domain-specific/finance/financial-modeling.yaml`
- ... (共10个)

**验收标准**:
- 通过Schema验证
- 等级定义完整
- 学习路径可操作

---

### [ ] 6.4 生成Schema参考文档
**优先级**: P1
**预计时间**: 2小时
**依赖**: 2.7

**实施**:
创建 `scripts/generate_schema_docs.py`:
- 从JSON Schema生成Markdown文档
- 输出到 `docs/schemas/`
- 包含字段说明、类型、示例

**验收标准**:
- 生成4个Schema文档
- 文档可读性好

---

### [ ] 6.5 编写数据建模最佳实践指南
**优先级**: P1
**预计时间**: 3小时
**依赖**: 6.1, 6.2, 6.3

**实施**:
创建 `docs/data-modeling-guide.md`:
- 如何设计好的场景定义
- 角色职责划分原则
- 能力等级定义标准
- 常见错误和解决方案
- ID命名规范
- 引用管理技巧

**验收标准**:
- 内容实用可操作
- 包含真实示例

---

### [ ] 6.6 创建快速开始教程
**优先级**: P1
**预计时间**: 2小时
**依赖**: 所有Phase 5任务

**实施**:
创建 `docs/quickstart.md`:
1. 安装项目
2. 验证示例数据
3. 创建第一个场景
4. 创建第一个角色
5. 探索数据
6. 生成报告

**验收标准**:
- 新用户可以在30分钟内完成
- 所有命令可执行

---

## Summary

**总任务数**: 32
**预计总时长**: 80-90 小时

**关键里程碑**:
1. ✅ Phase 1完成: 可以运行基础Python项目
2. ✅ Phase 2完成: 核心数据模型可用
3. ✅ Phase 3完成: 可以读写YAML数据
4. ✅ Phase 4完成: 数据验证功能完备
5. ✅ Phase 5完成: CLI工具可用
6. ✅ Phase 6完成: 示例数据和文档齐全

**开发顺序建议**:
1. 严格按Phase顺序执行
2. 每完成一个Phase进行集成测试
3. Phase 2-4可部分并行(不同开发者)
4. Phase 6可与Phase 5并行

**测试策略**:
- 单元测试: 每个任务完成后立即编写
- 集成测试: 每个Phase完成后执行
- 端到端测试: Phase 5完成后执行

**风险缓解**:
- Phase 2耗时可能超预期 → 预留buffer时间
- 数据示例创建需要领域知识 → 提前研究
- CLI用户体验需要迭代 → 尽早获取反馈
