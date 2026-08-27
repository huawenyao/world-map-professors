const DATA = {
  scene: {
    id: "scn-tech-software-dev",
    name: "软件研发",
    industry: "科技互联网",
    desc: "从需求到上线的研发闭环。广场样板街区：人物、品牌、产品、流程、Agent、工具挂在同一坐标上。",
    coverage: { people: 2, brands: 3, products: 3, tools: 3, assets: 4 },
    density: "100%",
    claimsOpen: 2,
  },
  kpis: [
    { label: "旗舰场景正式条", value: "12", note: "人+品牌+产品+工具" },
    { label: "坐标密度", value: "100%", note: "均含 scenario_ref" },
    { label: "待审认领", value: "2", note: "InboxHub 语法" },
    { label: "精选位写入榜", value: "0", note: "隔离检查通过" },
  ],
  products: [
    {
      id: "prd-github-copilot",
      name: "GitHub Copilot",
      brand: "GitHub",
      brandId: "brd-github",
      category: "编程助手",
      fit: "high",
      band: "S",
      rank: 1,
      user: "开发者",
      pricing: "订阅",
      kpis: ["编码吞吐", "样板代码耗时"],
      tools: ["tool-code-generator"],
      desc: "嵌入编辑器的编程助手。在本场景适配度为 high。",
      sources: 2,
    },
    {
      id: "prd-anthropic-claude",
      name: "Claude",
      brand: "Anthropic",
      brandId: "brd-anthropic",
      category: "搜索与问答",
      fit: "high",
      band: "A",
      rank: 2,
      user: "开发者 / 企业",
      pricing: "免费+用量",
      kpis: ["代码理解速度", "审查意见覆盖"],
      tools: ["tool-code-generator", "tool-code-reviewer"],
      desc: "长上下文代码阅读与审查辅助。场景适配 high。",
      sources: 2,
    },
    {
      id: "prd-openai-chatgpt",
      name: "ChatGPT",
      brand: "OpenAI",
      brandId: "brd-openai",
      category: "搜索与问答",
      fit: "medium",
      band: "A",
      rank: 3,
      user: "通用",
      pricing: "免费+订阅",
      kpis: ["需求澄清速度", "文档初稿耗时"],
      tools: ["tool-code-generator"],
      desc: "通用对话产品。软件场景适配 medium，不因热度压过专用助手。",
      sources: 2,
    },
  ],
  brands: [
    { id: "brd-github", name: "GitHub", type: "公司", band: "S", rank: 1, products: ["GitHub Copilot"], note: "工具与产品直接挂在编码工作流。" },
    { id: "brd-anthropic", name: "Anthropic", type: "实验室", band: "A", rank: 2, products: ["Claude"], note: "模型被代码生成/审查工具引用。" },
    { id: "brd-openai", name: "OpenAI", type: "实验室", band: "A", rank: 3, products: ["ChatGPT"], note: "代码生成工具供应商之一。" },
  ],
  people: [
    {
      id: "psn-tech-sample-ai-engineer",
      name: "示例·AI增强型软件工程师",
      type: "human",
      sample: true,
      headline: "样例实践者画像（非真人排行）",
    },
    {
      id: "psn-tech-sample-coding-persona",
      name: "示例·仓库编程分身",
      type: "digital-persona",
      sample: true,
      headline: "数字人格样例，已披露运营方 Anthropic / Claude",
    },
  ],
  tools: [
    { id: "tool-code-generator", name: "代码生成器", iface: "function-call", steps: "生成代码 / 重构", plaza: true },
    { id: "tool-code-reviewer", name: "AI代码审查工具", iface: "function-call", steps: "审查", plaza: true },
    { id: "tool-test-generator", name: "测试用例生成器", iface: "function-call", steps: "单测生成", plaza: true },
  ],
  assets: [
    { id: "scn-tech-software-dev", kind: "场景", name: "软件研发" },
    { id: "wf-tech-sd-feature-dev", kind: "流程", name: "功能开发流程" },
    { id: "agt-tech-sd-coding", kind: "Agent", name: "编程助手Agent" },
    { id: "cap-tech-001", kind: "能力", name: "编程能力" },
  ],
  claims: [
    { id: "c1", status: "pending", entity: "prd-github-copilot", who: "GitHub 官方申请（演示）", ask: "确认场景适配 high，补充企业合规摘录" },
    { id: "c2", status: "pending", entity: "prd-anthropic-claude", who: "Anthropic 文档站", ask: "把审查工具挂载写进产品页" },
    { id: "c3", status: "claimed", entity: "brd-openai", who: "开放收录", ask: "尚未认领，仅公开资料" },
    { id: "c4", status: "rejected", entity: "prd-spam", who: "未知域名", ask: "要求总榜第一（已拒：名次不可买）" },
  ],
};

