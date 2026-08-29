const DATA = {
  people: [
    {
      id: "psn-tech-sample-ai-engineer",
      name: "阿凯",
      type: "human",
      role: "软件研发实践者",
      scene: "软件研发",
      fit: "high",
      contrib: "A",
      status: "可建联",
      sample: true,
      why: "场景内有可复核实践。样例条目，非正式达人排行。",
    },
    {
      id: "psn-tech-sample-coding-persona",
      name: "小仓",
      type: "digital-persona",
      role: "编程数字人格",
      scene: "软件研发",
      fit: "high",
      contrib: "B",
      status: "可调用",
      sample: true,
      why: "已披露非真人。可辅助编码，不可充当真人达人投放。",
    },
  ],
  specialists: [
    {
      id: "aim-tech-sd-feature",
      name: "阿码",
      type: "ai-man",
      role: "软件研发数字专才",
      scene: "软件研发",
      fit: "high",
      contrib: "S",
      status: "可交付",
      why: "绑定功能交付解决方案。审查必须人签。不进真人达人榜。",
    },
  ],
  brands: [
    { id: "brd-github", name: "GitHub", type: "公司", scene: "软件研发", fit: "high", band: "S", partner: "开发者生态合作", status: "可建联", note: "产品 GitHub Copilot 锚定本场景。", products: ["GitHub Copilot"] },
    { id: "brd-anthropic", name: "Anthropic", type: "实验室", scene: "软件研发", fit: "high", band: "A", partner: "模型与审查能力", status: "可建联", note: "Claude 适合仓库级理解与审查。", products: ["Claude"] },
    { id: "brd-openai", name: "OpenAI", type: "实验室", scene: "软件研发", fit: "medium", band: "A", partner: "通用对话能力", status: "开放收录", note: "熟，但不是本场景第一供给。", products: ["ChatGPT"] },
  ],
  products: [
    { id: "prd-github-copilot", name: "GitHub Copilot", brand: "GitHub", brandId: "brd-github", category: "编程助手", fit: "high", band: "S", desc: "编码助手，场景适配高。" },
    { id: "prd-anthropic-claude", name: "Claude", brand: "Anthropic", brandId: "brd-anthropic", category: "搜索与问答", fit: "high", band: "A", desc: "长上下文审查与方案讨论。" },
    { id: "prd-openai-chatgpt", name: "ChatGPT", brand: "OpenAI", brandId: "brd-openai", category: "搜索与问答", fit: "medium", band: "A", desc: "通用对话。本场景不排第一。" },
  ],
  assets: [
    { id: "scn-tech-software-dev", kind: "场景", name: "软件研发" },
    { id: "wf-tech-sd-feature-dev", kind: "流程", name: "功能开发流程" },
    { id: "agt-tech-sd-coding", kind: "Agent", name: "编程助手 Agent" },
    { id: "cap-tech-001", kind: "能力", name: "编程能力" },
  ],
  tools: [
    { id: "tool-code-generator", name: "代码生成器", steps: "生成 / 重构" },
    { id: "tool-code-reviewer", name: "代码审查工具", steps: "审查" },
    { id: "tool-test-generator", name: "测试用例生成器", steps: "单测生成" },
  ],
  campaigns: [
    { id: "camp-dev", name: "软件研发功能交付", kind: "场景交付", status: "交付中", supply: "阿码", scene: "软件研发", sent: 4, wait: 1, replies: 2, go: "deliver" },
    { id: "camp-org", name: "开发者生态企业合作", kind: "找企业", status: "建联中", supply: "GitHub", scene: "软件研发", sent: 2, wait: 1, replies: 0, go: "orgs" },
    { id: "camp-wm", name: "财富管理达人合作", kind: "覆盖不足", status: "不可用", supply: "—", scene: "财富管理", sent: 0, wait: 0, replies: 0, blocked: true, go: "people" },
  ],
  inbox: [
    { id: "i1", col: "link", title: "GitHub 企业合作意向", who: "需求方发出（演示）", body: "希望确认 Copilot 企业场景适配与合规摘录。" },
    { id: "i2", col: "claim", title: "Claude 条目纠错", who: "Anthropic 文档站", body: "请把审查工具挂载写进产品页。" },
    { id: "i3", col: "open", title: "OpenAI 开放收录", who: "系统", body: "尚未认领，仅公开资料。" },
    { id: "i4", col: "reject", title: "要求总榜第一", who: "未知域名", body: "已拒：名次不可买。付费只买曝光位。" },
  ],
  evals: {
    person: [
      { dim: "场景适配", val: "high", note: "主场软件研发，有流程锚点。" },
      { dim: "专业贡献", val: "A", note: "可复核实践，非正式排行。" },
      { dim: "可交付", val: "可建联", note: "真人实践者，适合联合方案而非投放粉数。" },
      { dim: "身份", val: "真人", note: "样例 Schema，非名人榜事实。" },
    ],
    org: [
      { dim: "场景适配", val: "high", note: "开发者工作流覆盖完整。" },
      { dim: "专业贡献", val: "S", note: "产品进入本场景短名单。" },
      { dim: "可交付", val: "可建联", note: "企业合作，不是广告位。" },
      { dim: "身份", val: "公司", note: "品牌 ≠ 产品。合作看产品组合。" },
    ],
  },
  runSteps: [
    { name: "需求理解", status: "done" },
    { name: "方案确认", status: "done", gate: true },
    { name: "编码实现", status: "done" },
    { name: "测试生成", status: "done" },
    { name: "代码审查", status: "gate", gate: true },
    { name: "合并上线", status: "queued" },
  ],
  adapt: {
    home: { label: "软件研发（本场）", fit: "high", allow: true, body: "主场交付。三处人机门仍需签收。" },
    qa: { label: "测试与质量（相邻）", fit: "high", allow: true, body: "可改编：测试工具前置，审查仍要人。" },
    wealth: { label: "财富管理（跨域）", fit: "low", allow: false, body: "拒绝自动交付。缺金融评估能力，不得用研发供给充数。" },
  },
};

