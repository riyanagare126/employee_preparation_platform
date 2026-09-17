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
  if (tabQuestionsBtn) tabQuestionsBtn.addEventListener("click", () => { activateTab(tabQuestionsBtn, viewQuestions); loadQuestions(); });
  if (tabTrendsBtn) tabTrendsBtn.addEventListener("click", () => { activateTab(tabTrendsBtn, viewTrends); loadTrends(); });
  if (tabTemplatesBtn) tabTemplatesBtn.addEventListener("click", () => { activateTab(tabTemplatesBtn, viewTemplates); loadTemplates(); });
  if (tabFluencyBtn) tabFluencyBtn.addEventListener("click", () => { activateTab(tabFluencyBtn, viewFluency); loadFluencyQuestions(); });

  if (btnRefresh) {
    btnRefresh.addEventListener("click", async () => {
      await loadAdminStats();
      await loadUsers();
      showToast("Admin data refreshed!", "info");
    });
  }

  // Initial Load
  await loadAdminStats();
  await loadUsers();
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
                ${u.is_admin ? '<span class="badge badge-danger">Admin 🛡️</span>' : '<span class="badge" style="background: var(--bg-subtle);">Candidate</span>'}
              </td>
              <td style="padding: 10px;">
                <button class="btn btn-secondary btn-sm" onclick="window.deleteCandidate(${u.id})" style="color: #ef4444; border-color: #fca5a5;">
                  Delete 🗑️
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
    tbody.innerHTML = `<tr><td colspan="6" style="padding: 20px; text-align: center; color: var(--text-muted);">Loading company blueprints...</td></tr>`;

    try {
      const res = await fetch(`${API_BASE}/api/admin/companies`);
      if (res.ok) {
        const data = await res.json();
        if (data.success && data.companies) {
          tbody.innerHTML = data.companies.map(c => `
            <tr style="border-bottom: 1px solid var(--border-color);">
              <td style="padding: 10px; font-weight: 700; display: flex; align-items: center; gap: 8px;">
                <span>${c.logo_emoji || '🏢'}</span>
                <span>${escapeHtml(c.company_name)}</span>
              </td>
              <td style="padding: 10px; font-family: monospace; font-size: 0.8rem; color: var(--primary-700);">${escapeHtml(c.slug)}</td>
              <td style="padding: 10px;">${escapeHtml(c.category || 'Technology')}</td>
              <td style="padding: 10px;"><span class="badge badge-warning">${escapeHtml(c.difficulty)}</span></td>
              <td style="padding: 10px; font-size: 0.8rem; max-width: 250px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">
                ${escapeHtml(c.common_roles || 'Software Developer, Java Developer, Python Developer')}
              </td>
              <td style="padding: 10px; white-space: nowrap;">
                <button class="btn btn-secondary btn-sm" onclick="window.editCompany('${c.slug}')">Edit ✏️</button>
                <button class="btn btn-secondary btn-sm" onclick="window.deleteCompany('${c.slug}')" style="color: #ef4444;">Delete 🗑️</button>
              </td>
            </tr>
          `).join("");
        }
      }
    } catch (e) {
      tbody.innerHTML = `<tr><td colspan="6" style="padding: 20px; text-align: center; color: var(--danger-color);">Failed to load companies.</td></tr>`;
    }
  }

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
          logo_emoji: document.getElementById("comp-emoji").value.trim() || "🏢",
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
        document.getElementById("comp-emoji").value = c.logo_emoji || "🏢";
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
                <button class="btn btn-secondary btn-sm" onclick="window.deleteRole(${r.id})" style="color: #ef4444;">Delete 🗑️</button>
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

  async function loadQuestions() {
    const container = document.getElementById("admin-questions-list");
    if (!container) return;
    container.innerHTML = `<div style="text-align: center; padding: 20px; color: var(--text-muted);">Loading question bank...</div>`;

    try {
      const res = await fetch(`${API_BASE}/api/admin/questions`);
      if (res.ok) {
        const data = await res.json();
        if (data.success && data.questions) {
          if (data.questions.length === 0) {
            container.innerHTML = `<div style="text-align: center; padding: 20px; color: var(--text-muted);">No custom questions in database. Click '+ Add & Assign Question' to seed new questions.</div>`;
            return;
          }

          container.innerHTML = data.questions.map(q => `
            <div class="card" style="padding: 14px; border: 1px solid var(--border-color); display: flex; justify-content: space-between; align-items: flex-start; gap: 14px;">
              <div>
                <div style="display: flex; gap: 6px; align-items: center; margin-bottom: 6px;">
                  <span class="badge badge-primary">${escapeHtml(q.question_type.toUpperCase())}</span>
                  <span class="badge badge-purple">🏢 ${escapeHtml(q.company_slug.toUpperCase())}</span>
                  <span class="badge" style="background: var(--bg-subtle);">🎯 ${escapeHtml(q.role_name)}</span>
                  <span class="badge badge-warning">${escapeHtml(q.difficulty)}</span>
                </div>
                <div style="font-weight: 600; font-size: 0.95rem; color: var(--text-main); margin-bottom: 4px;">
                  ${escapeHtml(q.question)}
                </div>
                ${q.explanation ? `<div style="font-size: 0.8rem; color: var(--text-muted);"><strong>Model Answer:</strong> ${escapeHtml(q.explanation)}</div>` : ''}
              </div>
              <button class="btn btn-secondary btn-sm" onclick="window.deleteQuestion(${q.id})" style="color: #ef4444; white-space: nowrap;">
                Delete 🗑️
              </button>
            </div>
          `).join("");
        }
      }
    } catch (e) {
      container.innerHTML = `<div style="color: var(--danger-color); padding: 10px;">Failed to load questions.</div>`;
    }
  }

  window.deleteQuestion = async function(qId) {
    if (!confirm(`Are you sure you want to delete question #${qId}?`)) return;
    try {
      const res = await fetch(`${API_BASE}/api/admin/question/${qId}`, { method: "DELETE" });
      const data = await res.json();
      if (data.success) {
        showToast("Question deleted.", "success");
        await loadQuestions();
      } else {
        showToast(data.message || "Failed to delete question.", "error");
      }
    } catch (e) {
      showToast("Error connecting to server.", "error");
    }
  };

  function setupQuestionModal() {
    const modal = document.getElementById("question-modal");
    const btnAdd = document.getElementById("btn-add-question");
    const btnClose = document.getElementById("btn-close-q-modal");
    const btnCancel = document.getElementById("btn-cancel-q");
    const form = document.getElementById("form-question");

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
          question_type: document.getElementById("q-type").value,
          category: document.getElementById("q-cat").value.trim() || "Technical",
          company_slug: document.getElementById("q-comp").value.trim().toLowerCase() || "all",
          role_name: document.getElementById("q-role").value.trim() || "all",
          question: document.getElementById("q-text").value.trim(),
          explanation: document.getElementById("q-exp").value.trim()
        };

        try {
          const res = await fetch(`${API_BASE}/api/admin/questions`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
          });
          const data = await res.json();
          if (data.success) {
            showToast("Question created and assigned successfully!", "success");
            closeModal();
            await loadQuestions();
          } else {
            showToast(data.message || "Failed to create question.", "error");
          }
        } catch (err) {
          showToast("Error creating question.", "error");
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
              <div style="font-size: 0.8rem; color: var(--text-muted);">💡 <strong>Tip:</strong> ${escapeHtml(t.actionable_tip || t.content || '')}</div>
            </td>
            <td style="padding: 10px;"><span class="badge badge-purple">${escapeHtml(t.category)}</span></td>
            <td style="padding: 10px; font-size: 0.82rem; color: var(--text-muted);">${escapeHtml(t.role_tag || 'All')} / ${escapeHtml(t.company_tag || 'All')}</td>
            <td style="padding: 10px;">
              <span class="badge ${t.is_active ? 'badge-success' : 'badge-secondary'}">${t.is_active ? 'Active' : 'Inactive'}</span>
            </td>
            <td style="padding: 10px;">
              <button class="btn btn-secondary btn-sm" onclick="window.deleteTrend(${t.id})" style="color: #ef4444; padding: 3px 8px;">
                Delete 🗑️
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
                Delete 🗑️
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
          badge_text: document.getElementById("tmpl-badge").value.trim() || "🔥 Trending 2026",
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
                💡 <strong>Recruiter Criteria:</strong> ${escapeHtml(q.context_hint || '')}
              </div>
            </div>
            <button class="btn btn-secondary btn-sm" onclick="window.deleteFluencyQuestion(${q.id})" style="color: #ef4444; white-space: nowrap; padding: 4px 10px;">
              Delete 🗑️
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

