# 数字时代广场 · 可点击 Demo

对标 Success.ai 的两层 Demo：

| 文件 | 对标 | 用途 |
|------|------|------|
| `index.html` | https://demo.success.ai/demo | 营销 Demo：工作流口号、模块、对比表、打开工作台 |
| `app.html` | https://app.success.ai | 工作台 OS：左导航、场景发现、五馆、认领队列、套餐 |

数据来自仓库旗舰街区 **科技 / 软件研发**（GitHub Copilot、Claude、ChatGPT 及对应品牌/工具）。人物两条为 Schema 样例，页面上已标明。

## 本地打开

本地：

```bash
python3 -m http.server 4173 --directory demo/plaza
# 营销页 http://127.0.0.1:4173/
# 工作台 http://127.0.0.1:4173/app.html#solutions
# AI Man 改编台 http://127.0.0.1:4173/app.html#aiman
```

或直接用浏览器打开 `index.html`（部分环境对 file:// 的 hash 路由也可用）。