const $ = (id) => document.getElementById(id);
let shortlist = new Set(["psn-tech-sample-ai-engineer", "brd-github"]);
let inboxId = "i1";
let adaptKey = "home";
let pf = { scene: "软件研发", type: "all" };
let of = { scene: "软件研发", type: "all" };
let productCat = "all";

function go(hash) {
  location.hash = hash.startsWith("#") ? hash : "#" + hash;
}
function parse() {
  const raw = (location.hash || "#home").slice(1);
  const [name, id] = raw.split("/");
  return { name: name || "home", id };
}
function navActive(name) {
  const map = {
    home: "home",
    people: "people",
    person: "people",
    orgs: "orgs",
    brand: "orgs",
    eval: "eval",
    shortlist: "shortlist",
    campaigns: "campaigns",
    deliver: "deliver",
    inbox: "inbox",
    "supply-people": "supply-people",
    "supply-brands": "supply-brands",
    "supply-products": "supply-products",
    product: "supply-products",
    "supply-assets": "supply-assets",
    "supply-tools": "supply-tools",
    method: "method",
    pricing: "pricing",
  };
  document.querySelectorAll(".nav-item").forEach((b) => {
    b.classList.toggle("active", map[name] === b.getAttribute("data-go"));
  });
}
function q() {
  return ($("q")?.value || "").trim();
}
function typeLabel(t) {
  return { human: "真人", "digital-persona": "数字人格", "ai-man": "数字专才" }[t] || t;
}
function fitTag(f) {
  return `<span class="tag ${f === "high" ? "ok" : "warn"}">适配 ${f}</span>`;
}
function allPeople() {
  return [...DATA.people, ...DATA.specialists];
}

function metrics(c) {
  return `<div class="metric-row">
    <div class="metric"><span>建联</span><b>${c.sent}</b></div>
    <div class="metric"><span>待处理</span><b>${c.wait}</b></div>
    <div class="metric"><span>回复</span><b>${c.replies}</b></div>
  </div>`;
}

