# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目愿景

**world-professors** 是一个 **AI时代的数字角色与能力维基百科**,以行业场景为目录树组织结构。

### 核心定位
这不是传统的行业分类研究,而是一个面向AI时代的**角色能力知识库**:
- **维基特性**: 开放、协作、持续演进的知识体系
- **数字角色**: 定义AI时代各行业中的工作角色及其能力画像
- **能力体系**: 构建可量化、可学习、可转移的能力模型
- **场景驱动**: 以真实行业场景为索引和组织框架

### 类比理解
- **传统维基百科**: 收录概念、人物、事件等知识条目
- **本项目**: 收录AI时代的数字角色、能力技能、应用场景等实践知识

## 项目目标

### 1. 构建行业场景目录树
基于权威行业分类体系(申万、GICS、Wind等),提炼出:
- **行业分类层级**: 作为知识组织的主干结构
- **场景分类法**: 每个行业下的典型业务场景
- **价值流视角**: 从价值创造流程识别关键场景节点

### 2. 定义数字角色体系
在每个行业场景中识别和定义:
- **传统角色**: 现有的人类工作角色
- **AI增强角色**: AI辅助下的升级角色
- **新兴角色**: AI催生的全新角色
- **AI Agent角色**: 完全由AI承担的自主角色

### 3. 构建能力知识图谱
为每个角色定义:
- **核心能力**: 角色必备的关键能力
- **能力要素**: 能力的可分解组成部分
- **能力等级**: 从初级到专家的成长路径
- **能力迁移**: 跨场景、跨行业的可复用性

### 4. 沉淀最佳实践模式
记录和提炼:
- **AI应用模式**: 各场景下AI的典型应用方式
- **流程变革案例**: 传统流程→AI流程的转型实例
- **能力培养路径**: 如何获得和提升特定能力
- **工具技术栈**: 支撑角色能力的技术和工具

## 项目架构

### 当前状态
项目使用 **Spec Workflow** 系统进行规范化开发管理,目前处于初始化阶段:

```
world-professors/
├── .spec-workflow/          # 规范工作流系统
│   ├── templates/           # 默认模板
│   ├── user-templates/      # 自定义模板(可覆盖默认)
│   ├── specs/               # 功能规范文档
│   ├── steering/            # 项目指导文档
│   ├── approvals/           # 审批流程
│   └── archive/             # 归档内容
└── CLAUDE.md               # 本文档
```

### 核心架构设计

```
world-professors/
├── taxonomy/                      # 行业场景分类体系
│   ├── industry-tree.json        # 行业目录树(主索引)
│   ├── scenarios/                # 场景定义
│   │   ├── finance/              # 金融行业场景
│   │   ├── healthcare/           # 医疗健康场景
│   │   ├── manufacturing/        # 制造业场景
│   │   └── ...                   # 其他行业
│   └── value-flows/              # 价值流模型
│       └── {industry}/           # 各行业价值流定义
│
├── roles/                         # 数字角色库
│   ├── role-ontology.json        # 角色本体(类型体系)
│   └── {industry}/               # 按行业组织
│       └── {scenario}/           # 按场景组织
│           ├── traditional/      # 传统角色
│           ├── ai-enhanced/      # AI增强角色
│           ├── emerging/         # 新兴角色
│           └── ai-agents/        # AI Agent角色
│
├── capabilities/                  # 能力知识库
│   ├── capability-graph.json     # 能力图谱(关系网络)
│   ├── core-skills/              # 核心技能定义
│   │   ├── cognitive/            # 认知能力
│   │   ├── technical/            # 技术能力
│   │   ├── interpersonal/        # 人际能力
│   │   └── domain-specific/      # 领域专业能力
│   ├── competency-matrix/        # 能力矩阵
│   │   └── {role-id}/            # 每个角色的能力要求
│   └── learning-paths/           # 能力培养路径
│       └── {capability-id}/      # 每项能力的学习路径
│
├── practices/                     # 最佳实践库
│   ├── ai-patterns/              # AI应用模式
│   │   ├── automation/           # 自动化模式
│   │   ├── augmentation/         # 增强模式
│   │   ├── generation/           # 生成模式
│   │   └── orchestration/        # 编排模式
│   ├── transformation-cases/     # 流程变革案例
│   │   └── {industry}/           # 按行业分类
│   │       └── {scenario}/       # 具体场景案例
│   └── toolkits/                 # 工具技术栈
│       └── {role-id}/            # 每个角色的工具集
│
├── wiki/                          # 维基文档(面向用户)
│   ├── industries/               # 行业导航页
│   ├── scenarios/                # 场景详解页
│   ├── roles/                    # 角色详解页
│   ├── capabilities/             # 能力详解页
│   └── guides/                   # 指南和教程
│
├── data/                          # 原始数据和研究资料
│   ├── industry-standards/       # 行业标准文档
│   ├── research/                 # 研究报告
│   └── references/               # 参考资料
│
├── tools/                         # 工具和脚本
│   ├── data-import/              # 数据导入工具
│   ├── graph-builder/            # 图谱构建工具
│   ├── wiki-generator/           # 维基页面生成器
│   └── visualizers/              # 可视化工具
│
└── api/                           # API接口(如需Web服务)
    ├── taxonomy-api/             # 分类查询API
    ├── role-api/                 # 角色查询API
    └── capability-api/           # 能力查询API
```

