# Project Structure

## Overview

world-professors 采用 **内容与代码分离** 的架构设计:
- **内容仓库**: 存储行业/场景/角色/能力数据(YAML格式)
- **代码仓库**: 存储工具和生成器(Python包)

本文档定义项目的目录结构、命名规范和组织原则。

## Root Directory Structure

```
world-professors/
├── .spec-workflow/              # 规范工作流系统
│   ├── steering/                # 项目指导文档
│   ├── specs/                   # 功能规范
│   ├── templates/               # 模板
│   └── approvals/               # 审批记录
│
├── data/
├── taxonomy/                    # 行业场景分类体系
├── roles/                       # 数字角色库
├── capabilities/                # 能力知识库
├── practices/                   # 最佳实践库
└── plaza/                       # 数字时代广场实体（人物/品牌/产品/榜单）
    ├── catalogs/                # 受控词表
    ├── people/
    ├── brands/
    ├── products/
    ├── rankings/
    │   ├── methods/
    │   └── snapshots/
    ├── ads/                     # 精选位；禁止被排名模块读取
    └── templates/
│
├── src/                         # Python源代码
│   └── world_professors/        # 主包
│       ├── models/              # Pydantic数据模型
│       ├── repositories/        # 数据访问层
│       ├── services/            # 业务逻辑
│       ├── generators/          # 内容生成器
│       ├── cli/                 # CLI命令
│       └── utils/               # 工具函数
│
├── tests/                       # 测试代码
│   ├── unit/                    # 单元测试
│   ├── integration/             # 集成测试
│   └── fixtures/                # 测试数据
│
├── wiki/                        # 生成的维基页面(Markdown)
│   ├── industries/              # 行业导航页
│   ├── scenarios/               # 场景详解页
│   ├── roles/                   # 角色详解页
│   ├── capabilities/            # 能力详解页
│   └── index.md                 # 首页
│
├── docs/                        # 项目文档(开发者)
│   ├── architecture/            # 架构设计文档
│   ├── guides/                  # 开发指南
│   └── api/                     # API文档(自动生成)
│
├── scripts/                     # 辅助脚本
│   ├── data-import/             # 数据导入脚本
│   ├── validation/              # 数据验证脚本
│   └── deploy/                  # 部署脚本
│
├── .github/                     # GitHub配置
│   ├── workflows/               # CI/CD流程
│   └── ISSUE_TEMPLATE/          # Issue模板
│
├── pyproject.toml               # Poetry项目配置
├── poetry.lock                  # 依赖锁定文件
├── README.md                    # 项目说明
├── CLAUDE.md                    # AI辅助开发指南
├── CONTRIBUTING.md              # 贡献指南
└── LICENSE                      # 开源许可证
```

## Detailed Structure

### 1. Content Data (`data/`)

内容数据是项目的核心资产,采用Git进行版本管理。

#### 1.1 Taxonomy (行业场景分类)

```
data/taxonomy/
├── industries.yaml              # 行业分类主索引
│   # 结构: id, name, description, sub-industries[]
│
├── scenarios/                   # 场景定义目录
│   ├── finance/                 # 金融行业
│   │   ├── wealth-management/
│   │   │   ├── scenario.yaml    # 场景元数据
│   │   │   └── value-flow.yaml  # 价值流定义
│   │   ├── investment-research/
│   │   └── risk-management/
│   │
│   ├── technology/              # 科技行业
│   │   ├── software-development/
│   │   ├── product-management/
│   │   └── data-engineering/
│   │
│   └── consulting/              # 咨询行业
│       ├── strategy-consulting/
│       └── it-consulting/
│
└── README.md                    # 分类体系说明文档
```

**文件命名规范**:
- 目录名: 小写字母 + 连字符 (e.g., `wealth-management`)
- 文件名: 功能描述 (e.g., `scenario.yaml`, `value-flow.yaml`)

#### 1.2 Roles (数字角色库)

