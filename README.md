# World Professors 🎓

> AI时代的数字角色与能力维基百科

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Tests](https://img.shields.io/badge/Tests-81%20passed-brightgreen.svg)](#)
[![Coverage](https://img.shields.io/badge/Coverage-80%25-yellow.svg)](#)

## 🌟 项目愿景

在AI快速改变工作形态的时代，**World Professors** 致力于构建一个开放、协作、持续演进的知识体系，帮助：

- **知识工作者**：理解自己角色的AI转型路径
- **职业发展者**：发现高潜力的职业转型方向  
- **企业L&D部门**：设计员工AI能力提升计划
- **教育机构**：设计面向未来的课程体系

## 🏗️ 核心架构

```
┌─────────────────────────────────────────────────────────────┐
│                    行业场景导航系统                          │
│  金融 → 财富管理 → 客户画像 / 方案设计 / 风险监控           │
└──────────────────────────┬──────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│                     数字角色知识库                           │
│  传统角色 → AI增强角色 → 新兴角色 → AI Agent角色            │
└──────────────────────────┬──────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│                      能力知识图谱                            │
│  认知能力 / 技术能力 / 人际能力 / 领域专业能力               │
└──────────────────────────┬──────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│                     AI应用模式库                             │
│  自动化 / 增强 / 生成 / 编排                                 │
└─────────────────────────────────────────────────────────────┘
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

- [项目状态与路线图](docs/project-status-and-roadmap.md)
- [产品愿景](.spec-workflow/steering/product.md)
- [技术架构](.spec-workflow/steering/tech.md)
- [数据模型规范](.spec-workflow/specs/data-models-foundation/)

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