## 核心数据模型

### 1. 行业场景模型

```yaml
# taxonomy/scenarios/{industry}/{scenario-id}.yaml

scenario:
  id: "fin-wealth-mgmt-001"
  name: "财富管理咨询"
  industry: "金融服务"
  sub-industry: "资产管理"

  description: "为高净值客户提供个性化资产配置建议"

  value-flow:
    - stage: "客户画像"
      activities: ["需求调研", "风险评估", "资产盘点"]
    - stage: "方案设计"
      activities: ["市场分析", "产品筛选", "配置建模"]
    - stage: "执行落地"
      activities: ["产品购买", "账户管理", "风险监控"]
    - stage: "持续服务"
      activities: ["定期复盘", "动态调整", "业绩归因"]

  key-metrics:
    - "客户满意度"
    - "资产年化收益率"
    - "风险调整后收益(Sharpe Ratio)"

  traditional-pain-points:
    - "人工调研耗时长"
    - "方案个性化程度低"
    - "市场跟踪不及时"

  ai-opportunities:
    - "智能问卷与画像生成"
    - "AI驱动的资产配置优化"
    - "实时市场监控与预警"
```

### 2. 数字角色模型

```yaml
# roles/{industry}/{scenario}/ai-enhanced/role-{id}.yaml

role:
  id: "fin-wealth-mgmt-ai-advisor"
  name: "AI增强型财富顾问"
  type: "ai-enhanced"  # traditional | ai-enhanced | emerging | ai-agent

  scenario-ref: "fin-wealth-mgmt-001"

  description: |
    结合AI工具的财富管理顾问,利用AI进行数据分析和方案生成,
    专注于与客户的深度沟通和信任建立。

  traditional-role: "传统财富顾问"

  responsibilities:
    core:  # AI无法替代的核心职责
      - "建立客户信任关系"
      - "理解客户深层需求"
      - "最终方案决策把关"
    delegated-to-ai:  # 委托给AI的职责
      - "数据收集与整理"
      - "初步方案生成"
      - "市场数据监控"
    collaborative:  # 人机协作的职责
      - "风险偏好评估(AI分析+人工确认)"
      - "方案优化调整(AI建议+人工决策)"
      - "业绩归因分析(AI计算+人工解读)"

  required-capabilities:
    - capability-id: "cap-fin-001"  # 金融市场知识
      level: "expert"
    - capability-id: "cap-com-002"  # 客户沟通能力
      level: "expert"
    - capability-id: "cap-ai-003"   # AI工具使用能力
      level: "intermediate"
    - capability-id: "cap-data-004" # 数据解读能力
      level: "intermediate"

  ai-tools:
    - name: "智能客户画像系统"
      purpose: "自动化问卷分析和风险评估"
      vendor: ["内部开发", "第三方API"]
    - name: "AI资产配置引擎"
      purpose: "生成优化的资产组合建议"
      algorithms: ["均值-方差优化", "Black-Litterman模型"]
    - name: "市场情报Agent"
      purpose: "实时监控市场动态和风险事件"

  typical-workflow:
    - step: "AI收集客户信息"
      human-time: "10min"
      ai-time: "实时"
    - step: "人工深度访谈"
      human-time: "60min"
      ai-time: "N/A"
    - step: "AI生成初步方案"
      human-time: "5min(审核)"
      ai-time: "30sec"
    - step: "人工调整和定制化"
      human-time: "30min"
      ai-time: "N/A"
    - step: "AI持续监控和预警"
      human-time: "5min(响应)"
      ai-time: "7×24h"

  transformation-impact:
    efficiency-gain: "3x"  # 效率提升倍数
    quality-improvement: "客户满意度+25%"
    new-capabilities: ["服务更多客户", "更复杂的资产配置"]
    obsolete-skills: ["手工Excel建模", "人工数据收集"]
```