const $ = (id) => document.getElementById(id);
let compareSet = new Set(["prd-github-copilot", "prd-anthropic-claude"]);
let claimFocus = "c1";
let finder = { category: "all", fit: "all", q: "" };

function go(hash) {
  location.hash = hash.startsWith("#") ? hash : "#" + hash;
}

function parse() {
  const raw = (location.hash || "#home").slice(1);
  const [name, id] = raw.split("/");
  return { name: name || "home", id };
}

function navActive(name) {
  document.querySelectorAll(".nav-btn").forEach((b) => {
    const g = b.getAttribute("data-go");
    const map = {
      home: "home",
      finder: "finder",
      people: "people",
      brands: "brands",
      products: "products",
      assets: "assets",
      tools: "tools",
      compare: "compare",
      claims: "claims",
      method: "method",
      pricing: "pricing",
      scene: "home",
      product: "products",
      brand: "brands",
      person: "people",
      tool: "tools",
    };
    b.classList.toggle("active", map[name] === g);
  });
}

function kpis() {
  return `<div class="kpis">${DATA.kpis
    .map((k) => `<div class="kpi"><span>${k.label}</span><b>${k.value}</b><span>${k.note}</span></div>`)
    .join("")}</div>`;
}

function productRow(p, withCheck) {
  return `<tr>
    <td class="rank">${p.rank}</td>
    <td><button class="linkish" data-go="product/${p.id}">${p.name}</button><div style="color:var(--muted);font-size:12px">${p.desc}</div></td>
    <td><button class="linkish" data-go="brand/${p.brandId}">${p.brand}</button></td>
    <td><span class="tag">${p.category}</span></td>
    <td><span class="band ${p.band}">${p.band}</span></td>
    <td><span class="tag ${p.fit === "high" ? "ok" : ""}">${p.fit}</span></td>
    <td>${withCheck ? `<input type="checkbox" data-cmp="${p.id}" ${compareSet.has(p.id) ? "checked" : ""}/>` : p.pricing}</td>
  </tr>`;
}

function viewHome() {
  const s = DATA.scene;
  return `
    <h1 class="page">工作台</h1>
    <p class="sub">对标 Campaigns + Analytics：场景是工作单元，不是栏目首页。</p>
    ${kpis()}
    <div class="tiles">
      <article class="card tile">
        <span class="tag gold">旗舰街区</span>
        <h3>${s.industry} · ${s.name}</h3>
        <p>${s.desc}</p>
        <div class="stats">
          <span>产品 <b>${s.coverage.products}</b></span>
          <span>工具 <b>${s.coverage.tools}</b></span>
          <span>认领待审 <b>${s.claimsOpen}</b></span>
        </div>
        <p style="margin-top:14px"><button class="btn-blue" data-go="scene/${s.id}">打开街区</button></p>
      </article>
      <article class="card tile">
        <span class="tag">空态示例</span>
        <h3>财富管理</h3>
        <p>金融种子已有场景与工具，产品/人物正式条不足 5，按规则显示覆盖不足，禁止拿研发网红产品填坑。</p>
        <div class="stats"><span>产品 <b>0</b></span><span>坐标密度 <b>—</b></span></div>
        <p class="empty" style="padding:12px 0 0">覆盖不足</p>
      </article>
      <article class="card tile">
        <span class="tag">方法</span>
        <h3>影响力 v1 · 专业贡献 v1</h3>
        <p>编辑快照 v0。付费精选目录与排名快照隔离，当前写入榜的精选条数为 0。</p>
        <p style="margin-top:14px"><button class="btn-line" data-go="method">查看方法</button></p>
      </article>
    </div>`;
}

