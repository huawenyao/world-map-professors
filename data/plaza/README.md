# Plaza 数据目录

广场实体的 YAML 事实源。规范见 `docs/plaza/04-data-model.md`。

- `catalogs/` 受控词表，禁止在条目里自创同义标签
- `templates/` 编辑模板
- `people/` `brands/` `products/` 一实体一文件
- `ai-men/` 交付用数字专才；`solutions/` 场景解决方案 SKU
- `rankings/methods/` 方法版本；`rankings/snapshots/` 只读快照
- `ads/` 精选/广告，**排名计算不得读取本目录**

新增条目：复制模板 → 填来源与场景锚点 → 通过引用校验后再发榜。
