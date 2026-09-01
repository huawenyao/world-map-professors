const PEOPLE = [
  {
    id: "psn-tech-sample-ai-engineer",
    kind: "person",
    name: "阿凯",
    legal: "示例·AI增强型软件工程师",
    subtitle: "软件研发实践者",
    type: "human",
    typeLabel: "真人 · 样例",
    scene: "软件研发",
    sceneId: "software",
    fit: "High",
    contrib: "A",
    status: "可建联",
    getLabel: "建联",
    color: "linear-gradient(145deg,#5b7cfa,#3b5bdb)",
    mono: "凯",
    sample: true,
    orgId: "brd-github",
    orgName: "GitHub",
    why: "主场软件研发，能力绑定编程。样例条目，非正式达人排行。",
    bio: "Schema 示意：一类在编码、审查、测试中使用 AI 编程助手的工程师画像。不是对任何真实个人的评价，也不能当作名人榜事实。",
    sources: 2,
    previews: [
      { t: "编码", d: "把助手嵌进仓库工作流", bg: "linear-gradient(160deg,#1d1d1f,#5b7cfa)" },
      { t: "审查", d: "关键节点仍由人签", bg: "linear-gradient(160deg,#0b3d2e,#34c759)" },
      { t: "坐标", d: "行业 · 场景 · 能力", bg: "linear-gradient(160deg,#2c1a4d,#af52de)" },
    ],
  },
  {
    id: "psn-tech-sample-qa",
    kind: "person",
    name: "阿测",
    legal: "示例·测试实践者",
    subtitle: "测试与质量实践者",
    type: "human",
    typeLabel: "真人 · 样例",
    scene: "软件研发",
    sceneId: "software",
    fit: "High",
    contrib: "B",
    status: "可建联",
    getLabel: "建联",
    color: "linear-gradient(145deg,#30d158,#0b8a3e)",
    mono: "测",
    sample: true,
    orgId: "brd-github",
    orgName: "GitHub",
    why: "相邻测试场景可改编。样例条目。",
    bio: "用于撑起「人」货架的第二位真人样例，演示同场景相关推荐，而非扩写粉丝榜。",
    sources: 2,
    previews: [
      { t: "测试", d: "用例生成仍要人判", bg: "linear-gradient(160deg,#0b3d2e,#30d158)" },
      { t: "质量门", d: "合并前不可跳过", bg: "linear-gradient(160deg,#1d1d1f,#86868b)" },
      { t: "适配", d: "软件研发 · High", bg: "linear-gradient(160deg,#00332a,#64d2ff)" },
    ],
  },
  {
    id: "psn-tech-sample-coding-persona",
    kind: "person",
    name: "小仓",
    legal: "示例·仓库编程分身",
    subtitle: "产品内编程人格",
    type: "digital-persona",
    typeLabel: "数字人格 · 非真人",
    scene: "软件研发",
    sceneId: "software",
    fit: "High",
    contrib: "B",
    status: "可调用",
    getLabel: "加入",
    color: "linear-gradient(145deg,#bf5af2,#5e5ce6)",
    mono: "仓",
    sample: true,
    orgId: "brd-anthropic",
    orgName: "Anthropic",
    why: "已披露运营方 Anthropic。不可充当真人达人投放，不进真人示意榜。",
    bio: "数字人格样例。标题区必须可见非自然人标识，并写明运营品牌与模型披露。",
    sources: 2,
    operator: "Anthropic · Claude 类模型（样例披露）",
    previews: [
      { t: "分身", d: "产品内人格，不是网红", bg: "linear-gradient(160deg,#2c1250,#bf5af2)" },
      { t: "披露", d: "运营方 + 模型必须可见", bg: "linear-gradient(160deg,#1d1d1f,#5e5ce6)" },
      { t: "隔离", d: "单独货架，不进达人榜", bg: "linear-gradient(160deg,#3a2a00,#ffd60a)" },
    ],
  },
  {
    id: "aim-tech-sd-feature",
    kind: "person",
    name: "阿码",
    legal: "研发交付 AI Man",
    subtitle: "功能交付数字专才",
    type: "ai-man",
    typeLabel: "数字专才 · 非达人榜",
    scene: "软件研发",
    sceneId: "software",
    fit: "High",
    contrib: "S",
    status: "可调用",
    getLabel: "调用",
    color: "linear-gradient(145deg,#1d1d1f,#434344)",
    mono: "码",
    sample: false,
    orgId: "brd-github",
    orgName: "GitHub",
    why: "绑定功能开发解决方案。审查必须人签。不进入真人达人榜。",
    bio: "软件研发主场的数字专才。按流程执行需求拆解、编码、测试与审查。财富管理等监管场景禁止自动交付。",
    sources: 2,
    event: true,
    previews: [
      { t: "交付", d: "按功能开发流程推进", bg: "linear-gradient(160deg,#111,#0071e3)" },
      { t: "人机门", d: "方案确认 / 代码审查", bg: "linear-gradient(160deg,#3a2a00,#ff9f0a)" },
      { t: "拒单", d: "低适配不换皮继续", bg: "linear-gradient(160deg,#3b0008,#ff375f)" },
    ],
  },
];

