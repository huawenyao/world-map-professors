(function (global) {
  const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

  function detectScene(brief) {
    const t = brief || "";
    if (/财富|理财|投顾|管钱/.test(t)) {
      return {
        id: "scn-fin-wealth-mgmt",
        name: "财富管理",
        covered: false,
        job: "find_talent",
      };
    }
    return {
      id: "scn-tech-software-dev",
      name: "软件研发",
      covered: true,
      job: /企业|品牌|联合|合作/.test(t) ? "talent_and_enterprise" : "talent_and_enterprise",
    };
  }

  function tools(catalog) {
    return {
      parse_brief(brief) {
        const scene = detectScene(brief);
        return {
          scene_id: scene.id,
          scene_name: scene.name,
          covered: scene.covered,
          jobs: scene.covered ? ["找人", "找企业", "评估", "建联", "交付"] : ["找人"],
          note: scene.covered
            ? "锁定软件研发。将并行检索实践者与可合作企业。"
            : "识别为财富管理。先查覆盖，禁止用其他场景供给填充。",
        };
      },
      search_talent(sceneId) {
        const rows = catalog.talent.filter((p) => p.scene === sceneId);
        return {
          scene_id: sceneId,
          count: rows.length,
          coverage: rows.length ? "ok" : "gap",
          items: rows.map((p) => ({ id: p.id, name: p.name, type: p.typeLabel, fit: p.fit })),
        };
      },
      search_enterprises(sceneId) {
        const rows = catalog.enterprises.filter((e) => e.scene === sceneId);
        return {
          scene_id: sceneId,
          count: rows.length,
          coverage: rows.length ? "ok" : "gap",
          items: rows.map((e) => ({ id: e.id, name: e.name, type: e.type, fit: e.fit })),
        };
      },
      evaluate_fit(id) {
        const hit =
          catalog.talent.find((p) => p.id === id) ||
          catalog.enterprises.find((e) => e.id === id);
        if (!hit) return { error: "not_found", id };
        return {
          id: hit.id,
          name: hit.name,
          scene: hit.sceneName,
          fit: hit.fit,
          contrib: hit.contrib,
          identity: hit.typeLabel || hit.type,
          reason: hit.why,
          partner: hit.partner || hit.role,
        };
      },
      compose_shortlist(ids) {
        return ids.map((id) => {
          const hit =
            catalog.talent.find((p) => p.id === id) ||
            catalog.enterprises.find((e) => e.id === id);
          return hit
            ? { id: hit.id, name: hit.name, kind: hit.partner ? "enterprise" : "talent", fit: hit.fit }
            : { id, missing: true };
        });
      },
      draft_outreach(shortlist) {
        return shortlist.map((row) => ({
          to: row.name,
          channel: row.kind === "enterprise" ? "企业合作接口" : "实践者建联",
          subject: row.kind === "enterprise" ? "软件研发场景联合方案意向" : "场景实践合作意向（非投放粉数）",
          body:
            row.kind === "enterprise"
              ? `基于广场坐标系，贵司在「软件研发」场景适配为 ${row.fit}。希望确认联合方案切口与产品挂载，不涉及购买名次。`
              : `基于场景贡献而非粉丝数，邀请就「软件研发」实践合作做一次对齐。数字人格/数字专才将保持非真人标识。`,
        }));
      },
      refuse(reason) {
        return { refused: true, reason, continue: false };
      },
      open_campaign() {
        return {
          campaign_id: "camp-dev-native",
          name: catalog.solution.name,
          ai_man: catalog.solution.aiMan,
          status: "交付中",
          human_checkpoints: catalog.solution.checkpoints,
        };
      },
      advance_delivery(step) {
        const steps = [
          { id: "s1", name: "需求拆解", status: "done" },
          { id: "s2", name: "方案确认", status: "done", gate: true },
          { id: "s3", name: "编码实现", status: "done" },
          { id: "s4", name: "测试生成", status: "done" },
          { id: "s5", name: "代码审查", status: step === "sign" ? "done" : "gate", gate: true },
          { id: "s6", name: "合并上线", status: step === "sign" ? "queued" : "queued" },
        ];
        return { steps, waiting: step !== "sign" };
      },
    };
  }

  async function runNative({ brief, catalog, emit, waitGate }) {
    const T = tools(catalog);
    const call = async (name, input) => {
      emit({ type: "tool", name, input, status: "running" });
      await sleep(280);
      const output = T[name](input);
      emit({ type: "tool", name, input, output, status: "done" });
      await sleep(160);
      return output;
    };

    emit({ type: "status", value: "running", text: "Agent 已接管作战室" });
    const parsed = await call("parse_brief", brief);
    emit({ type: "artifact", key: "brief", value: parsed });

    if (!parsed.covered) {
      const talent = await call("search_talent", parsed.scene_id);
      emit({ type: "artifact", key: "talent", value: talent });
      const refusal = await call(
        "refuse",
        "财富管理达人库存覆盖不足。禁止用软件研发实践者、数字人格或 AI Man 充数，亦不可自动交付。"
      );
      emit({ type: "artifact", key: "refusal", value: refusal });
      emit({ type: "status", value: "refused", text: "已拒绝自动交付" });
      return { status: "refused" };
    }

    const talent = await call("search_talent", parsed.scene_id);
    const orgs = await call("search_enterprises", parsed.scene_id);
    emit({ type: "artifact", key: "talent", value: talent });
    emit({ type: "artifact", key: "orgs", value: orgs });

    const evalIds = ["psn-tech-sample-ai-engineer", "aim-tech-sd-feature", "brd-github"];
    const evals = [];
    for (const id of evalIds) evals.push(await call("evaluate_fit", id));
    emit({ type: "artifact", key: "evals", value: evals });

    const shortlist = await call("compose_shortlist", [
      "psn-tech-sample-ai-engineer",
      "aim-tech-sd-feature",
      "brd-github",
    ]);
    emit({ type: "artifact", key: "shortlist", value: shortlist });

    const gate1 = await waitGate({
      id: "shortlist",
      title: "签收短名单",
      body: "人 + 数字专才 + 企业将进入同一合作项目。数字专才不进入真人达人榜。",
    });
    if (gate1 !== "approve") {
      emit({ type: "status", value: "stopped", text: "需求方驳回短名单，作战结束" });
      return { status: "stopped" };
    }
    emit({ type: "status", value: "running", text: "短名单已签，生成建联稿" });

    const drafts = await call("draft_outreach", shortlist);
    emit({ type: "artifact", key: "outreach", value: drafts });
    const gate2 = await waitGate({
      id: "outreach",
      title: "签收建联稿",
      body: "仅生成合作说明，不群发冷邮件。名次不可买。",
    });
    if (gate2 !== "approve") {
      emit({ type: "status", value: "stopped", text: "建联稿未通过" });
      return { status: "stopped" };
    }
    emit({ type: "status", value: "running", text: "建联已签，启动交付" });

    const campaign = await call("open_campaign", {});
    const delivery = await call("advance_delivery", "wait");
    emit({ type: "artifact", key: "campaign", value: campaign });
    emit({ type: "artifact", key: "delivery", value: delivery });

    const gate3 = await waitGate({
      id: "delivery",
      title: "签收代码审查",
      body: "人机门仍开着。不点头则不合并。",
    });
    if (gate3 !== "approve") {
      emit({ type: "status", value: "stopped", text: "审查未通过，交付停在检查点" });
      return { status: "stopped" };
    }

    const signed = await call("advance_delivery", "sign");
    emit({ type: "artifact", key: "delivery", value: signed });
    emit({ type: "status", value: "done", text: "战役完成：供给已链接，审查已签收" });
    return { status: "done" };
  }

  global.PlazaNative = { runNative, detectScene };
})(window);
