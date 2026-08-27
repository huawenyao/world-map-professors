# 数字时代广场：数据模型

在现有 Industry / Scenario / Workflow / Agent / Role / Capability / Tool 之上，增加广场实体，并用引用而不是复制来连边。

## 1. 实体关系

```
Person ──affiliated_with──► Brand
Person ──known_for────────► Product
Person ──capabilities─────► Capability
Person ──scenarios────────► Scenario

Brand ──owns──────────────► Product
Brand ──industries────────► Industry

Product ──implements──────► Tool          (可选，产品暴露的可调用面)
Product ──serves──────────► Scenario
Product ──enhances────────► Role
Product ──owned_by────────► Brand

Tool  (已有) ──scenario / capability / workflow.step

RankingSnapshot ──entries──► Person | Brand | Product | Tool
RankingSnapshot ──method_ref──► RankingMethod
RankingSnapshot ──scope──► Scenario | Industry | global

IndustryAsset 不是新表，而是广场对已有本体条目的「资产视图」标签与引用计数。
```

ID 规范（与 structure.md 一致，前缀区分馆）：

| 实体 | 前缀 | 示例 |
|------|------|------|
| Person | `psn-` | `psn-tech-karpathy` |
| Brand | `brd-` | `brd-openai` |
| Product | `prd-` | `prd-cursor` |
| Ranking method | `rnk-m-` | `rnk-m-influence-v1` |
| Ranking snapshot | `rnk-s-` | `rnk-s-prd-coding-2026q3` |

## 2. Person

```yaml
# data/plaza/people/{industry}/{id}.yaml
id: psn-tech-example
name: 示例人物
name_en: Example Person
persona_type: human          # human | digital-persona
status: published            # draft | published | claimed | archived

headline: 一句话公共身份
bio: |
  基于公开资料的简介。禁止未证实的私人信息。

affiliations:
  - brand_ref: brd-example
    role_title: 职务
    current: true

coordinates:
  industries: [ind-technology]
  scenarios: [scn-tech-software-dev]
  capabilities:
    - capability_id: cap-tech-001
      level: expert          # 仅当有公开依据
      evidence: "开源项目 / 著作 / 课程，需可点开"

known_for_products: [prd-example]
contributed_assets:          # 对本库条目的贡献
  - scn-tech-software-dev

scores:                      # 由快照写入，条目内可缓存最近一次
  influence:
    band: A                  # S/A/B/C/D，避免伪精确
    snapshot_ref: rnk-s-psn-tech-2026q3
  contribution:
    band: A
    snapshot_ref: rnk-s-psn-tech-contrib-2026q3

sources:
  - url: https://example.com
    type: official           # official | news | academic | repo
    retrieved_at: "2026-08-01"

claim:
  claimed: false
  claimed_at: null

metadata:
  schema_version: "1.0"
  author: "World Professors Team"
```

数字人格额外必填：`operator_brand_ref`、`model_disclosure`、`persona_type: digital-persona`。

## 3. Brand

```yaml
id: brd-example
name: 示例品牌
name_en: Example
org_type: company            # company | lab | opensource | alliance | university
region: global               # cn | us | eu | global | other
status: published

description: |
  公开定位。

coordinates:
  industries: [ind-technology]
  scenarios: [scn-tech-software-dev]

products: [prd-example]
tools: [tool-code-generator]  # 若品牌直接提供工具接口

presence:
  hq: ""
  founded_year: 2020
  stage: operating            # 仅用公开口径

sources:
  - url: https://example.com
    type: official
    retrieved_at: "2026-08-01"

claim:
  claimed: false

metadata:
  schema_version: "1.0"
```

## 4. Product

