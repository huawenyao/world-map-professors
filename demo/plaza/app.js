const DATA = {
  scene: {
    id: "scn-tech-software-dev",
    name: "软件研发",
    industry: "科技互联网",
    desc: "从想清楚要做什么，写到能上线。这条街上有人、有牌子，也有愿意把活做完的伙伴。",
  },
  scenarios: [
    {
      id: "scn-tech-software-dev",
      name: "软件研发",
      industry: "写代码这条街",
      blurb: "需求、编码、测试、审查。阿码就住在这儿。",
      coverage: "home",
      hue: 14,
    },
    {
      id: "scn-tech-qa",
      name: "测试和质量",
      industry: "隔壁那条街",
      blurb: "和写代码是邻居。阿码换把工具就能过来帮一把。",
      coverage: "near",
      hue: 32,
    },
    {
      id: "scn-fin-wealth-mgmt",
      name: "财富管理",
      industry: "管钱那条街",
      blurb: "给人管钱、做配置。我们还没走进去，也不拿写代码的人充数。",
      coverage: "gap",
      hue: 200,
    },
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
      user: "写代码的人",
      pricing: "按月请",
      hue: 210,
      tools: ["tool-code-generator"],
      desc: "就坐在你光标旁边，帮你把重复的那截写完。",
      vibe: "像一个不说话的搭档",
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
      user: "写代码的人，也有公司在用",
      pricing: "能免费聊，用多用付",
      hue: 28,
      tools: ["tool-code-generator", "tool-code-reviewer"],
      desc: "适合先把整份仓库读完，再慢慢跟你讨论。",
      vibe: "话少、记得住上下文",
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
      user: "谁都能聊",
      pricing: "能免费聊，想多聊再请",
      hue: 150,
      tools: ["tool-code-generator"],
      desc: "什么都能聊。写代码这条街上，TA 不该排第一。",
      vibe: "熟，但不专",
      sources: 2,
    },
  ],
  brands: [
    { id: "brd-github", name: "GitHub", type: "公司", band: "S", rank: 1, products: ["GitHub Copilot"], note: "程序员每天进进出出的那扇门。", hue: 210 },
    { id: "brd-anthropic", name: "Anthropic", type: "实验室", band: "A", rank: 2, products: ["Claude"], note: "把 Claude 带到这条街的人。", hue: 28 },
    { id: "brd-openai", name: "OpenAI", type: "实验室", band: "A", rank: 3, products: ["ChatGPT"], note: "几乎人人都聊过的那家。", hue: 150 },
  ],
  people: [
    {
      id: "psn-tech-sample-ai-engineer",
      name: "阿凯",
      type: "human",
      sample: true,
      hue: 18,
      headline: "白天写需求，晚上把收尾交给伙伴。",
      quote: "我不是来刷榜的。我只是想早点把这期做完。",
    },
    {
      id: "psn-tech-sample-coding-persona",
      name: "小仓",
      type: "digital-persona",
      sample: true,
      hue: 200,
      headline: "仓库里的编程分身。不是人，会事先说清楚。",
      quote: "我住在仓库里。你 @ 我的时候，我才出现。",
    },
  ],
  tools: [
    { id: "tool-code-generator", name: "代码生成器", note: "阿码写第一稿时伸出的那只手。", steps: "起草、改一改" },
    { id: "tool-code-reviewer", name: "看代码的镜子", note: "合并前，TA 先帮你盯一眼。", steps: "审查" },
    { id: "tool-test-generator", name: "补测试的小工", note: "你睡了，TA 还在给边界情况写例子。", steps: "补测试" },
  ],
  assets: [
    { id: "scn-tech-software-dev", kind: "这条街", name: "软件研发", note: "人、牌子、产品都挂在这儿，才算走进来了。" },
    { id: "wf-tech-sd-feature-dev", kind: "怎么做完", name: "把一个功能做完", note: "从听懂你要什么，到你点头合并。" },
    { id: "agt-tech-sd-coding", kind: "谁来做", name: "编程伙伴", note: "阿码的底子。不是真人，也不上名人榜。" },
    { id: "cap-tech-001", kind: "手艺", name: "写代码", note: "这条街吃饭的本事。" },
  ],
  claims: [
    { id: "c1", status: "pending", entity: "GitHub Copilot", who: "GitHub 的人来认领（示意）", ask: "这是我们的产品。请把企业里怎么用写清楚。", tone: "认领" },
    { id: "c2", status: "pending", entity: "Claude", who: "Anthropic 文档站", ask: "审查这只手，请写进产品介绍里。", tone: "纠正" },
    { id: "c3", status: "claimed", entity: "OpenAI", who: "开放收录", ask: "还没人认领，我们只写公开能查到的。", tone: "开放" },
    { id: "c4", status: "rejected", entity: "想买第一名的来信", who: "一个陌生域名", ask: "给我们总榜第一。", tone: "被退回" },
  ],
  aiMan: {
    id: "aim-tech-sd-feature",
    name: "阿码",
    home: "scn-tech-software-dev",
    homeName: "软件研发",
    hue: 14,
    quote: "审查这关，还得你点头。我不会替你按下合并。",
    desc: "我在写代码这条街。功能我能写完，测试我能补上。你要是让我去给人理财，我会拒绝——那不是我的活。",
    does: ["听懂你要什么", "把功能写完", "补上测试", "审查前提醒你"],
    wont: ["替你按合并", "假装会理财", "不打招呼就上线"],
  },
  solution: {
    id: "sol-tech-sd-feature-delivery",
    name: "把这个功能做完",
    promise: "你买的不是一个人格，是「把这期做完」这件事。",
    outcome: "一串你能合并的改动，测试和审查都在旁边。",
    checkpoints: ["先听懂你要什么", "方案你过一眼", "审查你点头"],
  },
  runSteps: [
    { id: "step-01", name: "听懂你要什么", status: "done", gate: true, said: "需求我拆好了，你过一眼。" },
    { id: "step-02", name: "方案你过一眼", status: "done", gate: true, said: "三步走，不动支付那块。" },
    { id: "step-03", name: "把代码写上", status: "done", gate: false, said: "第一稿在。重复的那截我代劳了。" },
    { id: "step-04", name: "补上测试", status: "done", gate: false, said: "边界情况我也写了例子。" },
    { id: "step-05", name: "审查，等你点头", status: "gate", gate: true, said: "意见贴在旁边。合并这关，只能你来。" },
    { id: "step-06", name: "合并、上线", status: "queued", gate: false, said: "你点头之后，我再动。" },
  ],
  thread: [
    { who: "ai", text: "需求我听懂了：把登录态带到新接口。拆成三步，你过一眼？" },
    { who: "you", text: "行。注意别动支付那块。" },
    { who: "ai", text: "代码写完了，测试也补上。审查意见在旁边。合并这关，还得你点头。" },
  ],
  adaptPlans: {
    home: {
      label: "今晚就写代码",
      scene: "软件研发",
      fit: "high",
      action: "我熟，直接干",
      detail: "需求、编码、测试、审查，这条路我走过。三处仍要你点头。",
      allow: true,
    },
    qa: {
      label: "顺便帮你测一测",
      scene: "测试和质量",
      fit: "high",
      action: "换一把手上的工具就行",
      detail: "和写代码是邻居。我会把测试拿在最前面，关键处还是会喊你。",
      allow: true,
    },
    wealth: {
      label: "去给人管钱",
      scene: "财富管理",
      fit: "low",
      action: "这活我不能接",
      detail: "我没有风险评估这门手艺，也不该对别人的钱做主。请找投顾街上的伙伴——我不会假装我行。",
      allow: false,
    },
  },
  plans: [
    {
      id: "free",
      name: "先逛逛",
      price: "免费",
      for: "进来看看街上有谁。",
      items: ["遇见人和伙伴", "货架和工具随便看", "名次不在价目表上"],
    },
    {
      id: "pro",
      name: "认领自己",
      price: "年费",
      for: "这牌子、这产品是我的。",
      items: ["更正介绍", "挂上「这是我」", "推荐位另标，不改名次"],
    },
    {
      id: "seat",
      name: "请一位伙伴",
      price: "按席位",
      for: "让阿码这类人把活做完。",
      items: ["请几位，交几桩活", "关键处仍要你点头", "不擅长的领域会拒绝"],
    },
  ],
};