### 3. 能力模型

```yaml
# capabilities/core-skills/technical/cap-ai-003.yaml

capability:
  id: "cap-ai-003"
  name: "AI工具应用能力"
  category: "technical"
  sub-category: "ai-literacy"

  description: |
    在专业工作场景中有效使用AI工具提升工作效率和质量的能力

  levels:
    beginner:
      description: "能使用基础AI工具完成标准任务"
      skills:
        - "理解AI工具的基本原理"
        - "使用ChatGPT等通用AI助手"
        - "编写有效的提示词(prompt)"
      tasks:
        - "用AI生成常规文案"
        - "AI辅助信息检索"

    intermediate:
      description: "能选择和组合多种AI工具解决复杂问题"
      skills:
        - "评估不同AI工具的适用场景"
        - "设计AI工作流和自动化流程"
        - "调试和优化AI输出结果"
      tasks:
        - "构建专业领域的AI助手"
        - "设计多步骤AI工作流"

    advanced:
      description: "能定制和训练AI模型,开发AI应用"
      skills:
        - "微调(fine-tune)现有AI模型"
        - "评估模型性能和改进方向"
        - "设计AI产品和服务"
      tasks:
        - "训练行业专用AI模型"
        - "开发AI驱动的业务系统"

    expert:
      description: "能引领组织的AI战略和创新应用"
      skills:
        - "架构企业级AI能力体系"
        - "评估AI技术前沿趋势"
        - "设计AI驱动的商业模式"
      tasks:
        - "制定企业AI转型战略"
        - "孵化AI创新业务"

  learning-path:
    prerequisites:
      - "基础数据素养"
      - "领域专业知识"

    resources:
      courses:
        - "Andrew Ng - AI For Everyone"
        - "DeepLearning.AI - Prompt Engineering"
      books:
        - "《AI超级个体》"
        - "《Co-Intelligence》"
      practice:
        - "每日AI工具实践(30天计划)"
        - "构建个人AI工作流"

    milestones:
      - month: 1
        goal: "掌握3种AI工具的熟练使用"
      - month: 3
        goal: "建立个人AI工作流,效率提升50%"
      - month: 6
        goal: "能够培训他人使用AI工具"

  related-capabilities:
    - "cap-data-004: 数据解读能力"
    - "cap-sys-005: 系统思维能力"

  applicable-roles:
    - "几乎所有知识工作角色"
    - "重点: 分析师、顾问、创意工作者"
```

## 核心功能模块

### 1. 行业场景导航器
- **功能**: 按行业→场景→价值流节点浏览
- **输出**: 交互式场景目录树
- **技术**: 树形数据结构 + 可视化组件

### 2. 角色能力画像生成器
- **输入**: 行业 + 场景 + 角色类型
- **输出**: 完整角色定义文档
- **包含**: 职责、能力要求、工具栈、工作流