function viewScene() {
  const s = DATA.scene;
  return `
    <h1 class="page">${s.industry} · ${s.name}</h1>
    <p class="sub">${s.desc}</p>
    <div class="coord">
      <span class="tag gold">${s.id}</span>
      <span class="tag">流程 wf-tech-sd-feature-dev</span>
      <span class="tag">Agent agt-tech-sd-coding</span>
    </div>
    <div class="detail-grid">
      <div>
        <h3>产品短名单（影响力编辑 v0）</h3>
        <table class="data">
          <thead><tr><th>#</th><th>产品</th><th>品牌</th><th>品类</th><th>带</th><th>适配</th><th>加入对比</th></tr></thead>
          <tbody>${DATA.products.map((p) => productRow(p, true)).join("")}</tbody>
        </table>
        <p style="margin-top:10px"><button class="btn-blue" data-go="compare">去对比台</button></p>
      </div>
      <div>
        <div class="card">
          <h3>资产</h3>
          ${DATA.assets.map((a) => `<p><span class="tag">${a.kind}</span> ${a.name}</p>`).join("")}
        </div>
        <div class="card" style="margin-top:12px">
          <h3>工具（可调用）</h3>
          ${DATA.tools.map((t) => `<p><button class="linkish" data-go="tool/${t.id}">${t.name}</button> · ${t.iface}</p>`).join("")}
        </div>
      </div>
    </div>`;
}

function viewFinder() {
  const list = DATA.products.filter((p) => {
    if (finder.category !== "all" && p.category !== finder.category) return false;
    if (finder.fit !== "all" && p.fit !== finder.fit) return false;
    const q = (finder.q || $("q").value || "").trim();
    if (q && !`${p.name}${p.brand}${p.category}`.includes(q)) return false;
    return true;
  });
  return `
    <h1 class="page">场景发现</h1>
    <p class="sub">对标 Lead Finder：先滤场景与适配，再看实体。当前范围锁定样例街区「软件研发」。</p>
    <div class="filters">
      <select id="f-cat">
        <option value="all">全部品类</option>
        <option ${finder.category === "编程助手" ? "selected" : ""}>编程助手</option>
        <option ${finder.category === "搜索与问答" ? "selected" : ""}>搜索与问答</option>
      </select>
      <select id="f-fit">
        <option value="all">全部适配</option>
        <option value="high" ${finder.fit === "high" ? "selected" : ""}>high</option>
        <option value="medium" ${finder.fit === "medium" ? "selected" : ""}>medium</option>
      </select>
    </div>
    <table class="data">
      <thead><tr><th>#</th><th>产品</th><th>品牌</th><th>品类</th><th>带</th><th>适配</th><th>定价</th></tr></thead>
      <tbody>${list.map((p) => productRow(p, false)).join("") || `<tr><td colspan="7" class="empty">没有匹配。不会用其它场景产品填充。</td></tr>`}</tbody>
    </table>`;
}

