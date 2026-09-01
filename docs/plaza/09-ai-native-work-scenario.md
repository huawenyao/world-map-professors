# B2B AI 原生工作场景

场景：**开发者生态联合方案作战室**  
用户：科技企业生态 / 市场负责人（资源需求方）  
形态：Agent 以工具调用推进工作，而不是聊天框套一层 UI。

## 为何算 AI 原生

| 传统 B2B 后台 | 本 Demo |
|---------------|---------|
| 人去各个菜单里点筛选、导出、再开邮件 | Brief 进作战室，Agent 按工具链自己找、评、拟稿 |
| AI 是侧边写作助手 | AI 是运行时：parse → search → evaluate → gate → outreach → deliver |
| 低适配也让你继续点下一步 | `refuse` 是工具结果，没有换皮继续 |

工具读的是 `data/plaza/` 同一套供给（人、品牌、解决方案、AI Man），不是演示用假名单。

## 工作场景脚本

**目标**：在软件研发场景同时完成「找人 + 找企业合作」，评估后建联，并启动功能交付。

1. `parse_brief` 锁定场景与任务类型  
2. `search_talent` / `search_enterprises` 查库存  
3. `evaluate_fit` 输出适配、贡献、身份、匹配理由  
4. **人机门：短名单**  
5. `draft_outreach` 生成建联说明（不群发冷邮件）  
6. **人机门：建联稿**  
7. `open_campaign` + `advance_delivery` 打开功能交付  
8. **人机门：审查签收**  

对照 brief（财富管理达人投放）会在检索后 `refuse`：覆盖不足，禁止用研发供给充数。

入口：从 Plaza Store 数字专才详情点「调用 / 打开交付」，或直接打开 `demo/plaza/native/`。
