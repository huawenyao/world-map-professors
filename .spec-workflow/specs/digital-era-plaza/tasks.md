# Tasks: Digital Era Plaza

本 Spec 的 P0 以「规划落地为可校验数据 + 文档」为主；代码模型可随后按仓库既有 Pydantic 风格实现。

- [x] 1. 撰写广场愿景、商业模式、产品规划、数据模型、GTM
  - Files: `docs/plaza/*.md`
  - Purpose: 作为产品与商业的单一说明源
  - _Requirements: Alignment_

- [x] 2. 建立 Spec（requirements / design / tasks）
  - Files: `.spec-workflow/specs/digital-era-plaza/`
  - Purpose: 后续实现可验收
  - _Requirements: All_

- [x] 3. 增加广场受控词表与实体模板
  - Files: `data/plaza/catalogs/*`, `data/plaza/templates/*`
  - Purpose: 编辑可按同一 Schema 生产
  - _Requirements: 8.1_

- [x] 4. 增加旗舰场景样例实体（人物/品牌/产品/方法/快照）
  - Files: `data/plaza/people|brands|products|rankings/`
  - Purpose: 证明坐标互链，服务 MVP 叙事
  - _Requirements: 1, 2, 3_

- [x] 5. 为现有 Tool/Scenario 增加可选 plaza 元数据
  - Files: 种子 YAML
  - Purpose: 资产库可发布到广场
  - _Requirements: 5.1_

- [x] 6. 更新 product.md、README、项目路线图索引
  - Purpose: 仓库主叙事与广场对齐
  - _Requirements: Alignment_

- [x] 6b. 对标 Success.ai 实际 Demo，落地可点击工作台原型
  - Files: `docs/plaza/06-success-ai-reference.md`, `demo/plaza/`
  - Purpose: 产品形态从百科页改为 Finder / 场景卡 / 认领队列 / 三档套餐
  - _Requirements: 1, 2, 3, 7_

- [ ] 7. 实现 Pydantic 模型与 JSON Schema（实现阶段）
  - Files: `src/world_professors/models/plaza.py`, `schemas/plaza-*.json`
  - Purpose: 与现有 Scenario/Role 校验一致
  - _Leverage: models/base.py, 现有 schema_
  - _Requirements: 8.1, 8.2_

- [ ] 8. 实现 Plaza Repository 与场景聚合
  - Files: `repositories/plaza_repo.py`, 未来 `services/scene_assembler.py`
  - Purpose: 按 scenario_id 列出五馆短名单
  - _Requirements: 1.2, 2.1_

- [ ] 9. 扩展 DataValidator：plaza 引用 + 广告/排名隔离检查
  - _Requirements: 3.2, 5.3, 8.2, 8.3_

- [ ] 10. 场景页 / 五馆静态生成模板
  - _Requirements: 1, 2, 9 空态_

- [x] 11. 认领 Issue 模板与审核清单（P1 可用流程代替系统）
  - Files: `.github/ISSUE_TEMPLATE/plaza-claim.md`
  - _Requirements: 7_

- [ ] 12. P2 排名流水线与只读 API（依赖校验与覆盖密度）
  - _Requirements: 3, 企业/开发者故事_