function viewList(kind) {
  if (kind === "products") {
    return `<h1 class="page">产品榜 · 软件研发</h1>
      <p class="sub">双榜中的影响力编辑 v0。ChatGPT 热度更高，但适配 medium，故排在专用助手之后。</p>
      <table class="data"><thead><tr><th>#</th><th>产品</th><th>品牌</th><th>品类</th><th>带</th><th>适配</th><th>定价</th></tr></thead>
      <tbody>${DATA.products.map((p) => productRow(p, false)).join("")}</tbody></table>`;
  }
  if (kind === "brands") {
    return `<h1 class="page">品牌榜 · 专业贡献 v0</h1>
      <table class="data"><thead><tr><th>#</th><th>品牌</th><th>类型</th><th>带</th><th>产品</th><th>依据</th></tr></thead>
      <tbody>${DATA.brands
        .map(
          (b) => `<tr><td class="rank">${b.rank}</td><td><button class="linkish" data-go="brand/${b.id}">${b.name}</button></td>
          <td>${b.type}</td><td><span class="band ${b.band}">${b.band}</span></td><td>${b.products.join("、")}</td><td>${b.note}</td></tr>`
        )
        .join("")}</tbody></table>`;
  }
  if (kind === "people") {
    return `<h1 class="page">名人榜</h1>
      <p class="sub">样例条目，非正式真人排行。数字人格强制标记。</p>
      <table class="data"><thead><tr><th>名称</th><th>类型</th><th>说明</th></tr></thead>
      <tbody>${DATA.people
        .map(
          (p) => `<tr><td><button class="linkish" data-go="person/${p.id}">${p.name}</button></td>
          <td>${p.type === "digital-persona" ? '<span class="tag warn">数字人格</span>' : '<span class="tag">自然人</span>'}
          ${p.sample ? '<span class="tag">样例</span>' : ""}</td><td>${p.headline}</td></tr>`
        )
        .join("")}</tbody></table>`;
  }
  if (kind === "tools") {
    return `<h1 class="page">工具库</h1>
      <p class="sub">接口类型可过滤。全部已 publish_to_plaza。</p>
      <table class="data"><thead><tr><th>工具</th><th>接口</th><th>步骤</th></tr></thead>
      <tbody>${DATA.tools
        .map(
          (t) => `<tr><td><button class="linkish" data-go="tool/${t.id}">${t.name}</button></td>
          <td><span class="tag">${t.iface}</span></td><td>${t.steps}</td></tr>`
        )
        .join("")}</tbody></table>`;
  }
  return `<h1 class="page">行业资产库</h1>
    <p class="sub">同一 YAML 事实源，不另起 CMS。</p>
    <table class="data"><thead><tr><th>类型</th><th>名称</th><th>ID</th></tr></thead>
    <tbody>${DATA.assets.map((a) => `<tr><td><span class="tag">${a.kind}</span></td><td>${a.name}</td><td>${a.id}</td></tr>`).join("")}</tbody></table>`;
}

function viewProduct(id) {
  const p = DATA.products.find((x) => x.id === id) || DATA.products[0];
  return `
    <h1 class="page">${p.name}</h1>
    <p class="sub">${p.desc}</p>
    <div class="coord">
      <span class="tag gold">scn-tech-software-dev</span>
      <span class="tag">品牌 ${p.brand}</span>
      <span class="tag">适配 ${p.fit}</span>
      <span class="band ${p.band}">影响力 ${p.band}</span>
    </div>
    <div class="detail-grid">
      <div class="card">
        <h3>场景适配表</h3>
        <p>软件研发 · 增强编码/审查 · KPI：${p.kpis.join("、")}</p>
        <h3 style="margin-top:16px">实现的工具</h3>
        ${p.tools.map((t) => `<p><button class="linkish" data-go="tool/${t}">${t}</button></p>`).join("")}
        <p style="margin-top:16px"><button class="btn-line" data-cmp-toggle="${p.id}">${compareSet.has(p.id) ? "已加入对比" : "加入对比"}</button>
        <button class="btn-blue" data-go="claims">申请认领</button></p>
      </div>
      <div class="card">
        <h3>来源</h3>
        <p>${p.sources} 条官方来源（演示）。正式发布需可点开。</p>
        <h3 style="margin-top:16px">定价</h3>
        <p>${p.pricing} · ${p.user}</p>
      </div>
    </div>`;
}

function viewBrand(id) {
  const b = DATA.brands.find((x) => x.id === id) || DATA.brands[0];
  const ps = DATA.products.filter((p) => p.brandId === b.id);
  return `<h1 class="page">${b.name}</h1>
    <p class="sub">${b.note}</p>
    <div class="coord"><span class="band ${b.band}">贡献 ${b.band}</span><span class="tag">${b.type}</span></div>
    <h3>产品组合</h3>
    <table class="data"><tbody>${ps.map((p) => productRow(p, false)).join("")}</tbody></table>`;
}

function viewPerson(id) {
  const p = DATA.people.find((x) => x.id === id) || DATA.people[0];
  return `<h1 class="page">${p.name}</h1>
    ${p.type === "digital-persona" ? '<div class="featured">非自然人 · 运营方 / 模型已披露。不进入真人影响力榜。</div>' : ""}
    ${p.sample ? '<span class="tag">Schema 样例，非正式名人榜事实</span>' : ""}
    <p class="sub">${p.headline}</p>
    <div class="coord"><span class="tag gold">scn-tech-software-dev</span><span class="tag">cap-tech-001</span></div>`;
}

