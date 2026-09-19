/**
 * AI Employee Preparation Platform - Admin Dashboard Controller
 */

document.addEventListener("DOMContentLoaded", async () => {
  const employee = requireAuth();
  if (!employee) return;

  // Basic admin check (if candidate is not admin, warn or allow preview)
  const isSuperAdmin = employee.is_admin || employee.email.includes("admin");

  // Tab Elements
  const tabUsersBtn = document.getElementById("tab-users-btn");
  const tabCompaniesBtn = document.getElementById("tab-companies-btn");
  const tabRolesBtn = document.getElementById("tab-roles-btn");
  const tabQuestionsBtn = document.getElementById("tab-questions-btn");
  const tabTrendsBtn = document.getElementById("tab-trends-btn");
  const tabTemplatesBtn = document.getElementById("tab-templates-btn");
  const tabFluencyBtn = document.getElementById("tab-fluency-btn");

  const viewUsers = document.getElementById("admin-users-view");
  const viewCompanies = document.getElementById("admin-companies-view");
  const viewRoles = document.getElementById("admin-roles-view");
  const viewQuestions = document.getElementById("admin-questions-view");
  const viewTrends = document.getElementById("admin-trends-view");
  const viewTemplates = document.getElementById("admin-templates-view");
  const viewFluency = document.getElementById("admin-fluency-view");

  const btnRefresh = document.getElementById("btn-refresh-admin");

  // Setup tabs
  function activateTab(btn, view) {
    [tabUsersBtn, tabCompaniesBtn, tabRolesBtn, tabQuestionsBtn, tabTrendsBtn, tabTemplatesBtn, tabFluencyBtn].forEach(b => {
      if (b) {
        b.className = "btn btn-secondary btn-sm";
        b.style.border = "none";
      }
    });
    [viewUsers, viewCompanies, viewRoles, viewQuestions, viewTrends, viewTemplates, viewFluency].forEach(v => {
      if (v) v.style.display = "none";
    });

    if (btn) btn.className = "btn btn-primary btn-sm";
    if (view) view.style.display = "block";
  }

  if (tabUsersBtn) tabUsersBtn.addEventListener("click", () => { activateTab(tabUsersBtn, viewUsers); loadUsers(); });
  if (tabCompaniesBtn) tabCompaniesBtn.addEventListener("click", () => { activateTab(tabCompaniesBtn, viewCompanies); loadCompanies(); });
  if (tabRolesBtn) tabRolesBtn.addEventListener("click", () => { activateTab(tabRolesBtn, viewRoles); loadRoles(); });
  if (tabQuestionsBtn) tabQuestionsBtn.addEventListener("click", () => { activateTab(tabQuestionsBtn, viewQuestions); populateCompanyDropdowns(); loadQuestions(); });
  if (tabTrendsBtn) tabTrendsBtn.addEventListener("click", () => { activateTab(tabTrendsBtn, viewTrends); loadTrends(); });
  if (tabTemplatesBtn) tabTemplatesBtn.addEventListener("click", () => { activateTab(tabTemplatesBtn, viewTemplates); loadTemplates(); });
  if (tabFluencyBtn) tabFluencyBtn.addEventListener("click", () => { activateTab(tabFluencyBtn, viewFluency); loadFluencyQuestions(); });

  if (btnRefresh) {
    btnRefresh.addEventListener("click", async () => {
      await loadAdminStats();
      await loadUsers();
      await populateCompanyDropdowns();
      showToast("Admin data refreshed!", "info");
    });
  }

  // Initial Load
  await loadAdminStats();
  await loadUsers();
  await populateCompanyDropdowns();
  setupCompanyModal();
  setupRoleModal();
  setupQuestionModal();
  setupTrendModal();
  setupTemplateModal();
  setupFluencyModal();

  async function loadAdminStats() {
    try {
      const res = await fetch(`${API_BASE}/api/admin/stats`);
      if (res.ok) {
        const data = await res.json();
        if (data.success && data.stats) {
          const s = data.stats;
          if (document.getElementById("stat-total-users")) document.getElementById("stat-total-users").textContent = s.total_users || 0;
          if (document.getElementById("stat-total-aptitude")) document.getElementById("stat-total-aptitude").textContent = s.total_aptitude_tests || 0;
          if (document.getElementById("stat-total-coding")) document.getElementById("stat-total-coding").textContent = s.total_coding_solved || 0;
          if (document.getElementById("stat-total-companies")) document.getElementById("stat-total-companies").textContent = s.total_companies || 20;
        }
      }
    } catch (e) {
      console.warn("Error fetching admin stats:", e);
    }
  }

  async function loadUsers() {
    const tbody = document.getElementById("admin-users-tbody");
    if (!tbody) return;
    tbody.innerHTML = `<tr><td colspan="6" style="padding: 20px; text-align: center; color: var(--text-muted);">Loading registered candidates...</td></tr>`;

    try {
      const res = await fetch(`${API_BASE}/api/admin/users`);
      if (res.ok) {
        const data = await res.json();
        if (data.success && data.users) {
          if (data.users.length === 0) {
            tbody.innerHTML = `<tr><td colspan="6" style="padding: 20px; text-align: center; color: var(--text-muted);">No candidates found.</td></tr>`;
            return;
          }

          tbody.innerHTML = data.users.map(u => `
            <tr style="border-bottom: 1px solid var(--border-color);">
              <td style="padding: 10px; font-weight: 600;">#${u.id}</td>
              <td style="padding: 10px; font-weight: 600; color: var(--text-main);">${escapeHtml(u.name)}</td>
              <td style="padding: 10px; color: var(--text-muted);">${escapeHtml(u.email)}</td>
              <td style="padding: 10px;">
                <span class="badge badge-primary">${escapeHtml(u.target_company || 'TCS')}</span>
                <span class="badge badge-purple">${escapeHtml(u.target_role || u.job_role || 'Software Engineer')}</span>
              </td>
              <td style="padding: 10px;">
                ${u.is_admin ? '<span class="badge badge-danger">Admin <i class="fa-solid fa-shield-halved"></i></span>' : '<span class="badge" style="background: var(--bg-subtle);">Candidate</span>'}
              </td>
              <td style="padding: 10px;">
                <button class="btn btn-secondary btn-sm" onclick="window.deleteCandidate(${u.id})" style="color: #ef4444; border-color: #fca5a5;">
                  Delete <i class="fa-solid fa-trash-can"></i>
                </button>
              </td>
            </tr>
          `).join("");
        }
      }
    } catch (e) {
      tbody.innerHTML = `<tr><td colspan="6" style="padding: 20px; text-align: center; color: var(--danger-color);">Failed to load candidates.</td></tr>`;
    }
  }

  window.deleteCandidate = async function(userId) {
    if (!confirm(`Are you sure you want to permanently delete candidate #${userId}?`)) return;
    try {
      const res = await fetch(`${API_BASE}/api/admin/user/${userId}`, { method: "DELETE" });
      const data = await res.json();
      if (data.success) {
        showToast("Candidate deleted successfully.", "success");
        await loadUsers();
        await loadAdminStats();
      } else {
        showToast(data.message || "Failed to delete candidate.", "error");
      }
    } catch (e) {
      showToast("Error connecting to server.", "error");
    }
  };

  async function loadCompanies() {
    const tbody = document.getElementById("admin-companies-tbody");
    if (!tbody) return;
    tbody.innerHTML = `<tr><td colspan="7" style="padding: 20px; text-align: center; color: var(--text-muted);">Loading company blueprints...</td></tr>`;

    try {
      const res = await fetch(`${API_BASE}/api/admin/companies`);
      if (res.ok) {
        const data = await res.json();
        if (data.success && data.companies) {
          tbody.innerHTML = data.companies.map(c => `
            <tr style="border-bottom: 1px solid var(--border-color);">
              <td style="padding: 10px; font-weight: 700; display: flex; align-items: center; gap: 8px;">
                <span><i class="fa-solid ${escapeHtml(c.logo || c.logo_emoji || 'fa-building')}"></i></span>
                <span>${escapeHtml(c.company_name || c.name)}</span>
              </td>
              <td style="padding: 10px; font-family: monospace; font-size: 0.8rem; color: var(--primary-700);">${escapeHtml(c.slug)}</td>
              <td style="padding: 10px;">${escapeHtml(c.category || c.industry || 'Technology')}</td>
              <td style="padding: 10px;"><span class="badge badge-warning">${escapeHtml(c.difficulty)}</span></td>
              <td style="padding: 10px; font-size: 0.8rem; max-width: 220px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">
                ${escapeHtml(c.common_roles || 'Software Developer, Java Developer, Python Developer')}
              </td>
              <td style="padding: 10px;">
                <span class="badge ${c.is_active !== 0 ? 'badge-success' : 'badge-danger'}" style="cursor: pointer;" onclick="window.toggleCompany('${c.slug}')" title="Click to toggle status">
                  ${c.is_active !== 0 ? 'Active' : 'Disabled'}
                </span>
              </td>
              <td style="padding: 10px; white-space: nowrap;">
                <button class="btn btn-secondary btn-sm" onclick="window.toggleCompany('${c.slug}')" title="${c.is_active !== 0 ? 'Disable' : 'Enable'}">
                  <i class="fa-solid ${c.is_active !== 0 ? 'fa-eye-slash' : 'fa-eye'}"></i>
                </button>
                <button class="btn btn-secondary btn-sm" onclick="window.editCompany('${c.slug}')">Edit <i class="fa-solid fa-pencil"></i></button>
                <button class="btn btn-secondary btn-sm" onclick="window.deleteCompany('${c.slug}')" style="color: #ef4444;">Delete <i class="fa-solid fa-trash-can"></i></button>
              </td>
            </tr>
          `).join("");
        }
      }
    } catch (e) {
      tbody.innerHTML = `<tr><td colspan="7" style="padding: 20px; text-align: center; color: var(--danger-color);">Failed to load companies.</td></tr>`;
    }
  }

  window.toggleCompany = async function(slug) {
    try {
      const res = await fetch(`${API_BASE}/api/admin/company/${slug}/toggle`, { method: "POST" });
      const data = await res.json();
      if (data.success) {
        showToast(data.message || `Company '${slug}' status updated.`, "success");
        await loadCompanies();
        await populateCompanyDropdowns();
      } else {
        showToast(data.message || "Failed to update company status.", "error");
      }
    } catch (e) {
      showToast("Error toggling company status.", "error");
    }
  };

  window.deleteCompany = async function(slug) {
    if (!confirm(`Are you sure you want to delete company blueprint '${slug}'?`)) return;
    try {
      const res = await fetch(`${API_BASE}/api/admin/company/${slug}`, { method: "DELETE" });
      const data = await res.json();
      if (data.success) {
        showToast(`Company '${slug}' deleted.`, "success");
        await loadCompanies();
        await loadAdminStats();
      } else {
        showToast(data.message || "Failed to delete company.", "error");
      }
    } catch (e) {
      showToast("Error communicating with server.", "error");
    }
  };

  function setupCompanyModal() {
    const modal = document.getElementById("company-modal");
    const btnAdd = document.getElementById("btn-add-company");
    const btnClose = document.getElementById("btn-close-company-modal");
    const btnCancel = document.getElementById("btn-cancel-comp");
    const form = document.getElementById("form-company");

    if (btnAdd) {
      btnAdd.addEventListener("click", () => {
        form.reset();
        document.getElementById("company-modal-title").textContent = "Add Company Blueprint";
        document.getElementById("comp-slug").readOnly = false;
        modal.style.display = "flex";
      });
    }

    const closeModal = () => modal.style.display = "none";
    if (btnClose) btnClose.addEventListener("click", closeModal);
    if (btnCancel) btnCancel.addEventListener("click", closeModal);

    if (form) {
      form.addEventListener("submit", async (e) => {
        e.preventDefault();
        const payload = {
          company_name: document.getElementById("comp-name").value.trim(),
          slug: document.getElementById("comp-slug").value.trim().toLowerCase(),
          logo_emoji: document.getElementById("comp-emoji").value.trim() || "fa-building",
          category: document.getElementById("comp-cat").value.trim() || "IT Services",
          difficulty: document.getElementById("comp-diff").value,
          description: document.getElementById("comp-desc").value.trim(),
          hiring_rounds: document.getElementById("comp-rounds").value.trim(),
          aptitude_pattern: document.getElementById("comp-apt").value.trim(),
          coding_pattern: document.getElementById("comp-code").value.trim(),
          technical_focus: document.getElementById("comp-tech").value.trim(),
          hr_tips: document.getElementById("comp-hr").value.trim(),
          common_roles: document.getElementById("comp-roles").value.trim(),
          recommended_skills: document.getElementById("comp-skills").value.trim()
        };

        try {
          const res = await fetch(`${API_BASE}/api/admin/companies`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
          });
          const data = await res.json();
          if (data.success) {
            showToast(`Company '${payload.company_name}' saved successfully!`, "success");
            closeModal();
            await loadCompanies();
            await loadAdminStats();
          } else {
            showToast(data.message || "Failed to save company.", "error");
          }
        } catch (err) {
          showToast("Error saving company blueprint.", "error");
        }
      });
    }
  }

  window.editCompany = async function(slug) {
    try {
      const res = await fetch(`${API_BASE}/api/admin/company/${slug}`);
      const data = await res.json();
      if (data.success && data.company) {
        const c = data.company;
        document.getElementById("comp-name").value = c.company_name || "";
        document.getElementById("comp-slug").value = c.slug || "";
        document.getElementById("comp-slug").readOnly = true;
        document.getElementById("comp-emoji").value = c.logo_emoji || "fa-building";
        document.getElementById("comp-cat").value = c.category || "IT Services";
        document.getElementById("comp-diff").value = c.difficulty || "Medium";
        document.getElementById("comp-desc").value = c.description || "";
        document.getElementById("comp-rounds").value = c.hiring_rounds || "";
        document.getElementById("comp-apt").value = c.aptitude_pattern || "";
        document.getElementById("comp-code").value = c.coding_pattern || "";
        document.getElementById("comp-tech").value = c.technical_focus || "";
        document.getElementById("comp-hr").value = c.hr_tips || "";
        document.getElementById("comp-roles").value = c.common_roles || "";
        document.getElementById("comp-skills").value = c.recommended_skills || "";

        document.getElementById("company-modal-title").textContent = `Edit Blueprint: ${c.company_name}`;
        document.getElementById("company-modal").style.display = "flex";
      }
    } catch (e) {
      showToast("Error loading company details.", "error");
    }
  };

  async function loadRoles() {
    const tbody = document.getElementById("admin-roles-tbody");
    if (!tbody) return;
    tbody.innerHTML = `<tr><td colspan="6" style="padding: 20px; text-align: center; color: var(--text-muted);">Loading job roles...</td></tr>`;

    try {
      const res = await fetch(`${API_BASE}/api/admin/roles?company_slug=all`);
      if (res.ok) {
        const data = await res.json();
        if (data.success && data.roles) {
          tbody.innerHTML = data.roles.map(r => `
            <tr style="border-bottom: 1px solid var(--border-color);">
              <td style="padding: 10px; font-weight: 600;">#${r.id}</td>
              <td style="padding: 10px; font-weight: 700; color: var(--primary-700);">${escapeHtml(r.role_name)}</td>
              <td style="padding: 10px;"><span class="badge badge-primary">${escapeHtml(r.company_slug)}</span></td>
              <td style="padding: 10px; font-size: 0.85rem;">${escapeHtml(r.description || 'Target engineering role')}</td>
              <td style="padding: 10px; font-size: 0.85rem; color: var(--text-muted);">${escapeHtml(r.skills_required || 'General')}</td>
              <td style="padding: 10px;">
                <button class="btn btn-secondary btn-sm" onclick="window.deleteRole(${r.id})" style="color: #ef4444;">Delete <i class="fa-solid fa-trash-can"></i></button>
              </td>
            </tr>
          `).join("");
        }
      }
    } catch (e) {
      tbody.innerHTML = `<tr><td colspan="6" style="padding: 20px; text-align: center; color: var(--danger-color);">Failed to load roles.</td></tr>`;
    }
  }

  window.deleteRole = async function(roleId) {
    if (!confirm(`Are you sure you want to delete job role #${roleId}?`)) return;
    try {
      const res = await fetch(`${API_BASE}/api/admin/role/${roleId}`, { method: "DELETE" });
      const data = await res.json();
      if (data.success) {
        showToast("Job role deleted.", "success");
        await loadRoles();
      } else {
        showToast(data.message || "Failed to delete role.", "error");
      }
    } catch (e) {
      showToast("Error connecting to server.", "error");
    }
  };

  function setupRoleModal() {
    const modal = document.getElementById("role-modal");
    const btnAdd = document.getElementById("btn-add-role");
    const btnClose = document.getElementById("btn-close-role-modal");
    const btnCancel = document.getElementById("btn-cancel-role");
    const form = document.getElementById("form-role");

    if (btnAdd) {
      btnAdd.addEventListener("click", () => {
        form.reset();
        modal.style.display = "flex";
      });
    }

    const closeModal = () => modal.style.display = "none";
    if (btnClose) btnClose.addEventListener("click", closeModal);
    if (btnCancel) btnCancel.addEventListener("click", closeModal);

    if (form) {
      form.addEventListener("submit", async (e) => {
        e.preventDefault();
        const payload = {
          role_name: document.getElementById("role-name-input").value.trim(),
          company_slug: document.getElementById("role-comp-slug").value.trim().toLowerCase(),
          description: document.getElementById("role-desc-input").value.trim(),
          skills_required: document.getElementById("role-skills-input").value.trim()
        };

        try {
          const res = await fetch(`${API_BASE}/api/admin/roles`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
          });
          const data = await res.json();
          if (data.success) {
            showToast(`Role '${payload.role_name}' added successfully!`, "success");
            closeModal();
            await loadRoles();
          } else {
            showToast(data.message || "Failed to add role.", "error");
          }
        } catch (err) {
          showToast("Error creating role.", "error");
        }
      });
    }
  }

  // ==========================================
  // COMPANY QUESTIONS CMS CONTROLLER (Task 3)
  // ==========================================

  let currentCompanyQuestions = [];
  let currentQuestionsPage = 1;
  const questionsLimit = 50;

  async function populateCompanyDropdowns() {
    try {
      const res = await fetch(`${API_BASE}/api/companies`);
      if (res.ok) {
        const data = await res.json();
        const companies = data.companies || [];

        // 1. Filter dropdown
        const filterSelect = document.getElementById("q-filter-company");
        if (filterSelect) {
          const prevVal = filterSelect.value || "all";
          filterSelect.innerHTML = `<option value="all">All Companies (${companies.length})</option>` +
            companies.map(c => `<option value="${escapeHtml(c.slug)}">${escapeHtml(c.company_name || c.name)}</option>`).join("");
          if ([...filterSelect.options].some(o => o.value === prevVal)) filterSelect.value = prevVal;
        }

        // 2. Modal company select
        const modalSelect = document.getElementById("cq-company-select");
        if (modalSelect) {
          modalSelect.innerHTML = companies.map(c => `<option value="${escapeHtml(c.slug)}">${escapeHtml(c.company_name || c.name)}</option>`).join("");
        }

        // 3. Import company select
        const importSelect = document.getElementById("import-company-select");
        if (importSelect) {
          importSelect.innerHTML = companies.map(c => `<option value="${escapeHtml(c.slug)}">${escapeHtml(c.company_name || c.name)}</option>`).join("");
        }
      }
    } catch (e) {
      console.warn("Error loading companies for dropdowns:", e);
    }
  }

  async function loadQuestions(page = 1) {
    const tbody = document.getElementById("admin-company-questions-tbody");
    const countLabel = document.getElementById("q-count-label");
    if (!tbody) return;

    currentQuestionsPage = page;
    const filterComp = document.getElementById("q-filter-company")?.value || "all";
    const filterCat = document.getElementById("q-filter-category")?.value || "all";
    const filterRole = document.getElementById("q-filter-role")?.value || "all";
    const filterSearch = document.getElementById("q-filter-search")?.value.trim() || "";

    tbody.innerHTML = `<tr><td colspan="7" style="padding: 24px; text-align: center; color: var(--text-muted);"><i class="fa-solid fa-spinner fa-spin"></i> Loading question bank...</td></tr>`;

    try {
      const params = new URLSearchParams({
        company_slug: filterComp,
        category: filterCat,
        role: filterRole,
        search: filterSearch,
        limit: questionsLimit,
        offset: (page - 1) * questionsLimit,
        active_only: "false"
      });

      const res = await fetch(`${API_BASE}/api/admin/company-questions?${params.toString()}`);
      if (res.ok) {
        const data = await res.json();
        if (data.success) {
          currentCompanyQuestions = data.questions || [];
          const total = data.total || 0;
          if (countLabel) {
            const start = total > 0 ? (page - 1) * questionsLimit + 1 : 0;
            const end = Math.min(page * questionsLimit, total);
            let pagerHtml = `Showing <strong>${start}-${end}</strong> of <strong>${total}</strong> questions`;
            if (total > questionsLimit) {
              const maxPage = Math.ceil(total / questionsLimit);
              pagerHtml += ` | Page ${page} of ${maxPage} <button class="btn btn-secondary btn-sm" onclick="window.prevQuestionsPage()" ${page <= 1 ? 'disabled' : ''}>&laquo; Prev</button> <button class="btn btn-secondary btn-sm" onclick="window.nextQuestionsPage()" ${page >= maxPage ? 'disabled' : ''}>Next &raquo;</button>`;
            }
            countLabel.innerHTML = pagerHtml;
          }

          if (currentCompanyQuestions.length === 0) {
            tbody.innerHTML = `<tr><td colspan="7" style="padding: 24px; text-align: center; color: var(--text-muted);">No questions match the current filters. Click '+ Add Question' or 'Bulk Import' to add questions.</td></tr>`;
            return;
          }

          const catBadges = {
            aptitude: "badge-primary",
            coding: "badge-purple",
            technical: "badge-warning",
            ai_interview: "badge-success",
            hr: "badge-info"
          };

          tbody.innerHTML = currentCompanyQuestions.map(q => {
            const catClass = catBadges[q.category] || "badge-secondary";
            const isAptitude = q.category === "aptitude";

            let detailsHtml = `<div style="font-weight: 600; color: var(--text-main); margin-bottom: 4px;">${escapeHtml(q.question)}</div>`;
            if (isAptitude && q.options && Array.isArray(q.options)) {
              detailsHtml += `<div style="font-size: 0.78rem; color: var(--text-muted); margin-bottom: 2px;">
                <strong>Options:</strong> ${q.options.map(o => escapeHtml(o)).join(" | ")}
              </div>`;
            }
            if (q.correct_answer) {
              detailsHtml += `<div style="font-size: 0.78rem; color: var(--success-color);">
                <strong>Correct:</strong> ${escapeHtml(q.correct_answer)}
              </div>`;
            }
            if (q.explanation) {
              detailsHtml += `<div style="font-size: 0.75rem; color: var(--text-muted); font-style: italic; max-width: 480px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">
                <strong>Guidance:</strong> ${escapeHtml(q.explanation)}
              </div>`;
            }

            return `
              <tr style="border-bottom: 1px solid var(--border-color);">
                <td style="padding: 10px; font-weight: 600;">#${q.id}</td>
                <td style="padding: 10px;">
                  <span class="badge ${catClass}">${escapeHtml((q.category || '').toUpperCase())}</span>
                  <div style="font-size: 0.72rem; color: var(--text-muted); margin-top: 2px;">
                    <i class="fa-solid fa-building"></i> ${escapeHtml((q.company_slug || '').toUpperCase())}
                  </div>
                </td>
                <td style="padding: 10px;">
                  <span class="badge" style="background: var(--bg-subtle); border: 1px solid var(--border-color); font-size: 0.78rem;">
                    ${escapeHtml(q.role || 'All')}
                  </span>
                </td>
                <td style="padding: 10px; max-width: 380px;">${detailsHtml}</td>
                <td style="padding: 10px;"><span class="badge badge-warning">${escapeHtml(q.difficulty || 'Medium')}</span></td>
                <td style="padding: 10px;">
                  <span class="badge ${q.is_active !== 0 ? 'badge-success' : 'badge-danger'}" style="cursor: pointer;" onclick="window.toggleCompanyQuestion(${q.id})" title="Click to toggle status">
                    ${q.is_active !== 0 ? 'Active' : 'Disabled'}
                  </span>
                </td>
                <td style="padding: 10px; white-space: nowrap;">
                  <button class="btn btn-secondary btn-sm" onclick="window.toggleCompanyQuestion(${q.id})" title="${q.is_active !== 0 ? 'Disable' : 'Enable'}">
                    <i class="fa-solid ${q.is_active !== 0 ? 'fa-eye-slash' : 'fa-eye'}"></i>
                  </button>
                  <button class="btn btn-secondary btn-sm" onclick="window.editCompanyQuestion(${q.id})">
                    <i class="fa-solid fa-pencil"></i>
                  </button>
                  <button class="btn btn-secondary btn-sm" onclick="window.deleteCompanyQuestion(${q.id})" style="color: #ef4444;">
                    <i class="fa-solid fa-trash-can"></i>
                  </button>
                </td>
              </tr>
            `;
          }).join("");
        }
      }
    } catch (e) {
      tbody.innerHTML = `<tr><td colspan="7" style="padding: 20px; text-align: center; color: var(--danger-color);">Failed to load questions.</td></tr>`;
    }
  }

  window.prevQuestionsPage = function() {
    if (currentQuestionsPage > 1) loadQuestions(currentQuestionsPage - 1);
  };

  window.nextQuestionsPage = function() {
    loadQuestions(currentQuestionsPage + 1);
  };

  window.toggleCompanyQuestion = async function(qid) {
    try {
      const res = await fetch(`${API_BASE}/api/admin/company-questions/${qid}/toggle`, { method: "POST" });
      const data = await res.json();
      if (data.success) {
        showToast(data.message || "Question status updated.", "success");
        await loadQuestions(currentQuestionsPage);
      } else {
        showToast(data.message || "Failed to toggle question.", "error");
      }
    } catch (e) {
      showToast("Error updating question status.", "error");
    }
  };

  window.deleteCompanyQuestion = async function(qid) {
    if (!confirm(`Are you sure you want to permanently delete question #${qid}?`)) return;
    try {
      const res = await fetch(`${API_BASE}/api/admin/company-questions/${qid}`, { method: "DELETE" });
      const data = await res.json();
      if (data.success) {
        showToast(`Question #${qid} deleted.`, "success");
        await loadQuestions(currentQuestionsPage);
      } else {
        showToast(data.message || "Failed to delete question.", "error");
      }
    } catch (e) {
      showToast("Error connecting to server.", "error");
    }
  };

  window.editCompanyQuestion = async function(qid) {
    try {
      const res = await fetch(`${API_BASE}/api/admin/company-questions/${qid}`);
      const data = await res.json();
      if (data.success && data.question) {
        const q = data.question;
        const modal = document.getElementById("company-question-cms-modal");
        document.getElementById("cq-edit-id").value = q.id;
        document.getElementById("cq-modal-title").textContent = `Edit Question #${q.id}`;
        document.getElementById("cq-company-select").value = q.company_slug || "tcs";
        document.getElementById("cq-category-select").value = q.category || "aptitude";
        document.getElementById("cq-role-select").value = q.role || "Java Developer";
        document.getElementById("cq-difficulty-select").value = q.difficulty || "Medium";
        document.getElementById("cq-question-text").value = q.question || "";

        const opts = Array.isArray(q.options) ? q.options.join("; ") : (q.options || "");
        document.getElementById("cq-options-text").value = opts;
        document.getElementById("cq-answer-text").value = q.correct_answer || "";
        document.getElementById("cq-active-select").value = q.is_active !== undefined ? String(q.is_active) : "1";
        document.getElementById("cq-explanation-text").value = q.explanation || "";

        let starterCode = "";
        if (q.extra && typeof q.extra === "object") {
          starterCode = q.extra.starter_code || JSON.stringify(q.extra, null, 2);
        }
        document.getElementById("cq-starter-code-text").value = starterCode;

        adjustQuestionModalFields(q.category);
        modal.style.display = "flex";
      }
    } catch (e) {
      showToast("Error fetching question details.", "error");
    }
  };

  function adjustQuestionModalFields(cat) {
    const optsGroup = document.getElementById("cq-options-group");
    const starterGroup = document.getElementById("cq-starter-code-group");
    const ansGroup = document.getElementById("cq-answer-group");

    if (cat === "coding") {
      if (optsGroup) optsGroup.style.display = "none";
      if (ansGroup) ansGroup.style.display = "none";
      if (starterGroup) starterGroup.style.display = "block";
    } else if (cat === "aptitude") {
      if (optsGroup) optsGroup.style.display = "block";
      if (ansGroup) ansGroup.style.display = "block";
      if (starterGroup) starterGroup.style.display = "none";
    } else {
      if (optsGroup) optsGroup.style.display = "none";
      if (ansGroup) ansGroup.style.display = "block";
      if (starterGroup) starterGroup.style.display = "none";
    }
  }

  function setupQuestionModal() {
    const modal = document.getElementById("company-question-cms-modal");
    const btnAdd = document.getElementById("btn-add-company-question");
    const btnClose = document.getElementById("btn-close-cq-modal");
    const btnCancel = document.getElementById("btn-cancel-cq");
    const form = document.getElementById("form-company-question");
    const catSelect = document.getElementById("cq-category-select");

    // Filter bar event listeners
    const filterComp = document.getElementById("q-filter-company");
    const filterCat = document.getElementById("q-filter-category");
    const filterRole = document.getElementById("q-filter-role");
    const filterSearch = document.getElementById("q-filter-search");

    if (filterComp) filterComp.addEventListener("change", () => loadQuestions(1));
    if (filterCat) filterCat.addEventListener("change", () => loadQuestions(1));
    if (filterRole) filterRole.addEventListener("change", () => loadQuestions(1));

    let searchTimer = null;
    if (filterSearch) {
      filterSearch.addEventListener("input", () => {
        clearTimeout(searchTimer);
        searchTimer = setTimeout(() => loadQuestions(1), 350);
      });
    }

    if (catSelect) {
      catSelect.addEventListener("change", (e) => adjustQuestionModalFields(e.target.value));
    }

    if (btnAdd) {
      btnAdd.addEventListener("click", () => {
        form.reset();
        document.getElementById("cq-edit-id").value = "";
        document.getElementById("cq-modal-title").textContent = "Add Company Question";
        if (filterComp && filterComp.value !== "all") document.getElementById("cq-company-select").value = filterComp.value;
        if (filterCat && filterCat.value !== "all") document.getElementById("cq-category-select").value = filterCat.value;
        if (filterRole && filterRole.value !== "all") document.getElementById("cq-role-select").value = filterRole.value;
        adjustQuestionModalFields(document.getElementById("cq-category-select").value);
        modal.style.display = "flex";
      });
    }

    const closeModal = () => { if (modal) modal.style.display = "none"; };
    if (btnClose) btnClose.addEventListener("click", closeModal);
    if (btnCancel) btnCancel.addEventListener("click", closeModal);

    if (form) {
      form.addEventListener("submit", async (e) => {
        e.preventDefault();
        const editId = document.getElementById("cq-edit-id").value.trim();
        const cat = document.getElementById("cq-category-select").value;
        const optionsRaw = document.getElementById("cq-options-text").value.trim();
        let optionsList = null;
        if (cat === "aptitude" && optionsRaw) {
          optionsList = optionsRaw.includes(";") ? optionsRaw.split(";").map(s => s.trim()).filter(Boolean) : optionsRaw.split("\n").map(s => s.trim()).filter(Boolean);
        }

        const starterCode = document.getElementById("cq-starter-code-text").value.trim();
        let extraObj = {};
        if (starterCode) {
          try {
            extraObj = JSON.parse(starterCode);
          } catch {
            extraObj = { starter_code: starterCode };
          }
        }

        const payload = {
          company_slug: document.getElementById("cq-company-select").value,
          category: cat,
          role: document.getElementById("cq-role-select").value,
          difficulty: document.getElementById("cq-difficulty-select").value,
          question: document.getElementById("cq-question-text").value.trim(),
          options: optionsList,
          correct_answer: document.getElementById("cq-answer-text").value.trim(),
          explanation: document.getElementById("cq-explanation-text").value.trim(),
          extra: extraObj,
          is_active: parseInt(document.getElementById("cq-active-select").value) || 1
        };

        try {
          const url = editId ? `${API_BASE}/api/admin/company-questions/${editId}` : `${API_BASE}/api/admin/company-questions`;
          const method = editId ? "PUT" : "POST";
          const res = await fetch(url, {
            method,
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
          });
          const data = await res.json();
          if (data.success) {
            showToast(data.message || "Question saved successfully!", "success");
            closeModal();
            await loadQuestions(currentQuestionsPage);
          } else {
            showToast(data.message || "Failed to save question.", "error");
          }
        } catch (err) {
          showToast("Error connecting to server.", "error");
        }
      });
    }

    // Export Handlers
    const btnExportCsv = document.getElementById("btn-export-questions-csv");
    const btnExportJson = document.getElementById("btn-export-questions-json");

    if (btnExportCsv) {
      btnExportCsv.addEventListener("click", () => {
        const slug = document.getElementById("q-filter-company")?.value || "all";
        const cat = document.getElementById("q-filter-category")?.value || "all";
        const role = document.getElementById("q-filter-role")?.value || "all";
        window.location.href = `${API_BASE}/api/admin/company-questions/export?format=csv&company_slug=${encodeURIComponent(slug)}&category=${encodeURIComponent(cat)}&role=${encodeURIComponent(role)}`;
      });
    }

    if (btnExportJson) {
      btnExportJson.addEventListener("click", async () => {
        const slug = document.getElementById("q-filter-company")?.value || "all";
        const cat = document.getElementById("q-filter-category")?.value || "all";
        const role = document.getElementById("q-filter-role")?.value || "all";
        const url = `${API_BASE}/api/admin/company-questions/export?format=json&company_slug=${encodeURIComponent(slug)}&category=${encodeURIComponent(cat)}&role=${encodeURIComponent(role)}`;
        try {
          const res = await fetch(url);
          const data = await res.json();
          const blob = new Blob([JSON.stringify(data, null, 2)], { type: "application/json" });
          const a = document.createElement("a");
          a.href = URL.createObjectURL(blob);
          a.download = `company_questions_${slug}.json`;
          a.click();
        } catch (e) {
          showToast("Failed to export JSON.", "error");
        }
      });
    }

    setupBulkImportModal();
  }

  function setupBulkImportModal() {
    const modal = document.getElementById("bulk-import-modal");
    const btnOpen = document.getElementById("btn-import-questions");
    const btnClose = document.getElementById("btn-close-import-modal");
    const btnCancel = document.getElementById("btn-cancel-import");
    const form = document.getElementById("form-bulk-import");

    if (btnOpen) {
      btnOpen.addEventListener("click", () => {
        form.reset();
        const filterComp = document.getElementById("q-filter-company")?.value;
        if (filterComp && filterComp !== "all") {
          document.getElementById("import-company-select").value = filterComp;
        }
        modal.style.display = "flex";
      });
    }

    const closeModal = () => { if (modal) modal.style.display = "none"; };
    if (btnClose) btnClose.addEventListener("click", closeModal);
    if (btnCancel) btnCancel.addEventListener("click", closeModal);

    if (form) {
      form.addEventListener("submit", async (e) => {
        e.preventDefault();
        const companySlug = document.getElementById("import-company-select").value;
        const fileInput = document.getElementById("import-file-input");
        const jsonText = document.getElementById("import-json-text").value.trim();

        if (fileInput.files.length > 0) {
          const formData = new FormData();
          formData.append("company_slug", companySlug);
          formData.append("file", fileInput.files[0]);

          try {
            showToast("Importing questions...", "info");
            const res = await fetch(`${API_BASE}/api/admin/company-questions/import`, {
              method: "POST",
              body: formData
            });
            const data = await res.json();
            if (data.success) {
              showToast(`Imported ${data.imported} questions (${data.skipped} skipped).`, "success");
              closeModal();
              await loadQuestions(1);
            } else {
              showToast(data.message || "Import failed.", "error");
            }
          } catch (err) {
            showToast("Error uploading import file.", "error");
          }
        } else if (jsonText) {
          try {
            const parsed = JSON.parse(jsonText);
            const questions = Array.isArray(parsed) ? parsed : (parsed.questions || []);
            if (!questions.length) {
              showToast("No questions found in JSON.", "error");
              return;
            }
            showToast("Importing questions...", "info");
            const res = await fetch(`${API_BASE}/api/admin/company-questions/import`, {
              method: "POST",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify({ company_slug: companySlug, questions })
            });
            const data = await res.json();
            if (data.success) {
              showToast(`Imported ${data.imported} questions (${data.skipped} skipped).`, "success");
              closeModal();
              await loadQuestions(1);
            } else {
              showToast(data.message || "Import failed.", "error");
            }
          } catch (err) {
            showToast("Invalid JSON string: " + err.message, "error");
          }
        } else {
          showToast("Please choose a file or paste JSON questions to import.", "error");
        }
      });
    }
  }

  // ==========================================
  // 2026 CMS: TREND INSIGHTS
  // ==========================================
  async function loadTrends() {
    const tbody = document.getElementById("admin-trends-tbody");
    if (!tbody) return;
    tbody.innerHTML = `<tr><td colspan="6" style="padding: 20px; text-align: center; color: var(--text-muted);">Loading trend insights...</td></tr>`;

    try {
      const res = await fetch(`${API_BASE}/api/admin/trends`);
      const data = await res.json();
      if (data.success && Array.isArray(data.trends)) {
        if (data.trends.length === 0) {
          tbody.innerHTML = `<tr><td colspan="6" style="padding: 20px; text-align: center; color: var(--text-muted);">No trend insights found.</td></tr>`;
          return;
        }

        tbody.innerHTML = data.trends.map(t => `
          <tr style="border-bottom: 1px solid var(--border-color);">
            <td style="padding: 10px; font-weight: 600;">#${t.id}</td>
            <td style="padding: 10px;">
              <div style="font-weight: 700; color: var(--text-main); margin-bottom: 2px;">${escapeHtml(t.title)}</div>
              <div style="font-size: 0.8rem; color: var(--text-muted);"><i class="fa-solid fa-lightbulb text-warning"></i> <strong>Tip:</strong> ${escapeHtml(t.actionable_tip || t.content || '')}</div>
            </td>
            <td style="padding: 10px;"><span class="badge badge-purple">${escapeHtml(t.category)}</span></td>
            <td style="padding: 10px; font-size: 0.82rem; color: var(--text-muted);">${escapeHtml(t.role_tag || 'All')} / ${escapeHtml(t.company_tag || 'All')}</td>
            <td style="padding: 10px;">
              <span class="badge ${t.is_active ? 'badge-success' : 'badge-secondary'}">${t.is_active ? 'Active' : 'Inactive'}</span>
            </td>
            <td style="padding: 10px;">
              <button class="btn btn-secondary btn-sm" onclick="window.deleteTrend(${t.id})" style="color: #ef4444; padding: 3px 8px;">
                Delete <i class="fa-solid fa-trash-can"></i>
              </button>
            </td>
          </tr>
        `).join("");
      }
    } catch (e) {
      tbody.innerHTML = `<tr><td colspan="6" style="padding: 15px; color: var(--danger-color); text-align: center;">Error loading trend insights.</td></tr>`;
    }
  }

  window.deleteTrend = async function(id) {
    if (!confirm(`Delete trend insight #${id}?`)) return;
    try {
      const res = await fetch(`${API_BASE}/api/admin/trends/${id}`, { method: "DELETE" });
      const data = await res.json();
      if (data.success) {
        showToast("Trend insight deleted.", "success");
        await loadTrends();
      } else {
        showToast(data.message || "Failed to delete trend.", "error");
      }
    } catch (e) {
      showToast("Error deleting trend.", "error");
    }
  };

  function setupTrendModal() {
    const modal = document.getElementById("modal-trend");
    const btnAdd = document.getElementById("btn-add-trend");
    const btnClose = document.getElementById("btn-close-trend-modal");
    const btnCancel = document.getElementById("btn-cancel-trend");
    const form = document.getElementById("form-trend");

    if (btnAdd) {
      btnAdd.addEventListener("click", () => {
        form.reset();
        modal.style.display = "flex";
      });
    }

    const closeModal = () => modal.style.display = "none";
    if (btnClose) btnClose.addEventListener("click", closeModal);
    if (btnCancel) btnCancel.addEventListener("click", closeModal);

    if (form) {
      form.addEventListener("submit", async (e) => {
        e.preventDefault();
        const payload = {
          title: document.getElementById("trend-title").value.trim(),
          category: document.getElementById("trend-category").value,
          priority: parseInt(document.getElementById("trend-priority").value) || 1,
          role_tag: document.getElementById("trend-role").value.trim() || "All",
          company_tag: document.getElementById("trend-company").value.trim() || "All",
          content: document.getElementById("trend-content").value.trim(),
          actionable_tip: document.getElementById("trend-tip").value.trim()
        };

        try {
          const res = await fetch(`${API_BASE}/api/admin/trends`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
          });
          const data = await res.json();
          if (data.success) {
            showToast("Trend insight added! Live on student dashboards.", "success");
            closeModal();
            await loadTrends();
          } else {
            showToast(data.message || "Failed to add trend insight.", "error");
          }
        } catch (err) {
          showToast("Error saving trend insight.", "error");
        }
      });
    }
  }

  // ==========================================
  // 2026 CMS: RESUME TEMPLATES
  // ==========================================
  async function loadTemplates() {
    const tbody = document.getElementById("admin-templates-tbody");
    if (!tbody) return;
    tbody.innerHTML = `<tr><td colspan="6" style="padding: 20px; text-align: center; color: var(--text-muted);">Loading resume templates...</td></tr>`;

    try {
      const res = await fetch(`${API_BASE}/api/admin/templates`);
      const data = await res.json();
      if (data.success && Array.isArray(data.templates)) {
        if (data.templates.length === 0) {
          tbody.innerHTML = `<tr><td colspan="6" style="padding: 20px; text-align: center; color: var(--text-muted);">No templates found.</td></tr>`;
          return;
        }

        tbody.innerHTML = data.templates.map(t => `
          <tr style="border-bottom: 1px solid var(--border-color);">
            <td style="padding: 10px; font-weight: 600;">#${t.id}</td>
            <td style="padding: 10px;">
              <div style="font-weight: 700; color: var(--text-main);">${escapeHtml(t.name)}</div>
              <div style="font-size: 0.78rem; color: var(--text-muted);">${escapeHtml(t.description || '')}</div>
            </td>
            <td style="padding: 10px; font-size: 0.82rem; font-family: monospace;">
              <div>${escapeHtml(t.template_id)}</div>
              <div style="color: var(--primary-600);">${escapeHtml(t.css_class)}</div>
            </td>
            <td style="padding: 10px;"><span class="badge badge-primary">${escapeHtml(t.badge_text)}</span></td>
            <td style="padding: 10px;">
              <span class="badge ${t.is_active ? 'badge-success' : 'badge-secondary'}">${t.is_active ? 'Active' : 'Inactive'}</span>
            </td>
            <td style="padding: 10px;">
              <button class="btn btn-secondary btn-sm" onclick="window.deleteTemplate(${t.id})" style="color: #ef4444; padding: 3px 8px;">
                Delete <i class="fa-solid fa-trash-can"></i>
              </button>
            </td>
          </tr>
        `).join("");
      }
    } catch (e) {
      tbody.innerHTML = `<tr><td colspan="6" style="padding: 15px; color: var(--danger-color); text-align: center;">Error loading templates.</td></tr>`;
    }
  }

  window.deleteTemplate = async function(id) {
    if (!confirm(`Delete template #${id}?`)) return;
    try {
      const res = await fetch(`${API_BASE}/api/admin/templates/${id}`, { method: "DELETE" });
      const data = await res.json();
      if (data.success) {
        showToast("Template deleted.", "success");
        await loadTemplates();
      } else {
        showToast(data.message || "Failed to delete template.", "error");
      }
    } catch (e) {
      showToast("Error deleting template.", "error");
    }
  };

  function setupTemplateModal() {
    const modal = document.getElementById("modal-template");
    const btnAdd = document.getElementById("btn-add-template");
    const btnClose = document.getElementById("btn-close-template-modal");
    const btnCancel = document.getElementById("btn-cancel-template");
    const form = document.getElementById("form-template");

    if (btnAdd) {
      btnAdd.addEventListener("click", () => {
        form.reset();
        modal.style.display = "flex";
      });
    }

    const closeModal = () => modal.style.display = "none";
    if (btnClose) btnClose.addEventListener("click", closeModal);
    if (btnCancel) btnCancel.addEventListener("click", closeModal);

    if (form) {
      form.addEventListener("submit", async (e) => {
        e.preventDefault();
        const payload = {
          template_id: document.getElementById("tmpl-id").value.trim().toLowerCase(),
          name: document.getElementById("tmpl-name").value.trim(),
          badge_text: document.getElementById("tmpl-badge").value.trim() || "Trending 2026",
          css_class: document.getElementById("tmpl-class").value.trim() || "template-modern-single",
          description: document.getElementById("tmpl-desc").value.trim(),
          is_trending: 1
        };

        try {
          const res = await fetch(`${API_BASE}/api/admin/templates`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
          });
          const data = await res.json();
          if (data.success) {
            showToast("Resume template created successfully!", "success");
            closeModal();
            await loadTemplates();
          } else {
            showToast(data.message || "Failed to create template.", "error");
          }
        } catch (err) {
          showToast("Error creating template.", "error");
        }
      });
    }
  }

  // ==========================================
  // 2026 CMS: AI FLUENCY QUESTIONS
  // ==========================================
  async function loadFluencyQuestions() {
    const container = document.getElementById("admin-fluency-list");
    if (!container) return;
    container.innerHTML = `<div style="text-align: center; padding: 20px; color: var(--text-muted);">Loading fluency questions...</div>`;

    try {
      const res = await fetch(`${API_BASE}/api/admin/ai-fluency-questions`);
      const data = await res.json();
      if (data.success && Array.isArray(data.questions)) {
        if (data.questions.length === 0) {
          container.innerHTML = `<div style="text-align: center; padding: 20px; color: var(--text-muted);">No AI fluency questions found.</div>`;
          return;
        }

        container.innerHTML = data.questions.map(q => `
          <div class="card" style="padding: 16px 20px; border: 1px solid var(--border-color); border-radius: var(--radius-sm); display: flex; justify-content: space-between; align-items: flex-start; gap: 14px;">
            <div style="flex: 1;">
              <div style="display: flex; gap: 8px; align-items: center; margin-bottom: 6px; flex-wrap: wrap;">
                <span class="badge badge-purple">${escapeHtml(q.category)}</span>
                <span class="badge badge-primary">${escapeHtml(q.difficulty)}</span>
                <span style="font-size: 0.75rem; color: var(--text-muted);">ID #${q.id}</span>
              </div>
              <div style="font-weight: 600; font-size: 0.95rem; color: var(--text-main); margin-bottom: 6px;">
                ${escapeHtml(q.question_text)}
              </div>
              <div style="font-size: 0.82rem; color: var(--text-muted); background: var(--bg-subtle); padding: 8px 12px; border-radius: 4px;">
                <i class="fa-solid fa-lightbulb text-warning"></i> <strong>Recruiter Criteria:</strong> ${escapeHtml(q.context_hint || '')}
              </div>
            </div>
            <button class="btn btn-secondary btn-sm" onclick="window.deleteFluencyQuestion(${q.id})" style="color: #ef4444; white-space: nowrap; padding: 4px 10px;">
              Delete <i class="fa-solid fa-trash-can"></i>
            </button>
          </div>
        `).join("");
      }
    } catch (e) {
      container.innerHTML = `<div style="color: var(--danger-color); padding: 10px;">Failed to load fluency questions.</div>`;
    }
  }

  window.deleteFluencyQuestion = async function(id) {
    if (!confirm(`Delete fluency question #${id}?`)) return;
    try {
      const res = await fetch(`${API_BASE}/api/admin/ai-fluency-questions/${id}`, { method: "DELETE" });
      const data = await res.json();
      if (data.success) {
        showToast("Fluency question deleted.", "success");
        await loadFluencyQuestions();
      } else {
        showToast(data.message || "Failed to delete question.", "error");
      }
    } catch (e) {
      showToast("Error deleting fluency question.", "error");
    }
  };

  function setupFluencyModal() {
    const modal = document.getElementById("modal-fluency");
    const btnAdd = document.getElementById("btn-add-fluency");
    const btnClose = document.getElementById("btn-close-fluency-modal");
    const btnCancel = document.getElementById("btn-cancel-fluency");
    const form = document.getElementById("form-fluency");

    if (btnAdd) {
      btnAdd.addEventListener("click", () => {
        form.reset();
        modal.style.display = "flex";
      });
    }

    const closeModal = () => modal.style.display = "none";
    if (btnClose) btnClose.addEventListener("click", closeModal);
    if (btnCancel) btnCancel.addEventListener("click", closeModal);

    if (form) {
      form.addEventListener("submit", async (e) => {
        e.preventDefault();
        const rawPoints = document.getElementById("fluency-points").value;
        const points = rawPoints ? rawPoints.split(/[\n,]+/).map(p => p.trim()).filter(Boolean) : [];

        const payload = {
          category: document.getElementById("fluency-cat").value,
          difficulty: document.getElementById("fluency-diff").value,
          question_text: document.getElementById("fluency-prompt").value.trim(),
          context_hint: document.getElementById("fluency-hint").value.trim(),
          ideal_talking_points: points
        };

        try {
          const res = await fetch(`${API_BASE}/api/admin/ai-fluency-questions`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
          });
          const data = await res.json();
          if (data.success) {
            showToast("AI Fluency question added successfully!", "success");
            closeModal();
            await loadFluencyQuestions();
          } else {
            showToast(data.message || "Failed to add fluency question.", "error");
          }
        } catch (err) {
          showToast("Error creating fluency question.", "error");
        }
      });
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

