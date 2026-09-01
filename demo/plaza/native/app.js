const WEALTH_BRIEF =
  "帮我找财富管理达人做投顾投放，要能管客户资产配置。预算充足，可以先用研发侧的人顶上。";

const TOOL_META = {
  parse_brief: { label: "锁定场景" },
  search_talent: { label: "检索达人库存" },
  search_enterprises: { label: "检索可合作企业" },
  evaluate_fit: { label: "评估适配" },
  compose_shortlist: { label: "生成短名单" },
  draft_outreach: { label: "起草建联稿" },
  refuse: { label: "拒绝覆盖不足" },
  open_campaign: { label: "打开合作项目" },
  advance_delivery: { label: "推进交付" },
};

const traceEl = document.getElementById("trace");
const artsEl = document.getElementById("arts");
const gateEl = document.getElementById("gate");
const statusEl = document.getElementById("run-status");
const briefEl = document.getElementById("brief");
const artifacts = {};
let gateResolver = null;
let running = false;
let toolCount = 0;
let gateCount = 0;

function setStatus(value, text) {
  statusEl.className = "run-status " + (value || "");
  statusEl.textContent = text || value || "待命";
}

function setKpis() {
  document.getElementById("kpi-tools").textContent = String(toolCount);
  document.getElementById("kpi-gates").textContent = `${gateCount} / 3`;
  document.getElementById("kpi-arts").textContent = String(Object.keys(artifacts).length);
}

function summarize(name, payload, status) {
  if (status === "running") {
    if (name === "evaluate_fit") return "正在评估下一条供给…";
    if (name === "advance_delivery") return "正在推进交付检查点…";
    return `${TOOL_META[name]?.label || name} 调用中`;
  }
  const o = payload || {};
  switch (name) {
    case "parse_brief":
      return o.covered
        ? `场景锁定「${o.scene_name}」。将并行检索实践者与可合作企业。`
        : `识别为「${o.scene_name}」。先查覆盖，禁止用其他场景供给填充。`;
    case "search_talent":
      return o.count ? `找到 ${o.count} 条达人 / 专才，覆盖 ${o.coverage}。` : "达人库存为空。覆盖不足，不充数。";
    case "search_enterprises":
      return o.count ? `找到 ${o.count} 家可合作企业。` : "企业库存为空。";
    case "evaluate_fit":
      return o.error ? "条目不存在。" : `${o.name} · 适配 ${o.fit} · ${o.identity}`;
    case "compose_shortlist":
      return `短名单 ${o.length} 条：人 + 数字专才 + 企业可混排。`;
    case "draft_outreach":
      return `生成 ${o.length} 封建联说明。仅合作接口，不群发冷邮件。`;
    case "refuse":
      return o.reason || "已拒绝。continue = false。";
    case "open_campaign":
      return `${o.name} · ${o.ai_man} · ${o.status}`;
    case "advance_delivery": {
      const gate = (o.steps || []).find((s) => s.status === "gate");
      return gate ? `停在人机门「${gate.name}」。` : "检查点已推进。";
    }
    default:
      return "已返回。";
  }
}

function emit(ev) {
  if (ev.type === "status") setStatus(ev.value, ev.text);
  if (ev.type === "tool") {
    const meta = TOOL_META[ev.name] || { label: ev.name };
    const refused = ev.name === "refuse" && ev.status === "done";
    const row = document.createElement("article");
    row.className = "tool-card " + (refused ? "refused" : ev.status || "");
    row.innerHTML = `<span class="dot"></span>
      <div>
        <div class="tool-name">${meta.label}</div>
        <div class="tool-sum">${summarize(ev.name, ev.status === "running" ? ev.input : ev.output, ev.status)}</div>
      </div>`;
    if (ev.status === "done") {
      toolCount += 1;
      const last = [...traceEl.querySelectorAll(".tool-card.running")].pop();
      if (last && last.textContent.includes(meta.label)) last.replaceWith(row);
      else traceEl.appendChild(row);
    } else traceEl.appendChild(row);
    traceEl.scrollTop = traceEl.scrollHeight;
    setKpis();
  }
  if (ev.type === "artifact") {
    artifacts[ev.key] = ev.value;
    renderArts();
    setKpis();
  }
}