const ORGS = [
  {
    id: "brd-github",
    kind: "org",
    name: "GitHub",
    subtitle: "开发者生态合作",
    type: "公司",
    typeLabel: "公司",
    scene: "软件研发",
    sceneId: "software",
    fit: "High",
    contrib: "S",
    status: "可建联",
    getLabel: "合作",
    color: "linear-gradient(145deg,#24292f,#57606a)",
    mono: "GH",
    partner: "基础设施 + Copilot 联合方案",
    why: "产品 GitHub Copilot 锚定本场景。企业合作不是广告位。",
    bio: "软件协作与代码托管平台。广场评估的是场景覆盖与可交付产品，而不是估值叙事。",
    sources: 2,
    products: ["GitHub Copilot"],
    people: ["psn-tech-sample-ai-engineer", "psn-tech-sample-qa", "aim-tech-sd-feature"],
    previews: [
      { t: "Copilot", d: "编程助手，场景适配 High", bg: "linear-gradient(160deg,#0d1117,#2f81f7)" },
      { t: "协作", d: "仓库是本场景的工作现场", bg: "linear-gradient(160deg,#1b1f23,#6e7681)" },
      { t: "生态", d: "可谈联合方案，不买名次", bg: "linear-gradient(160deg,#002d26,#3dd68c)" },
    ],
  },
  {
    id: "brd-anthropic",
    kind: "org",
    name: "Anthropic",
    subtitle: "模型与审查能力",
    type: "实验室",
    typeLabel: "实验室",
    scene: "软件研发",
    sceneId: "software",
    fit: "High",
    contrib: "A",
    status: "可建联",
    getLabel: "合作",
    color: "linear-gradient(145deg,#c4a484,#8a6a4b)",
    mono: "An",
    partner: "长上下文审查与方案讨论",
    why: "Claude 适合仓库级理解。旗下数字人格必须单独披露。",
    bio: "实验室型供给。人货架上的「小仓」由本机构运营，不进真人榜。",
    sources: 2,
    products: ["Claude"],
    people: ["psn-tech-sample-coding-persona"],
    previews: [
      { t: "Claude", d: "审查与长上下文", bg: "linear-gradient(160deg,#3d2b1f,#c4a484)" },
      { t: "人格", d: "产品内分身需强制披露", bg: "linear-gradient(160deg,#2c1250,#bf5af2)" },
      { t: "合作", d: "模型能力，不是投放粉数", bg: "linear-gradient(160deg,#1d1d1f,#86868b)" },
    ],
  },
  {
    id: "brd-openai",
    kind: "org",
    name: "OpenAI",
    subtitle: "通用对话能力",
    type: "实验室",
    typeLabel: "实验室",
    scene: "软件研发",
    sceneId: "software",
    fit: "Medium",
    contrib: "A",
    status: "开放收录",
    getLabel: "合作",
    color: "linear-gradient(145deg,#10a37f,#0d7a5f)",
    mono: "OA",
    partner: "通用对话，本场景不排第一",
    why: "可收录、可谈，但不是软件研发第一供给。",
    bio: "熟，却不是本场景短名单的默认第一名。品类筛选后可能从编程助手货架消失。",
    sources: 2,
    products: ["ChatGPT"],
    people: [],
    previews: [
      { t: "ChatGPT", d: "通用对话 · 适配 Medium", bg: "linear-gradient(160deg,#04402f,#10a37f)" },
      { t: "边界", d: "不因为知名就排第一", bg: "linear-gradient(160deg,#1d1d1f,#86868b)" },
      { t: "收录", d: "开放资料，尚未官方认领", bg: "linear-gradient(160deg,#002c4d,#64d2ff)" },
    ],
  },
];