```yaml
id: prd-example
name: 示例产品
name_en: Example Product
status: published
category: coding-assistant   # 受控词表，见 plaza/catalogs/product-categories.yaml
user_type: [developer]       # consumer | business | developer
brand_ref: brd-example

description: |
  产品做什么，不写广告套话。

pricing:
  model: subscription        # free | freemium | subscription | usage | enterprise
  notes: "公开页面摘要，非实时爬价"

coordinates:
  industries: [ind-technology]
  scenarios:
    - scenario_ref: scn-tech-software-dev
      fit: high              # high | medium | experimental
      enhances_roles: []     # 可选 role id
      kpis: ["编码吞吐", "评审漏过率"]

implements_tools: [tool-code-generator]

compliance_notes: ""         # 公开声明摘要
sources:
  - url: https://example.com
    type: official
    retrieved_at: "2026-08-01"

claim:
  claimed: false

metadata:
  schema_version: "1.0"
```

## 5. RankingMethod 与 RankingSnapshot

方法与快照分离：方法变更必须升版本；历史快照只读。

```yaml
# data/plaza/rankings/methods/influence-v1.yaml
id: rnk-m-influence-v1
name: 影响力方法 v1
applies_to: [person, brand, product]
window: trailing_90d
paid_features_excluded: true
signals:
  - id: independent_citations
    weight: 0.4
    note: 独立媒体/论文/标准引用
  - id: product_adoption_public
    weight: 0.3
    note: 可复核的公开采用证据
  - id: scenario_relevance
    weight: 0.3
    note: 与目标场景坐标的匹配
exclusions:
  - 付费曝光
  - 无法复核的自报指标
appeal_window_days: 14
```

```yaml
# data/plaza/rankings/snapshots/prd-coding-2026q3.yaml
id: rnk-s-prd-coding-2026q3
method_ref: rnk-m-influence-v1
entity_type: product
scope:
  type: scenario
  ref: scn-tech-software-dev
computed_at: "2026-08-01T00:00:00Z"
entries:
  - rank: 1
    entity_ref: prd-example
    band: S
    notes: "编辑 v0：依据见 sources"
```

v0 允许 `notes` 为编辑精选；P2 起 `entries` 必须能追溯到信号表。

## 6. 行业资产视图

不新建平行宇宙。在现有 YAML 的 `metadata` 中增加广场字段即可：

```yaml
# 附加于 scenario / workflow / agent / capability / tool
plaza:
  asset_class: scenario      # industry|scenario|workflow|role|agent|capability|tool|case|dataset
  publish_to_plaza: true
  featured_on_plaza: false   # 运营精选，与排名分数无关
```

数据集 / 模型卡若后续新增，放 `data/plaza/assets/datasets/`，用同样的 `coordinates` 挂场景。

## 7. 目录与受控词

| 文件 | 用途 |
|------|------|
| `data/plaza/catalogs/product-categories.yaml` | 产品品类 |
| `data/plaza/catalogs/persona-types.yaml` | 人物类型 |
| `data/plaza/catalogs/org-types.yaml` | 组织类型 |
| `data/plaza/catalogs/source-types.yaml` | 来源类型 |

品类变更走 PR，避免每个编辑自创「AIGC 神器」类标签。

## 8. 与代码层的衔接

| 现有 | 广场扩展 |
|------|---------|
| `models/taxonomy.py` 等 | 新增 `plaza.py`：Person, Brand, Product, Ranking* |
| `repositories/*_repo.py` | `PersonRepository` 等，按 `data/plaza/` 扫描 |
| 引用完整性 | `scenario_ref` / `brand_ref` / `tool_id` 必须能解析 |
| JSON Schema | `src/world_professors/schemas/plaza-*.json` |

v0 可先只提交 YAML 与 Schema，不强制一次实现全部 Pydantic。但正式发布条目前，校验脚本必须覆盖引用。

## 9. 数据伦理

- 人物条目最小化：职业公共信息，不收录私人联系方式。
- 来源可点开；无法来源的分数不得进入正式快照。
- 认领 diff 进入 Git 历史。
- 付费精选存在独立文件 `data/plaza/ads/`（或后续独立库），**禁止写入 RankingSnapshot.entries**。