function campCard(c, opts = {}) {
  const goTo = opts.go || (c.go === "deliver" ? "deliver" : c.go === "orgs" ? "inbox" : c.go);
  const label = opts.label || "进入";
  const blockedText = opts.blockedText || "无「用研发达人充数」按钮";
  return `<article class="camp-card">
    <span class="tag ${c.blocked ? "bad" : c.status === "交付中" ? "gold" : "ok"}">${c.status}</span>
    <h3>${c.name}</h3>
    <p class="muted">${c.kind} · 供给 ${c.supply} · ${c.scene}</p>
    ${metrics(c)}
    <div class="actions">
      ${c.blocked
        ? `<span class="muted">${blockedText}</span>`
        : `<button class="btn-blue" data-go="${goTo}">${label}</button>`}
    </div>
  </article>`;
}

function viewHome() {
  const running = DATA.campaigns.filter((c) => !c.blocked).length;
  return `
    <h1 class="page">需求方工作台</h1>
    <p class="sub">Find · Evaluate · Link · Deliver。五馆是库存；合作项目才是成交单元。</p>
    <div class="kpis">
      <div class="kpi"><span>浏览</span><b>无限</b><span>找人 / 找企业只读不限</span></div>
      <div class="kpi"><span>建联额度</span><b>12</b><span>本档演示额度，名次不在价目</span></div>
      <div class="kpi"><span>交付席位</span><b>1</b><span>数字专才并发 · 人机门仍开</span></div>
      <div class="kpi"><span>进行中战役</span><b>${running}</b><span>1 条覆盖不足已拒绝</span></div>
    </div>
    <article class="card" style="margin-bottom:14px">
      <span class="tag gold">AI Operator</span>
      <h3>开发者生态联合方案</h3>
      <p>作战室对标 Campaign 运行页：Brief → 工具活动流 → 人机门。不是聊天套壳。</p>
      <div class="actions"><a class="btn-blue" href="native/index.html">打开作战室</a></div>
    </article>
    <div class="camp-grid">${DATA.campaigns.map((c) => campCard(c, { go: c.go, label: "打开", blockedText: "无「用研发达人充数」按钮" })).join("")}</div>`;
}

function viewPeople() {
  const list = allPeople().filter((p) => {
    if (pf.scene !== "all" && p.scene !== pf.scene) return false;
    if (pf.type !== "all" && p.type !== pf.type) return false;
    const s = q();
    if (s && !`${p.name}${p.role}${p.scene}`.includes(s)) return false;
    return true;
  });
  return `
    <h1 class="page">找人</h1>
    <p class="sub">对标 Lead Finder / 海汇选号。先锁场景，再看身份与适配。财富管理当前覆盖不足。</p>
    <div class="filters">
      <select id="pf-scene">
        <option ${pf.scene === "软件研发" ? "selected" : ""}>软件研发</option>
        <option ${pf.scene === "测试与质量" ? "selected" : ""}>测试与质量</option>
        <option ${pf.scene === "财富管理" ? "selected" : ""}>财富管理</option>
        <option value="all" ${pf.scene === "all" ? "selected" : ""}>全部场景</option>
      </select>
      <select id="pf-type">
        <option value="all">全部身份</option>
        <option value="human" ${pf.type === "human" ? "selected" : ""}>真人</option>
        <option value="digital-persona" ${pf.type === "digital-persona" ? "selected" : ""}>数字人格</option>
        <option value="ai-man" ${pf.type === "ai-man" ? "selected" : ""}>数字专才</option>
      </select>
    </div>
    ${
      pf.scene === "财富管理"
        ? `<div class="empty">财富管理达人库存覆盖不足。不会用软件研发供给填充。</div>`
        : `<table class="data">
            <thead><tr><th>名称</th><th>身份</th><th>角色</th><th>适配</th><th>贡献</th><th>状态</th><th></th></tr></thead>
            <tbody>${list.map((p) => `
              <tr>
                <td><button class="linkish" data-go="person/${p.id}">${p.name}</button>
                  ${p.sample ? '<div class="muted">样例</div>' : ""}</td>
                <td><span class="tag ${p.type === "human" ? "ok" : "warn"}">${typeLabel(p.type)}</span></td>
                <td>${p.role}</td>
                <td>${fitTag(p.fit)}</td>
                <td><span class="band ${p.contrib}">${p.contrib}</span></td>
                <td>${p.status}</td>
                <td><button class="btn-line" data-sl="${p.id}">${shortlist.has(p.id) ? "已在短名单" : "加入短名单"}</button></td>
              </tr>`).join("") || `<tr><td colspan="7" class="empty">无匹配供给</td></tr>`}
            </tbody>
          </table>`
    }`;
}

