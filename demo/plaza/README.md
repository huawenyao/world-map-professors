# Plaza Store

交互对标 **Apple App Store**。货架上不是 App，而是**个人**和**企业**。

| 路径 | 对标 |
|------|------|
| `index.html#/today` | Today 编辑专题 |
| `#/people` | Games/Apps：人的货架、真人示意榜、数字人格隔离 |
| `#/orgs` | 企业货架 |
| `#/search` | Search |
| `#/library` | 已加入 / 进行中 / 通知 |
| `#/resource/{id}` | 资源详情页（Get、预览、评估、信息） |
| `native/` | 数字专才的交付活动（In-App Event） |

硬约束：名次不可买；数字人格不进真人榜；财富管理覆盖不足不得用研发供给填充。

```bash
python3 -m http.server 4173 --directory demo/plaza
# http://127.0.0.1:4173/
```
