# World Professors: 行业Agent标准库架构

> 定义行业→场景→流程→Agent→能力→工具的标准化体系

## 一、核心定位重述

### 1.1 定位差异

| 维度 | 之前理解 | 正确定位 |
|------|---------|---------|
| 性质 | 知识维基百科 | **行业Agent标准库** |
| 目标 | 人类阅读理解 | **机器/Agent可消费** |
| 输出 | 静态文档页面 | **标准化数据模型** |
| 用户 | 职业发展者 | **AI系统/Agent开发者** |

### 1.2 核心价值

```
当你要构建一个"金融投顾Agent"时，应该能够：
1. 查询标准库：金融 → 财富管理场景 → 有哪些标准流程？
2. 获取定义：该场景下的Agent需要什么能力？使用什么工具？
3. 直接使用：按标准定义配置Agent的能力边界和工具集
```

---

## 二、标准模型体系

### 2.1 核心链路

```
┌─────────────────────────────────────────────────────────────────┐
│  Industry (行业)                                                 │
│  └── 金融服务 / 科技互联网 / 医疗健康 / 制造业 / ...            │
└────────────────────────────┬────────────────────────────────────┘
                             ↓
┌─────────────────────────────────────────────────────────────────┐
│  Scenario (场景)                                                 │
│  └── 财富管理 / 投资研究 / 风险控制 / 客户服务 / ...            │
└────────────────────────────┬────────────────────────────────────┘
                             ↓
┌─────────────────────────────────────────────────────────────────┐
│  Workflow (流程) ⭐ 新增独立模型                                 │
│  └── 客户画像流程 / 方案设计流程 / 风险评估流程 / ...           │
│      └── Step → Step → Step (带输入/输出/工具定义)              │
└────────────────────────────┬────────────────────────────────────┘
                             ↓
┌─────────────────────────────────────────────────────────────────┐
│  Agent (智能体) ⭐ 升级为独立模型                                │
│  └── 投顾Agent / 研报Agent / 风控Agent / 客服Agent / ...       │
│      ├── 能力集 (capabilities)                                   │
│      ├── 工具集 (tools)                                          │
│      ├── 可执行流程 (workflows)                                  │
│      └── 输入/输出规范 (input/output schema)                    │
└────────────────────────────┬────────────────────────────────────┘
                             ↓
┌─────────────────────────────────────────────────────────────────┐
│  Capability (能力)                                               │
│  └── 金融分析 / 风险评估 / 客户沟通 / 数据处理 / ...            │
└────────────────────────────┬────────────────────────────────────┘
                             ↓
┌─────────────────────────────────────────────────────────────────┐
│  Tool (工具) ⭐ 新增独立模型                                     │
│  └── 市场数据API / 投资组合优化器 / 文档生成器 / ...            │
│      └── 接口定义 / 参数规范 / 调用示例                         │
└─────────────────────────────────────────────────────────────────┘
```

### 2.2 模型关系图

```
                    Industry
                       │
                       ▼
                   Scenario ─────────────────┐
                       │                     │
          ┌────────────┼────────────┐        │
          ▼            ▼            ▼        │
      Workflow     Workflow     Workflow     │
          │            │            │        │
          └─────────┬──┴────────────┘        │
                    │                        │
                    ▼                        │
                  Agent ◄────────────────────┘
                    │
        ┌───────────┼───────────┐
        ▼           ▼           ▼
   Capability   Capability    Tool
        │                       │
        └───────────┬───────────┘
                    │
                    ▼
            (可组合、可复用)
```

---

## 三、标准模型定义

### 3.1 Industry (行业)

```yaml
# data/industries/finance.yaml
id: ind-finance
name: 金融服务
name_en: Financial Services
description: 银行、证券、保险、资管等金融服务领域

# 子行业列表
sub_industries:
  - id: ind-finance-banking
    name: 银行业
  - id: ind-finance-securities
    name: 证券业
  - id: ind-finance-insurance
    name: 保险业
  - id: ind-finance-asset-mgmt
    name: 资产管理

# 行业特征
characteristics:
  regulatory_level: high        # 监管程度
  data_sensitivity: high        # 数据敏感度
  ai_maturity: medium           # AI成熟度
  
# 通用能力要求
common_capabilities:
  - cap-fin-001  # 金融合规
  - cap-fin-002  # 风险管理基础
```

### 3.2 Scenario (场景) - 增强