function viewOrgs() {
  const list = DATA.brands.filter((b) => {
    if (of.scene !== "all" && b.scene !== of.scene) return false;
    if (of.type !== "all" && b.type !== of.type) return false;
    const s = q();
    if (s && !`${b.name}${b.partner}${b.type}`.includes(s)) return false;
    return true;
  });
  return `
    <h1 class="page">找企业</h1>
    <p class="sub">同一套 Lead Finder 语法，目标换成可合作品牌与机构。</p>
    <div class="filters">
      <select id="of-scene">
        <option ${of.scene === "软件研发" ? "selected" : ""}>软件研发</option>
        <option ${of.scene === "财富管理" ? "selected" : ""}>财富管理</option>
        <option value="all" ${of.scene === "all" ? "selected" : ""}>全部场景</option>
      </select>
      <select id="of-type">
        <option value="all">全部类型</option>
        <option ${of.type === "公司" ? "selected" : ""}>公司</option>
        <option ${of.type === "实验室" ? "selected" : ""}>实验室</option>
      </select>
    </div>
    ${
      of.scene === "财富管理"
        ? `<div class="empty">财富管理可合作企业覆盖不足。不拿科技公司充数。</div>`
        : `<table class="data">
            <thead><tr><th>企业</th><th>类型</th><th>合作切口</th><th>适配</th><th>贡献带</th><th></th></tr></thead>
            <tbody>${list.map((b) => `
              <tr>
                <td><button class="linkish" data-go="brand/${b.id}">${b.name}</button></td>
                <td>${b.type}</td>
                <td>${b.partner}<div class="reason">${b.note}</div></td>
                <td>${fitTag(b.fit)}</td>
                <td><span class="band ${b.band}">${b.band}</span></td>
                <td><button class="btn-line" data-sl="${b.id}">${shortlist.has(b.id) ? "已在短名单" : "加入短名单"}</button></td>
              </tr>`).join("")}
            </tbody>
          </table>`
    }`;
}

function viewEval() {
  return `
    <h1 class="page">评估</h1>
    <p class="sub">对标海汇荐号评分，但尺子是场景坐标系：适配、贡献、可交付、身份。粉丝数不进正式名次。</p>
    <div class="grid-2">
      <article class="card">
        <span class="tag ok">人 · 样例</span>
        <h3>阿凯 · 软件研发实践者</h3>
        ${DATA.evals.person.map((e) => `<p><strong>${e.dim}</strong> ${e.val}<span class="reason"> ${e.note}</span></p>`).join("")}
        <div class="actions"><button class="btn-blue" data-sl="psn-tech-sample-ai-engineer">加入短名单</button></div>
      </article>
      <article class="card">
        <span class="tag">企业</span>
        <h3>GitHub · 开发者生态合作</h3>
        ${DATA.evals.org.map((e) => `<p><strong>${e.dim}</strong> ${e.val}<span class="reason"> ${e.note}</span></p>`).join("")}
        <div class="actions"><button class="btn-blue" data-sl="brd-github">加入短名单</button></div>
      </article>
    </div>
    <p class="featured" style="margin-top:14px">数字专才「阿码」可评估可交付，但单独成列，不进入真人达人榜。</p>`;
}

function viewShortlist() {
  const people = allPeople().filter((p) => shortlist.has(p.id));
  const orgs = DATA.brands.filter((b) => shortlist.has(b.id));
  return `
    <h1 class="page">短名单</h1>
    <p class="sub">人与企业混排，对应海汇「荐号包」+ 企业合作意向。下一步是合作项目。</p>
    ${!people.length && !orgs.length ? `<div class="empty">短名单为空。从找人或找企业加入。</div>` : ""}
    <div class="grid-2">
      ${people.map((p) => `<article class="card"><span class="tag ${p.type === "human" ? "ok" : "warn"}">${typeLabel(p.type)}</span><h3>${p.name}</h3><p>${p.role} · ${p.why}</p></article>`).join("")}
      ${orgs.map((b) => `<article class="card"><span class="tag">${b.type}</span><h3>${b.name}</h3><p>${b.partner} · ${b.note}</p></article>`).join("")}
    </div>
    <div class="actions"><button class="btn-blue" data-go="campaigns">转为合作项目</button></div>`;
}