```
data/roles/
├── role-ontology.yaml           # 角色本体定义(类型体系)
│   # 定义: traditional, ai-enhanced, emerging, ai-agent
│
└── by-industry/                 # 按行业组织
    ├── finance/
    │   └── wealth-management/   # 按场景组织
    │       ├── traditional/
    │       │   ├── wealth-advisor.yaml
    │       │   └── portfolio-manager.yaml
    │       │
    │       ├── ai-enhanced/
    │       │   ├── ai-wealth-advisor.yaml
    │       │   └── ai-portfolio-analyst.yaml
    │       │
    │       ├── emerging/
    │       │   └── ai-investment-strategist.yaml
    │       │
    │       └── ai-agents/
    │           └── auto-rebalancing-agent.yaml
    │
    └── technology/
        └── software-development/
            ├── traditional/
            ├── ai-enhanced/
            └── ai-agents/
```

**角色ID命名规范**:
- 格式: `{industry-abbr}-{scenario-abbr}-{role-type}-{name}`
- 示例: `fin-wm-ai-advisor` (finance - wealth management - ai-enhanced - advisor)

#### 1.3 Capabilities (能力知识库)

```
data/capabilities/
├── capability-catalog.yaml      # 能力总目录(索引)
│   # 字段: id, name, category, subcategory, applicable-roles[]
│
├── core-skills/                 # 核心技能定义
│   ├── cognitive/               # 认知能力
│   │   ├── critical-thinking.yaml
│   │   ├── systems-thinking.yaml
│   │   └── creative-problem-solving.yaml
│   │
│   ├── technical/               # 技术能力
│   │   ├── ai-literacy/
│   │   │   ├── prompt-engineering.yaml
│   │   │   ├── ai-tool-mastery.yaml
│   │   │   └── ai-workflow-design.yaml
│   │   │
│   │   ├── data-analysis/
│   │   └── programming/
│   │
│   ├── interpersonal/           # 人际能力
│   │   ├── communication.yaml
│   │   ├── collaboration.yaml
│   │   └── leadership.yaml
│   │
│   └── domain-specific/         # 领域专业能力
│       ├── finance/
│       │   ├── financial-modeling.yaml
│       │   ├── risk-assessment.yaml
│       │   └── market-analysis.yaml
│       │
│       └── technology/
│           ├── software-architecture.yaml
│           └── devops.yaml
│
├── competency-matrix/           # 能力矩阵(角色×能力)
│   └── by-role/
│       ├── fin-wm-ai-advisor.yaml
│       └── tech-sd-ai-engineer.yaml
│
└── learning-paths/              # 学习路径
    ├── prompt-engineering/
    │   ├── path.yaml            # 学习路径定义
    │   └── resources.yaml       # 资源清单
    │
    └── ai-literacy/
        ├── beginner-path.yaml
        ├── intermediate-path.yaml
        └── advanced-path.yaml
```

**能力ID命名规范**:
- 格式: `cap-{category-abbr}-{序号}`
- 示例: `cap-ai-001` (AI相关能力第1个)

#### 1.4 Practices (最佳实践库)

```
data/practices/
├── ai-patterns/                 # AI应用模式
│   ├── automation/
│   │   ├── pattern-definition.yaml
│   │   └── examples/
│   │       ├── email-auto-reply.yaml
│   │       └── report-generation.yaml
│   │
│   ├── augmentation/            # 增强模式
│   ├── generation/              # 生成模式
│   └── orchestration/           # 编排模式
│
├── transformation-cases/        # 流程变革案例
│   └── by-industry/
│       ├── finance/
│       │   └── wealth-management/
│       │       ├── case-001-ai-portfolio.yaml
│       │       └── case-002-robo-advisor.yaml
│       │
│       └── technology/
│
└── toolkits/                    # 工具技术栈
    └── by-role/
        ├── ai-wealth-advisor/
        │   ├── toolkit.yaml     # 工具清单
        │   └── workflows.yaml   # 工作流定义
        │
        └── ai-engineer/
            └── toolkit.yaml
```

