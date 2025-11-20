# Requirements: Data Models Foundation

## Overview

定义 world-professors 项目的核心数据模型,包括场景(Scenario)、角色(Role)、能力(Capability)和实践(Practice)的结构化表示。这些模型是整个知识库的基础,需要具备良好的可扩展性、验证能力和互操作性。

## Goals

### Primary Goals

1. **建立标准化数据Schema**
   - 定义4个核心实体的完整数据结构
   - 使用JSON Schema和Pydantic实现双重验证
   - 支持YAML和JSON两种格式

2. **确保数据一致性**
   - 跨文件引用的完整性检查
   - 必填字段和可选字段的明确定义
   - 数据类型和格式约束

3. **支持灵活扩展**
   - 预留自定义字段空间
   - 版本化Schema管理
   - 向后兼容的演进机制

4. **提供友好的开发体验**
   - 清晰的类型提示(Type Hints)
   - 自动化数据验证
   - 有意义的错误信息

### Secondary Goals

5. **生成文档和示例**
   - 自动生成Schema文档
   - 提供完整的数据示例
   - 编写最佳实践指南

6. **性能优化**
   - 快速加载和验证(单文件 < 100ms)
   - 支持延迟加载和缓存

## User Stories

### Story 1: 内容贡献者创建新场景
**作为** 内容贡献者
**我想要** 根据模板快速创建新的业务场景定义
**以便** 扩展知识库覆盖范围

**验收标准**:
- [ ] 提供清晰的YAML模板文件
- [ ] 填写必填字段后通过验证
- [ ] 遇到错误时提示具体哪个字段有问题

### Story 2: 开发者加载和验证数据
**作为** 开发者
**我想要** 使用Python代码加载YAML数据并自动验证
**以便** 确保数据质量,避免运行时错误

**验收标准**:
- [ ] 使用Pydantic模型自动验证数据
- [ ] 验证失败时抛出详细错误信息
- [ ] 支持批量验证多个文件

### Story 3: 角色与能力的关联
**作为** 系统
**我想要** 验证角色引用的能力ID确实存在
**以便** 保证数据引用完整性

**验收标准**:
- [ ] 检查`required-capabilities`中的`capability-id`有效性
- [ ] 验证时报告所有无效引用
- [ ] 支持延迟验证(允许先创建再关联)

### Story 4: 学习路径的构建
**作为** 学习路径规划器
**我想要** 访问能力的前置要求和相关能力
**以便** 构建完整的学习依赖图

**验收标准**:
- [ ] 能力模型包含`prerequisites`字段
- [ ] 能力模型包含`related-capabilities`字段
- [ ] 支持循环依赖检测

### Story 5: AI模式的匹配
**作为** AI模式匹配引擎
**我想要** 根据场景特征查找适用的AI应用模式
**以便** 为用户推荐最佳实践

**验收标准**:
- [ ] 场景包含`traditional-pain-points`和`ai-opportunities`
- [ ] AI模式包含`applicable-scenarios`标签
- [ ] 支持标签匹配和相似度计算

## Functional Requirements

### FR1: Scenario (场景) 数据模型

**必填字段**:
- `id` (string): 唯一标识符,格式: `{industry}-{scenario}-{num}`
- `name` (string): 场景名称
- `industry` (string): 所属行业
- `description` (string): 场景描述

**可选字段**:
- `sub-industry` (string): 子行业
- `tags` (string[]): 标签列表
- `value-flow` (object[]): 价值流定义
  - `stage` (string): 阶段名称
  - `activities` (string[]): 活动列表
- `key-metrics` (string[]): 关键指标
- `traditional-pain-points` (string[]): 传统痛点
- `ai-opportunities` (string[]): AI机会点
- `related-scenarios` (string[]): 相关场景ID
- `metadata` (object): 元数据
  - `created-at` (datetime): 创建时间
  - `updated-at` (datetime): 更新时间
  - `author` (string): 作者
  - `version` (string): 版本号

### FR2: Role (角色) 数据模型

**必填字段**:
- `id` (string): 角色ID,格式: `{industry}-{scenario}-{type}-{name}`
- `name` (string): 角色名称
- `type` (enum): 角色类型 - `traditional | ai-enhanced | emerging | ai-agent`
- `scenario-ref` (string): 关联场景ID
- `description` (string): 角色描述

