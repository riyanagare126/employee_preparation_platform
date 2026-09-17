/**
 * Top 20 Companies Preparation Portal Logic
 */

document.addEventListener("DOMContentLoaded", () => {
  const employee = getLoggedInEmployee();
  if (!employee) return;

  let allCompanies = [];
  let currentSelectedCompany = null;

  const grid = document.getElementById("companies-grid");
  const searchInput = document.getElementById("company-search");
  const categoryFilter = document.getElementById("filter-category");
  const difficultyFilter = document.getElementById("filter-difficulty");

  const modal = document.getElementById("company-modal");
  const btnCloseModal = document.getElementById("btn-close-modal");
  const roleSelect = document.getElementById("modal-role-select");

  const compareModal = document.getElementById("compare-modal");
  const btnOpenCompare = document.getElementById("btn-open-compare");
  const btnCloseCompare = document.getElementById("btn-close-compare");
  const compareSelect1 = document.getElementById("compare-select-1");
  const compareSelect2 = document.getElementById("compare-select-2");
  const compareTableContainer = document.getElementById("compare-table-container");

  // Load companies on startup
  fetchCompanies();

  // Search & Filter listeners
  searchInput.addEventListener("input", filterAndRenderCompanies);
  categoryFilter.addEventListener("change", filterAndRenderCompanies);
  difficultyFilter.addEventListener("change", filterAndRenderCompanies);

  // Close modals
  if (btnCloseModal) btnCloseModal.addEventListener("click", () => modal.style.display = "none");
  if (modal) {
    modal.addEventListener("click", (e) => {
      if (e.target === modal) modal.style.display = "none";
    });
  }

  if (btnOpenCompare) btnOpenCompare.addEventListener("click", openCompareModal);
  if (btnCloseCompare) btnCloseCompare.addEventListener("click", () => compareModal.style.display = "none");
  if (compareModal) {
    compareModal.addEventListener("click", (e) => {
      if (e.target === compareModal) compareModal.style.display = "none";
    });
  }

  if (compareSelect1) compareSelect1.addEventListener("change", executeComparison);
  if (compareSelect2) compareSelect2.addEventListener("change", executeComparison);

  // Role select change inside company hub modal
  if (roleSelect) {
    roleSelect.addEventListener("change", () => {
      if (currentSelectedCompany) {
        loadCompanyRecommendations(currentSelectedCompany.slug, roleSelect.value);
      }
    });
  }

  async function fetchCompanies() {
    try {
      const res = await fetch(`${API_BASE}/api/companies`);
      const data = await res.json();
      if (data.success && data.companies) {
        allCompanies = data.companies;
        renderCompanyCards(allCompanies);
      }
    } catch (err) {
      grid.innerHTML = `<div class="card" style="grid-column: 1/-1; text-align: center; color: var(--danger-color);">Failed to load company preparation catalog.</div>`;
    }
  }

  function filterAndRenderCompanies() {
    const q = searchInput.value.toLowerCase().trim();
    const cat = categoryFilter.value;
    const diff = difficultyFilter.value;

    const filtered = allCompanies.filter(c => {
      const matchSearch = !q || c.company_name.toLowerCase().includes(q) ||
        (c.description && c.description.toLowerCase().includes(q)) ||
        (c.recommended_skills && c.recommended_skills.toLowerCase().includes(q)) ||
        (c.common_roles && c.common_roles.toLowerCase().includes(q));

      const matchCat = cat === "All" || (c.category && c.category.includes(cat));
      const matchDiff = diff === "All" || (c.difficulty && c.difficulty.includes(diff));

      return matchSearch && matchCat && matchDiff;
    });

    renderCompanyCards(filtered);
  }

  function renderCompanyCards(companies) {
    if (!companies || companies.length === 0) {
      grid.innerHTML = `<div class="card" style="grid-column: 1/-1; text-align: center; padding: 40px; color: var(--text-muted);">
        <p style="font-size: 1.1rem; margin-bottom: 8px;">🔍 No companies found matching your filter criteria.</p>
        <button class="btn btn-secondary btn-sm" onclick="document.getElementById('company-search').value=''; document.getElementById('filter-category').value='All'; document.getElementById('filter-difficulty').value='All'; window.location.reload();">Reset Filters</button>
      </div>`;
      return;
    }

    grid.innerHTML = companies.map(c => {
      const roles = c.common_roles ? c.common_roles.split(",").slice(0, 3).map(r => `<span class="badge" style="font-size: 0.75rem; background: var(--bg-subtle); color: var(--text-main);">${escapeHtml(r.trim())}</span>`).join(" ") : "";
      const skills = (c.recommended_skills || "").split(",").slice(0, 3).map(s => `<span class="badge" style="font-size: 0.7rem; background: #e0f2fe; color: #0369a1;">${escapeHtml(s.trim())}</span>`).join(" ");

      return `
        <div class="card" style="display: flex; flex-direction: column; justify-content: space-between; transition: transform 0.2s, box-shadow 0.2s; border: 1px solid var(--border-color);" onmouseover="this.style.transform='translateY(-3px)'; this.style.boxShadow='var(--shadow-md)'" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='var(--shadow-sm)'">
          <div>
            <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px;">
              <span style="font-size: 2.2rem;">${c.logo_emoji || '🏢'}</span>
              <span class="badge ${c.difficulty.includes('Hard') ? 'badge-danger' : (c.difficulty.includes('Medium') ? 'badge-warning' : 'badge-primary')}" style="font-size: 0.75rem;">
                ${escapeHtml(c.difficulty)}
              </span>
            </div>

            <h3 style="font-size: 1.15rem; color: var(--text-main); margin-bottom: 4px;">${escapeHtml(c.company_name)}</h3>
            <span style="font-size: 0.8rem; color: var(--text-muted); display: block; margin-bottom: 10px;">${escapeHtml(c.category || 'Technology')}</span>

            <p style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 14px; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;">
              ${escapeHtml(c.description || 'Comprehensive placement syllabus and round-by-round preparation roadmap.')}
            </p>

            <div style="margin-bottom: 12px;">
              <div style="display: flex; flex-wrap: wrap; gap: 4px;">${roles}</div>
            </div>

            <div style="margin-bottom: 16px;">
              <span style="font-size: 0.75rem; color: var(--text-muted); font-weight: 600;">Key Skills:</span>
              <div style="display: flex; flex-wrap: wrap; gap: 4px; margin-top: 4px;">${skills}</div>
            </div>
          </div>

          <div style="display: flex; gap: 8px;">
            <button class="btn btn-secondary btn-sm" onclick="window.previewCompany('${c.slug}')" style="flex: 1;">
              Overview ℹ
            </button>
            <button class="btn btn-primary" onclick="window.startCompanyPrep('${c.slug}', '${escapeHtml(c.company_name)}')" style="flex: 2; display: flex; justify-content: center; align-items: center; gap: 6px;">
              <span>Start Preparation</span>
              <span>→</span>
            </button>
          </div>
        </div>
      `;
    }).join("");
  }

  window.startCompanyPrep = async function(slug, name) {
    await setSelectedCompany(slug, name, employee.target_role || employee.job_role || "Java Developer");
    window.location.href = `company-prep.html?company=${encodeURIComponent(slug)}`;
  };

  window.previewCompany = function(slug) {
    const comp = allCompanies.find(c => c.slug === slug);
    if (!comp) return;

    currentSelectedCompany = comp;

    document.getElementById("modal-company-emoji").innerText = comp.logo_emoji || "🏢";
    document.getElementById("modal-company-name").innerText = comp.company_name;
    document.getElementById("modal-company-diff").innerText = comp.difficulty;
    document.getElementById("modal-company-cat").innerText = comp.category || "IT Services";

    // Populate role select
    if (comp.common_roles) {
      const roles = comp.common_roles.split(",").map(r => r.trim());
      roleSelect.innerHTML = roles.map(r => `<option value="${escapeHtml(r)}">${escapeHtml(r)}</option>`).join("");
      if (employee.job_role && roles.includes(employee.job_role)) {
        roleSelect.value = employee.job_role;
      }
    }

    // Populate roadmap steps
    const roadmapContainer = document.getElementById("modal-roadmap-steps");
    const steps = comp.roadmap && comp.roadmap.length ? comp.roadmap : ["Aptitude", "Coding Round", "Technical Interview", "HR Interview", "Mock Interview"];
    roadmapContainer.innerHTML = steps.map((s, idx) => `
      <div style="background: var(--card-bg); border: 1px solid var(--border-color); border-radius: 6px; padding: 8px 12px; font-size: 0.8rem; font-weight: 600; white-space: nowrap; display: flex; align-items: center; gap: 6px;">
        <span style="background: var(--primary-500); color: #fff; width: 18px; height: 18px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; font-size: 0.65rem;">${idx + 1}</span>
        <span>${escapeHtml(s)}</span>
      </div>
    `).join("");

    // Populate breakdown
    document.getElementById("modal-rounds").innerText = comp.hiring_rounds || "Online Test → Technical Round → HR Round";
    document.getElementById("modal-aptitude").innerText = comp.aptitude_pattern || "Quantitative, Logical Reasoning, and Verbal Ability.";
    document.getElementById("modal-coding").innerText = comp.coding_pattern || "2 Algorithmic Coding Challenges.";
    document.getElementById("modal-technical").innerText = comp.technical_focus || "Core OOPs, DBMS, SQL, and Capstone Project.";
    document.getElementById("modal-hr").innerText = comp.hr_tips || "Highlight project contributions, adaptability, and clear communication.";

    const skillsCont = document.getElementById("modal-skills");
    const skillsList = (comp.recommended_skills || "").split(",").filter(Boolean);
    skillsCont.innerHTML = skillsList.map(s => `<span class="badge badge-primary">${escapeHtml(s.trim())}</span>`).join(" ");

    // Link modal start prep button to full hub
    const modalPrepBtn = document.getElementById("modal-btn-start-hub");
    if (modalPrepBtn) {
      modalPrepBtn.onclick = () => window.startCompanyPrep(slug, comp.company_name);
    }

    // Fetch AI recommendations
    loadCompanyRecommendations(slug, roleSelect.value);

    modal.style.display = "flex";
  };

  async function loadCompanyRecommendations(slug, role) {
    const strongCont = document.getElementById("modal-strong-skills");
    const missingCont = document.getElementById("modal-missing-skills");
    const actionsCont = document.getElementById("modal-ai-actions");

    if (!strongCont || !missingCont) return;

    strongCont.innerText = "Analyzing candidate profile...";
    missingCont.innerText = "Scanning placement benchmarks...";
    if (actionsCont) actionsCont.innerHTML = "";

    try {
      const res = await fetch(`${API_BASE}/api/companies/${slug}/recommendations?employee_id=${employee.id}&role=${encodeURIComponent(role)}`);
      const data = await res.json();
      if (data.success) {
        strongCont.innerHTML = (data.strong_skills || ["Core Programming"]).map(s => `<span class="badge" style="background: #dcfce7; color: #166534; margin: 2px;">✔ ${escapeHtml(s)}</span>`).join(" ");
        missingCont.innerHTML = (data.needs_improvement || ["Advanced Algorithms"]).map(s => `<span class="badge" style="background: #fee2e2; color: #991b1b; margin: 2px;">▲ ${escapeHtml(s)}</span>`).join(" ");

        if (actionsCont && data.recommendations && data.recommendations.length) {
          actionsCont.innerHTML = `
            <div style="margin-top: 8px; border-top: 1px dashed #86efac; padding-top: 8px;">
              <strong style="color: #166534; font-size: 0.8rem;">Recommended Action Items:</strong>
              <ul style="margin: 4px 0 0 16px; padding: 0; font-size: 0.8rem;">
                ${data.recommendations.map(r => `<li>${escapeHtml(r)}</li>`).join("")}
              </ul>
            </div>
          `;
        }
      }
    } catch (err) {
      strongCont.innerText = "Problem Solving, Core CS";
      missingCont.innerText = "System Design, Microservices";
    }
  }

  function openCompareModal() {
    if (!allCompanies || allCompanies.length < 2) return;

    compareSelect1.innerHTML = allCompanies.map(c => `<option value="${c.slug}">${c.logo_emoji || '🏢'} ${escapeHtml(c.company_name)}</option>`).join("");
    compareSelect2.innerHTML = allCompanies.map(c => `<option value="${c.slug}">${c.logo_emoji || '🏢'} ${escapeHtml(c.company_name)}</option>`).join("");

    compareSelect1.value = allCompanies[0].slug;
    compareSelect2.value = allCompanies[1].slug;

    executeComparison();
    compareModal.style.display = "flex";
  }

  async function executeComparison() {
    const slug1 = compareSelect1.value;
    const slug2 = compareSelect2.value;

    if (!slug1 || !slug2) return;

    compareTableContainer.innerHTML = `<div style="text-align: center; padding: 20px; color: var(--text-muted);">Comparing company benchmarks...</div>`;

    try {
      const res = await fetch(`${API_BASE}/api/companies/compare`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ slug1, slug2 })
      });
      const data = await res.json();
      if (data.success) {
        const c1 = data.company_1;
        const c2 = data.company_2;

        compareTableContainer.innerHTML = `
          <table style="width: 100%; border-collapse: collapse; font-size: 0.88rem; margin-top: 10px;">
            <thead>
              <tr style="background: var(--bg-subtle); border-bottom: 2px solid var(--border-color); text-align: left;">
                <th style="padding: 10px; width: 22%;">Benchmark Metric</th>
                <th style="padding: 10px; width: 39%; color: var(--primary-700);">${c1.logo_emoji || '🏢'} ${escapeHtml(c1.company_name)}</th>
                <th style="padding: 10px; width: 39%; color: #0369a1;">${c2.logo_emoji || '🏢'} ${escapeHtml(c2.company_name)}</th>
              </tr>
            </thead>
            <tbody>
              <tr style="border-bottom: 1px solid var(--border-color);">
                <td style="padding: 10px; font-weight: 600;">Difficulty Rating</td>
                <td style="padding: 10px;"><span class="badge badge-primary">${escapeHtml(c1.difficulty)}</span></td>
                <td style="padding: 10px;"><span class="badge badge-primary">${escapeHtml(c2.difficulty)}</span></td>
              </tr>
              <tr style="border-bottom: 1px solid var(--border-color);">
                <td style="padding: 10px; font-weight: 600;">Industry Category</td>
                <td style="padding: 10px;">${escapeHtml(c1.category || 'Technology')}</td>
                <td style="padding: 10px;">${escapeHtml(c2.category || 'Technology')}</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--border-color);">
                <td style="padding: 10px; font-weight: 600;">Hiring Rounds</td>
                <td style="padding: 10px; font-size: 0.82rem;">${escapeHtml(c1.hiring_rounds)}</td>
                <td style="padding: 10px; font-size: 0.82rem;">${escapeHtml(c2.hiring_rounds)}</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--border-color);">
                <td style="padding: 10px; font-weight: 600;">Aptitude Pattern</td>
                <td style="padding: 10px; font-size: 0.82rem;">${escapeHtml(c1.aptitude_pattern)}</td>
                <td style="padding: 10px; font-size: 0.82rem;">${escapeHtml(c2.aptitude_pattern)}</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--border-color);">
                <td style="padding: 10px; font-weight: 600;">Coding Focus</td>
                <td style="padding: 10px; font-size: 0.82rem;">${escapeHtml(c1.coding_pattern)}</td>
                <td style="padding: 10px; font-size: 0.82rem;">${escapeHtml(c2.coding_pattern)}</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--border-color);">
                <td style="padding: 10px; font-weight: 600;">Technical Focus</td>
                <td style="padding: 10px; font-size: 0.82rem;">${escapeHtml(c1.technical_focus)}</td>
                <td style="padding: 10px; font-size: 0.82rem;">${escapeHtml(c2.technical_focus)}</td>
              </tr>
            </tbody>
          </table>
        `;
      }
    } catch (err) {
      compareTableContainer.innerHTML = `<div style="color: var(--danger-color); padding: 10px;">Failed to execute comparison.</div>`;
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