const HELLO = {
  home: "今晚写代码的话，街上有人等你。",
  finder: "先说你卡在哪条街。",
  solutions: "你买的是把事做完，不是买一个人。",
  aiman: "阿码还在。审查这关，只能你来。",
  run: "TA 起草，你拍板。",
  people: "先见到人。数字人格会自己说：我不是真人。",
  brands: "招牌不是货架。",
  products: "今晚你手头会用到的东西。",
  assets: "这条街吃饭的手艺。",
  tools: "阿码手里实际伸出的那些。",
  compare: "放在一起看，别被广告带跑。",
  claims: "认领自己，或拿出证据说话。",
  method: "我们怎么排，说给你听。",
  pricing: "花钱请的是座位和活，不是名次。",
  scene: "写代码这条街，今晚有人在。",
  product: "先看它到底帮你做哪一段。",
  brand: "背后是谁在认真做。",
  person: "先听 TA 自己说。",
  tool: "干活的家伙，不是明星。",
};

const $ = (id) => document.getElementById(id);
let compareSet = new Set(["prd-github-copilot", "prd-anthropic-claude"]);
let claimFocus = "c1";
let finder = { q: "" };
let productCat = "all";
let adaptKey = "home";
let mergeNote = "";

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
      solutions: "solutions",
      aiman: "aiman",
      run: "solutions",
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