### 3. 能力学习路径规划器
- **输入**: 目标角色或能力清单
- **输出**: 个性化学习计划
- **功能**: 差距分析、资源推荐、里程碑设定

### 4. AI应用模式匹配器
- **输入**: 业务场景描述
- **输出**: 适用的AI应用模式和案例
- **功能**: 模式库检索、案例推荐

### 5. 维基页面生成器
- **输入**: 结构化数据(YAML/JSON)
- **输出**: Markdown维基页面
- **功能**: 模板渲染、交叉引用、索引生成

## Spec Workflow 使用指南

### 初始化项目指导文档

创建三个核心指导文档:

```bash
# .spec-workflow/steering/product.md - 产品愿景
# .spec-workflow/steering/tech.md - 技术栈选择
# .spec-workflow/steering/structure.md - 代码组织规范
```

### 功能开发规范流程

每个功能模块开发遵循四阶段:

**阶段 1: Requirements (需求定义)**
- 明确功能目标和用户价值
- 定义数据模型和接口契约
- 识别技术约束和依赖

**阶段 2: Design (设计方案)**
- 数据结构设计(JSON Schema)
- 算法和业务逻辑设计
- UI/UX设计(如有界面)

**阶段 3: Tasks (任务分解)**
- 拆解为可独立完成的任务
- 定义验收标准
- 估算工作量

**阶段 4: Implementation (实施与日志)**
- 编码实现
- 单元测试
- 使用 `log-implementation` 工具记录

## 开发优先级建议

### Phase 1: 基础设施(Foundation)
1. **行业场景分类体系**
   - Spec: `taxonomy-system`
   - 交付: `industry-tree.json` + 场景定义模板

2. **数据模型定义**
   - Spec: `data-models`
   - 交付: JSON Schema for scenarios/roles/capabilities

3. **样例数据集**
   - Spec: `sample-dataset`
   - 交付: 2-3个行业的完整示例数据

### Phase 2: 核心功能(Core Features)
4. **角色库构建工具**
   - Spec: `role-builder`
   - 交付: CLI工具用于创建和验证角色定义

5. **能力图谱构建器**
   - Spec: `capability-graph`
   - 交付: 能力关系网络和可视化

6. **维基页面生成器**
   - Spec: `wiki-generator`
   - 交付: 自动化Markdown文档生成

### Phase 3: 增值功能(Value-Add Features)
7. **学习路径规划器**
   - Spec: `learning-planner`
   - 交付: 个性化学习计划生成

8. **AI模式匹配引擎**
   - Spec: `pattern-matcher`
   - 交付: 场景→模式的智能推荐

9. **可视化看板**
   - Spec: `visualization-dashboard`
   - 交付: 交互式行业地图和角色网络图

### Phase 4: 生态扩展(Ecosystem)
10. **API服务**
    - Spec: `api-service`
    - 交付: RESTful API for external access

11. **协作编辑系统**
    - Spec: `collaboration-system`
    - 交付: 多人共建知识库的工作流

12. **AI辅助内容生成**
    - Spec: `ai-content-assistant`
    - 交付: 使用LLM辅助创建角色和场景定义

## 技术栈建议

### 数据层
- **格式**: YAML(人类友好) + JSON(机器处理)
- **Schema验证**: JSON Schema / Pydantic
- **存储**: Git仓库(版本控制) + SQLite(查询优化,可选)
- **图数据**: NetworkX(Python) / Neo4j(如需复杂图查询)

### 应用层
- **核心语言**: Python 3.11+ (数据处理和工具开发)
- **CLI框架**: Typer / Click (命令行工具)
- **数据分析**: pandas, numpy
- **图处理**: NetworkX, igraph

### 展示层
- **维基生成**: Jinja2模板 + Markdown
- **静态站点**: MkDocs / VuePress / Docusaurus
- **可视化**: D3.js / Cytoscape.js (网络图)
- **交互组件**: Streamlit / Gradio (快速原型)

### AI/LLM集成
- **LLM调用**: OpenAI API / Anthropic Claude API
- **Prompt工程**: LangChain / LlamaIndex
- **向量检索**: ChromaDB / Pinecone (语义搜索,可选)