```yaml
# data/scenarios/finance/wealth-management.yaml
id: scn-fin-wealth-mgmt
name: 财富管理
industry_ref: ind-finance
sub_industry_ref: ind-finance-asset-mgmt

description: |
  为高净值客户提供个性化资产配置和财富增值服务

# 场景特征
characteristics:
  complexity: high
  human_interaction: high
  automation_potential: medium

# 关联的标准流程
workflows:
  - wf-fin-wm-profiling      # 客户画像流程
  - wf-fin-wm-planning       # 方案设计流程
  - wf-fin-wm-execution      # 执行交易流程
  - wf-fin-wm-monitoring     # 持续监控流程

# 场景下的Agent类型
agents:
  - agt-fin-wm-advisor       # 投顾Agent
  - agt-fin-wm-analyst       # 分析Agent
  - agt-fin-wm-monitor       # 监控Agent

# 关键指标
kpis:
  - name: 客户满意度
    target: ">= 90%"
  - name: 资产年化收益
    target: "> benchmark + 2%"
```

### 3.3 Workflow (流程) ⭐ 新增

```yaml
# data/workflows/finance/wealth-management/client-profiling.yaml
id: wf-fin-wm-profiling
name: 客户画像流程
scenario_ref: scn-fin-wealth-mgmt

description: |
  从客户接触到完成风险画像的标准化流程

# 流程步骤定义
steps:
  - id: step-01
    name: 基础信息采集
    type: automated  # manual | assisted | automated
    
    # 输入规范
    input:
      schema:
        type: object
        properties:
          client_id: { type: string }
          source: { type: string, enum: [app, web, offline] }
    
    # 输出规范
    output:
      schema:
        type: object
        properties:
          basic_info: { $ref: "#/definitions/ClientBasicInfo" }
    
    # 可使用的工具
    tools:
      - tool-crm-api
      - tool-ocr-id-card
    
    # 所需能力
    capabilities:
      - cap-data-001  # 数据采集

  - id: step-02
    name: 风险偏好评估
    type: assisted
    
    input:
      schema:
        $ref: "#/definitions/ClientBasicInfo"
    
    output:
      schema:
        type: object
        properties:
          risk_profile:
            type: object
            properties:
              risk_tolerance: { type: string, enum: [conservative, moderate, aggressive] }
              investment_horizon: { type: string }
              liquidity_needs: { type: string }
    
    tools:
      - tool-risk-questionnaire
      - tool-behavioral-analysis
    
    capabilities:
      - cap-fin-003  # 风险评估

  - id: step-03
    name: 画像生成与确认
    type: automated
    
    input:
      - step-01.output
      - step-02.output
    
    output:
      schema:
        $ref: "#/definitions/ClientProfile"
    
    tools:
      - tool-profile-generator
    
    capabilities:
      - cap-ai-001  # AI生成

# 流程元数据
metadata:
  avg_duration: "30min"
  automation_rate: "70%"
  human_checkpoints: [step-02]  # 需人工确认的步骤
```

### 3.4 Agent (智能体) ⭐ 升级

```yaml
# data/agents/finance/wealth-management/advisor-agent.yaml
id: agt-fin-wm-advisor
name: 财富管理投顾Agent
name_en: Wealth Management Advisor Agent

# 关联信息
scenario_ref: scn-fin-wealth-mgmt
agent_type: domain-expert  # general | domain-expert | specialist | orchestrator

description: |
  为财富管理场景提供智能投顾服务的Agent，
  可独立完成客户画像、方案设计、持续跟踪等任务

# === Agent能力边界 ===
capabilities:
  required:  # 必须具备
    - id: cap-fin-001
      level: expert
      description: 金融市场知识
    - id: cap-fin-003
      level: advanced
      description: 风险评估能力
    - id: cap-ai-002
      level: intermediate
      description: 自然语言理解
  
  optional:  # 可选增强
    - id: cap-comm-001
      level: intermediate
      description: 客户沟通

# === Agent工具集 ===
tools:
  # 数据获取类
  - tool_ref: tool-market-data-api
    usage: 获取实时市场行情
    required: true
  
  - tool_ref: tool-portfolio-optimizer
    usage: 资产配置优化计算
    required: true
  
  - tool_ref: tool-risk-calculator
    usage: 风险指标计算
    required: true
  
  # 生成类
  - tool_ref: tool-report-generator
    usage: 生成投资建议报告
    required: false

# === 可执行流程 ===
executable_workflows:
  - wf-fin-wm-profiling      # 可独立执行
  - wf-fin-wm-planning       # 可独立执行
  - wf-fin-wm-monitoring     # 可独立执行

# === 接口规范 ===
interface:
  # 输入格式
  input_schema:
    type: object
    properties:
      task_type:
        type: string
        enum: [profiling, planning, monitoring, qa]
      client_id:
        type: string
      query:
        type: string
        description: 用户自然语言请求
    required: [task_type]
  
  # 输出格式
  output_schema:
    type: object
    properties:
      status:
        type: string
        enum: [success, partial, failed, need_human]
      result:
        type: object
      confidence:
        type: number
        minimum: 0
        maximum: 1
      next_actions:
        type: array
        items:
          type: string

# === 行为约束 ===
constraints:
  # 合规约束
  compliance:
    - "不得提供具体投资建议（仅供参考）"
    - "必须披露风险提示"
    - "敏感操作需人工确认"
  
  # 能力边界
  boundaries:
    - "不能直接执行交易"
    - "不能访问未授权客户数据"
    - "单次建议金额上限100万"
  
  # 升级条件（何时转人工）
  escalation:
    - condition: "客户投诉"
      action: transfer_to_human
    - condition: "置信度 < 0.7"
      action: request_review
    - condition: "涉及金额 > 500万"
      action: require_approval

# === 评估指标 ===
metrics:
  quality:
    - name: 建议采纳率
      target: ">= 60%"
    - name: 客户满意度
      target: ">= 4.5/5"
  
  efficiency:
    - name: 平均响应时间
      target: "< 3s"
    - name: 自动化完成率
      target: ">= 80%"
```