**可选字段**:
- `traditional-role` (string): 对应的传统角色名称(仅ai-enhanced类型)
- `responsibilities` (object):
  - `core` (string[]): 核心职责(AI不可替代)
  - `delegated-to-ai` (string[]): 委托给AI的职责
  - `collaborative` (string[]): 人机协作职责
- `required-capabilities` (object[]):
  - `capability-id` (string): 能力ID
  - `level` (enum): 要求等级 - `beginner | intermediate | advanced | expert`
  - `priority` (enum): 优先级 - `must-have | should-have | nice-to-have`
- `ai-tools` (object[]):
  - `name` (string): 工具名称
  - `purpose` (string): 用途
  - `vendor` (string[]): 提供商
  - `cost` (enum): 成本 - `free | freemium | paid`
- `typical-workflow` (object[]):
  - `step` (string): 步骤描述
  - `human-time` (string): 人工耗时
  - `ai-time` (string): AI耗时
  - `automation-level` (enum): 自动化程度 - `manual | assisted | automated`
- `transformation-impact` (object):
  - `efficiency-gain` (string): 效率提升
  - `quality-improvement` (string): 质量改进
  - `new-capabilities` (string[]): 新增能力
  - `obsolete-skills` (string[]): 过时技能
- `salary-range` (object): 薪资范围(可选)
  - `min` (number): 最低薪资
  - `max` (number): 最高薪资
  - `currency` (string): 货币单位
  - `region` (string): 地区
- `metadata` (object): 同上

### FR3: Capability (能力) 数据模型

**必填字段**:
- `id` (string): 能力ID,格式: `cap-{category}-{num}`
- `name` (string): 能力名称
- `category` (enum): 类别 - `cognitive | technical | interpersonal | domain-specific`
- `description` (string): 能力描述

**可选字段**:
- `sub-category` (string): 子类别
- `aliases` (string[]): 别名
- `levels` (object): 能力等级定义
  - `beginner` (object):
    - `description` (string): 等级描述
    - `skills` (string[]): 具体技能
    - `tasks` (string[]): 可完成任务
  - `intermediate` (object): 同上
  - `advanced` (object): 同上
  - `expert` (object): 同上
- `learning-path` (object):
  - `prerequisites` (string[]): 前置能力ID
  - `estimated-time` (string): 预计学习时间
  - `resources` (object):
    - `courses` (string[]): 推荐课程
    - `books` (string[]): 推荐书籍
    - `practice` (string[]): 实践项目
  - `milestones` (object[]):
    - `month` (number): 月份
    - `goal` (string): 目标
- `related-capabilities` (string[]): 相关能力ID
- `applicable-roles` (string[]): 适用角色(描述性,非严格引用)
- `transferability` (object): 可迁移性
  - `across-industries` (enum): 跨行业 - `high | medium | low`
  - `across-scenarios` (enum): 跨场景 - `high | medium | low`
- `ai-impact` (enum): AI影响程度 - `enhanced | augmented | automated | obsolete`
- `metadata` (object): 同上

### FR4: Practice (实践) 数据模型

**AI Pattern子类型**:
- `id` (string): 模式ID
- `name` (string): 模式名称
- `type` (enum): 类型 - `automation | augmentation | generation | orchestration`
- `description` (string): 模式描述
- `applicable-scenarios` (string[]): 适用场景(标签)
- `implementation-steps` (string[]): 实施步骤
- `success-factors` (string[]): 成功要素
- `common-pitfalls` (string[]): 常见陷阱
- `examples` (object[]): 案例引用

**Transformation Case子类型**:
- `id` (string): 案例ID
- `title` (string): 案例标题
- `industry` (string): 行业
- `scenario-ref` (string): 关联场景
- `summary` (string): 案例摘要
- `before` (object): 变革前状态
  - `process` (string): 流程描述
  - `pain-points` (string[]): 痛点
  - `metrics` (object): 关键指标
- `after` (object): 变革后状态
  - `process` (string): 新流程
  - `improvements` (string[]): 改进点
  - `metrics` (object): 新指标
- `ai-tools-used` (string[]): 使用的AI工具
- `roi` (object): 投资回报
  - `cost` (string): 成本
  - `benefit` (string): 收益
  - `payback-period` (string): 回本周期
- `lessons-learned` (string[]): 经验教训
- `metadata` (object): 同上

## Non-Functional Requirements

### NFR1: 性能要求
- 单个YAML文件解析和验证时间 < 100ms
- 批量验证1000个文件 < 10s
- Pydantic模型实例化 < 10ms