function avatar(name, hue, size) {
  const ch = String(name || "?").slice(0, 1);
  return `<span class="avatar ${size || ""}" style="--h:${hue || 14}">${ch}</span>`;
}

function greet(title, sub, who, hue) {
  return `
    <div class="meet">
      ${avatar(who || title, hue, "lg")}
      <div>
        <h1 class="page">${title}</h1>
        <p class="sub">${sub}</p>
      </div>
    </div>`;
}

function q() {
  return (finder.q || $("q")?.value || "").trim();
}

function matchQ(parts) {
  const needle = q();
  if (!needle) return true;
  return parts.join(" ").includes(needle);
}

function coverageChip(c) {
  if (c === "home") return `<span class="tag ok">我们熟</span>`;
  if (c === "near") return `<span class="tag gold">隔壁也能帮</span>`;
  return `<span class="tag warn">还没走进去</span>`;
}

function productCard(p, extra = "") {
  return `
    <article class="person-card product-card">
      ${avatar(p.name, p.hue)}
      <div>
        <div class="who-row">
          <h3><button class="linkish" data-go="product/${p.id}">${p.name}</button></h3>
          <span class="tag">${p.category}</span>
        </div>
        <p class="lead">${p.vibe}</p>
        <p>${p.desc}</p>
        ${extra}
      </div>
    </article>`;
}

function viewHome() {
  const a = DATA.aiMan;
  const s = DATA.scene;
  return `
    ${greet("嘿，今天想把哪件事做完？", "阿码还在等你点头。审查这关，只能你来。", a.name, a.hue)}
    <div class="grid-2">
      <article class="card talk">
        <div class="who-row">${avatar(a.name, a.hue, "sm")}<strong>${a.name}</strong><span class="tag">你的编程伙伴</span></div>
        <p class="quote">${a.quote}</p>
        <div class="actions">
          <button class="btn-blue" data-go="run/${DATA.solution.id}">去看看 TA 写到哪了</button>
          <button class="btn-line" data-go="aiman">跟阿码打个招呼</button>
        </div>
      </article>
      <article class="card">
        <h3>街上最近在聊</h3>
        <div class="feed" style="margin-top:12px">
          ${DATA.people.map((p) => `
            <div class="who-row">
              ${avatar(p.name, p.hue, "sm")}
              <div>
                <strong>${p.name}</strong>
                <span class="tag ${p.type === "human" ? "ok" : "warn"}">${p.type === "human" ? "真人" : "数字人格"}</span>
                <p>${p.quote}</p>
              </div>
            </div>`).join("")}
        </div>
        <div class="actions">
          <button class="btn-line" data-go="people">去街上走走</button>
          <button class="btn-line" data-go="scene/${s.id}">走进${s.name}</button>
        </div>
      </article>
    </div>`;
}

