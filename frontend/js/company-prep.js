/**
 * Dedicated Company Preparation Hub Controller
 */

document.addEventListener("DOMContentLoaded", async () => {
  const employee = requireAuth();
  if (!employee) return;

  // Determine current company slug from URL query params or stored state
  const urlParams = new URLSearchParams(window.location.search);
  let companySlug = (urlParams.get("company") || "").toLowerCase().trim();

  if (!companySlug) {
    const active = getSelectedCompany();
    companySlug = (active.slug || "tcs").toLowerCase();
  }

  let currentCompany = null;
  let currentRole = urlParams.get("role") || employee.target_role || employee.job_role || "Java Developer";
  let activeTrackModule = "aptitude";

  // Setup button listeners immediately so they work even before network fetches complete
  setupModuleButtons();
  await loadCompanyHubData(companySlug);

  async function loadCompanyHubData(slug) {
    try {
      const res = await fetch(`${API_BASE}/api/companies/${slug}`);
      if (!res.ok) {
        showToast("Company not found. Loading TCS catalog default.", "error");
        if (slug !== "tcs") {
          window.location.href = "company-prep.html?company=tcs";
          return;
        }
      }

      const data = await res.json();
      if (data.success && data.company) {
        currentCompany = data.company;
        renderCompanyHub(currentCompany);

        // Store active selected company
        await setSelectedCompany(slug, currentCompany.company_name, currentRole);
      }
    } catch (e) {
      console.error("Error loading company hub:", e);
      showToast("Failed to connect to backend server.", "error");
    }

    // Load isolated progress for this company
    await loadCompanyProgress(slug);

    // Load questions with options stacked one below another (A, B, C, D)
    await loadCompanyQuestions(slug, currentRole, activeTrackModule);
  }

  function renderCompanyHub(comp) {
    document.title = `${comp.company_name} Preparation | AI Employee Prep`;
    document.getElementById("breadcrumb-company-name").textContent = comp.company_name;
    document.getElementById("company-hero-emoji").textContent = comp.logo_emoji || "🏢";
    document.getElementById("company-hero-title").textContent = `${comp.company_name} Preparation`;
    document.getElementById("company-target-label").textContent = comp.company_name;
    document.getElementById("company-hero-cat").textContent = comp.category || "IT Services";
    document.getElementById("company-hero-diff").textContent = `Difficulty: ${comp.difficulty || 'Medium'}`;
    document.getElementById("label-module-target").textContent = comp.company_name;

    // Detailed Syllabus Breakdown
    document.getElementById("detail-rounds").textContent = comp.hiring_rounds || "Round 1: Online Assessment | Round 2: Technical Interview | Round 3: HR";
    document.getElementById("detail-aptitude").textContent = comp.aptitude_pattern || "Quantitative, Logical, and Verbal reasoning tests.";
    document.getElementById("detail-coding").textContent = comp.coding_pattern || "Algorithmic data structures and string/array problems.";
    document.getElementById("detail-technical").textContent = comp.technical_focus || "Core OOPs, DBMS, SQL, and Capstone Project Architecture.";

    // Module Snippet Badges
    document.getElementById("mod-apt-pattern").textContent = comp.aptitude_pattern ? comp.aptitude_pattern.split("[")[0].slice(0, 75) + "..." : "Quantitative & Logical";
    document.getElementById("mod-code-pattern").textContent = comp.coding_pattern ? comp.coding_pattern.slice(0, 75) + "..." : "2 Algorithmic challenges";
    document.getElementById("mod-tech-pattern").textContent = comp.technical_focus ? comp.technical_focus.slice(0, 75) + "..." : "Core CS & OOP";
    document.getElementById("mod-hr-pattern").textContent = comp.hr_tips ? comp.hr_tips.slice(0, 75) + "..." : "STAR Behavioral framing";

    // Populate role selector from company common roles or database job_roles
    const roleSelect = document.getElementById("role-select");
    const roles = (comp.job_roles && comp.job_roles.length)
      ? comp.job_roles.map(r => r.role_name)
      : (comp.common_roles ? comp.common_roles.split(",").map(r => r.trim()) : [
          "Software Developer", "Java Developer", "Python Developer",
          "Web Developer", "Data Analyst", "Software Engineer", "QA Tester"
        ]);

    roleSelect.innerHTML = roles.map(r => `<option value="${escapeHtml(r)}">${escapeHtml(r)}</option>`).join("");
    
    if (roles.includes(currentRole)) {
      roleSelect.value = currentRole;
    } else {
      currentRole = roles[0];
      roleSelect.value = currentRole;
    }

    const btnSaveRole = document.getElementById("btn-save-role");
    if (btnSaveRole) {
      btnSaveRole.onclick = async () => {
        currentRole = roleSelect.value;
        await setSelectedCompany(comp.slug, comp.company_name, currentRole);
        showToast(`Target role updated to: ${currentRole}`, "success");
        await loadCompanyProgress(comp.slug);
        await loadCompanyQuestions(comp.slug, currentRole, activeTrackModule);
      };
    }
  }

  async function loadCompanyProgress(slug) {
    try {
      const res = await fetch(`${API_BASE}/api/companies/${slug}/progress?employee_id=${employee.id}`);
      if (res.ok) {
        const data = await res.json();
        if (data.success && data.preparation) {
          const prep = data.preparation;
          const overall = prep.progress || 0.0;
          const apt = prep.aptitude_progress || 0.0;
          const cod = prep.coding_progress || 0.0;
          const tech = prep.technical_progress || 0.0;
          const intv = prep.interview_progress || 0.0;
          const hr = prep.hr_progress || 0.0;
          const resProg = prep.resume_progress || 0.0;
          const sk = prep.skills_progress || 0.0;
          const rd = prep.roadmap_progress || 0.0;

          const hPct = document.getElementById("hero-progress-pct");
          if (hPct) hPct.textContent = `${Math.round(overall)}%`;
          const hStat = document.getElementById("hero-progress-status");
          if (hStat) hStat.textContent = overall >= 90 ? "Job Ready 🚀" : (overall > 0 ? "In Progress ⚡" : "Not Attempted");

          const pApt = document.getElementById("prog-aptitude");
          if (pApt) pApt.textContent = `${Math.round(apt)}%`;
          const pCod = document.getElementById("prog-coding");
          if (pCod) pCod.textContent = `${Math.round(cod)}%`;
          const pTech = document.getElementById("prog-technical");
          if (pTech) pTech.textContent = `${Math.round(tech)}%`;
          const pIntv = document.getElementById("prog-interview");
          if (pIntv) pIntv.textContent = `${Math.round(intv)}%`;
          const pHr = document.getElementById("prog-hr");
          if (pHr) pHr.textContent = `${Math.round(hr)}%`;

          // Fill progress bars
          if (document.getElementById("fill-apt")) document.getElementById("fill-apt").style.width = `${apt}%`;
          if (document.getElementById("fill-coding")) document.getElementById("fill-coding").style.width = `${cod}%`;
          if (document.getElementById("fill-technical")) document.getElementById("fill-technical").style.width = `${tech}%`;
          if (document.getElementById("fill-interview")) document.getElementById("fill-interview").style.width = `${intv}%`;
          if (document.getElementById("fill-hr")) document.getElementById("fill-hr").style.width = `${hr}%`;
          if (document.getElementById("fill-resume")) document.getElementById("fill-resume").style.width = `${resProg}%`;
          if (document.getElementById("fill-skills")) document.getElementById("fill-skills").style.width = `${sk}%`;
          if (document.getElementById("fill-roadmap")) document.getElementById("fill-roadmap").style.width = `${rd}%`;
        }
      }
    } catch (e) {
      console.error("Error loading progress:", e);
    }
  }

  function setupModuleButtons() {
    const roleParam = () => encodeURIComponent(document.getElementById("role-select") ? document.getElementById("role-select").value : currentRole);
    const slugParam = () => encodeURIComponent(companySlug || "tcs");

    function bind(id, urlGenerator) {
      const btn = document.getElementById(id);
      if (btn) {
        btn.onclick = (e) => {
          e.preventDefault();
          window.location.href = urlGenerator();
        };
      }
    }

    // 1. Aptitude Test Button
    bind("btn-start-aptitude", () => `aptitude.html?company=${slugParam()}&role=${roleParam()}`);

    // 2. Coding Practice Button
    bind("btn-start-coding", () => `preparation.html?company=${slugParam()}&role=${roleParam()}&mode=coding`);

    // 3. Technical Questions Button
    bind("btn-start-technical", () => `preparation.html?company=${slugParam()}&role=${roleParam()}&mode=technical`);

    // 4. HR Interview Button
    bind("btn-start-hr", () => `interview.html?company=${slugParam()}&role=${roleParam()}&type=hr`);

    // 5. AI Mock Interview Button
    bind("btn-start-interview", () => `interview.html?company=${slugParam()}&role=${roleParam()}&type=mock`);

    // 6. Resume Preparation Button
    bind("btn-prepare-resume", () => `resume.html?company=${slugParam()}&role=${roleParam()}`);

    // 7. Skill Assessment Button
    bind("btn-assess-skills", () => `skills.html?company=${slugParam()}&role=${roleParam()}`);

    // 8. Learning Roadmap Button
    bind("btn-view-roadmap", () => `roadmap.html?company=${slugParam()}&role=${roleParam()}`);

    // 9. Launch Full Timed Test Button
    bind("btn-launch-full-test", () => `aptitude.html?company=${slugParam()}&role=${roleParam()}`);

    // 10. Refresh / Change Company Questions Button
    const btnRefreshMCQs = document.getElementById("btn-refresh-company-mcqs");
    if (btnRefreshMCQs) {
      btnRefreshMCQs.onclick = async (e) => {
        e.preventDefault();
        btnRefreshMCQs.disabled = true;
        btnRefreshMCQs.innerHTML = "<span>🔄 Shuffling...</span>";
        await loadCompanyQuestions(slugParam(), roleParam(), activeTrackModule);
        btnRefreshMCQs.disabled = false;
        btnRefreshMCQs.innerHTML = "<span>🔄 Change / New Questions</span>";
        showToast(`Fresh ${activeTrackModule.toUpperCase()} questions loaded for ${currentCompany ? currentCompany.company_name : 'company'}! 🎯`, "success");
      };
    }

    // 11. Company Question Category Tabs (Aptitude, Technical, Coding, HR)
    const trackBtns = document.querySelectorAll(".comp-track-btn");
    trackBtns.forEach(btn => {
      btn.onclick = async (e) => {
        e.preventDefault();
        trackBtns.forEach(b => {
          b.className = "btn btn-secondary btn-sm comp-track-btn";
        });
        btn.className = "btn btn-primary btn-sm comp-track-btn";
        activeTrackModule = btn.dataset.module || "aptitude";
        await loadCompanyQuestions(slugParam(), roleParam(), activeTrackModule);
      };
    });
  }

  const loadCompanySampleMCQs = loadCompanyQuestions;

  /**
   * Load and render Company Questions for any selected track:
   * - aptitude: Quantitative & Reasoning MCQs (stacked A, B, C, D)
   * - technical: Core CS & Domain MCQs
   * - coding: Company-Specific Coding Challenges
   * - hr: Company Behavioral & Leadership Principles
   */
  async function loadCompanyQuestions(slug, role, moduleName = "aptitude") {
    const listEl = document.getElementById("company-mcqs-list");
    const targetNameEl = document.getElementById("company-mcq-target-name");
    if (!listEl) return;

    if (targetNameEl && currentCompany) {
      targetNameEl.textContent = currentCompany.company_name;
    }

    listEl.innerHTML = `
      <div style="text-align: center; padding: 28px; color: var(--text-muted);">
        <div style="font-size: 1.8rem; margin-bottom: 8px;">⏳</div>
        Loading ${escapeHtml(moduleName.toUpperCase())} questions for ${currentCompany ? currentCompany.company_name : slug}...
      </div>
    `;

    try {
      const res = await fetch(`${API_BASE}/api/companies/${slug}/modules/${moduleName}?role=${encodeURIComponent(role)}&_t=${Date.now()}`);
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

      // CASE 1: CODING PROBLEMS
      if (moduleName === "coding") {
        questions.forEach((p, pIdx) => {
          const pCard = document.createElement("div");
          pCard.className = "card";
          pCard.style.cssText = "border: 1px solid var(--border-color); background: var(--bg-card); padding: 22px; border-radius: var(--radius-lg); box-shadow: var(--shadow-sm);";

          pCard.innerHTML = `
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; flex-wrap: wrap; gap: 8px;">
              <div style="display: flex; gap: 8px; align-items: center;">
                <span class="badge badge-purple">${escapeHtml(p.category || "Algorithms")}</span>
                <span class="badge ${p.difficulty === 'Easy' ? 'badge-success' : (p.difficulty === 'Medium' ? 'badge-warning' : 'badge-primary')}">
                  ${escapeHtml(p.difficulty || "Medium")}
                </span>
              </div>
              <span style="font-size: 0.8rem; color: var(--text-muted);">🏢 Asked in ${escapeHtml(currentCompany ? currentCompany.company_name : slug)}</span>
            </div>

            <h4 style="font-size: 1.15rem; margin-bottom: 8px; color: var(--text-main);">
              ${pIdx + 1}. ${escapeHtml(p.title)}
            </h4>
            <p style="font-size: 0.9rem; color: var(--text-muted); line-height: 1.5; margin-bottom: 16px;">
              ${escapeHtml(p.description || "")}
            </p>

            <div style="display: flex; justify-content: flex-end;">
              <a href="preparation.html?company=${encodeURIComponent(slug)}&problem=${encodeURIComponent(p.id)}&mode=coding" class="btn btn-primary btn-sm" style="display: inline-flex; align-items: center; gap: 6px;">
                <span>Solve in Coding Workspace 💻</span>
              </a>
            </div>
          `;
          listEl.appendChild(pCard);
        });
        return;
      }

      // CASE 2: HR / BEHAVIORAL QUESTIONS
      if (moduleName === "hr") {
        questions.forEach((q, qIdx) => {
          const hCard = document.createElement("div");
          hCard.className = "card";
          hCard.style.cssText = "border: 1px solid var(--border-color); background: var(--bg-card); padding: 22px; border-radius: var(--radius-lg); box-shadow: var(--shadow-sm);";

          hCard.innerHTML = `
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
              <span class="badge badge-purple">${escapeHtml(q.category || "Behavioral")}</span>
              <span class="badge badge-info">Round: HR & Culture</span>
            </div>

            <h4 style="font-size: 1.12rem; margin-bottom: 14px; line-height: 1.5; color: var(--text-main);">
              ${qIdx + 1}. ${escapeHtml(q.question)}
            </h4>

            <div style="background: #f8fafc; border: 1px solid var(--border-color); border-left: 4px solid var(--primary-600); border-radius: 8px; padding: 14px 18px; font-size: 0.88rem; color: var(--text-muted); line-height: 1.5;">
              <strong style="color: var(--primary-800); display: block; margin-bottom: 4px;">💡 Interview Strategy & Key Focus:</strong>
              ${escapeHtml(q.tips || q.guidance || "Focus on structured communication using the STAR technique.")}
            </div>
          `;
          listEl.appendChild(hCard);
        });
        return;
      }

      // CASE 3: APTITUDE OR TECHNICAL MCQs (Options stacked vertically A, B, C, D)
      const letters = ["A", "B", "C", "D", "E"];

      questions.forEach((q, qIdx) => {
        const qCard = document.createElement("div");
        qCard.className = "card";
        qCard.style.cssText = "border: 1px solid var(--border-color); background: var(--bg-card); padding: 22px; border-radius: var(--radius-lg); box-shadow: var(--shadow-sm);";

        const optionsHtml = (q.options || []).map((opt, oIdx) => `
          <button type="button" class="option-btn" id="comp-q-${qIdx}-opt-${oIdx}" data-qidx="${qIdx}" data-oidx="${oIdx}">
            <span class="option-letter">${letters[oIdx]}</span>
            <span class="option-label">${escapeHtml(opt)}</span>
          </button>
        `).join("");

        qCard.innerHTML = `
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
            <span class="badge badge-purple" style="font-size: 0.8rem; font-weight: 600;">${escapeHtml(q.category || (moduleName === 'technical' ? 'Technical' : 'Aptitude'))}</span>
            <span class="badge ${q.difficulty === 'Easy' ? 'badge-success' : (q.difficulty === 'Medium' ? 'badge-warning' : 'badge-primary')}" style="font-size: 0.8rem;">
              ${escapeHtml(q.difficulty || "Medium")}
            </span>
          </div>

          <h4 style="font-size: 1.08rem; margin-bottom: 16px; line-height: 1.5; color: var(--text-main);">
            ${qIdx + 1}. ${escapeHtml(q.question)}
          </h4>

          <!-- Vertical stack: Option A on line 1, Option B on line 2, Option C on line 3, Option D on line 4 -->
          <div class="options-container" style="display: flex; flex-direction: column; gap: 12px; width: 100%; margin-bottom: 14px;">
            ${optionsHtml}
          </div>

          <div id="comp-exp-${qIdx}" style="display: none; background: #f0fdf4; border: 1px solid #bbf7d0; border-left: 4px solid #10b981; border-radius: 8px; padding: 12px 16px; font-size: 0.88rem; color: #166534; margin-top: 12px;">
            <strong>💡 Explanation:</strong> ${escapeHtml(q.explanation || "Standard logic applied.")}
          </div>
        `;

        listEl.appendChild(qCard);

        // Bind click events for immediate feedback
        (q.options || []).forEach((_, oIdx) => {
          const btn = qCard.querySelector(`#comp-q-${qIdx}-opt-${oIdx}`);
          if (btn) {
            btn.addEventListener("click", () => {
              const isCorrect = (oIdx === q.correctIndex);
              const expDiv = qCard.querySelector(`#comp-exp-${qIdx}`);

              (q.options || []).forEach((_, resetIdx) => {
                const sib = qCard.querySelector(`#comp-q-${qIdx}-opt-${resetIdx}`);
                if (sib) {
                  sib.classList.remove("selected", "correct", "incorrect");
                }
              });

              if (isCorrect) {
                btn.classList.add("correct");
                showToast("Correct Answer! 🎉", "success");
              } else {
                btn.classList.add("incorrect");
                const correctBtn = qCard.querySelector(`#comp-q-${qIdx}-opt-${q.correctIndex}`);
                if (correctBtn) correctBtn.classList.add("correct");
                showToast("Incorrect option. Check explanation below.", "error");
              }

              if (expDiv) expDiv.style.display = "block";
            });
          }
        });
      });

    } catch (err) {
      console.error("Error loading company questions:", err);
      listEl.innerHTML = `<div style="color: var(--text-muted); padding: 12px;">Could not load questions.</div>`;
    }
  }

  // Alias for backward compatibility
  const loadCompanySampleMCQs = loadCompanyQuestions;

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
