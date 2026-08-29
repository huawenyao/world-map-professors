const WEALTH_BRIEF =
  "帮我找财富管理达人做投顾投放，要能管客户资产配置。预算充足，可以先用研发侧的人顶上。";

const traceEl = document.getElementById("trace");
const artsEl = document.getElementById("arts");
const gateEl = document.getElementById("gate");
const statusEl = document.getElementById("run-status");
const briefEl = document.getElementById("brief");
const artifacts = {};
let gateResolver = null;
let running = false;

function setStatus(value, text) {
  statusEl.className = "run-status " + (value || "");
  statusEl.textContent = text || value || "待命";
}

function pretty(v) {
  return JSON.stringify(v, null, 2);
}

function emit(ev) {
  if (ev.type === "status") setStatus(ev.value, ev.text);
  if (ev.type === "tool") {
    const row = document.createElement("article");
    row.className = "tool-card " + (ev.status || "");
    row.innerHTML = `<div><b>${ev.name}</b> · ${ev.status === "running" ? "调用中" : "返回"}</div>
      <pre>${pretty(ev.status === "running" ? ev.input : ev.output)}</pre>`;
    if (ev.status === "done") {
      const last = traceEl.querySelector(".tool-card.running:last-of-type");
      if (last && last.textContent.includes(ev.name)) last.replaceWith(row);
      else traceEl.appendChild(row);
    } else traceEl.appendChild(row);
    traceEl.scrollTop = traceEl.scrollHeight;
  }
  if (ev.type === "artifact") {
    artifacts[ev.key] = ev.value;
    renderArts();
  }
}

function renderArts() {
  const blocks = [];
  if (artifacts.brief) {
    blocks.push(`<div class="art-block"><h4>场景锁定</h4><p>${artifacts.brief.scene_name} · 覆盖 ${artifacts.brief.covered ? "是" : "否"}</p><p class="muted">${artifacts.brief.note}</p></div>`);
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
    blocks.push(`<div class="art-block"><h4>合作项目</h4><p>${artifacts.campaign.name} · ${artifacts.campaign.ai_man} · ${artifacts.campaign.status}</p></div>`);
  }
  if (artifacts.delivery) {
    blocks.push(`<div class="art-block"><h4>交付检查点</h4><ul>${artifacts.delivery.steps
      .map((s) => `<li>${s.name} · ${s.status}${s.gate ? "（人机门）" : ""}</li>`)
      .join("")}</ul></div>`);
  }
  if (artifacts.refusal) {
    blocks.push(`<div class="art-block"><h4>拒绝</h4><p>${artifacts.refusal.reason}</p><p class="muted">continue = ${artifacts.refusal.continue}</p></div>`);
  }
  artsEl.innerHTML = blocks.join("") || `<p class="muted">产物将在工具返回后出现。</p>`;
}

function tableBlock(title, rows, keys) {
  if (!rows || !rows.length) return `<div class="art-block"><h4>${title}</h4><p class="muted">空。覆盖不足，不充数。</p></div>`;
  return `<div class="art-block"><h4>${title}</h4><table><thead><tr>${keys.map((k) => `<th>${k}</th>`).join("")}</tr></thead>
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
  traceEl.innerHTML = "";
  gateEl.hidden = true;
  gateEl.innerHTML = "";
  renderArts();
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
    gateEl.hidden = true;
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
  r(b.getAttribute("data-gate"));
});

renderArts();