function viewFinder() {
  const list = DATA.scenarios.filter((s) => matchQ([s.name, s.industry, s.blurb]));
  return `
    ${greet("你眼下卡在哪一步？", "先说清场景。场景对了，人、产品和伙伴才对得上。", "场", 200)}
    <div class="stack">
      ${list.map((s) => `
        <article class="person-card">
          ${avatar(s.name, s.hue)}
          <div class="grow">
            <div class="who-row"><h3>${s.name}</h3>${coverageChip(s.coverage)}</div>
            <p class="lead">${s.industry}</p>
            <p>${s.blurb}</p>
            <div class="actions">
              ${s.coverage === "gap"
                ? `<span class="soft">空着就空着。我们不拿写代码的人来充管钱的活。</span>`
                : `<button class="btn-blue" data-go="${s.coverage === "home" ? "scene/" + s.id : "aiman"}">${s.coverage === "home" ? "就是这个" : "问问阿码能不能帮"}</button>`}
            </div>
          </div>
        </article>`).join("") || `<div class="empty">没找到这条街。我们不编一条给你。</div>`}
    </div>`;
}

function viewScene() {
  const s = DATA.scene;
  return `
    ${greet(s.name, s.desc, "街", 14)}
    <div class="grid-2">
      <div>
        <h3 class="block-title">今晚用什么</h3>
        ${DATA.products.map((p) => productCard(p, `<p class="soft">${p.fit === "high" ? "这条街很合适。" : "熟，但不是专为这里。"}</p>`)).join("")}
        <div class="actions"><button class="btn-line" data-go="compare">放在一起比一比</button></div>
      </div>
      <div>
        <article class="card talk">
          <div class="who-row">${avatar("阿", 14, "sm")}<strong>把这个功能做完</strong></div>
          <p class="quote">${DATA.solution.promise}</p>
          <p>${DATA.solution.outcome}</p>
          <div class="actions">
            <button class="btn-blue" data-go="run/${DATA.solution.id}">让阿码开工</button>
            <button class="btn-line" data-go="aiman">先认识阿码</button>
          </div>
        </article>
        <article class="card" style="margin-top:14px">
          <h3>这条街的手艺</h3>
          ${DATA.assets.map((a) => `<p><span class="tag">${a.kind}</span> ${a.name}</p>`).join("")}
        </article>
      </div>
    </div>`;
}

function viewSolutions() {
  const s = DATA.solution;
  const m = DATA.aiMan;
  return `
    ${greet("把这件事交给谁？", s.promise, "活", 14)}
    <article class="card talk featured-soft">
      <div class="who-row">${avatar(m.name, m.hue)}<div><h3>${s.name}</h3><p class="soft">阿码来做日常；合并之前，一定问你。</p></div></div>
      <p class="lead" style="margin-top:12px">${s.outcome}</p>
      <p>三道门还是你来开：${s.checkpoints.join(" · ")}</p>
      <div class="actions">
        <button class="btn-blue" data-go="aiman">先认识阿码</button>
        <button class="btn-line" data-go="run/${s.id}">好，让 TA 开工</button>
      </div>
    </article>
    <article class="card" style="margin-top:14px">
      <div class="who-row">${avatar("钱", 200, "sm")}<h3>给人管钱？这条还空着</h3></div>
      <p>写代码的伙伴不能硬上。等投顾街上有人住进来，再把活交出去。</p>
      <p class="empty" style="padding:12px 0 0">没有「勉强继续」的按钮。</p>
    </article>`;
}