function viewTool(id) {
  const t = DATA.tools.find((x) => x.id === id) || DATA.tools[0];
  const used = DATA.products.filter((p) => p.tools.includes(t.id));
  return `<h1 class="page">${t.name}</h1>
    <p class="sub">接口 ${t.iface} · 步骤 ${t.steps} · 已发布到广场</p>
    <h3>被哪些产品实现</h3>
    <table class="data"><tbody>${used.map((p) => productRow(p, false)).join("") || "<tr><td>无</td></tr>"}</tbody></table>`;
}

function viewCompare() {
  const rows = DATA.products.filter((p) => compareSet.has(p.id));
  const dims = ["场景", "适配", "品类", "定价", "工具", "来源数"];
  return `
    <h1 class="page">对比台</h1>
    <p class="sub">对标 Success.ai 的 Features &amp; ROI 表，但维度是场景适配，不是发信量。精选广告不会出现在此表。</p>
    <div class="featured">本区为有机对比。付费精选位另有虚线样式，且不能改名次。</div>
    <table class="cmp">
      <thead><tr><th>维度</th>${rows.map((p) => `<th>${p.name}</th>`).join("")}</tr></thead>
      <tbody>
        <tr><td>场景</td>${rows.map(() => "<td>软件研发</td>").join("")}</tr>
        <tr><td>适配</td>${rows.map((p) => `<td>${p.fit}</td>`).join("")}</tr>
        <tr><td>品类</td>${rows.map((p) => `<td>${p.category}</td>`).join("")}</tr>
        <tr><td>定价</td>${rows.map((p) => `<td>${p.pricing}</td>`).join("")}</tr>
        <tr><td>工具</td>${rows.map((p) => `<td>${p.tools.join("<br>")}</td>`).join("")}</tr>
        <tr><td>影响力带</td>${rows.map((p) => `<td><span class="band ${p.band}">${p.band}</span></td>`).join("")}</tr>
      </tbody>
    </table>
    <p class="sub" style="margin-top:12px">勾选产品榜中的「加入对比」可改列。当前：${[...compareSet].join("、") || "无"}</p>`;
}

function viewClaims() {
  const groups = {
    pending: DATA.claims.filter((c) => c.status === "pending"),
    claimed: DATA.claims.filter((c) => c.status === "claimed"),
    rejected: DATA.claims.filter((c) => c.status === "rejected"),
  };
  const cur = DATA.claims.find((c) => c.id === claimFocus) || DATA.claims[0];
  const col = (title, arr, key) => `
    <div class="q-col">
      <h3>${title} (${arr.length})</h3>
      ${arr
        .map(
          (c) => `<div class="q-item ${c.id === cur.id ? "active" : ""}" data-claim="${c.id}">
            <b>${c.entity}</b><div style="color:var(--muted);font-size:12px">${c.who}</div></div>`
        )
        .join("")}
    </div>`;
  return `
    <h1 class="page">认领队列</h1>
    <p class="sub">对标 InboxHub：Sent / Inbox / Unread 换成 待审 / 已认证 / 驳回。认证不等于改名次。</p>
    <div class="queue">
      ${col("待审", groups.pending)}
      ${col("已认证 / 开放收录", groups.claimed)}
      <div class="q-col">
        <h3>工单详情</h3>
        <p><span class="tag">${cur.status}</span> ${cur.entity}</p>
        <p>${cur.who}</p>
        <p>${cur.ask}</p>
        ${cur.status === "rejected" ? '<p class="tag warn">拒绝理由：名次不可买</p>' : ""}
        <p style="margin-top:16px"><button class="btn-line">通过（演示）</button> <button class="btn-line">驳回（演示）</button></p>
        <h3 style="margin-top:20px">驳回箱 (${groups.rejected.length})</h3>
        ${groups.rejected.map((c) => `<div class="q-item" data-claim="${c.id}">${c.entity}<div style="font-size:12px;color:var(--muted)">${c.ask}</div></div>`).join("")}
      </div>
    </div>`;
}

