# Requirements: Digital Era Plaza

## Introduction

在 world-professors 既有本体（行业、场景、流程、角色、Agent、能力、工具）之上，建设面向公众与产业的产品层「数字时代广场」，覆盖五馆：AI 名人榜、AI 品牌榜、AI 产品榜、AI 行业资产库、AI 工具库。目标是用同一套场景坐标同时服务注意力（榜单）、资产（标准库）与调用（工具/Agent）。

完整商业与产品说明见 `docs/plaza/`。本文件只定义可验收需求。

## Alignment with Product Vision

- 延续 product.md：场景驱动、开放协作、可操作、人机双读。
- 升华点：为本体补上公共入口与可收费的入驻/订阅层，且**付费不得改变名次**。
- 行业资产库 = 现有知识库的产品化视图；工具库 = 现有 Tool 模型的目录化。

## Requirements

### Requirement 1: 场景作为主导航

**User Story:** 作为访客，我想从行业场景进入广场，以便同时看到该场景下的人物、品牌、产品、资产与工具。

#### Acceptance Criteria

1. WHEN 用户打开广场首页 THEN 系统 SHALL 提供行业→场景入口，且场景入口优先于五馆平铺。
2. WHEN 用户进入已发布场景页 THEN 系统 SHALL 展示该场景的价值流/流程摘要，并链接到人物、品牌、产品、工具（有则显示，无则显示覆盖不足）。
3. IF 某场景下正式产品少于 5 条 THEN 系统 SHALL NOT 用无关场景的网红产品填充。

### Requirement 2: 五馆实体可互链

**User Story:** 作为访客，我想在人物、品牌、产品、工具、资产之间跳转，以便理解「谁做了什么、用什么、服务哪个场景」。

#### Acceptance Criteria

1. WHEN 打开已发布的人物/品牌/产品/工具页 THEN 系统 SHALL 展示坐标条（行业、场景；能力若有依据则展示）。
2. WHEN 产品声明 `brand_ref` 或 `implements_tools` THEN 系统 SHALL 能解析到对应条目或报告引用损坏。
3. WHEN 实体 `persona_type` 为 digital-persona THEN 系统 SHALL 在标题区强制展示非自然人标识及运营方/模型披露。

### Requirement 3: 双榜与付费隔离

**User Story:** 作为访客，我想看到可解释的影响力榜与专业贡献榜，以便区分热度与贡献；作为厂商，我想购买曝光但不能购买名次。

#### Acceptance Criteria

1. WHEN 发布正式榜快照 THEN 系统 SHALL 绑定 `method_ref`、计算窗口、适用范围（场景或行业）。
2. WHEN 展示名次 THEN 系统 SHALL NOT 将精选/广告条目写入 RankingSnapshot 的有机名次列表。
3. IF 展示精选位 THEN 系统 SHALL 使用与有机榜可区分的视觉与「精选」文案。
4. WHEN 方法版本变更 THEN 系统 SHALL 升 `RankingMethod` 版本且历史快照只读。

### Requirement 4: 上榜资格

**User Story:** 作为编辑，我想拒绝无坐标、无来源的条目进入正式榜，以便保护公信力。

#### Acceptance Criteria

1. WHEN 条目进入正式榜 THEN 系统 SHALL 要求至少 1 个有效场景或行业锚点。
2. WHEN 条目进入正式榜 THEN 系统 SHALL 要求至少 2 个独立来源，或 `claim.claimed = true` 且审核通过。
3. IF 来源在连续两个计算周期无法复核 THEN 系统 SHALL 将其移出正式榜或标为观察名单。

### Requirement 5: 行业资产库视图

**User Story:** 作为 Agent 开发者或 L&D，我想在广场中使用现有标准库对象，以便不维护第二套 CMS。

#### Acceptance Criteria

1. WHEN 场景/流程/Agent/能力/工具 `plaza.publish_to_plaza` 为 true THEN 广场 SHALL 可导航到该对象。
2. WHEN 资产内容变更 THEN 广场 SHALL 展示来自同一 YAML 事实源的内容，不得静默分叉。
3. WHEN 引用的 capability_id 或 tool id 不存在 THEN 校验 SHALL 失败并阻止发布流水线。

### Requirement 6: 工具库可过滤

**User Story:** 作为开发者，我想按场景、接口类型、定价模式筛选工具，以便配置 Agent。

#### Acceptance Criteria

1. WHEN 用户按场景筛选工具 THEN 系统 SHALL 只返回 `applicable_scenarios` 或坐标匹配的工具。
2. WHEN 工具含 interface 定义 THEN 工具页 SHALL 展示类型（rest-api / function-call / mcp-tool / sdk）与主要端点或函数名。
3. WHEN 工具无任何场景锚点 THEN 系统 SHALL NOT 将其标为「场景适配正式条」。

### Requirement 7: 认领

**User Story:** 作为品牌或产品官方，我想认领条目并纠正场景标签，以便被正确检索。

#### Acceptance Criteria

1. WHEN 提交认领 THEN 系统 SHALL 记录申请人、对象 ID、证明材料，并进入待审。
2. WHEN 认领通过 THEN 系统 SHALL 设置 claimed 状态，并保留变更 diff。
3. IF 认领材料不能证明商标或域名所有权 THEN 系统 SHALL 拒绝认证标。

### Requirement 8: 开放数据与校验

**User Story:** 作为贡献者，我想用 YAML 提交广场实体并由现有校验体系检查，以便与仓库工作流一致。

#### Acceptance Criteria

1. WHEN 新增 Person/Brand/Product YAML THEN Schema 校验 SHALL 覆盖必填字段与枚举。
2. WHEN 运行仓库校验 THEN 损坏的 `scenario_ref` / `brand_ref` / `tool` 引用 SHALL 被报告。
3. WHEN 付费精选数据存在 THEN 其存储位置 SHALL 与 RankingSnapshot 分离。

## Non-Functional Requirements

### Architecture

- 延续内容与代码分离、YAML 单一事实源、Repository 模式。
- 广场实体放 `data/plaza/`，禁止另起不可 diff 的大 JSON 作为主库。

### Integrity

- 排名计算与广告投放模块物理隔离（不同目录或不同服务），代码评审检查交叉写入。

### Performance

- 单场景页聚合（资产摘要 + 各馆短名单）在静态生成下可接受；动态 API P2 目标 < 500ms 缓存命中。

### Security & Compliance

- 人物仅公共职业信息；不存储私人电话邮箱。
- 利益披露字段可被方法页引用。
- 不收录攻击性、未授权访问、绕过安全控制的「工具」。

### Usability

- 中文优先；专名保留英文 `name_en`。
- 空态明确「覆盖不足」，禁止静默凑数。