### 开发工具
- **代码质量**: ruff(linting) + black(formatting)
- **类型检查**: mypy
- **测试**: pytest
- **文档**: Sphinx / MkDocs

## 数据内容建设策略

### 行业选择优先级

**Tier 1 (优先覆盖):**
- 金融服务: 场景丰富,AI应用成熟
- 科技互联网: AI原生行业
- 专业服务(咨询/法律): 知识密集型

**Tier 2 (次优先):**
- 医疗健康: 高价值但监管复杂
- 制造业: 实体经济代表
- 教育培训: AI影响深远

**Tier 3 (长期规划):**
- 零售电商、文化娱乐、房地产、能源等

### 内容生产流程

```mermaid
graph LR
    A[选择行业] --> B[研究价值流]
    B --> C[识别典型场景]
    C --> D[定义角色体系]
    D --> E[提取能力要求]
    E --> F[收集最佳实践]
    F --> G[生成维基页面]
    G --> H[评审与迭代]
```

### 质量标准

每个场景条目需包含:
- ✅ 清晰的价值流定义
- ✅ 至少3种角色(传统/AI增强/AI Agent)
- ✅ 每个角色的能力画像
- ✅ 至少1个真实案例或最佳实践
- ✅ 可视化流程图或能力图谱

## 关键原则

### KISS (Keep It Simple)
- 数据模型尽量扁平化,避免过度嵌套
- 优先使用标准格式(JSON/YAML/Markdown)
- 工具开发聚焦核心功能

### DRY (Don't Repeat Yourself)
- 能力定义集中管理,角色引用能力ID
- 行业分类作为主索引,避免重复定义
- 模板化内容生成流程

### YAGNI (You Aren't Gonna Need It)
- 初期不构建复杂的Web应用
- 优先静态内容生成,按需添加交互功能
- 避免过早优化数据库和API

### 领域特定原则

**维基精神**: 内容开放、可编辑、版本可追溯
**实用导向**: 每个条目需有实际应用价值
**前瞻性**: 聚焦AI时代的新角色和新能力
**可信度**: 引用权威来源,标注数据来源

## 快速开始

### Step 1: 创建项目指导文档

使用spec-workflow MCP工具或手动创建:
- `product.md`: 详细阐述维基百科的产品愿景
- `tech.md`: 确定技术栈和架构选择
- `structure.md`: 定义目录结构和命名规范

### Step 2: 建立数据模型

创建 Spec: `data-models-foundation`
- 定义 Scenario / Role / Capability 的JSON Schema
- 创建数据验证脚本
- 编写样例数据

### Step 3: 构建第一个行业示例

创建 Spec: `finance-industry-pilot`
- 选择"金融服务"作为首个行业
- 定义3个典型场景(如:财富管理、投资研究、风险控制)
- 每个场景创建5-10个角色
- 提取和定义相关能力

### Step 4: 开发基础工具

创建 Spec: `core-tooling`
- 数据验证工具(validate.py)
- 维基页面生成器(wiki-gen.py)
- 交互式浏览CLI(explore.py)

## 参考资源

### 知识本体设计
- O*NET职业信息网络(美国劳工部)
- European Skills, Competences, Qualifications and Occupations (ESCO)
- LinkedIn Skills Taxonomy

### AI能力框架
- AI Skills Framework (UK Government)
- AI Competency Framework (Various consulting firms)
- Future of Jobs Report (World Economic Forum)

### 行业价值流
- Porter's Value Chain
- Business Process Model and Notation (BPMN)
- Value Stream Mapping (Lean)

### 维基系统设计
- MediaWiki架构
- Notion Database设计
- Obsidian知识图谱

---

**重要提醒**:
本项目是一个**内容密集型**项目,技术开发应服务于内容生产。优先级顺序:
1. 定义清晰的数据模型
2. 建立内容生产流程
3. 开发辅助工具
4. 构建展示系统

所有架构决策应记录在 `.spec-workflow/steering/` 文档中。