function viewAiMan() {
  const m = DATA.aiMan;
  const plan = DATA.adaptPlans[adaptKey];
  return `
    <div class="meet">
      ${avatar(m.name, m.hue, "lg")}
      <div>
        <h1 class="page">嗨，我是${m.name}</h1>
        <p class="sub">住在「${m.homeName}」这条街 · 不是真人，不上名人榜</p>
      </div>
    </div>
    <div class="grid-2">
      <article class="card talk">
        <p class="quote">${m.quote}</p>
        <p><strong>我能帮你</strong>　${m.does.join("、")}</p>
        <p><strong>请你自己来</strong>　${m.wont.join("、")}</p>
        <p class="soft" style="margin-top:10px">${m.desc}</p>
      </article>
      <article class="card">
        <h3>换个活试试？</h3>
        <p>相邻的活我可以改改肩上的担子；太远的，我会直说不接。</p>
        <div class="choice">
          ${Object.entries(DATA.adaptPlans)
            .map(
              ([k, p]) => `<button class="choice-btn ${adaptKey === k ? "on" : ""} ${p.allow ? "" : "warn"}" data-adapt="${k}">${p.label}</button>`
            )
            .join("")}
        </div>
        <p class="quote ${plan.allow ? "" : "refuse"}">${plan.detail}</p>
        <p><strong>${plan.action}</strong> · ${plan.scene}</p>
        <div class="actions">
          ${
            plan.allow
              ? `<button class="btn-blue" data-go="run/${DATA.solution.id}">${adaptKey === "qa" ? "好，按测试的节奏来" : "那就按这个来"}</button>`
              : `<p class="soft">没有「勉强继续」的按钮。换一条更近的街，或回去找场景。</p>
                 <button class="btn-line" data-go="finder">回去找场景</button>`
          }
        </div>
      </article>
    </div>`;
}

function viewRun() {
  const st = { done: "done", gate: "gate", queued: "", run: "run" };
  return `
    ${greet("阿码正在写", "TA 起草，你拍板。没点头之前，这活不算完。", "阿", 14)}
    <div class="detail-grid">
      <div class="thread">
        ${DATA.thread
          .map(
            (t) => `
          <div class="msg ${t.who}">
            ${t.who === "ai" ? avatar("阿", 14, "sm") : avatar("你", 200, "sm")}
            <p class="quote">${t.text}</p>
          </div>`
          )
          .join("")}
        <article class="card talk">
          <p>合并这扇门还开着。点头或驳回，都是你的。</p>
          <div class="actions">
            <button class="btn-blue" type="button" data-merge="ok">点头，合并吧</button>
            <button class="btn-line" type="button" data-merge="no">先驳回，我有话要说</button>
          </div>
          ${mergeNote ? `<p class="quote" style="margin-top:12px">${mergeNote}</p>` : ""}
        </article>
      </div>
      <div>
        <h3 class="block-title">做到哪了</h3>
        <ul class="timeline">
          ${DATA.runSteps
            .map(
              (step) => `<li>
                <span class="dot ${st[step.status] || ""}"></span>
                <b>${step.name}</b>
                <div class="soft">${step.said}</div>
                <div>${
                  step.status === "gate"
                    ? '<span class="tag gold">等你点头</span>'
                    : step.status === "done"
                      ? '<span class="tag ok">做过了</span>'
                      : '<span class="tag">还没到</span>'
                }</div>
              </li>`
            )
            .join("")}
        </ul>
        <article class="card" style="margin-top:8px">
          <p>手头用的是 <button class="linkish" data-go="product/prd-github-copilot">Copilot</button> 和
          <button class="linkish" data-go="product/prd-anthropic-claude">Claude</button>。</p>
          <p style="margin-top:10px"><button class="btn-line" data-go="aiman">活不对？去跟阿码说</button></p>
        </article>
      </div>
    </div>`;
}