function viewCampaigns() {
  return `
    <h1 class="page">合作项目</h1>
    <p class="sub">对标 Success.ai Campaigns：状态 + 建联 / 待处理 / 回复 三数字。一个项目 = 一次供给调用。</p>
    <div class="camp-grid">${DATA.campaigns.map((c) => campCard(c, { blockedText: "已拒绝自动交付" })).join("")}</div>`;
}

function viewDeliver() {
  const a = DATA.adapt[adaptKey];
  return `
    <h1 class="page">交付 · 软件研发功能交付</h1>
    <p class="sub">数字专才阿码按流程执行。金色节点必须人签。低适配场景拒绝充数。</p>
    <div class="grid-2">
      <ul class="timeline">
        ${DATA.runSteps.map((s) => `
          <li>
            <span class="dot ${s.status === "done" ? "done" : s.status === "gate" ? "gate" : ""}"></span>
            <b>${s.name}</b>
            <div>${s.status === "gate" ? '<span class="tag gold">待签收</span> <button class="btn-blue" data-sign="1">签收（演示）</button>' : s.status === "done" ? '<span class="tag ok">已完成</span>' : '<span class="tag">排队</span>'}</div>
          </li>`).join("")}
      </ul>
      <article class="card">
        <h3>场景改编</h3>
        <p>相邻可改编；跨域拒绝。没有换皮继续。</p>
        <div class="adapt-row">
          ${Object.entries(DATA.adapt).map(([k, v]) => `<button class="choice ${adaptKey === k ? "on" : ""} ${v.allow ? "" : "warn"}" data-adapt="${k}">${v.label}</button>`).join("")}
        </div>
        <p class="${a.allow ? "" : "featured"}">${a.body}</p>
        ${a.allow ? `<div class="actions"><span class="tag ok">可继续交付</span></div>` : `<div class="actions"><button class="btn-line" data-go="people">回找人</button></div>`}
      </article>
    </div>`;
}

function viewInbox() {
  const groups = {
    link: DATA.inbox.filter((i) => i.col === "link"),
    claim: DATA.inbox.filter((i) => i.col === "claim" || i.col === "open"),
    reject: DATA.inbox.filter((i) => i.col === "reject"),
  };
  const cur = DATA.inbox.find((i) => i.id === inboxId) || DATA.inbox[0];
  const list = [...groups.link, ...groups.claim, ...groups.reject];
  return `
    <h1 class="page">收件箱</h1>
    <p class="sub">对标 InboxHub：顶部三计数 + 列表 + 详情。认证不等于改名次。</p>
    <div class="hub-tiles">
      <div class="hub-tile"><span>建联 Sent</span><b>${groups.link.length}</b></div>
      <div class="hub-tile"><span>认领 Inbox</span><b>${groups.claim.length}</b></div>
      <div class="hub-tile"><span>驳回</span><b>${groups.reject.length}</b></div>
    </div>
    <div class="hub-split">
      <div class="hub-list">
        ${list.map((i) => `<button class="q-item ${i.id === cur.id ? "active" : ""}" data-inbox="${i.id}"><b>${i.title}</b><div class="muted">${i.who}</div></button>`).join("")}
      </div>
      <div class="hub-detail">
        <p><span class="tag ${cur.col === "reject" ? "bad" : cur.col === "link" ? "ok" : ""}">${cur.col === "reject" ? "已驳回" : cur.col === "link" ? "建联" : "认领"}</span></p>
        <h3 style="margin:10px 0 8px">${cur.title}</h3>
        <p class="muted">${cur.who}</p>
        <p style="margin-top:12px">${cur.body}</p>
        ${cur.col === "reject" ? '<p class="featured" style="margin-top:14px">拒绝理由：名次不可买。付费只买曝光位。</p>' : ""}
      </div>
    </div>`;
}