const STORIES = [
  {
    id: "today-person",
    kicker: "今日人物",
    title: "把实践者放上货架，而不是热搜。",
    body: "阿凯是软件研发场景的样例实践者。点进去看适配、贡献和预览，再决定要不要建联。",
    resourceId: "psn-tech-sample-ai-engineer",
    bg: "linear-gradient(165deg,#0b1b4a 0%,#5b7cfa 55%,#a8c1ff 100%)",
  },
  {
    id: "today-org",
    kicker: "今日企业",
    title: "合作对象是公司，不是一款产品海报。",
    body: "GitHub 作为可合作企业上架。产品 Copilot 是它的交付物，名次仍不可买。",
    resourceId: "brd-github",
    bg: "linear-gradient(165deg,#0d1117 0%,#21262d 40%,#2f81f7 100%)",
  },
  {
    id: "today-rule",
    kicker: "编辑说明",
    title: "数字人格有自己的货架。",
    body: "小仓和阿码可以调用，但不能混进真人示意榜。这是商店规则，不是装饰。",
    resourceId: "psn-tech-sample-coding-persona",
    bg: "linear-gradient(165deg,#2c1250 0%,#5e5ce6 50%,#ffd60a 120%)",
  },
];

const INBOX = [
  { id: "i1", title: "GitHub 企业合作意向", who: "你发出的建联", body: "希望确认 Copilot 企业场景适配与合规摘录。", tag: "建联" },
  { id: "i2", title: "Claude 条目纠错", who: "Anthropic 文档站", body: "请把审查工具挂载写进产品页。", tag: "认领" },
  { id: "i3", title: "要求总榜第一", who: "未知域名", body: "已拒：名次不可买。付费只买曝光位。", tag: "驳回", reject: true },
];

const CAMPS = [
  { id: "camp-dev", name: "软件研发功能交付", res: "阿码", status: "交付中", sent: 4, wait: 1, replies: 2, ok: true },
  { id: "camp-org", name: "开发者生态企业合作", res: "GitHub", status: "建联中", sent: 2, wait: 1, replies: 0, ok: true },
  { id: "camp-wm", name: "财富管理达人合作", res: "—", status: "不可用", sent: 0, wait: 0, replies: 0, ok: false },
];

const shortlist = new Set(["psn-tech-sample-ai-engineer", "brd-github"]);
let q = "";
let noticeId = "i3";
let lastTab = "today";

function $(sel, root = document) { return root.querySelector(sel); }
function all() { return [...PEOPLE, ...ORGS]; }
function byId(id) { return all().find((x) => x.id === id); }
function humans() { return PEOPLE.filter((p) => p.type === "human"); }
function personas() { return PEOPLE.filter((p) => p.type !== "human"); }
function orgs() { return ORGS; }
function labs() { return ORGS.filter((o) => o.type === "实验室"); }

