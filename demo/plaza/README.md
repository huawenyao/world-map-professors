# 数字时代广场 · 可点击 Demo

一条有人的街，不是企业后台。

| 文件 | 用途 |
|------|------|
| `index.html` | 门厅：先见到人，再把活交给谁 |
| `app.html` | 广场里：问候、人物、货架、把活交给阿码 |

样例街区是 **科技 / 软件研发**（GitHub Copilot、Claude、ChatGPT）。人物两条为示意，页面上会标明不是真人排行。

## 本地打开

```bash
python3 -m http.server 4173 --directory demo/plaza
# 门厅 http://127.0.0.1:4173/
# 广场 http://127.0.0.1:4173/app.html#home
# 阿码  http://127.0.0.1:4173/app.html#aiman
```

点「去给人管钱」时，阿码会拒绝，且没有继续自动交付的按钮。