function viewMethod() {
  return `
    <h1 class="page">方法与信任</h1>
    <p class="sub">对标 Analytics：公开窗口与剔除规则，而不是虚荣 PV。</p>
    <div class="grid-2">
      <article class="card">
        <h3>影响力方法 v1</h3>
        <p>窗口 90 天。信号：独立引用 0.4 · 公开采用 0.3 · 场景相关 0.3。排除付费曝光与自报 GMV。</p>
      </article>
      <article class="card">
        <h3>专业贡献方法 v1</h3>
        <p>窗口 180 天。信号：标准库引用 0.4 · 可复核产物 0.35 · 场景适配 0.25。</p>
      </article>
    </div>
    <div class="featured" style="margin-top:16px">广告目录 data/plaza/ads/ 不得写入 RankingSnapshot。本 Demo 精选写入名次 = 0。</div>`;
}

function viewPricing() {
  return `
    <h1 class="page">套餐</h1>
    <p class="sub">对标 Success.ai「三个套餐，两个数字」：全平台功能都在，差的是量与深度，不按席把团队拆碎。名次不在价目表里。</p>
    <div class="price-grid">
      <article class="card price">
        <h3>广场访客</h3>
        <div class="num">¥0</div>
        <p>两个数字：浏览无限 · 对比 0 次导出</p>
        <ul><li>场景页与有机榜</li><li>方法说明</li><li>无认领工单</li></ul>
      </article>
      <article class="card price">
        <h3>厂商认证</h3>
        <div class="num">年费</div>
        <p>两个数字：产品数 · 精选曝光槽（可选）</p>
        <ul><li>官方描述与纠错</li><li>认证标</li><li>精选须标注，不进分数</li></ul>
        <button class="btn-blue" data-go="claims">去认领队列</button>
      </article>
      <article class="card price">
        <h3>企业坐标</h3>
        <div class="num">年费</div>
        <p>两个数字：席位 · 行业包</p>
        <ul><li>能力矩阵导出</li><li>场景短名单 API</li><li>私有映射（P2）</li></ul>
      </article>
    </div>`;
}

function render() {
  const { name, id } = parse();
  navActive(name);
  const root = $("view");
  const map = {
    home: viewHome,
    finder: viewFinder,
    people: () => viewList("people"),
    brands: () => viewList("brands"),
    products: () => viewList("products"),
    assets: () => viewList("assets"),
    tools: () => viewList("tools"),
    compare: viewCompare,
    claims: viewClaims,
    method: viewMethod,
    pricing: viewPricing,
    scene: viewScene,
    product: () => viewProduct(id),
    brand: () => viewBrand(id),
    person: () => viewPerson(id),
    tool: () => viewTool(id),
  };
  root.innerHTML = (map[name] || viewHome)();

  root.querySelector("#f-cat")?.addEventListener("change", (e) => {
    finder.category = e.target.value;
    render();
  });
  root.querySelector("#f-fit")?.addEventListener("change", (e) => {
    finder.fit = e.target.value;
    render();
  });
}

document.addEventListener("click", (e) => {
  const goBtn = e.target.closest("[data-go]");
  if (goBtn) {
    e.preventDefault();
    go(goBtn.getAttribute("data-go"));
    return;
  }
  const cmp = e.target.closest("[data-cmp]");
  if (cmp) {
    const id = cmp.getAttribute("data-cmp");
    if (cmp.checked) compareSet.add(id);
    else compareSet.delete(id);
    return;
  }
  const tog = e.target.closest("[data-cmp-toggle]");
  if (tog) {
    const id = tog.getAttribute("data-cmp-toggle");
    if (compareSet.has(id)) compareSet.delete(id);
    else compareSet.add(id);
    render();
    return;
  }
  const cl = e.target.closest("[data-claim]");
  if (cl) {
    claimFocus = cl.getAttribute("data-claim");
    render();
  }
});

$("q").addEventListener("input", () => {
  finder.q = $("q").value;
  if (parse().name === "finder") render();
});

window.addEventListener("hashchange", render);
if (!location.hash) location.hash = "#home";
else render();
