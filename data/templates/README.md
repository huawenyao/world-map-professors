# YAML 模板使用指南

本目录包含三个核心实体的 YAML 模板文件,用于快速创建符合规范的数据文件。

## 📁 模板文件列表

| 模板文件 | 用途 | 目标目录 |
|---------|------|---------|
| `scenario-template.yaml` | 业务场景定义 | `data/taxonomy/scenarios/{industry}/` |
| `role-template.yaml` | 数字角色定义 | `data/roles/by-industry/{industry}/` |
| `capability-template.yaml` | 能力/技能定义 | `data/capabilities/core-skills/` |
| 广场人物/品牌/产品/榜单 | 见 `data/plaza/templates/` | `data/plaza/` |

## 🚀 快速开始

### 1. 创建业务场景 (Scenario)

```bash
# 复制模板
cp data/templates/scenario-template.yaml \
   data/taxonomy/scenarios/software/tech-saas-product-001.yaml

# 编辑文件,填写必填字段
# - id: 场景ID (格式: {industry}-{scenario}-{num})
# - name: 场景名称
# - description: 场景描述
# - industry: 所属行业

# 验证文件
world-professors validate scenario data/taxonomy/scenarios/software/tech-saas-product-001.yaml
```

### 2. 创建数字角色 (Role)

```bash
# 复制模板
cp data/templates/role-template.yaml \
   data/roles/by-industry/software/ai-product-manager-001.yaml

# 编辑文件,根据角色类型 (type) 填写:
# - traditional: 传统角色
# - ai-enhanced: AI增强角色 (需要指定 traditional_role)
# - emerging: 新兴角色
# - ai-agent: AI代理角色

# 验证文件
world-professors validate role data/roles/by-industry/software/ai-product-manager-001.yaml
```

### 3. 创建能力定义 (Capability)

```bash
# 复制模板
cp data/templates/capability-template.yaml \
   data/capabilities/core-skills/cap-cognitive-001.yaml

# 编辑文件,注意:
# - id: 格式必须为 cap-{category}-{num}, {num}为3位数字
# - category: cognitive | technical | interpersonal | domain-specific
# - levels: 至少定义2个等级 (beginner/intermediate/advanced/expert)

# 验证文件
world-professors validate capability data/capabilities/core-skills/cap-cognitive-001.yaml
```

## 📋 字段说明

### 必填字段 (REQUIRED)

#### Scenario 场景
- `id`: 唯一标识符,格式 `{industry}-{scenario}-{num}`
- `name`: 场景名称 (最多200字符)
- `description`: 场景描述
- `industry`: 所属行业

#### Role 角色
- `id`: 唯一标识符,格式 `[a-z0-9-]+`
- `name`: 角色名称 (最多200字符)
- `description`: 角色描述
- `type`: 角色类型 (traditional/ai-enhanced/emerging/ai-agent)
- `scenario_ref`: 关联场景ID
- **特殊规则**: `ai-enhanced` 类型必须填写 `traditional_role`

#### Capability 能力
- `id`: 唯一标识符,格式 `cap-{category}-{num}` (num为3位数字,如001)
- `name`: 能力名称 (最多200字符)
- `description`: 能力描述
- `category`: 能力分类 (cognitive/technical/interpersonal/domain-specific)
- `levels`: 等级定义 (至少2个等级)

### 建议填写字段 (RECOMMENDED)

所有模板中带有详细注释的可选字段都建议填写,以提供更完整的信息:

- **Scenario**: `value_flow`, `key_metrics`, `traditional_pain_points`, `ai_opportunities`
- **Role**: `responsibilities`, `required_capabilities`, `ai_tools`, `typical_workflow`
- **Capability**: `learning_path`, `transferability`, `ai_impact`

## ✅ 验证规则

### ID 格式规则

| 实体 | 格式 | 示例 | 正则表达式 |
|-----|------|------|-----------|
| Scenario | `{industry}-{scenario}-{num}` | `tech-saas-product-001` | - |
| Role | `[a-z0-9-]+` | `ai-product-manager-001` | `^[a-z0-9-]+$` |
| Capability | `cap-{category}-{num}` | `cap-cognitive-001` | `^cap-[a-z]+-\d{3}$` |

### 枚举值规则

#### RoleType (角色类型)
- `traditional`: 传统角色
- `ai-enhanced`: AI增强角色
- `emerging`: 新兴角色
- `ai-agent`: AI代理角色

#### CapabilityCategory (能力分类)
- `cognitive`: 认知能力
- `technical`: 技术能力
- `interpersonal`: 人际能力
- `domain-specific`: 领域专属能力

#### CapabilityLevel (能力等级)
- `beginner`: 初学者
- `intermediate`: 中级
- `advanced`: 高级
- `expert`: 专家