### NFR2: 数据质量
- 所有模型必须通过Schema验证
- 引用完整性检查覆盖率 100%
- 数据示例覆盖所有必填字段

### NFR3: 可维护性
- 每个模型有完整的Docstring
- Schema变更有版本记录
- 提供迁移脚本模板

### NFR4: 可扩展性
- 支持通过`custom-fields`扩展
- Schema支持向后兼容的演进
- 预留未来需求的扩展点

### NFR5: 开发体验
- 类型提示覆盖率 100%
- 错误信息包含字段路径和建议修复
- 提供VS Code的Schema自动补全

## Data Validation Rules

### 通用规则
1. 所有ID必须唯一(同类型内)
2. 所有引用必须有效(除非标记为`allow-dangling`)
3. 日期格式: ISO 8601 (`YYYY-MM-DD` 或 `YYYY-MM-DDTHH:MM:SSZ`)
4. 版本号格式: Semantic Versioning (`major.minor.patch`)

### 场景特定规则
- `value-flow.stage` 不允许重复
- `related-scenarios` 不允许自引用

### 角色特定规则
- `type=ai-enhanced` 时 `traditional-role` 必填
- `required-capabilities.level` 必须是有效枚举值
- `typical-workflow` 中步骤顺序必须合理(非必须验证)

### 能力特定规则
- `levels` 至少定义两个等级
- `learning-path.prerequisites` 不允许循环依赖
- `related-capabilities` 不允许自引用

## Success Criteria

1. **Schema完整性**
   - ✅ 4个核心实体的JSON Schema定义完成
   - ✅ 所有必填字段和可选字段有清晰定义
   - ✅ 枚举值和约束条件完整

2. **Pydantic模型**
   - ✅ 4个核心Pydantic模型类实现
   - ✅ 自定义验证器覆盖特殊规则
   - ✅ 类型提示100%覆盖

3. **数据示例**
   - ✅ 每个模型至少2个完整示例
   - ✅ 覆盖典型场景和边界情况
   - ✅ 所有示例通过验证

4. **验证工具**
   - ✅ 提供CLI命令验证单文件
   - ✅ 支持批量验证目录
   - ✅ 生成验证报告(成功/失败/警告)

5. **文档输出**
   - ✅ 自动生成Schema参考文档
   - ✅ 编写数据建模最佳实践指南
   - ✅ 提供常见错误和解决方案FAQ

## Out of Scope (本阶段不包含)

- ❌ Web界面的可视化编辑器
- ❌ 数据库存储(仅基于文件)
- ❌ 实时协作编辑功能
- ❌ 自动化内容生成(AI辅助)
- ❌ 复杂的图查询(能力依赖图)
- ❌ 多语言支持(i18n)

这些功能将在后续spec中实现。

## Dependencies

- Python 3.11+
- Pydantic v2
- PyYAML
- jsonschema
- typer (用于CLI)
- rich (用于输出美化)

## Risks & Mitigations

**风险1: Schema过于复杂导致贡献门槛高**
- 缓解: 提供丰富的模板和示例
- 缓解: 开发Schema辅助工具(自动补全、验证)

**风险2: 引用完整性检查性能问题**
- 缓解: 实现增量验证(仅检查变更文件)
- 缓解: 构建引用索引缓存

**风险3: Schema演进导致旧数据不兼容**
- 缓解: 严格遵循向后兼容原则
- 缓解: 提供自动化迁移脚本

**风险4: 跨实体依赖关系复杂难以维护**
- 缓解: 使用弱引用(字符串ID)而非强引用(对象)
- 缓解: 提供可视化依赖图工具

## Open Questions

1. 是否需要支持多语言字段(如`name-zh`, `name-en`)?
   - 建议: Phase 1仅支持中文,Phase 2引入i18n

2. 能力等级是否需要标准化(跨所有能力一致)?
   - 建议: 提供推荐定义,但允许灵活调整

3. 是否允许用户自定义枚举值?
   - 建议: 核心枚举固定,`tags`和`custom-fields`允许自由扩展

4. 数据验证是强制还是建议性?
   - 建议: 必填字段强制,可选字段警告但不阻塞

## Acceptance Criteria

- [ ] 所有4个核心实体的Schema定义完成并评审通过
- [ ] Pydantic模型实现并有单元测试覆盖
- [ ] 至少提供8个完整的数据示例(每个实体2个)
- [ ] CLI验证工具能运行并输出友好报告
- [ ] Schema文档自动生成并可阅读
- [ ] 内部团队评审通过,无重大设计缺陷