function viewList(kind) {
  if (kind === "products") {
    const list = DATA.products.filter((p) => {
      if (productCat !== "all" && p.category !== productCat) return false;
      return matchQ([p.name, p.brand, p.category, p.desc, p.vibe]);
    });
    return `
      ${greet("今晚用什么", "选对品类，货架才干净。写代码的桌上，不该把什么都能聊的排第一。", "货", 32)}
      <div class="filters">
        <button class="chip-btn ${productCat === "all" ? "on" : ""}" data-cat="all">全部</button>
        <button class="chip-btn ${productCat === "编程助手" ? "on" : ""}" data-cat="编程助手">写代码用的</button>
        <button class="chip-btn ${productCat === "搜索与问答" ? "on" : ""}" data-cat="搜索与问答">随便聊聊的</button>
      </div>
      <div class="grid-2">
        ${list.map((p) => productCard(p, `
          <div class="actions">
            <label class="soft"><input type="checkbox" data-cmp="${p.id}" ${compareSet.has(p.id) ? "checked" : ""}/> 放进比一比</label>
          </div>`)).join("") || `<div class="empty">这格货架还空着。我们不拿别的东西充数。</div>`}
      </div>`;
  }
  if (kind === "brands") {
    const list = DATA.brands.filter((b) => matchQ([b.name, b.note, b.type]));
    return `
      ${greet("街上的招牌", "谁还在认真做这件事。招牌不是货架。", "牌", 28)}
      <div class="grid-2">
        ${list.map((b) => `
          <article class="person-card">
            ${avatar(b.name, b.hue)}
            <div>
              <h3><button class="linkish" data-go="brand/${b.id}">${b.name}</button></h3>
              <p class="lead">${b.note}</p>
              <p>桌上放着 ${b.products.join("、")}</p>
            </div>
          </article>`).join("")}
      </div>`;
  }
  if (kind === "people") {
    const list = DATA.people.filter((p) => matchQ([p.name, p.headline, p.quote]));
    return `
      ${greet("街上的人", "先见到人。数字人格会老实告诉你：TA 不是真人。这两位是示意，不是真人排行。", "人", 18)}
      <div class="grid-2">
        ${list.map((p) => `
          <article class="person-card">
            ${avatar(p.name, p.hue)}
            <div>
              <span class="tag ${p.type === "human" ? "ok" : "warn"}">${p.type === "human" ? "真人" : "数字人格 · 不是真人"}</span>
              <h3><button class="linkish" data-go="person/${p.id}">${p.name}</button></h3>
              <p class="quote">${p.quote}</p>
              <p>${p.headline}</p>
            </div>
          </article>`).join("") || `<div class="empty">街上这会儿没人应。我们不编一位给你。</div>`}
      </div>`;
  }
  if (kind === "tools") {
    const list = DATA.tools.filter((t) => matchQ([t.name, t.note, t.steps]));
    return `
      ${greet("工具箱", "干活的家伙。工具不是明星产品。", "器", 48)}
      <div class="grid-2">
        ${list.map((t) => `
          <article class="card">
            <h3><button class="linkish" data-go="tool/${t.id}">${t.name}</button></h3>
            <p class="lead">${t.note}</p>
            <p>${t.steps}</p>
          </article>`).join("")}
      </div>`;
  }
  const assets = DATA.assets.filter((a) => matchQ([a.name, a.kind, a.note]));
  return `
    ${greet("广场背后的地图", "坐标系，不是排行。地图不会给你打分。", "图", 200)}
    <div class="grid-2">
      ${assets.map((a) => `
        <article class="card">
          <span class="tag">${a.kind}</span>
          <h3>${a.name}</h3>
          <p>${a.note}</p>
        </article>`).join("")}
    </div>`;
}

function viewProduct(id) {
  const p = DATA.products.find((x) => x.id === id) || DATA.products[0];
  return `
    <div class="meet">
      ${avatar(p.name, p.hue, "lg")}
      <div>
        <h1 class="page">${p.name}</h1>
        <p class="sub">${p.vibe}</p>
      </div>
    </div>
    <p class="quote">${p.desc}</p>
    <div class="grid-2">
      <article class="card">
        <h3>在这条街上</h3>
        <p>${p.fit === "high" ? "很合适。写代码的人会把它放在手边。" : "谁都聊得来，但不是这条街的第一把交椅。"}</p>
        <p style="margin-top:10px">牌子是 <button class="linkish" data-go="brand/${p.brandId}">${p.brand}</button> · ${p.pricing}</p>
        <div class="actions">
          <button class="btn-line" data-cmp-toggle="${p.id}">${compareSet.has(p.id) ? "已放进比一比" : "放进比一比"}</button>
          <button class="btn-blue" data-go="claims">这是我的 / 写错了</button>
        </div>
      </article>
      <article class="card">
        <h3>伸出来的手</h3>
        ${p.tools.map((t) => {
          const tool = DATA.tools.find((x) => x.id === t);
          return `<p><button class="linkish" data-go="tool/${t}">${tool ? tool.name : t}</button></p>`;
        }).join("")}
      </article>
    </div>`;
}