#### Priority (优先级)
- `must-have`: 必备
- `should-have`: 应有
- `nice-to-have`: 可选

#### AutomationLevel (自动化程度)
- `manual`: 人工
- `assisted`: 辅助
- `automated`: 自动化

#### AIImpact (AI影响)
- `enhanced`: AI增强
- `augmented`: AI辅助
- `automated`: 可自动化
- `obsolete`: 已过时

#### Transferability (可迁移性)
- `high`: 高
- `medium`: 中
- `low`: 低

## 🔧 工具命令

### 验证模板文件

```bash
# 验证所有模板
poetry run python scripts/validate_templates.py

# 验证单个文件
world-professors validate scenario data/taxonomy/scenarios/software/example.yaml
world-professors validate role data/roles/by-industry/software/example.yaml
world-professors validate capability data/capabilities/core-skills/example.yaml
```

### 生成 JSON Schema

```bash
# 生成所有 JSON Schema 文件
poetry run python scripts/generate_schemas.py

# Schema 文件位置
# - src/world_professors/schemas/scenario-schema.json
# - src/world_professors/schemas/role-schema.json
# - src/world_professors/schemas/capability-schema.json
```

## 📖 模板示例

### Scenario 示例

```yaml
id: "tech-saas-product-001"
name: "SaaS产品研发与交付"
description: "面向B端企业客户的SaaS产品研发全流程"
industry: "软件与信息技术服务"
sub_industry: "企业级SaaS"

value_flow:
  - stage: "需求发现"
    activities: ["客户访谈", "竞品分析"]
  - stage: "产品设计"
    activities: ["原型设计", "方案评审"]

key_metrics:
  - "产品交付周期"
  - "客户满意度"

ai_opportunities:
  - "AI辅助需求分析"
  - "智能代码生成"
```

### Role 示例 (AI增强型)

```yaml
id: "ai-product-manager-001"
name: "AI增强型产品经理"
description: "利用AI工具辅助的现代产品经理"
type: "ai-enhanced"
traditional_role: "产品经理"
scenario_ref: "tech-saas-product-001"

responsibilities:
  core:
    - "产品战略规划"
    - "关键决策判断"
  delegated_to_ai:
    - "竞品分析"
    - "数据报表生成"
  collaborative:
    - "需求文档撰写"

ai_tools:
  - name: "Claude"
    purpose: "需求分析、PRD生成"
    vendor: ["Anthropic"]
    cost: "paid"
```

### Capability 示例

```yaml
id: "cap-cognitive-001"
name: "提示工程能力"
description: "设计和优化AI提示词的能力"
category: "cognitive"
sub_category: "AI交互与应用"

levels:
  beginner:
    description: "能够使用基础提示词"
    skills: ["零样本提示", "基本指令"]
    tasks: ["编写清晰指令", "指定输出格式"]

  intermediate:
    description: "熟练运用多种提示词技术"
    skills: ["少样本学习", "思维链提示"]
    tasks: ["设计多步骤推理", "优化提示词"]

learning_path:
  prerequisites: ["cap-cognitive-critical-thinking"]
  estimated_time: "3-6个月"
  milestones:
    - month: 1
      goal: "掌握基础提示词技术"
    - month: 3
      goal: "能够设计多步骤工作流"
```

## ⚠️ 常见错误

### 1. Capability ID 格式错误

❌ 错误:
```yaml
id: "cap-cognitive-prompt-engineering"  # 不能使用描述性名称
```

✅ 正确:
```yaml
id: "cap-cognitive-001"  # 必须是3位数字
```

### 2. AI增强角色缺少 traditional_role

❌ 错误:
```yaml
type: "ai-enhanced"
# 缺少 traditional_role 字段
```

✅ 正确:
```yaml
type: "ai-enhanced"
traditional_role: "产品经理"
```

### 3. Capability 等级定义不足

❌ 错误:
```yaml
levels:
  beginner:
    description: "初学者"
# 至少需要2个等级
```

✅ 正确:
```yaml
levels:
  beginner:
    description: "初学者"
  intermediate:
    description: "中级"
```

## 📚 参考资源

- [数据模型设计文档](.spec-workflow/specs/data-models-foundation/design.md)
- [需求文档](.spec-workflow/specs/data-models-foundation/requirements.md)
- [JSON Schema 文件](../../src/world_professors/schemas/)
- [Pydantic 模型源码](../../src/world_professors/models/)

## 🤝 贡献指南

创建新数据文件时:

1. ✅ 使用对应的模板文件
2. ✅ 填写所有必填字段
3. ✅ 建议填写推荐字段以提供完整信息
4. ✅ 运行验证命令确保格式正确
5. ✅ 提交前进行代码审查

---

**版本**: 1.0
**更新时间**: 2025-01-20
**维护者**: 数字角色研究组