function viewSupply(kind) {
  if (kind === "people") {
    return `<h1 class="page">供给库存 · 人</h1><p class="sub">库存视图。找人是需求入口；这里是五馆供给。</p>
      <table class="data"><thead><tr><th>名称</th><th>身份</th><th>说明</th></tr></thead>
      <tbody>${DATA.people.map((p) => `<tr><td>${p.name}</td><td>${typeLabel(p.type)}</td><td>${p.why}</td></tr>`).join("")}</tbody></table>`;
  }
  if (kind === "brands") {
    return `<h1 class="page">供给库存 · 品牌</h1>
      <table class="data"><thead><tr><th>#</th><th>品牌</th><th>类型</th><th>带</th><th>切口</th></tr></thead>
      <tbody>${DATA.brands.map((b, i) => `<tr><td>${i + 1}</td><td>${b.name}</td><td>${b.type}</td><td><span class="band ${b.band}">${b.band}</span></td><td>${b.partner}</td></tr>`).join("")}</tbody></table>`;
  }
  if (kind === "products") {
    const list = DATA.products.filter((p) => productCat === "all" || p.category === productCat);
    return `<h1 class="page">供给库存 · 产品</h1>
      <div class="filters">
        <select id="pcat">
          <option value="all">全部品类</option>
          <option value="编程助手" ${productCat === "编程助手" ? "selected" : ""}>编程助手</option>
          <option value="搜索与问答" ${productCat === "搜索与问答" ? "selected" : ""}>搜索与问答</option>
        </select>
      </div>
      <table class="data"><thead><tr><th>产品</th><th>品牌</th><th>品类</th><th>适配</th></tr></thead>
      <tbody>${list.map((p) => `<tr><td><button class="linkish" data-go="product/${p.id}">${p.name}</button></td><td>${p.brand}</td><td>${p.category}</td><td>${fitTag(p.fit)}</td></tr>`).join("") || `<tr><td colspan="4" class="empty">该品类无供给，不充数。</td></tr>`}</tbody></table>`;
  }
  if (kind === "tools") {
    return `<h1 class="page">供给库存 · 工具</h1>
      <table class="data"><thead><tr><th>工具</th><th>步骤</th></tr></thead>
      <tbody>${DATA.tools.map((t) => `<tr><td>${t.name}</td><td>${t.steps}</td></tr>`).join("")}</tbody></table>`;
  }
  return `<h1 class="page">供给库存 · 资产</h1>
    <table class="data"><thead><tr><th>类型</th><th>名称</th></tr></thead>
    <tbody>${DATA.assets.map((a) => `<tr><td><span class="tag">${a.kind}</span></td><td>${a.name}</td></tr>`).join("")}</tbody></table>`;
}

function viewPerson(id) {
  const p = allPeople().find((x) => x.id === id) || DATA.people[0];
  return `<h1 class="page">${p.name}</h1>
    <p class="sub">${p.role} · ${p.scene}</p>
    <p><span class="tag ${p.type === "human" ? "ok" : "warn"}">${typeLabel(p.type)}</span> ${fitTag(p.fit)}</p>
    <p style="margin-top:12px">${p.why}</p>
    ${p.type === "ai-man" ? '<p class="featured" style="margin-top:12px">数字专才，不进入真人达人榜。</p>' : ""}
    <div class="actions"><button class="btn-blue" data-sl="${p.id}">加入短名单</button></div>`;
}

function viewBrand(id) {
  const b = DATA.brands.find((x) => x.id === id) || DATA.brands[0];
  return `<h1 class="page">${b.name}</h1>
    <p class="sub">${b.partner}</p>
    <p>${b.note}</p>
    <p style="margin-top:10px">产品：${b.products.join("、")}</p>
    <div class="actions"><button class="btn-blue" data-sl="${b.id}">加入短名单</button></div>`;
}

function viewProduct(id) {
  const p = DATA.products.find((x) => x.id === id) || DATA.products[0];
  return `<h1 class="page">${p.name}</h1>
    <p class="sub">${p.desc}</p>
    <p>品牌 <button class="linkish" data-go="brand/${p.brandId}">${p.brand}</button> · ${fitTag(p.fit)}</p>`;
}