### 2. Source Code (`src/world_professors/`)

Python包采用分层架构设计。

```
src/world_professors/
├── __init__.py
├── __version__.py
│
├── models/                      # 数据模型层(Pydantic)
│   ├── __init__.py
│   ├── base.py                  # 基础模型类
│   ├── taxonomy.py              # Industry, Scenario, ValueFlow
│   ├── role.py                  # Role, RoleType, Responsibility
│   ├── capability.py            # Capability, SkillLevel, LearningPath
│   └── practice.py              # AIPattern, Case, Toolkit
│
├── schemas/                     # JSON Schema定义
│   ├── scenario-schema.json
│   ├── role-schema.json
│   └── capability-schema.json
│
├── repositories/                # 数据访问层(Repository Pattern)
│   ├── __init__.py
│   ├── base.py                  # BaseRepository
│   ├── taxonomy_repo.py         # TaxonomyRepository
│   ├── role_repo.py             # RoleRepository
│   └── capability_repo.py       # CapabilityRepository
│
├── services/                    # 业务逻辑层
│   ├── __init__.py
│   ├── graph_builder.py         # 能力图谱构建
│   ├── path_planner.py          # 学习路径规划
│   ├── pattern_matcher.py       # 模式匹配引擎
│   └── validator.py             # 数据验证服务
│
├── generators/                  # 内容生成器
│   ├── __init__.py
│   ├── base.py                  # BaseGenerator
│   ├── wiki_generator.py        # 维基页面生成
│   ├── report_generator.py      # 报告生成
│   └── templates/               # Jinja2模板
│       ├── industry-page.md.j2
│       ├── scenario-page.md.j2
│       ├── role-page.md.j2
│       └── capability-page.md.j2
│
├── cli/                         # CLI命令(Typer)
│   ├── __init__.py
│   ├── app.py                   # 主CLI应用
│   ├── commands/
│   │   ├── __init__.py
│   │   ├── validate.py          # wp validate命令
│   │   ├── generate.py          # wp generate命令
│   │   ├── explore.py           # wp explore命令
│   │   └── plan.py              # wp plan命令
│   └── utils/
│       ├── console.py           # Rich控制台配置
│       └── formatters.py        # 输出格式化
│
├── utils/                       # 工具函数
│   ├── __init__.py
│   ├── file_io.py               # 文件读写(YAML/JSON)
│   ├── id_generator.py          # ID生成工具
│   └── graph_utils.py           # 图处理工具
│
└── config/                      # 配置管理
    ├── __init__.py
    ├── settings.py              # 全局设置(Pydantic Settings)
    └── constants.py             # 常量定义
```

### 3. Tests (`tests/`)

测试代码与源代码结构对应。

```
tests/
├── conftest.py                  # Pytest配置和fixtures
│
├── unit/                        # 单元测试
│   ├── models/
│   │   ├── test_taxonomy.py
│   │   ├── test_role.py
│   │   └── test_capability.py
│   │
│   ├── repositories/
│   ├── services/
│   └── generators/
│
├── integration/                 # 集成测试
│   ├── test_data_loading.py
│   ├── test_wiki_generation.py
│   └── test_graph_building.py
│
└── fixtures/                    # 测试数据
    ├── sample-scenario.yaml
    ├── sample-role.yaml
    └── sample-capability.yaml
```

### 4. Generated Wiki (`wiki/`)

由生成器自动创建的维基页面。

