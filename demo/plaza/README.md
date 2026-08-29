# 数字时代广场 · 需求方工作台 Demo

设计语法对标 Success.ai（左导航 OS、Lead Finder、Campaign 瓷砖、InboxHub）。  
能力对标新榜海汇选号评估 + 小豆芽任务/收件闭环。  
**不做**灯笼街景，也**不做**多账号矩阵分发。

| 文件 | 用途 |
|------|------|
| `index.html` | 营销页：Find · Evaluate · Link · Deliver |
| `app.html` | 需求方工作台 |

主路径：找人 / 找企业 → 评估 → 短名单 → 合作项目 → 交付签收。财富管理显示覆盖不足，研发供给不得充数。

```bash
python3 -m http.server 4173 --directory demo/plaza
# http://127.0.0.1:4173/
# http://127.0.0.1:4173/app.html#people
# http://127.0.0.1:4173/app.html#orgs
```