### 3.5 Tool (工具) ⭐ 新增独立模型

```yaml
# data/tools/finance/market-data-api.yaml
id: tool-market-data-api
name: 市场行情数据API
category: data-retrieval  # data-retrieval | computation | generation | action

description: |
  提供实时和历史市场行情数据查询

# 适用范围
applicable_industries:
  - ind-finance
applicable_scenarios:
  - scn-fin-wealth-mgmt
  - scn-fin-investment-research

# === 接口定义 ===
interface:
  type: rest-api  # rest-api | function-call | mcp-tool | sdk
  
  # API端点
  endpoints:
    - name: get_quote
      method: GET
      path: /api/v1/quote/{symbol}
      description: 获取单个标的实时行情
      
      parameters:
        - name: symbol
          in: path
          type: string
          required: true
          description: 标的代码
        - name: fields
          in: query
          type: array
          items: string
          description: 返回字段列表
      
      response:
        type: object
        properties:
          symbol: { type: string }
          price: { type: number }
          change: { type: number }
          volume: { type: integer }
          timestamp: { type: string, format: datetime }
      
      examples:
        - request:
            symbol: "AAPL"
            fields: ["price", "change"]
          response:
            symbol: "AAPL"
            price: 178.50
            change: 2.3

    - name: get_history
      method: GET
      path: /api/v1/history/{symbol}
      description: 获取历史行情数据
      # ...

# === 使用要求 ===
requirements:
  authentication:
    type: api-key
    header: X-API-Key
  
  rate_limit:
    requests_per_minute: 100
    requests_per_day: 10000
  
  permissions:
    - "market.read"

# === 成本信息 ===
pricing:
  model: usage-based  # free | subscription | usage-based
  cost_per_call: 0.001  # USD
  free_tier: 1000  # calls per month

# === 供应商信息 ===
providers:
  - name: Bloomberg
    tier: enterprise
  - name: Yahoo Finance
    tier: free
  - name: Alpha Vantage
    tier: freemium
```

### 3.6 Capability (能力) - 增强

```yaml
# data/capabilities/finance/risk-assessment.yaml
id: cap-fin-003
name: 风险评估能力
name_en: Risk Assessment

category: domain-specific
sub_category: finance

description: |
  评估投资组合、客户或业务的风险水平，
  包括市场风险、信用风险、流动性风险等

# === 能力等级定义 ===
levels:
  beginner:
    description: 理解基础风险概念
    skills:
      - 识别常见风险类型
      - 使用标准风险评估工具
    assessment_criteria:
      - 能够完成标准化风险问卷
      - 理解VaR等基础指标
  
  intermediate:
    description: 独立进行风险评估
    skills:
      - 设计风险评估框架
      - 多维度风险分析
    assessment_criteria:
      - 能够独立完成客户风险画像
      - 提出风险缓释建议
  
  advanced:
    description: 复杂场景风险建模
    skills:
      - 量化风险模型构建
      - 压力测试设计
    assessment_criteria:
      - 能够开发风险评估模型
      - 处理复杂衍生品风险
  
  expert:
    description: 风险体系设计
    skills:
      - 企业级风险管理框架
      - 创新风险产品设计

# === 关联工具 ===
associated_tools:
  - tool-risk-calculator
  - tool-var-model
  - tool-stress-test

# === 可迁移性 ===
transferability:
  across_industries: medium  # 可迁移到保险、银行等
  across_scenarios: high     # 同行业不同场景通用

# === AI影响评估 ===
ai_impact:
  level: augmented  # enhanced | augmented | automated | obsolete
  description: |
    AI可以自动化数据收集和基础计算，
    但复杂判断和最终决策仍需人类专家
```

---

## 四、数据目录结构调整