```
wiki/
├── index.md                     # 首页(导航入口)
│
├── industries/                  # 行业导航页
│   ├── index.md                 # 行业总览
│   ├── finance.md
│   ├── technology.md
│   └── consulting.md
│
├── scenarios/                   # 场景详解页
│   ├── finance/
│   │   ├── wealth-management.md
│   │   ├── investment-research.md
│   │   └── risk-management.md
│   └── technology/
│       └── software-development.md
│
├── roles/                       # 角色详解页
│   ├── by-type/                 # 按类型分类
│   │   ├── traditional.md
│   │   ├── ai-enhanced.md
│   │   ├── emerging.md
│   │   └── ai-agents.md
│   │
│   └── by-industry/             # 按行业分类
│       ├── finance/
│       │   └── wealth-management/
│       │       ├── wealth-advisor.md
│       │       └── ai-wealth-advisor.md
│       └── technology/
│
├── capabilities/                # 能力详解页
│   ├── index.md                 # 能力总览
│   ├── catalog/                 # 能力目录
│   │   ├── cognitive.md
│   │   ├── technical.md
│   │   ├── interpersonal.md
│   │   └── domain-specific.md
│   │
│   └── learning-paths/          # 学习路径
│       ├── ai-literacy.md
│       └── data-analysis.md
│
└── practices/                   # 最佳实践
    ├── ai-patterns/
    │   ├── automation.md
    │   ├── augmentation.md
    │   ├── generation.md
    │   └── orchestration.md
    │
    └── cases/
        └── finance/
            └── ai-wealth-management.md
```

## Naming Conventions

### 文件命名

**数据文件**(YAML):
- 使用小写字母
- 单词间用连字符 `-`
- 描述性命名
- 示例: `wealth-management.yaml`, `ai-literacy.yaml`

**Python文件**:
- 使用小写字母
- 单词间用下划线 `_`
- 模块名简洁明了
- 示例: `role_repo.py`, `wiki_generator.py`

**Markdown文件**:
- 使用小写字母
- 单词间用连字符 `-`
- 与数据文件对应
- 示例: `wealth-management.md`

### ID命名规范

**场景ID**:
- 格式: `{industry-abbr}-{scenario-name}-{序号}`
- 示例: `fin-wm-001` (finance - wealth management - 001)

**角色ID**:
- 格式: `{industry}-{scenario}-{type}-{name}`
- 示例: `fin-wm-ai-advisor`

**能力ID**:
- 格式: `cap-{category}-{序号}`
- 示例: `cap-ai-001`, `cap-fin-012`

**案例ID**:
- 格式: `case-{industry}-{scenario}-{序号}`
- 示例: `case-fin-wm-001`

### 代码命名

**类名**: PascalCase
- 示例: `RoleRepository`, `WikiGenerator`, `CapabilityGraph`

**函数名**: snake_case
- 示例: `load_scenario()`, `generate_wiki_page()`, `build_capability_graph()`

**常量**: UPPER_SNAKE_CASE
- 示例: `DEFAULT_DATA_DIR`, `MAX_DEPTH`, `SUPPORTED_FORMATS`

**私有成员**: 前缀 `_`
- 示例: `_validate_schema()`, `_load_cache()`

## Configuration Management

### 环境配置

使用 `.env` 文件管理环境特定配置(不入库):

```bash
# .env (示例)
DATA_DIR=/path/to/data
WIKI_OUTPUT_DIR=/path/to/wiki
OPENAI_API_KEY=sk-xxx
LOG_LEVEL=INFO
```

### 应用配置

使用 `config/settings.py` (Pydantic Settings):

```python
# src/world_professors/config/settings.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    data_dir: Path = Path("data")
    wiki_output_dir: Path = Path("wiki")
    log_level: str = "INFO"
    openai_api_key: str | None = None

    class Config:
        env_file = ".env"

settings = Settings()
```

## Data Organization Principles

### 1. 单一数据源(Single Source of Truth)

- YAML文件是唯一权威数据源
- 生成的内容(Wiki, JSON)都从YAML派生
- Git追踪所有YAML变更历史

### 2. 关注点分离(Separation of Concerns)

- 内容(`data/`) vs 代码(`src/`)
- 原始数据 vs 生成内容
- 配置 vs 业务逻辑

