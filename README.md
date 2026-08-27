# World Professors 🎓

> **数字时代广场** 的产业坐标系 — 行业 × 场景 × 流程 × Agent × 能力 × 工具  
> 产品层覆盖：AI 名人榜 · AI 品牌榜 · AI 产品榜 · AI 行业资产库 · AI 工具库

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Tests](https://img.shields.io/badge/Tests-81%20passed-brightgreen.svg)](#)
[![Coverage](https://img.shields.io/badge/Coverage-81%25-yellow.svg)](#)

## 🌟 项目定位

**World Professors** 是广场的知识层：**行业 Agent 标准库**，为人和 Agent 提供同一套场景坐标。

**数字时代广场** 是产品层：把标准库变成可被看见、认领、订阅和调用的公共广场。

| 核心价值 | 描述 |
|---------|------|
| 🏭 **行业标准化** | 统一的行业分类和场景定义 |
| 🔄 **流程标准化** | 每个场景的标准工作流程和步骤 |
| 🤖 **Agent标准化** | Agent的能力边界、工具集、行为约束 |
| 🛠️ **工具标准化** | 工具接口、参数、认证的统一规范 |
| 📊 **能力标准化** | 可量化、可评估的能力等级体系 |
| 🏛️ **广场五馆** | 名人 / 品牌 / 产品 / 行业资产 / 工具，全部挂在场景上 |

规划全文：[docs/plaza](docs/plaza/README.md)（愿景、商业模式、产品、数据模型、GTM）  
可点击 Demo：[demo/plaza](demo/plaza/README.md)（对标 Success.ai 工作台语法）

**使用场景**：当你需要构建一个"金融投顾Agent"时，直接查询标准库获取：
- 该场景的标准工作流程是什么？
- Agent需要哪些能力？使用哪些工具？
- 有什么行为约束和合规要求？

打开同一场景的广场街区时，还应看到：该场景下该关注谁、用哪类产品、哪些工具可被编排。

## 🏗️ 核心模型链路

```
Industry (行业)
    │ 金融服务 / 科技互联网 / 医疗健康 / 制造业
    ↓
Scenario (场景)
    │ 财富管理 / 投资研究 / 风险控制 / 客户服务
    ↓
Workflow (流程) ⭐
    │ 客户画像流程 / 方案设计流程 / 风险评估流程
    │ └── Step → Step → Step (输入/输出/工具)
    ↓
Agent (智能体) ⭐
    │ 投顾Agent / 研报Agent / 风控Agent
    │ ├── 能力集 (capabilities)
    │ ├── 工具集 (tools)
    │ ├── 可执行流程 (workflows)
    │ └── 行为约束 (constraints)
    ↓
Capability (能力)          Tool (工具) ⭐
    │ 金融分析                 │ 市场数据API
    │ 风险评估                 │ 投组优化器
    │ 客户沟通                 │ 报告生成器
    └──────────┬───────────────┘
               ↓
         (可组合、可复用)
```

## 🚀 快速开始

### 环境要求

- Python 3.11+
- Poetry (包管理器)

### 安装

```bash
# 克隆仓库
git clone https://github.com/your-org/world-professors.git
cd world-professors

# 安装依赖
poetry install

# 验证安装
poetry run python -c "from world_professors.models import Scenario, Role; print('✅ 安装成功!')"
```

### 基本使用

```python
from pathlib import Path
from world_professors.models import Scenario, Role, RoleType
from world_professors.repositories import ScenarioRepository, RoleRepository

# 加载场景数据
scenario_repo = ScenarioRepository(Path("data"))
scenarios = scenario_repo.load_all()

# 加载角色数据  
role_repo = RoleRepository(Path("data"))
ai_enhanced_roles = role_repo.get_by_type(RoleType.AI_ENHANCED)

for role in ai_enhanced_roles:
    print(f"{role.name}: {role.traditional_role} → AI增强版")
```

## 📁 项目结构

```
world-professors/
├── src/world_professors/    # Python主包
│   ├── models/              # 核心数据模型 (Pydantic)
│   ├── repositories/        # 数据访问层
│   ├── services/            # 业务逻辑服务
│   ├── cli/                 # 命令行工具
│   └── generators/          # 内容生成器
│
├── data/                    # 内容数据 (YAML)
│   ├── taxonomy/            # 行业场景分类
│   ├── roles/               # 数字角色定义
│   ├── capabilities/        # 能力定义
│   └── templates/           # 数据模板
│
├── tests/                   # 测试代码
├── docs/                    # 项目文档
└── wiki/                    # 生成的维基页面
```

## 🔧 核心数据模型

### Scenario (场景)

```yaml
# data/taxonomy/scenarios/finance/wealth-management/scenario.yaml
id: fin-wm-001
name: 财富管理咨询
industry: 金融服务
description: 为高净值客户提供个性化资产配置建议

value_flow:
  - stage: 客户画像
    activities: [需求调研, 风险评估, 资产盘点]
  - stage: 方案设计
    activities: [市场分析, 产品筛选, 配置建模]

traditional_pain_points:
  - 人工调研耗时长
  - 方案个性化程度低

ai_opportunities:
  - 智能问卷与画像生成
  - AI驱动的资产配置优化
```

### Role (角色)

```yaml
# data/roles/finance/wealth-management/ai-enhanced/advisor.yaml
id: fin-wm-ai-advisor
name: AI增强型财富顾问
type: ai-enhanced
scenario_ref: fin-wm-001
traditional_role: 传统财富顾问

responsibilities:
  core: [建立客户信任, 最终决策把关]
  delegated_to_ai: [数据收集, 初步方案生成]
  collaborative: [风险评估, 方案优化]

required_capabilities:
  - capability_id: cap-fin-001
    level: expert
  - capability_id: cap-ai-003
    level: intermediate

ai_tools:
  - name: AI资产配置引擎
    purpose: 生成优化的资产组合建议
```

### Capability (能力)

```yaml
# data/capabilities/technical/ai-literacy/prompt-engineering.yaml
id: cap-ai-001
name: Prompt工程
category: technical
sub_category: ai-literacy

levels:
  beginner:
    description: 能编写基础提示词
    skills: [理解AI工具原理, 使用ChatGPT]
  intermediate:
    description: 能设计复杂工作流
    skills: [多步骤提示设计, 上下文管理]
  advanced:
    description: 能优化和调试提示
    skills: [Prompt调优, 评估输出质量]

learning_path:
  prerequisites: [基础数据素养]
  estimated_time: 3个月
  milestones:
    - month: 1
      goal: 掌握3种AI工具
    - month: 3
      goal: 建立个人AI工作流
```

## 🧪 开发指南

### 运行测试

```bash
# 运行所有测试
poetry run pytest tests/ -v

# 运行特定测试
poetry run pytest tests/unit/models/ -v

# 查看覆盖率报告
poetry run pytest tests/ --cov=world_professors --cov-report=html
open htmlcov/index.html
```

### 代码质量

```bash
# Linting
poetry run ruff check src/

# 类型检查
poetry run mypy src/

# 格式化
poetry run black src/ tests/
```

## 📚 文档

- [数字时代广场规划](docs/plaza/README.md)
- [项目状态与路线图](docs/project-status-and-roadmap.md)
- [产品愿景](.spec-workflow/steering/product.md)
- [技术架构](.spec-workflow/steering/tech.md)
- [数据模型规范](.spec-workflow/specs/data-models-foundation/)
- [广场 Spec](.spec-workflow/specs/digital-era-plaza/)

## 🗺️ 路线图

### Phase 1: 基础建设 ✅
- [x] 核心数据模型 (Scenario, Role, Capability)
- [x] Repository数据访问层
- [x] 单元测试覆盖

### Phase 2: 工具完善 🚧
- [ ] 数据验证服务
- [ ] CLI命令行工具
- [ ] 示例数据填充

### Phase 3: 内容生成
- [ ] 维基页面生成器
- [ ] 能力关系图谱可视化
- [ ] 静态站点部署

### Phase 4: 内容扩展
- [ ] 金融行业完整覆盖
- [ ] 科技行业覆盖
- [ ] 开放社区贡献

### Phase 5: 数字时代广场
- [x] 商业模式与产品规划（`docs/plaza/`）
- [x] Person / Brand / Product 模板与旗舰场景样例
- [ ] Pydantic 模型、引用校验、场景聚合页
- [ ] 认领流与双榜快照流水线


## 🤝 贡献指南

我们欢迎各种形式的贡献：

1. **内容贡献**: 添加新的行业场景、角色、能力定义
2. **代码贡献**: 改进工具和功能
3. **文档贡献**: 完善文档和示例

详见 [CONTRIBUTING.md](CONTRIBUTING.md) (待创建)

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE)

---

<p align="center">
  <strong>让每个人都能在AI时代找到自己的位置</strong>
</p>
