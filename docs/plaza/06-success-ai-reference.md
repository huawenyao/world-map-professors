# 对标 Success.ai 实际产品 Demo

参考对象：

- 营销 Demo：https://demo.success.ai/demo
- 工作台入口：https://app.success.ai/login
- 帮助中心模块：Lead Finder、Campaigns、InboxHub、Analytics
- 定价页结构：三档套餐、两个计量数字、一口价不按席

Success.ai 的品类是 **AI Sales OS（获客外联）**，不是榜单广场。借鉴的是**产品形态与 Demo 语法**，不是业务域。

## 1. 从公开 Demo / 帮助中心看到的真实结构

登录后不是百科首页，而是**左侧模块工作台**：

| 模块 | 用户在干什么 | 界面语法 |
|------|-------------|---------|
| Lead Finder | 从 7 亿级库里按行业/职位/规模过滤人 | 多过滤器 + 结果表 |
| Campaigns | 外联战役作为工作单元 | 卡片瓷砖：状态 + Sent/Open/Reply |
| InboxHub | 处理回复（Sent / Inbox / Unread） | 三块计数 + 列表 + 详情 |
| Analytics | 看战役是否有效 | 柱状图 + KPI 卡 |
| CRM / Pipeline | 把回复变成成交 | Kanban |
| AI Writer / Operator | 写邮件、回邮件 | 嵌在战役流里，不单独当官网栏目 |

营销 Demo 页的语法也很稳定：

1. 一句工作流口号（Find, Contact & Close）
2. 模块卖点块（库、发送、预热、AI 写手、统一收件箱）
3. 对标替代名单（Instantly / Smartlead / Reply.io）
4. Features & ROI 对比表
5. 社会证明 + 预约 Demo CTA

定价语法：

- **三个套餐，两个数字**（token 用量 + 邮件量）
- 全平台功能都在，差别是量、深度、集成
- 一口价，不按席位把团队拆碎
- Self-serve vs Done-for-you 两条交付

## 2. 映射到数字时代广场

| Success.ai | 广场对应 | 不要做成 |
|-----------|---------|---------|
| Find → Contact → Close | **找人/找企业 → 评估短名单 → 合作项目交付** | 五个互不相通的栏目站；也不做成灯笼街景 |
| Lead Finder | **找人 + 找企业** 两套过滤器 | 全站只有关键词搜索 |
| 700M 联系人库 | **供给库存**：人/品牌/产品/资产/工具，全部带场景锚点 | 无过滤器的长文维基 |
| Campaign 瓷砖 | **合作项目**（建联中 / 交付中 / 待签收） | 只有排行榜大数字 |
| AI Writer | **场景交付 / AI Man** | 自动生成不可审的名次 |
| InboxHub | **合作收件箱**（建联、认领、驳回买名次） | 只有邮箱联系我们 |
| Analytics | **评估与方法** | 虚荣 PV、粉丝榜 |
| 三套餐两数字 | **浏览 / 建联额度 / 交付席位** | 按席把坐标订阅拆碎 |

## 3. 因此产品形态改为「广场 OS」

原规划偏维基站点。对标 Demo 后，P0 可点击物应是：

```
左侧导航（常驻）
├── 工作台         运行中的解决方案 + 场景卡
├── 场景发现       过滤器（对标 Lead Finder）
├── 解决方案       场景 SKU（对标 Campaigns）
├── AI Man         数字专才 + 改编台
├── 五馆           名人 / 品牌 / 产品 / 资产 / 工具
├── 对比台         场景维度并排（对标 Features & ROI）
├── 认领队列       待审 / 已认证 / 驳回（对标 InboxHub）
├── 方法           双榜说明，付费隔离
└── 套餐           三档两数字
```

主路径与 Success.ai 同构：

1. **找人 / 找企业**（Find）
2. **评估并加入短名单**（Evaluate）
3. **合作项目建联**（Link）
4. **场景交付与检查点签收**（Deliver / Sign-off）

可点击原型：[`demo/plaza/`](../../demo/plaza/README.md)（`index.html` 营销 Demo，`app.html` 工作台）。

## 4. 明确不抄的部分

- 不抄冷邮件、预热、无限发送。那是另一条增长飞轮，会污染广场公信力。
- 不抄小豆芽的 50+ 账号矩阵发布、混剪与免密登号。
- 不编造 ROI 客户证言。Demo 只用样例街区与方法说明。
- 不把 AI 生成直接写成名次。AI 只辅助短名单与初稿，正式条人审。