function viewBrand(id) {
  const b = DATA.brands.find((x) => x.id === id) || DATA.brands[0];
  const ps = DATA.products.filter((p) => p.brandId === b.id);
  return `
    <div class="meet">
      ${avatar(b.name, b.hue, "lg")}
      <div>
        <h1 class="page">${b.name}</h1>
        <p class="sub">${b.note}</p>
      </div>
    </div>
    <h3 class="block-title">桌上放着</h3>
    <div class="grid-2">${ps.map((p) => productCard(p)).join("")}</div>`;
}

function viewPerson(id) {
  const p = DATA.people.find((x) => x.id === id) || DATA.people[0];
  return `
    <div class="meet">
      ${avatar(p.name, p.hue, "lg")}
      <div>
        <h1 class="page">${p.name}</h1>
        <p class="sub">${p.headline}</p>
      </div>
    </div>
    <p class="quote">${p.quote}</p>
    ${p.type === "digital-persona" ? '<p class="featured">我不是真人。请别把我放进真人那一排。</p>' : '<p class="soft">真人。示意条目，不是排行榜上的名次。</p>'}`;
}

function viewTool(id) {
  const t = DATA.tools.find((x) => x.id === id) || DATA.tools[0];
  const used = DATA.products.filter((p) => p.tools.includes(t.id));
  return `
    ${greet(t.name, t.note, t.name, 48)}
    <p>用来：${t.steps}</p>
    <h3 class="block-title">谁在用</h3>
    <div class="grid-2">${used.map((p) => productCard(p)).join("") || `<div class="empty">还没人用这只手。</div>`}</div>`;
}

function viewCompare() {
  const rows = DATA.products.filter((p) => compareSet.has(p.id));
  if (!rows.length) {
    return `${greet("比一比", "先从货架上勾两样来。", "比", 32)}<div class="empty">桌上还空着。去货架勾两样过来。</div>`;
  }
  return `
    ${greet("放在一起看看", "比的是适不适合这条街，不是谁广告更大声。推荐位不会出现在这张桌上。", "比", 32)}
    <div class="compare-row">
      ${rows
        .map(
          (p) => `
        <article class="card">
          ${avatar(p.name, p.hue)}
          <h3>${p.name}</h3>
          <p class="lead">${p.vibe}</p>
          <p>${p.fit === "high" ? "这条街，合适。" : "熟，但不专。"}</p>
          <p>${p.category}</p>
          <p>${p.pricing}</p>
        </article>`
        )
        .join("")}
    </div>
    <p class="footnote">广告只出现在「推荐位」，不会改谁排前面。</p>`;
}

