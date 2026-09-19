/**
 * Dedicated Company Preparation Hub Controller
 * Fully dynamic: loads company from ?company=<slug> and renders all details,
 * questions, and isolated progress. Never falls back to TCS.
 */

document.addEventListener("DOMContentLoaded", async () => {
  const employee = requireAuth();
  if (!employee) return;

  const urlParams = new URLSearchParams(window.location.search);
  const companySlug = (urlParams.get("company") || "").toLowerCase().trim();

  // If slug is missing, immediately show Company Not Found view
  if (!companySlug) {
    showCompanyNotFound();
    return;
  }

  const notFoundView = document.getElementById("company-not-found-view");
  const hubContent = document.getElementById("company-hub-content");

  function showCompanyNotFound() {
    if (notFoundView) notFoundView.style.display = "block";
    if (hubContent) hubContent.style.display = "none";
    document.title = "Company Not Found | AI Employee Prep";
  }

  function showCompanyHub() {
    if (notFoundView) notFoundView.style.display = "none";
    if (hubContent) hubContent.style.display = "block";
  }

  // Role persistence per user + per company
  const roleStorageKey = `selected_role_${employee.id}_${companySlug}`;
  let currentRole = urlParams.get("role") || localStorage.getItem(roleStorageKey) || employee.target_role || employee.job_role || "Java Developer";

  let currentCompany = null;
  let activeTrackModule = "aptitude";

  const roleSelect = document.getElementById("role-select");
  if (roleSelect) {
    roleSelect.value = currentRole;
    roleSelect.addEventListener("change", async () => {
      currentRole = roleSelect.value;
      localStorage.setItem(roleStorageKey, currentRole);

      // Persist to backend
      try {
        await fetch(`${API_BASE}/api/companies/${encodeURIComponent(companySlug)}/select`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ employee_id: employee.id, role: currentRole })
        });
      } catch (e) {
        console.warn("Failed to sync role selection to backend:", e);
      }

      setupModuleButtons();
      await loadCompanyQuestions(companySlug, currentRole, activeTrackModule);
    });
  }

  // Setup navigation buttons early
  setupModuleButtons();

  // Load Company Data
  await loadCompanyHubData(companySlug);

  async function loadCompanyHubData(slug) {
    try {
      const res = await fetch(`${API_BASE}/api/companies/${encodeURIComponent(slug)}?_t=${Date.now()}`, {
        cache: "no-store"
      });

      if (!res.ok) {
        showCompanyNotFound();
        return;
      }

      const data = await res.json();
      if (!data.success || !data.company) {
        showCompanyNotFound();
        return;
      }

      currentCompany = data.company;
      showCompanyHub();
      renderCompanyHub(currentCompany);

      // Store in memory / session for current user without leaking across tabs
      await setSelectedCompany(slug, currentCompany.company_name, currentRole);

    } catch (e) {
      console.error("Error loading company hub:", e);
      showCompanyNotFound();
      return;
    }

    // Load isolated progress for this company
    await loadCompanyProgress(slug);

    // Load dynamic questions for active track
    await loadCompanyQuestions(slug, currentRole, activeTrackModule);
  }

  function renderCompanyHub(comp) {
    document.title = `${comp.company_name} Preparation | AI Employee Prep`;
    const breadcrumb = document.getElementById("breadcrumb-company-name");
    if (breadcrumb) breadcrumb.textContent = comp.company_name;

    const heroTitle = document.getElementById("company-hero-title");
    if (heroTitle) heroTitle.textContent = `${comp.company_name} Preparation`;

    const targetLabel = document.getElementById("company-target-label");
    if (targetLabel) targetLabel.textContent = comp.company_name;

    const catBadge = document.getElementById("company-hero-cat");
    if (catBadge) catBadge.textContent = comp.industry || comp.category || "IT Services";

    const diffBadge = document.getElementById("company-hero-diff");
    if (diffBadge) diffBadge.textContent = `Difficulty: ${comp.difficulty || 'Medium'}`;

    const modTarget = document.getElementById("label-module-target");
    if (modTarget) modTarget.textContent = comp.company_name;

    // Detailed Syllabus Breakdown
    const elRounds = document.getElementById("detail-rounds");
    if (elRounds) elRounds.textContent = comp.hiring_rounds || "Round 1: Online Assessment | Round 2: Technical Interview | Round 3: HR";

    const elApt = document.getElementById("detail-aptitude");
    if (elApt) elApt.textContent = comp.aptitude_pattern || "Quantitative, Logical, and Verbal reasoning tests.";

    const elCode = document.getElementById("detail-coding");
    if (elCode) elCode.textContent = comp.coding_pattern || "Algorithmic data structures and string/array problems.";

    const elTech = document.getElementById("detail-technical");
    if (elTech) elTech.textContent = comp.technical_focus || "Core OOPs, DBMS, SQL, and Capstone Project Architecture.";

    // Module Snippet Badges
    const modApt = document.getElementById("mod-apt-pattern");
    if (modApt) modApt.textContent = comp.aptitude_pattern ? comp.aptitude_pattern.split("[")[0].slice(0, 75) + "..." : "Quantitative & Logical";

    const modCode = document.getElementById("mod-code-pattern");
    if (modCode) modCode.textContent = comp.coding_pattern ? comp.coding_pattern.slice(0, 75) + "..." : "Algorithmic Challenges";

    const modTech = document.getElementById("mod-tech-pattern");
    if (modTech) modTech.textContent = comp.technical_focus ? comp.technical_focus.slice(0, 75) + "..." : "Core CS & Architecture";

    const modHr = document.getElementById("mod-hr-pattern");
    if (modHr) modHr.textContent = comp.hr_tips ? comp.hr_tips.slice(0, 75) + "..." : "STAR Behavioral framing";

    // Populate Company Placement Intelligence & Salary Tiers
    if (comp.intel) {
      const intel = comp.intel;
      const compNameEl = document.getElementById("intel-comp-name");
      if (compNameEl) compNameEl.textContent = comp.company_name;

      const tiersContainer = document.getElementById("intel-salary-tiers");
      if (tiersContainer && intel.salary_tiers) {
        tiersContainer.innerHTML = intel.salary_tiers.map(t => `
          <div style="background: var(--bg-subtle); border: 1px solid var(--border-color); border-radius: 8px; padding: 12px 14px; border-top: 3px solid #059669;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
              <strong style="font-size: 0.88rem; color: var(--text-main);">${escapeHtml(t.tier)}</strong>
              <span class="badge badge-success" style="font-size: 0.75rem;">${escapeHtml(t.package)}</span>
            </div>
            <div style="font-size: 0.8rem; color: var(--primary-700); font-weight: 600; margin-bottom: 4px;">${escapeHtml(t.role)}</div>
            <div style="font-size: 0.76rem; color: var(--text-muted);">${escapeHtml(t.criteria)}</div>
          </div>
        `).join("");
      }

      const eligEl = document.getElementById("intel-eligibility");
      if (eligEl && intel.eligibility) eligEl.textContent = intel.eligibility;

      const selEl = document.getElementById("intel-selection");
      if (selEl) selEl.textContent = `${intel.selection_ratio || '~8%'} • Timeline: ${intel.hiring_timeline || '2-3 recruitment rounds'}`;

      const tipsEl = document.getElementById("intel-tips");
      if (tipsEl && intel.winning_tips) {
        tipsEl.innerHTML = intel.winning_tips.map(tip => `<li style="margin-bottom: 4px;">${escapeHtml(tip)}</li>`).join("");
      }

      const pitfallsEl = document.getElementById("intel-pitfalls");
      if (pitfallsEl && intel.common_pitfalls) {
        pitfallsEl.innerHTML = intel.common_pitfalls.map(p => `<li style="margin-bottom: 4px;">${escapeHtml(p)}</li>`).join("");
      }
    }

    // Bind Quick Revision Cheatsheet Modal
    const csModal = document.getElementById("cheatsheet-modal");
    const btnOpenCs = document.getElementById("btn-open-cheatsheet");
    const btnCloseCs = document.getElementById("btn-close-cheatsheet");
    if (btnOpenCs && csModal) {
      btnOpenCs.onclick = () => csModal.style.display = "flex";
      if (btnCloseCs) btnCloseCs.onclick = () => csModal.style.display = "none";
      csModal.onclick = (e) => { if (e.target === csModal) csModal.style.display = "none"; };
    }
  }

  async function loadCompanyProgress(slug) {
    try {
      const res = await fetch(`${API_BASE}/api/companies/${encodeURIComponent(slug)}/progress?employee_id=${employee.id}&_t=${Date.now()}`, {
        cache: "no-store"
      });
      if (res.ok) {
        const data = await res.json();
        if (data.success && data.preparation) {
          const prep = data.preparation;
          const overallPct = Math.round(prep.progress || 0);

          const heroPct = document.getElementById("hero-progress-pct");
          if (heroPct) heroPct.textContent = `${overallPct}%`;

          const heroStatus = document.getElementById("hero-progress-status");
          if (heroStatus) heroStatus.textContent = overallPct >= 80 ? "Interview Ready" : "In Progress";

          // Mini progress bar stats
          const apt = Math.round(prep.aptitude_progress || 0);
          const code = Math.round(prep.coding_progress || 0);
          const tech = Math.round(prep.technical_progress || 0);
          const intv = Math.round(prep.interview_progress || 0);
          const hr = Math.round(prep.hr_progress || 0);
          const resProg = Math.round(prep.resume_progress || 0);
          const sk = Math.round(prep.skills_progress || 0);
          const rd = Math.round(prep.roadmap_progress || 0);

          if (document.getElementById("prog-aptitude")) document.getElementById("prog-aptitude").textContent = `${apt}%`;
          if (document.getElementById("prog-coding")) document.getElementById("prog-coding").textContent = `${code}%`;
          if (document.getElementById("prog-technical")) document.getElementById("prog-technical").textContent = `${tech}%`;
          if (document.getElementById("prog-interview")) document.getElementById("prog-interview").textContent = `${intv}%`;
          if (document.getElementById("prog-hr")) document.getElementById("prog-hr").textContent = `${hr}%`;

          if (document.getElementById("fill-apt")) document.getElementById("fill-apt").style.width = `${apt}%`;
          if (document.getElementById("fill-coding")) document.getElementById("fill-coding").style.width = `${code}%`;
          if (document.getElementById("fill-technical")) document.getElementById("fill-technical").style.width = `${tech}%`;
          if (document.getElementById("fill-interview")) document.getElementById("fill-interview").style.width = `${intv}%`;
          if (document.getElementById("fill-hr")) document.getElementById("fill-hr").style.width = `${hr}%`;
          if (document.getElementById("fill-resume")) document.getElementById("fill-resume").style.width = `${resProg}%`;
          if (document.getElementById("fill-skills")) document.getElementById("fill-skills").style.width = `${sk}%`;
          if (document.getElementById("fill-roadmap")) document.getElementById("fill-roadmap").style.width = `${rd}%`;
        }
      }
    } catch (e) {
      console.error("Error loading company progress:", e);
    }
  }

  function setupModuleButtons() {
    const roleParam = () => encodeURIComponent(currentRole);
    const slugParam = () => encodeURIComponent(companySlug);

    function bind(id, urlGenerator) {
      const btn = document.getElementById(id);
      if (btn) {
        btn.onclick = (e) => {
          e.preventDefault();
          window.location.href = urlGenerator();
        };
      }
    }

    bind("btn-start-aptitude", () => `aptitude.html?company=${slugParam()}&role=${roleParam()}`);
    bind("btn-start-coding", () => `preparation.html?company=${slugParam()}&role=${roleParam()}&mode=coding`);
    bind("btn-start-technical", () => `preparation.html?company=${slugParam()}&role=${roleParam()}&mode=technical`);
    bind("btn-start-hr", () => `interview.html?company=${slugParam()}&role=${roleParam()}&type=hr`);
    bind("btn-start-interview", () => `interview.html?company=${slugParam()}&role=${roleParam()}&type=mock`);
    bind("btn-prepare-resume", () => `resume.html?company=${slugParam()}&role=${roleParam()}`);
    bind("btn-assess-skills", () => `skills.html?company=${slugParam()}&role=${roleParam()}`);
    bind("btn-view-roadmap", () => `roadmap.html?company=${slugParam()}&role=${roleParam()}`);
    bind("btn-launch-full-test", () => `aptitude.html?company=${slugParam()}&role=${roleParam()}`);

    // Refresh questions button
    const btnRefreshMCQs = document.getElementById("btn-refresh-company-mcqs");
    if (btnRefreshMCQs) {
      btnRefreshMCQs.onclick = async (e) => {
        e.preventDefault();
        btnRefreshMCQs.disabled = true;
        btnRefreshMCQs.innerHTML = '<span><i class="fa-solid fa-arrows-rotate fa-spin"></i> Shuffling...</span>';
        await loadCompanyQuestions(companySlug, currentRole, activeTrackModule);
        btnRefreshMCQs.disabled = false;
        btnRefreshMCQs.innerHTML = '<span><i class="fa-solid fa-arrows-rotate"></i> Change / New Questions</span>';
        showToast(`Fresh ${activeTrackModule.toUpperCase()} questions loaded!`, "success");
      };
    }

    // Category track tabs
    const trackBtns = document.querySelectorAll(".comp-track-btn");
    trackBtns.forEach(btn => {
      btn.onclick = async (e) => {
        e.preventDefault();
        trackBtns.forEach(b => {
          b.className = "btn btn-secondary btn-sm comp-track-btn";
        });
        btn.className = "btn btn-primary btn-sm comp-track-btn";
        activeTrackModule = btn.dataset.module || "aptitude";
        await loadCompanyQuestions(companySlug, currentRole, activeTrackModule);
      };
    });
  }

  async function loadCompanyQuestions(slug, role, moduleName = "aptitude") {
    const listEl = document.getElementById("company-mcqs-list");
    const targetNameEl = document.getElementById("company-mcq-target-name");
    if (!listEl) return;

    if (targetNameEl && currentCompany) {
      targetNameEl.textContent = currentCompany.company_name;
    }

    listEl.innerHTML = `
      <div style="text-align: center; padding: 28px; color: var(--text-muted);">
        <div style="font-size: 1.8rem; margin-bottom: 8px; color: var(--primary-600);"><i class="fa-solid fa-hourglass-half"></i></div>
        Loading ${escapeHtml(moduleName.toUpperCase())} questions for ${currentCompany ? currentCompany.company_name : slug}...
      </div>
    `;

    try {
      const res = await fetch(`${API_BASE}/api/companies/${encodeURIComponent(slug)}/modules/${encodeURIComponent(moduleName)}?role=${encodeURIComponent(role)}&_t=${Date.now()}`, {
        cache: "no-store"
      });
      if (!res.ok) {
        listEl.innerHTML = `<div style="color: var(--text-muted); padding: 16px;">Questions for this track will appear here.</div>`;
        return;
      }

      const data = await res.json();
      const rawQuestions = data.questions || data.problems || [];
      const questions = rawQuestions.slice(0, 5);

      if (!questions.length) {
        listEl.innerHTML = `<div style="color: var(--text-muted); padding: 16px;">No questions found for this track. Try another tab above.</div>`;
        return;
      }

      listEl.innerHTML = "";

      // CODING PROBLEMS
      if (moduleName === "coding") {
        questions.forEach((p, pIdx) => {
          const pCard = document.createElement("div");
          pCard.className = "card";
          pCard.style.cssText = "border: 1px solid var(--border-color); background: var(--bg-card); padding: 22px; border-radius: var(--radius-lg); box-shadow: var(--shadow-sm); margin-bottom: 16px;";

          pCard.innerHTML = `
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; flex-wrap: wrap; gap: 8px;">
              <div style="display: flex; gap: 8px; align-items: center;">
                <span class="badge badge-purple">${escapeHtml(p.category || "Algorithms")}</span>
                <span class="badge ${p.difficulty === 'Easy' ? 'badge-success' : (p.difficulty === 'Medium' ? 'badge-warning' : 'badge-primary')}">
                  ${escapeHtml(p.difficulty || "Medium")}
                </span>
              </div>
              <span style="font-size: 0.8rem; color: var(--text-muted);"><i class="fa-solid fa-building"></i> Asked in ${escapeHtml(currentCompany ? currentCompany.company_name : slug)}</span>
            </div>

            <h4 style="font-size: 1.15rem; margin-bottom: 8px; color: var(--text-main);">
              ${pIdx + 1}. ${escapeHtml(p.title || p.question || "Coding Problem")}
            </h4>
            <p style="font-size: 0.9rem; color: var(--text-muted); line-height: 1.5; margin-bottom: 16px;">
              ${escapeHtml(p.description || p.question || "")}
            </p>

            <div style="display: flex; justify-content: flex-end;">
              <a href="preparation.html?company=${encodeURIComponent(slug)}&role=${encodeURIComponent(role)}&problem=${encodeURIComponent(p.id)}&mode=coding" class="btn btn-primary btn-sm" style="display: inline-flex; align-items: center; gap: 6px;">
                <span>Solve Problem in Code Studio</span> <i class="fa-solid fa-arrow-right"></i>
              </a>
            </div>
          `;
          listEl.appendChild(pCard);
        });
        return;
      }

      // APTITUDE, TECHNICAL, HR, AI INTERVIEW QUESTIONS
      questions.forEach((q, qIdx) => {
        const qCard = document.createElement("div");
        qCard.className = "card";
        qCard.style.cssText = "border: 1px solid var(--border-color); background: var(--bg-card); padding: 22px; border-radius: var(--radius-lg); box-shadow: var(--shadow-sm); margin-bottom: 16px;";

        const hasOptions = Array.isArray(q.options) && q.options.length > 0;

        let optionsHtml = "";
        if (hasOptions) {
          const optLetters = ["A", "B", "C", "D", "E", "F"];
          optionsHtml = `
            <div style="display: flex; flex-direction: column; gap: 10px; margin-bottom: 16px;">
              ${q.options.map((opt, oIdx) => {
                const letter = optLetters[oIdx] || String(oIdx + 1);
                return `
                  <button type="button" class="comp-opt-btn" data-qidx="${qIdx}" data-oidx="${oIdx}" data-opt="${escapeHtml(opt)}" id="comp-q-${qIdx}-opt-${oIdx}" style="display: flex; align-items: center; gap: 14px; text-align: left; padding: 12px 16px; background: var(--bg-subtle); border: 1px solid var(--border-color); border-radius: 8px; cursor: pointer; transition: all 0.2s; font-size: 0.92rem; color: var(--text-main);">
                    <span style="font-weight: 700; width: 28px; height: 28px; border-radius: 50%; background: #ffffff; border: 1px solid var(--border-color); display: flex; align-items: center; justify-content: center; font-size: 0.8rem; color: var(--primary-700); flex-shrink: 0;">${letter}</span>
                    <span style="line-height: 1.4;">${escapeHtml(opt)}</span>
                  </button>
                `;
              }).join("")}
            </div>
          `;
        }

        const guidanceText = q.explanation || q.tips || "Focus on practical problem solving and structured logic.";

        qCard.innerHTML = `
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; flex-wrap: wrap; gap: 8px;">
            <div style="display: flex; gap: 8px; align-items: center;">
              <span class="badge badge-purple">${escapeHtml(q.category || moduleName.toUpperCase())}</span>
              ${q.difficulty ? `<span class="badge ${q.difficulty === 'Easy' ? 'badge-success' : 'badge-warning'}">${escapeHtml(q.difficulty)}</span>` : ''}
            </div>
            <span style="font-size: 0.8rem; color: var(--text-muted);"><i class="fa-solid fa-building"></i> ${escapeHtml(currentCompany ? currentCompany.company_name : slug)}</span>
          </div>

          <h4 style="font-size: 1.05rem; margin-bottom: 14px; color: var(--text-main); line-height: 1.5;">
            ${qIdx + 1}. ${escapeHtml(q.question)}
          </h4>

          ${optionsHtml}

          <!-- Explanation box -->
          <div id="comp-exp-${qIdx}" style="display: ${hasOptions ? 'none' : 'block'}; background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 8px; padding: 12px 16px; font-size: 0.86rem; color: #166534; line-height: 1.5; margin-top: 10px;">
            <strong><i class="fa-solid fa-circle-check"></i> ${hasOptions ? 'Explanation & Answer' : 'Preparation Guidance'}:</strong>
            <p style="margin: 4px 0 0 0;">${escapeHtml(guidanceText)}</p>
          </div>
        `;

        listEl.appendChild(qCard);

        // Bind click handler for options
        if (hasOptions) {
          const optBtns = qCard.querySelectorAll(".comp-opt-btn");
          const expDiv = qCard.querySelector(`#comp-exp-${qIdx}`);

          optBtns.forEach(btn => {
            btn.addEventListener("click", () => {
              const selectedOpt = btn.dataset.opt;
              const isCorrect = String(selectedOpt).trim() === String(q.correct_answer).trim();

              optBtns.forEach(b => {
                b.style.pointerEvents = "none";
                if (String(b.dataset.opt).trim() === String(q.correct_answer).trim()) {
                  b.style.borderColor = "#10b981";
                  b.style.background = "#ecfdf5";
                } else if (b === btn && !isCorrect) {
                  b.style.borderColor = "#ef4444";
                  b.style.background = "#fef2f2";
                }
              });

              if (expDiv) expDiv.style.display = "block";
              if (isCorrect) {
                showToast("Correct Answer! 🎉", "success");
              } else {
                showToast("Incorrect option. Check the explanation below.", "error");
              }
            });
          });
        }
      });

    } catch (err) {
      console.error("Error loading company questions:", err);
      listEl.innerHTML = `<div style="color: var(--text-muted); padding: 12px;">Could not load questions.</div>`;
    }
  }

  function escapeHtml(str) {
    if (!str) return "";
    return String(str)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#039;");
  }
});