### 3. 可发现性(Discoverability)

- 清晰的目录层级
- 描述性的文件名
- 索引文件(如`industries.yaml`, `capability-catalog.yaml`)

### 4. 可扩展性(Extensibility)

- 按行业/场景分目录,支持无限扩展
- 插件式生成器架构
- 模板化内容生成

### 5. 版本控制友好(Git-Friendly)

- 一个文件一个实体(场景/角色/能力)
- 避免大JSON文件(难以diff)
- 有意义的commit粒度

## File Organization Best Practices

### 何时创建新目录?

**创建新目录**:
- ✅ 新增行业(如`data/taxonomy/scenarios/healthcare/`)
- ✅ 新增功能模块(如`src/world_professors/exporters/`)
- ✅ 相关文件超过5个

**避免过度分类**:
- ❌ 单个文件单独一个目录
- ❌ 超过4层的深度嵌套
- ❌ 命名模糊的"misc"或"utils"目录

### 何时拆分文件?

**拆分标准**:
- 单个文件超过500行
- 包含多个不相关的类/函数
- 职责不单一

**保持聚合**:
- 高内聚的功能放在同一文件
- 避免过度碎片化

## Documentation Standards

### 代码文档

**Docstring格式**: Google Style

```python
def generate_wiki_page(role_id: str, output_dir: Path) -> Path:
    """生成角色维基页面.

    Args:
        role_id: 角色ID,格式: {industry}-{scenario}-{type}-{name}
        output_dir: 输出目录路径

    Returns:
        生成的Markdown文件路径

    Raises:
        RoleNotFoundError: 角色ID不存在
        ValidationError: 角色数据验证失败

    Example:
        >>> path = generate_wiki_page("fin-wm-ai-advisor", Path("wiki"))
        >>> print(path)
        wiki/roles/finance/wealth-management/ai-wealth-advisor.md
    """
    pass
```

### 数据文档

**每个数据目录需包含 README.md**:
- 说明该目录的内容和组织方式
- 提供数据schema示例
- 列出关键字段说明

## Migration & Refactoring Guidelines

### 重构原则

1. **小步迭代**: 每次重构改动量控制在可review范围内
2. **测试先行**: 确保有测试覆盖再重构
3. **保持兼容**: 尽量向后兼容,必要时提供迁移脚本
4. **文档同步**: 代码变更后立即更新文档

### 数据迁移

**版本化数据Schema**:
- 在文件中记录schema版本:`schema_version: "1.0"`
- 提供迁移脚本:`scripts/migrate-v1-to-v2.py`
- 支持多版本并存(兼容性窗口)

---

## Quick Reference

### 常用路径

```python
# 在代码中引用
from world_professors.config import settings

DATA_DIR = settings.data_dir
TAXONOMY_DIR = DATA_DIR / "taxonomy"
ROLES_DIR = DATA_DIR / "roles"
CAPABILITIES_DIR = DATA_DIR / "capabilities"
WIKI_DIR = settings.wiki_output_dir
```

### 常用命令

```bash
# 验证数据
poetry run wp validate --all

# 生成维基页面
poetry run wp generate wiki --industry finance

# 探索数据
poetry run wp explore roles --industry finance --scenario wealth-management

# 规划学习路径
poetry run wp plan --target-role fin-wm-ai-advisor
```

### 新增内容工作流

```bash
# 1. 创建场景数据
touch data/taxonomy/scenarios/finance/new-scenario/scenario.yaml

# 2. 定义角色
touch data/roles/by-industry/finance/new-scenario/ai-enhanced/new-role.yaml

# 3. 验证数据
poetry run wp validate --file data/roles/.../new-role.yaml

# 4. 生成维基页面
poetry run wp generate wiki --role fin-new-new-role

# 5. 提交变更
git add data/ wiki/
git commit -m "feat(finance): add new-scenario and related roles"
```