function viewClaims() {
  const groups = {
    pending: DATA.claims.filter((c) => c.status === "pending"),
    claimed: DATA.claims.filter((c) => c.status === "claimed"),
    rejected: DATA.claims.filter((c) => c.status === "rejected"),
  };
  const cur = DATA.claims.find((c) => c.id === claimFocus) || DATA.claims[0];
  const letter = (c) => `
    <button class="letter ${c.id === cur.id ? "on" : ""}" data-claim="${c.id}" type="button">
      <b>${c.entity}</b>
      <span>${c.who}</span>
    </button>`;
  return `
    ${greet("这是我 / 这说错了", "认领自己，或拿出证据说话。钱买不走名次。", "我", 200)}
    <div class="queue">
      <div class="q-col">
        <h3>还在看的信</h3>
        ${groups.pending.map(letter).join("")}
      </div>
      <div class="q-col">
        <h3>已经认领 / 开放着</h3>
        ${groups.claimed.map(letter).join("")}
      </div>
      <article class="card talk">
        <span class="tag ${cur.status === "rejected" ? "warn" : "ok"}">${cur.tone}</span>
        <h3 style="margin-top:10px">${cur.entity}</h3>
        <p class="quote">${cur.ask}</p>
        <p class="soft">${cur.who}</p>
        ${cur.status === "rejected" ? '<p class="featured">退回了。名次不卖。</p>' : ""}
        <div class="actions">
          <button class="btn-line" type="button">好，记下了（示意）</button>
          <button class="btn-line" type="button">这说得不对（示意）</button>
        </div>
        <h3 style="margin-top:20px">退回去的</h3>
        ${groups.rejected.map(letter).join("")}
      </article>
    </div>`;
}

function viewMethod() {
  return `
    ${greet("我们怎么排", "看得见的方法，才值得信。花钱的位置另标，进不了分数。", "尺", 32)}
    <div class="grid-2">
      <article class="card">
        <h3>谁在被看见</h3>
        <p>看三个月里，有多少人认真提到、真正用上，以及是不是这条街上的事。自己报的流水、买来的曝光，都不算。</p>
      </article>
      <article class="card">
        <h3>谁在把事做完</h3>
        <p>看半年里，有没有经得起核对的东西留在街上，以及是不是帮你做完了眼前这桩。</p>
      </article>
    </div>
    <p class="featured" style="margin-top:16px">推荐位可以买。名次不行。这张桌子上，没有「付费即第一」。</p>`;
}

function viewPricing() {
  return `
    ${greet("你请几位伙伴，交几桩活", "逛广场免费。花钱请的是座位和活，不是名次。", "席", 32)}
    <div class="price-grid">
      ${DATA.plans
        .map(
          (p) => `
        <article class="card plan ${p.id === "seat" ? "featured-soft" : ""}">
          <h3>${p.name}</h3>
          <div class="num">${p.price}</div>
          <p class="lead">${p.for}</p>
          <ul>${p.items.map((i) => `<li>${i}</li>`).join("")}</ul>
          ${p.id === "pro" ? `<button class="btn-blue" data-go="claims">去认领</button>` : ""}
          ${p.id === "seat" ? `<button class="btn-blue" data-go="solutions">看看能交什么活</button>` : ""}
        </article>`
        )
        .join("")}
    </div>
    <p class="footnote">名次不卖。广告只出现在「推荐位」，不会改街上谁排前面。</p>`;
}

function render() {
  const { name, id } = parse();
  navActive(name);
  const hello = $("hello");
  if (hello) hello.textContent = HELLO[name] || HELLO.home;
  const root = $("view");
  const map = {
    home: viewHome,
    finder: viewFinder,
    solutions: viewSolutions,
    aiman: viewAiMan,
    run: viewRun,
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
}

document.addEventListener("click", (e) => {
  const goBtn = e.target.closest("[data-go]");
  if (goBtn) {
    e.preventDefault();
    go(goBtn.getAttribute("data-go"));
    return;
  }
  const cat = e.target.closest("[data-cat]");
  if (cat) {
    productCat = cat.getAttribute("data-cat");
    render();
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
    return;
  }
  const ad = e.target.closest("[data-adapt]");
  if (ad) {
    adaptKey = ad.getAttribute("data-adapt");
    render();
    return;
  }
  const mg = e.target.closest("[data-merge]");
  if (mg) {
    mergeNote =
      mg.getAttribute("data-merge") === "ok"
        ? "好。那我去合并。你不点头，我不动。"
        : "行，我先停着。你说哪要改，我再写一稿。";
    render();
  }
});

$("q").addEventListener("input", () => {
  finder.q = $("q").value;
  const n = parse().name;
  if (["finder", "people", "products", "brands", "tools", "assets"].includes(n)) render();
});

window.addEventListener("hashchange", render);
if (!location.hash) location.hash = "#home";
else render();