```
data/
├── industries/                    # 行业定义
│   ├── finance.yaml
│   ├── technology.yaml
│   └── healthcare.yaml
│
├── scenarios/                     # 场景定义
│   ├── finance/
│   │   ├── wealth-management.yaml
│   │   ├── investment-research.yaml
│   │   └── risk-control.yaml
│   └── technology/
│       └── software-development.yaml
│
├── workflows/                     # 流程定义 ⭐
│   ├── finance/
│   │   └── wealth-management/
│   │       ├── client-profiling.yaml
│   │       ├── portfolio-planning.yaml
│   │       └── risk-monitoring.yaml
│   └── _templates/
│       └── workflow-template.yaml
│
├── agents/                        # Agent定义 ⭐
│   ├── finance/
│   │   └── wealth-management/
│   │       ├── advisor-agent.yaml
│   │       ├── analyst-agent.yaml
│   │       └── monitor-agent.yaml
│   └── _templates/
│       └── agent-template.yaml
│
├── capabilities/                  # 能力定义
│   ├── cognitive/
│   ├── technical/
│   ├── interpersonal/
│   └── domain-specific/
│       ├── finance/
│       │   ├── financial-analysis.yaml
│       │   └── risk-assessment.yaml
│       └── technology/
│
├── tools/                         # 工具定义 ⭐
│   ├── finance/
│   │   ├── market-data-api.yaml
│   │   ├── portfolio-optimizer.yaml
│   │   └── risk-calculator.yaml
│   ├── general/
│   │   ├── document-generator.yaml
│   │   └── data-extractor.yaml
│   └── _templates/
│       └── tool-template.yaml
│
└── schemas/                       # JSON Schema定义
    ├── industry.schema.json
    ├── scenario.schema.json
    ├── workflow.schema.json
    ├── agent.schema.json
    ├── capability.schema.json
    └── tool.schema.json
```

---

## 五、使用场景示例

### 5.1 构建Agent时查询标准库

```python
from world_professors import StandardLibrary

lib = StandardLibrary()

# 查询：财富管理场景需要什么Agent？
scenario = lib.get_scenario("scn-fin-wealth-mgmt")
agents = lib.get_agents_for_scenario(scenario.id)

for agent in agents:
    print(f"Agent: {agent.name}")
    print(f"  能力要求: {[c.id for c in agent.capabilities.required]}")
    print(f"  工具集: {[t.tool_ref for t in agent.tools]}")
    print(f"  可执行流程: {agent.executable_workflows}")
```

### 5.2 按标准定义配置Agent

```python
# 获取标准Agent定义
advisor_spec = lib.get_agent("agt-fin-wm-advisor")

# 用于配置实际Agent系统
agent_config = {
    "name": advisor_spec.name,
    "capabilities": advisor_spec.capabilities,
    "tools": [lib.get_tool(t.tool_ref) for t in advisor_spec.tools],
    "constraints": advisor_spec.constraints,
    "input_schema": advisor_spec.interface.input_schema,
    "output_schema": advisor_spec.interface.output_schema,
}

# 传递给Agent框架
my_agent = AgentFramework.create(agent_config)
```

### 5.3 验证Agent符合标准

```python
from world_professors.validation import AgentValidator

validator = AgentValidator(lib)

# 验证自定义Agent是否符合标准
result = validator.validate(
    my_agent,
    against_standard="agt-fin-wm-advisor"
)

print(result.compliant)  # True/False
print(result.missing_capabilities)  # 缺失的能力
print(result.missing_tools)  # 缺失的工具
print(result.constraint_violations)  # 违反的约束
```

---

## 六、开发优先级调整

### 第一阶段：模型重构 (1周)

1. **新增 Industry 模型**
2. **新增 Workflow 模型** (最重要)
3. **新增 Tool 模型** (最重要)
4. **升级 Agent 模型** (从Role.AI_AGENT分离)
5. 更新 Scenario 模型
6. 增强 Capability 模型

### 第二阶段：标准库API (1周)

1. StandardLibrary 主入口类
2. 跨实体查询方法
3. 引用完整性验证
4. JSON Schema 自动生成

### 第三阶段：示例数据 (1周)

1. 金融-财富管理 完整示例
   - 1个行业 + 1个场景
   - 3个流程 + 3个Agent
   - 10个能力 + 10个工具

---

## 七、总结

| 维度 | 调整前 | 调整后 |
|------|--------|--------|
| 核心实体 | Scenario, Role, Capability | Industry, Scenario, **Workflow**, **Agent**, Capability, **Tool** |
| 角色定位 | 4类角色(含AI Agent) | **Agent独立为一等公民** |
| 流程定义 | Role.typical_workflow | **Workflow独立模型(含Step)** |
| 工具定义 | Role.ai_tools | **Tool独立模型(含接口规范)** |
| 使用方式 | 人类阅读文档 | **程序化查询和消费** |