function renderArts() {
  const blocks = [];
  if (artifacts.brief) {
    blocks.push(`<div class="art-block"><h4>场景锁定</h4><p><strong>${artifacts.brief.scene_name}</strong> · 覆盖 ${artifacts.brief.covered ? "是" : "否"}</p><p class="muted">${artifacts.brief.note}</p></div>`);
  }
  if (artifacts.talent) {
    blocks.push(tableBlock("找人结果", artifacts.talent.items || [], ["name", "type", "fit"]));
  }
  if (artifacts.orgs) {
    blocks.push(tableBlock("找企业结果", artifacts.orgs.items || [], ["name", "type", "fit"]));
  }
  if (artifacts.evals) {
    blocks.push(`<div class="art-block"><h4>评估</h4>${artifacts.evals
      .map((e) => `<p><strong>${e.name}</strong> 适配 ${e.fit} · ${e.identity}<br><span class="muted">${e.reason}</span></p>`)
      .join("")}</div>`);
  }
  if (artifacts.shortlist) {
    blocks.push(tableBlock("短名单", artifacts.shortlist, ["name", "kind", "fit"]));
  }
  if (artifacts.outreach) {
    blocks.push(`<div class="art-block"><h4>建联稿</h4>${artifacts.outreach
      .map((d) => `<p><strong>${d.to}</strong> · ${d.channel}<br>${d.body}</p>`)
      .join("")}</div>`);
  }
  if (artifacts.campaign) {
    blocks.push(`<div class="art-block"><h4>合作项目</h4>
      <p>${artifacts.campaign.name} · ${artifacts.campaign.ai_man} · ${artifacts.campaign.status}</p>
      <div class="metric-row" style="margin-top:10px">
        <div class="metric"><span>建联</span><b>3</b></div>
        <div class="metric"><span>待处理</span><b>1</b></div>
        <div class="metric"><span>回复</span><b>0</b></div>
      </div>
    </div>`);
  }
  if (artifacts.delivery) {
    blocks.push(`<div class="art-block"><h4>交付检查点</h4><ul>${artifacts.delivery.steps
      .map((s) => `<li>${s.name} · ${s.status}${s.gate ? "（人机门）" : ""}</li>`)
      .join("")}</ul></div>`);
  }
  if (artifacts.refusal) {
    blocks.push(`<div class="art-block"><h4>拒绝</h4><p>${artifacts.refusal.reason}</p><p class="muted">continue = ${artifacts.refusal.continue}。没有换皮继续。</p></div>`);
  }
  artsEl.innerHTML = blocks.join("") || `<p class="muted">产物会以战役卡出现，而不是调试 JSON。</p>`;
}

function tableBlock(title, rows, keys) {
  const labels = { name: "名称", type: "身份", fit: "适配", kind: "类型" };
  if (!rows || !rows.length) return `<div class="art-block"><h4>${title}</h4><p class="muted">空。覆盖不足，不充数。</p></div>`;
  return `<div class="art-block"><h4>${title}</h4><table><thead><tr>${keys.map((k) => `<th>${labels[k] || k}</th>`).join("")}</tr></thead>
    <tbody>${rows.map((r) => `<tr>${keys.map((k) => `<td>${r[k] ?? ""}</td>`).join("")}</tr>`).join("")}</tbody></table></div>`;
}

function waitGate(gate) {
  return new Promise((resolve) => {
    gateResolver = resolve;
    setStatus("waiting", "等待需求方签收");
    gateEl.hidden = false;
    gateEl.innerHTML = `<h4>${gate.title}</h4><p>${gate.body}</p>
      <div class="actions">
        <button class="btn-blue" type="button" data-gate="approve">签收，继续</button>
        <button class="btn-line" type="button" data-gate="reject">驳回</button>
      </div>`;
  });
}

async function start(brief) {
  if (running) return;
  running = true;
  Object.keys(artifacts).forEach((k) => delete artifacts[k]);
  toolCount = 0;
  gateCount = 0;
  traceEl.innerHTML = "";
  gateEl.hidden = true;
  gateEl.innerHTML = "";
  renderArts();
  setKpis();
  document.getElementById("btn-run").disabled = true;
  document.getElementById("btn-wealth").disabled = true;
  try {
    await PlazaNative.runNative({
      brief,
      catalog: NATIVE_CATALOG,
      emit,
      waitGate,
    });
  } finally {
    running = false;
    document.getElementById("btn-run").disabled = false;
    document.getElementById("btn-wealth").disabled = false;
    if (!gateResolver) gateEl.hidden = true;
  }
}

document.getElementById("btn-run").addEventListener("click", () => start(briefEl.value.trim()));
document.getElementById("btn-wealth").addEventListener("click", () => {
  briefEl.value = WEALTH_BRIEF;
  start(WEALTH_BRIEF);
});
gateEl.addEventListener("click", (e) => {
  const b = e.target.closest("[data-gate]");
  if (!b || !gateResolver) return;
  const r = gateResolver;
  gateResolver = null;
  gateEl.hidden = true;
  if (b.getAttribute("data-gate") === "approve") {
    gateCount += 1;
    setKpis();
  }
  r(b.getAttribute("data-gate"));
});

renderArts();
setKpis();