function viewMethod() {
  return `
    <h1 class="page">方法</h1>
    <p class="sub">评估窗口公开。付费曝光不得写入名次快照。</p>
    <div class="grid-2">
      <article class="card"><h3>影响力</h3><p>90 天。独立引用 0.4 · 公开采用 0.3 · 场景相关 0.3。排除付费曝光与自报 GMV。</p></article>
      <article class="card"><h3>专业贡献</h3><p>180 天。标准库引用 0.4 · 可复核产物 0.35 · 场景适配 0.25。</p></article>
    </div>
    <p class="featured" style="margin-top:14px">广告目录 data/plaza/ads/ 不写入 RankingSnapshot。</p>`;
}

function viewPricing() {
  return `
    <h1 class="page">套餐</h1>
    <p class="sub">三档两数字：建联额度 × 交付席位。名次不在价目表里。</p>
    <div class="price-grid">
      <article class="card price"><h3>访客</h3><div class="num">¥0</div><p>浏览无限 · 建联 0</p><ul><li>找人 / 找企业只读</li><li>方法公开</li></ul></article>
      <article class="card price"><h3>需求方</h3><div class="num">年费</div><p>建联额度 · 短名单导出</p><ul><li>评估与荐号包</li><li>合作项目</li><li>精选须标注，不进分数</li></ul></article>
      <article class="card price"><h3>交付</h3><div class="num">按席位</div><p>并发数字专才 × 场景包</p><ul><li>人机门签收</li><li>低适配拒绝硬上</li></ul>
        <button class="btn-blue" data-go="campaigns">看合作项目</button></article>
    </div>`;
}

function bindFilters() {
  $("pf-scene")?.addEventListener("change", (e) => { pf.scene = e.target.value; render(); });
  $("pf-type")?.addEventListener("change", (e) => { pf.type = e.target.value; render(); });
  $("of-scene")?.addEventListener("change", (e) => { of.scene = e.target.value; render(); });
  $("of-type")?.addEventListener("change", (e) => { of.type = e.target.value; render(); });
  $("pcat")?.addEventListener("change", (e) => { productCat = e.target.value; render(); });
}

function render() {
  const { name, id } = parse();
  navActive(name);
  const root = $("view");
  const map = {
    home: viewHome,
    people: viewPeople,
    orgs: viewOrgs,
    eval: viewEval,
    shortlist: viewShortlist,
    campaigns: viewCampaigns,
    deliver: viewDeliver,
    inbox: viewInbox,
    "supply-people": () => viewSupply("people"),
    "supply-brands": () => viewSupply("brands"),
    "supply-products": () => viewSupply("products"),
    "supply-assets": () => viewSupply("assets"),
    "supply-tools": () => viewSupply("tools"),
    method: viewMethod,
    pricing: viewPricing,
    person: () => viewPerson(id),
    brand: () => viewBrand(id),
    product: () => viewProduct(id),
  };
  root.innerHTML = (map[name] || viewHome)();
  bindFilters();
}

document.addEventListener("click", (e) => {
  const g = e.target.closest("[data-go]");
  if (g) { e.preventDefault(); go(g.getAttribute("data-go")); return; }
  const sl = e.target.closest("[data-sl]");
  if (sl) {
    const id = sl.getAttribute("data-sl");
    if (shortlist.has(id)) shortlist.delete(id); else shortlist.add(id);
    render();
    return;
  }
  const ib = e.target.closest("[data-inbox]");
  if (ib) { inboxId = ib.getAttribute("data-inbox"); render(); return; }
  const ad = e.target.closest("[data-adapt]");
  if (ad) { adaptKey = ad.getAttribute("data-adapt"); render(); return; }
  if (e.target.closest("[data-sign]")) {
    e.target.closest("[data-sign]").textContent = "已签收";
  }
});

$("q").addEventListener("input", () => {
  const n = parse().name;
  if (["people", "orgs", "supply-products"].includes(n)) render();
});
window.addEventListener("hashchange", render);
if (!location.hash) location.hash = "#home";
else render();