function parse() {
  const raw = (location.hash || "#/today").replace(/^#\/?/, "");
  const [name, id] = raw.split("/");
  return { name: name || "today", id };
}
function go(to) {
  location.hash = to.startsWith("#") ? to : "#/" + to.replace(/^#\//, "");
}
function icon(e, size) {
  return `<div class="icon ${size || ""}" style="background:${e.color}">${e.mono}</div>`;
}
function inLib(id) { return shortlist.has(id); }
function getBtn(e, dark) {
  if (e.sceneId === "wealth") return `<span class="get dead">不可用</span>`;
  const on = inLib(e.id);
  const cls = `${dark ? "get-dark" : "get"}${on ? " in" : ""}`;
  const label = on ? "已加入" : e.getLabel;
  return `<button class="${cls}" data-get="${e.id}">${label}</button>`;
}
function typeBadge(e) {
  if (e.type === "human") return `<span class="badge ok">${e.typeLabel}</span>`;
  if (e.type === "digital-persona" || e.type === "ai-man") return `<span class="badge warn">${e.typeLabel}</span>`;
  return `<span class="badge">${e.typeLabel || e.type}</span>`;
}
function row(e) {
  return `<div class="res-row" data-open="${e.id}">
    ${icon(e)}
    <div>
      <div class="name">${e.name}</div>
      <div class="sub2">${e.subtitle}</div>
    </div>
    <div>${getBtn(e)}</div>
  </div>`;
}
function mini(e) {
  return `<article class="mini-card" data-open="${e.id}">
    ${icon(e)}
    <b>${e.name}</b>
    <div class="muted">${e.subtitle}</div>
    <div>${getBtn(e)}</div>
  </article>`;
}
function shelf(title, items, allLink) {
  if (!items.length) return "";
  return `<section class="shelf">
    <div class="row-between">
      <h2 class="title-lg">${title}</h2>
      ${allLink ? `<button class="link" data-go="${allLink}">查看全部</button>` : ""}
    </div>
    <div class="shelf-scroll">${items.map(mini).join("")}</div>
  </section>`;
}
function chart(items) {
  return `<div class="list-card" style="padding:4px 16px">
    ${items.map((e, i) => `<div class="res-row chart-row" data-open="${e.id}">
      <span class="chart-n">${i + 1}</span>${icon(e)}
      <div><div class="name">${e.name}</div><div class="sub2">${e.subtitle}</div></div>
      <div>${getBtn(e)}</div>
    </div>`).join("")}
  </div>`;
}
function emptyWealth() {
  return `<div class="empty">
    <h3>此分类暂无资源</h3>
    <p>财富管理的个人与企业覆盖不足。<br/>不会用软件研发供给填充，也不能继续自动交付。</p>
  </div>`;
}

function viewToday() {
  return `
    <div class="date">9月1日 星期二</div>
    <h1 class="title-xl">今日</h1>
    ${STORIES.map((s) => {
      const e = byId(s.resourceId);
      return `<article class="story" style="background:${s.bg}" data-go="story/${s.id}">
        <div>
          <div class="eyebrow">${s.kicker}</div>
          <h2>${s.title}</h2>
          <p>${s.body}</p>
        </div>
        <div class="story-foot">
          ${icon(e, "sm")}
          <div class="meta"><b>${e.name}</b><span>${e.subtitle}</span></div>
          <div>${getBtn(e, true)}</div>
        </div>
      </article>`;
    }).join("")}`;
}

function viewStory(id) {
  const s = STORIES.find((x) => x.id === id) || STORIES[0];
  const e = byId(s.resourceId);
  return `
    <button class="back" data-go="today">‹ 今日</button>
    <article class="story" style="background:${s.bg}; min-height:280px">
      <div>
        <div class="eyebrow">${s.kicker}</div>
        <h2>${s.title}</h2>
        <p>${s.body}</p>
      </div>
    </article>
    <div class="block">
      <p>${e.bio}</p>
      <p class="muted" style="margin-top:10px">${e.why}</p>
    </div>
    <div class="list-card" style="padding:0 16px">${row(e)}</div>`;
}

function viewPeople() {
  return `
    <h1 class="title-xl">人</h1>
    <p class="sub">像浏览 App 一样浏览个人。真人、数字人格、数字专才分开放。</p>
    ${shelf("编辑精选", humans(), "charts/people")}
    <section class="shelf">
      <div class="row-between"><h2 class="title-lg">示意榜</h2><span class="muted">样例，非正式排行</span></div>
      <p class="note">只含真人实践者。数字人格与 AI Man 不进此榜。名次不可买。</p>
      ${chart(humans())}
    </section>
    ${shelf("数字人格", PEOPLE.filter((p) => p.type === "digital-persona"))}
    ${shelf("数字专才", PEOPLE.filter((p) => p.type === "ai-man"))}
    <section class="shelf">
      <h2 class="title-lg">浏览场景</h2>
      <div class="cats">
        <button class="cat" style="background:linear-gradient(135deg,#5b7cfa,#0071e3)" data-go="scene/software">软件研发</button>
        <button class="cat" style="background:linear-gradient(135deg,#8e8e93,#1d1d1f)" data-go="scene/wealth">财富管理</button>
      </div>
    </section>`;
}

function viewOrgs() {
  return `
    <h1 class="title-xl">企业</h1>
    <p class="sub">可合作的公司与实验室。点进详情看产品组合，再决定要不要合作。</p>
    ${shelf("值得合作", ORGS, "charts/orgs")}
    <section class="shelf">
      <div class="row-between"><h2 class="title-lg">示意榜</h2><span class="muted">样例，非正式排行</span></div>
      <p class="note">按场景贡献带排列示意，不是可购买的名次。</p>
      ${chart(ORGS)}
    </section>
    ${shelf("实验室", labs())}
    <section class="shelf">
      <h2 class="title-lg">浏览场景</h2>
      <div class="cats">
        <button class="cat" style="background:linear-gradient(135deg,#24292f,#2f81f7)" data-go="scene/software">软件研发</button>
        <button class="cat" style="background:linear-gradient(135deg,#8e8e93,#1d1d1f)" data-go="scene/wealth">财富管理</button>
      </div>
    </section>`;
}

function viewScene(id) {
  const wealth = id === "wealth";
  const title = wealth ? "财富管理" : "软件研发";
  const back = lastTab === "orgs" ? "orgs" : "people";
  const people = wealth ? [] : PEOPLE.filter((p) => p.sceneId === "software");
  const orgs = wealth ? [] : ORGS.filter((o) => o.sceneId === "software");
  return `
    <button class="back" data-go="${lastTab === "orgs" ? "orgs" : "people"}">‹ ${lastTab === "orgs" ? "企业" : "人"}</button>
    <h1 class="title-xl">${title}</h1>
    ${wealth ? emptyWealth() : `
      <p class="sub">此分类下的个人与企业。数字人格仍单独标记。</p>
      <h2 class="title-lg">人</h2>
      <div class="list-card" style="padding:0 16px;margin-bottom:18px">${people.map((e) => row(e)).join("")}</div>
      <h2 class="title-lg">企业</h2>
      <div class="list-card" style="padding:0 16px">${orgs.map((e) => row(e)).join("")}</div>
    `}`;
}

function viewCharts(kind) {
  const people = kind === "orgs";
  return `
    <button class="back" data-go="${people ? "orgs" : "people"}">‹ ${people ? "企业" : "人"}</button>
    <h1 class="title-xl">${people ? "企业" : "人"}排行</h1>
    <p class="note">样例示意，非正式排行。付费不能改名次。${people ? "" : "仅真人。"}</p>
    ${chart(people ? ORGS : humans())}`;
}

function searchPane() {
  const query = q.trim();
  const wealth = /财富|理财|投顾/.test(query);
  const list = all().filter((e) => {
    if (wealth) return false;
    if (!query) return false;
    return `${e.name}${e.legal || ""}${e.subtitle}${e.scene}`.toLowerCase().includes(query.toLowerCase());
  });
  if (!query) {
    return `
      <div class="muted" style="margin-bottom:8px">建议</div>
      <div class="suggest">
        ${["软件研发", "GitHub", "阿凯", "数字人格", "财富管理"].map((w) => `<button class="chip" data-q="${w}">${w}</button>`).join("")}
      </div>
      <div class="muted">热门资源</div>
      <div class="list-card" style="padding:0 16px">${[PEOPLE[0], ORGS[0], PEOPLE[3]].map((e) => row(e)).join("")}</div>`;
  }
  if (wealth) return emptyWealth();
  return `<div class="list-card" style="padding:0 16px">${list.map((e) => row(e)).join("") || `<div class="empty">无匹配。不拿其他场景供给充数。</div>`}</div>`;
}

function viewSearch() {
  return `
    <h1 class="title-xl">搜索</h1>
    <input class="search-box" id="qbox" placeholder="搜索人、企业或场景" value="${q.replace(/"/g, "&quot;")}" />
    <div id="search-pane">${searchPane()}</div>`;
}

function viewResource(id) {
  const e = byId(id);
  if (!e) return `<p>未找到资源。</p>`;
  const related = all().filter((x) => x.sceneId === e.sceneId && x.id !== e.id).slice(0, 4);
  const more = e.kind === "org"
    ? PEOPLE.filter((p) => p.orgId === e.id)
    : e.orgId ? [byId(e.orgId)].filter(Boolean) : [];
  return `
    <button class="back" data-go="${e.kind === "org" ? "orgs" : "people"}">‹ ${e.kind === "org" ? "企业" : "人"}</button>
    <div class="hero-head">
      ${icon(e, "lg")}
      <div>
        <h1>${e.name}</h1>
        <div class="sub" style="margin:0 0 8px">${e.subtitle}</div>
        ${typeBadge(e)}
        ${e.sample ? `<span class="badge">样例</span>` : ""}
        <div class="actions">${getBtn(e)}${e.event ? `<a class="btn-blue" href="native/index.html">打开交付</a>` : ""}</div>
      </div>
    </div>
    <div class="previews">${e.previews.map((p) => `<div class="shot" style="background:${p.bg}"><b>${p.t}</b><span>${p.d}</span></div>`).join("")}</div>
    <div class="block">
      <h3>${e.legal || e.name}</h3>
      <p>${e.bio}</p>
      <p class="muted" style="margin-top:10px">${e.why}</p>
    </div>
    <div class="block">
      <h3>评估</h3>
      <p class="muted">对标详情页的 Ratings，但尺子是场景坐标系，不是粉丝星级。</p>
      <div class="fit">
        <div><span>场景适配</span><b>${e.fit}</b></div>
        <div><span>专业贡献</span><b>${e.contrib}</b></div>
        <div><span>状态</span><b style="font-size:16px">${e.status}</b></div>
      </div>
    </div>
    <div class="block">
      <h3>信息</h3>
      <table class="info">
        <tr><th>提供方</th><td>${e.orgName || e.name}</td></tr>
        <tr><th>类别</th><td>${e.scene} · ${e.kind === "org" ? "企业" : "个人"}</td></tr>
        <tr><th>身份</th><td>${e.typeLabel}</td></tr>
        ${e.operator ? `<tr><th>运营披露</th><td>${e.operator}</td></tr>` : ""}
        ${e.products ? `<tr><th>产品</th><td>${e.products.join("、")}</td></tr>` : ""}
        <tr><th>来源</th><td>${e.sources} 条公开来源</td></tr>
        <tr><th>名次</th><td>不可买</td></tr>
        <tr><th>兼容</th><td>${e.getLabel} 后进入资料库</td></tr>
      </table>
    </div>
    ${more.length ? `<section class="shelf"><h2 class="title-lg">${e.kind === "org" ? "More by this enterprise" : "所属企业"}</h2>
      <div class="list-card" style="padding:0 16px">${more.map((x) => row(x)).join("")}</div></section>` : ""}
    <section class="shelf">
      <h2 class="title-lg">You Might Also Like</h2>
      <div class="shelf-scroll">${related.map(mini).join("")}</div>
    </section>`;
}

function viewLibrary() {
  const items = all().filter((e) => shortlist.has(e.id));
  const cur = INBOX.find((i) => i.id === noticeId) || INBOX[0];
  return `
    <h1 class="title-xl">资料库</h1>
    <p class="sub">已加入的人与企业，相当于 App Store 的已下载。进行中的合作是更新，不是首页。</p>
    <h2 class="title-lg">已加入</h2>
    <div class="list-card" style="padding:0 16px;margin-bottom:22px">
      ${items.length ? items.map((e) => `<button class="lib-item" data-open="${e.id}">${icon(e)}<div><b>${e.name}</b><div class="muted">${e.subtitle}</div></div></button>`).join("") : `<div class="empty">还没有 Get 任何资源。</div>`}
    </div>
    <h2 class="title-lg">进行中</h2>
    <div class="list-card" style="padding:12px 16px;margin-bottom:22px">
      ${CAMPS.map((c) => `<div style="padding:10px 0;border-bottom:1px solid var(--line)">
        <div class="row-between"><b>${c.name}</b><span class="badge ${c.ok ? "ok" : "bad"}">${c.status}</span></div>
        <div class="muted">供给 ${c.res} · 建联 ${c.sent} · 待处理 ${c.wait} · 回复 ${c.replies}</div>
        ${c.ok ? "" : `<div class="muted">已拒绝自动交付，无换皮继续。</div>`}
      </div>`).join("")}
    </div>
    <h2 class="title-lg">通知</h2>
    <div class="list-card" style="padding:4px 16px 16px;margin-bottom:22px">
      ${INBOX.map((i) => `<button class="notice" data-notice="${i.id}">
        ${icon({ color: i.reject ? "linear-gradient(#de071c,#ff6961)" : "linear-gradient(#0071e3,#64d2ff)", mono: i.tag[0] }, "sm")}
        <div><b>${i.title}</b><div class="muted">${i.who}</div></div>
      </button>`).join("")}
      <div class="block" style="margin:8px 0 0">
        <span class="badge ${cur.reject ? "bad" : "ok"}">${cur.tag}</span>
        <h3 style="margin-top:8px">${cur.title}</h3>
        <p>${cur.body}</p>
      </div>
    </div>
    <h2 class="title-lg">账户</h2>
    <div class="block">
      <p>浏览无限 · 建联额度 12 · 交付席位 1</p>
      <p class="muted" style="margin-top:8px">名次不在价目表。广告只出现在精选位，不进 RankingSnapshot。</p>
    </div>`;
}

const TABS = { today: "today", people: "people", orgs: "orgs", search: "search", library: "library", story: "today", scene: "people", charts: "people", resource: "people" };

function nav(name, id) {
  let tab = name;
  if (name === "story") tab = "today";
  else if (name === "charts") tab = id === "orgs" ? "orgs" : "people";
  else if (name === "scene") tab = "people";
  else if (name === "resource") {
    const e = byId(id);
    tab = e && e.kind === "org" ? "orgs" : "people";
  }
  document.querySelectorAll(".tab").forEach((b) => {
    b.classList.toggle("on", b.getAttribute("data-go") === tab);
  });
}

function render() {
  const { name, id } = parse();
  nav(name, id);
  const root = document.getElementById("view");
  const map = {
    today: viewToday,
    people: viewPeople,
    orgs: viewOrgs,
    search: viewSearch,
    library: viewLibrary,
    story: () => viewStory(id),
    scene: () => viewScene(id),
    charts: () => viewCharts(id),
    resource: () => viewResource(id),
  };
  root.innerHTML = (map[name] || viewToday)();
  const box = document.getElementById("qbox");
  if (box) {
    box.addEventListener("input", (e) => {
      q = e.target.value;
      const pane = document.getElementById("search-pane");
      if (pane) pane.innerHTML = searchPane();
    });
  }
}

document.addEventListener("click", (e) => {
  const get = e.target.closest("[data-get]");
  if (get) {
    e.preventDefault();
    e.stopPropagation();
    const id = get.getAttribute("data-get");
    if (shortlist.has(id)) shortlist.delete(id); else shortlist.add(id);
    render();
    return;
  }
  const open = e.target.closest("[data-open]");
  if (open) { e.preventDefault(); go("resource/" + open.getAttribute("data-open")); return; }
  const g = e.target.closest("[data-go]");
  if (g) {
    e.preventDefault();
    const to = g.getAttribute("data-go");
    if (["today", "people", "orgs", "search", "library"].includes(to)) lastTab = to;
    go(to);
    return;
  }
  const qq = e.target.closest("[data-q]");
  if (qq) {
    q = qq.getAttribute("data-q");
    lastTab = "search";
    if (parse().name === "search") render();
    else go("search");
    return;
  }
  const n = e.target.closest("[data-notice]");
  if (n) { noticeId = n.getAttribute("data-notice"); render(); }
});

window.addEventListener("hashchange", render);
if (!location.hash) location.hash = "#/today";
else render();
