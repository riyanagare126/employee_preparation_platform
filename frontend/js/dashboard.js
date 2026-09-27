/**
 * AI Employee Preparation Platform - Personalized Dashboard Controller
 * Fully dynamic 2026 Core Feature: live DB stats, trend insights, progress chart, and shortcuts
 */

document.addEventListener("DOMContentLoaded", async () => {
  const employee = requireAuth();
  if (!employee) return;

  // Initialize UI
  setupDashboardProfile(employee);
  setupGoalModal(employee);
  setupNoticePlan(employee);
  await loadCompanyPreparationBanner(employee);
  await loadNoticePlan(employee.id);
  await loadDashboardAnalytics(employee.id);

  // Quick AI Assistant button
  const btnQuickAi = document.getElementById("btn-quick-ai");
  if (btnQuickAi) {
    btnQuickAi.addEventListener("click", () => {
      showToast("AI Prep Assistant is analyzing your profile...", "info");
      setTimeout(() => {
        window.location.href = "interview.html";
      }, 500);
    });
  }

  // Open Company Hub button
  const btnOpenHub = document.getElementById("btn-open-comp-hub");
  if (btnOpenHub) {
    btnOpenHub.addEventListener("click", () => {
      const active = getSelectedCompany();
      if (active && active.slug) {
        window.location.href = `company-prep.html?company=${encodeURIComponent(active.slug)}`;
      } else {
        window.location.href = "companies.html";
      }
    });
  }
});

function setupDashboardProfile(employee) {
  // Avatar & Basic info
  const initials = employee.name ? employee.name.charAt(0).toUpperCase() : "C";
  const avatarEl = document.getElementById("profile-avatar-initials");
  if (avatarEl) avatarEl.textContent = initials;
  
  const nameEl = document.getElementById("profile-name");
  if (nameEl) nameEl.textContent = employee.name || "Candidate";
  
  const welcomeEl = document.getElementById("welcome-heading");
  if (welcomeEl) welcomeEl.innerHTML = `Welcome, ${escapeHtml(employee.name || 'Candidate')}! <i class="fa-solid fa-hand text-warning"></i>`;

  const jobRoleEl = document.getElementById("profile-job-role");
  if (jobRoleEl) jobRoleEl.textContent = employee.job_role || "Software Engineer";

  const emailEl = document.getElementById("profile-email");
  if (emailEl) emailEl.textContent = employee.email || "";

  const qualEl = document.getElementById("profile-qualification");
  if (qualEl) qualEl.textContent = employee.qualification || "B.Tech / BCA";

  const expEl = document.getElementById("profile-experience");
  if (expEl) expEl.textContent = employee.experience || "Fresher";

  const targetJobEl = document.getElementById("profile-target-job");
  if (targetJobEl) targetJobEl.textContent = employee.target_role || employee.job_role || "Java Developer";

  const skillsEl = document.getElementById("profile-skills");
  if (skillsEl) skillsEl.textContent = employee.skills || "Java, Python, SQL";

  // Career Goal Header & Sidebar
  const storedComp = getSelectedCompany();
  const company = (storedComp && storedComp.name) ? storedComp.name : (employee.target_company || "Select Target Company");
  const role = (storedComp && storedComp.role) ? storedComp.role : (employee.target_role || employee.job_role || "Software Engineer");

  const headComp = document.getElementById("header-target-company");
  const headRole = document.getElementById("header-target-role");
  const profComp = document.getElementById("profile-target-company");

  if (headComp) headComp.textContent = company;
  if (headRole) headRole.textContent = role;
  if (profComp) profComp.textContent = company;
}

async function loadCompanyPreparationBanner(employee) {
  const storedComp = getSelectedCompany();
  const compName = (storedComp && storedComp.name) ? storedComp.name : (employee.target_company || "");
  const roleName = (storedComp && storedComp.role) ? storedComp.role : (employee.target_role || employee.job_role || "Software Engineer");
  const compSlug = (storedComp && storedComp.slug) ? storedComp.slug : getCompanySlugFromName(compName);

  const titleEl = document.getElementById("current-prep-title");
  const progEl = document.getElementById("current-prep-progress");
  const emojiEl = document.getElementById("current-prep-emoji");

  if (titleEl) titleEl.textContent = compName ? `${compName} — ${roleName}` : "Select Target Company";

  if (!compSlug) return;

  try {
    const res = await fetch(`${API_BASE}/api/companies/${compSlug}/progress?employee_id=${employee.id}`);
    if (res.ok) {
      const data = await res.json();
      if (data.success) {
        if (emojiEl && data.company) emojiEl.innerHTML = '<i class="fa-solid fa-building"></i>';
        if (progEl && data.preparation) {
          const overall = data.preparation.progress || 0.0;
          progEl.textContent = `${Math.round(overall)}%`;
        }
      }
    }
  } catch (e) {
    console.warn("Could not fetch company progress banner:", e);
  }
}

function setupGoalModal(employee) {
  const modal = document.getElementById("goal-modal");
  const btnChange = document.getElementById("btn-change-goal");
  const btnClose = document.getElementById("btn-close-goal") || document.getElementById("btn-close-goal-modal");
  const btnCancel = document.getElementById("btn-cancel-goal");
  const formGoal = document.getElementById("form-career-goal");

  if (!modal) return;

  function openModal() {
    modal.style.display = "flex";
    const curComp = employee.target_company || "Tata Consultancy Services (TCS)";
    const curRole = employee.target_role || employee.job_role || "Java Developer";
    const compSelect = document.getElementById("goal-company") || document.getElementById("goal-company-select");
    const roleSelect = document.getElementById("goal-role") || document.getElementById("goal-role-select");
    if (compSelect) compSelect.value = curComp;
    if (roleSelect) roleSelect.value = curRole;
  }

  function closeModal() {
    modal.style.display = "none";
  }

  if (btnChange) btnChange.addEventListener("click", openModal);
  if (btnClose) btnClose.addEventListener("click", closeModal);
  if (btnCancel) btnCancel.addEventListener("click", closeModal);

  if (formGoal) {
    formGoal.addEventListener("submit", async (e) => {
      e.preventDefault();
      const compEl = document.getElementById("goal-company") || document.getElementById("goal-company-select");
      const roleEl = document.getElementById("goal-role") || document.getElementById("goal-role-select");
      const target_company = compEl ? compEl.value : "Tata Consultancy Services (TCS)";
      const target_role = roleEl ? roleEl.value : "Software Engineer";
      const slug = getCompanySlugFromName(target_company);

      try {
        const res = await fetch(`${API_BASE}/api/auth/set-career-goal`, {
          method: "POST",
          headers: getAuthHeaders(),
          body: JSON.stringify({ employee_id: employee.id, target_company, target_role })
        });
        const data = await res.json();
        if (data.success) {
          employee.target_company = target_company;
          employee.target_company_slug = slug;
          employee.target_role = target_role;
          setLoggedInEmployee(employee);

          await setSelectedCompany(slug, target_company, target_role);

          setupDashboardProfile(employee);
          await loadCompanyPreparationBanner(employee);
          closeModal();
          showToast(`Target company updated to ${target_company} — ${target_role}!`, "success");
          await loadDashboardAnalytics(employee.id);
        } else {
          showToast(data.message || "Failed to update goal.", "error");
        }
      } catch (err) {
        showToast("Error updating career goal.", "error");
      }
    });
  }
}

async function loadDashboardAnalytics(employeeId) {
  try {
    // 1. Fetch Master 2026 Dashboard Summary (Live DB values per employee_id)
    const resSummary = await fetch(`${API_BASE}/api/dashboard/summary?employee_id=${employeeId}`);
    if (resSummary.ok) {
      const sumData = await resSummary.json();
      if (sumData.success && sumData.data) {
        renderDashboardSummary(sumData.data);
      }
    }

    // 2. Fetch Skill Assessment & Readiness
    const resAssess = await fetch(`${API_BASE}/api/skills/assessment?employee_id=${employeeId}`);
    if (resAssess.ok) {
      const data = await resAssess.json();
      if (data.success && data.data) {
        renderReadinessAndSkills(data.data);
      }
    }

    // 3. Fetch Daily Preparation Plan (Fallback if no Notice Period Plan active)
    if (!window._hasActiveNoticePlan) {
      const resPlan = await fetch(`${API_BASE}/api/skills/daily-plan?employee_id=${employeeId}`);
      if (resPlan.ok) {
        const data = await resPlan.json();
        if (data.success && data.data) {
          renderDailyPlan(data.data, employeeId);
        }
      }
    }

    // 4. Fetch Historical Progression Trend
    const resTrend = await fetch(`${API_BASE}/api/skills/readiness-trend?employee_id=${employeeId}`);
    if (resTrend.ok) {
      const data = await resTrend.json();
      if (data.success && data.trend && data.trend.length > 0) {
        const trendEl = document.getElementById("readiness-trend-text");
        if (trendEl) {
          trendEl.textContent = data.trend.slice(-5).join(" → ");
        }
      }
    }
  } catch (err) {
    console.error("Error loading dashboard analytics:", err);
  }
}

function renderDashboardSummary(summary) {
  const stats = summary.stats || {};

  // 1. Update Stat Cards (Live DB values per employee_id)
  const intvTaken = document.getElementById("stat-interviews-taken");
  const avgScore = document.getElementById("stat-avg-score");
  const resScore = document.getElementById("stat-resume-score");
  const fluScore = document.getElementById("stat-fluency-score");
  const streakEl = document.getElementById("gamification-streak");
  const ptsEl = document.getElementById("gamification-points");

  if (intvTaken) intvTaken.textContent = stats.interviews_taken || 0;
  if (avgScore) avgScore.textContent = `${stats.avg_score || 0}%`;
  if (resScore) resScore.textContent = `${stats.resume_score || 0}%`;
  if (fluScore) fluScore.textContent = `${stats.ai_fluency_score || 0}%`;
  if (streakEl) streakEl.textContent = stats.streak_days || 1;
  if (ptsEl) ptsEl.textContent = stats.xp_points || 50;

  // 2. Render Trend Insight Widget
  const trendContainer = document.getElementById("trend-tips-container");
  const trendLabel = document.getElementById("trend-target-label");
  const compName = (summary.employee && summary.employee.target_company) ? summary.employee.target_company : "Target Enterprise";
  if (trendLabel) trendLabel.textContent = `Curated for ${compName}`;

  if (trendContainer && summary.trend_insights) {
    trendContainer.innerHTML = summary.trend_insights.map((tip, idx) => `
      <div class="trend-tip-box">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
          <span style="font-weight: 700; font-size: 0.95rem; color: #fff;"><i class="fa-solid fa-lightbulb text-warning"></i> ${escapeHtml(tip.title)}</span>
          <span style="background: rgba(99, 102, 241, 0.25); color: #c7d2fe; padding: 2px 8px; border-radius: 6px; font-size: 0.72rem; font-weight: 700; text-transform: uppercase;">
            ${escapeHtml(tip.category)}
          </span>
        </div>
        <p style="font-size: 0.86rem; color: #cbd5e1; margin: 0 0 8px 0; line-height: 1.5;">
          ${escapeHtml(tip.content)}
        </p>
        <div style="background: rgba(16, 185, 129, 0.15); border-left: 3px solid #10b981; padding: 6px 12px; border-radius: 4px; font-size: 0.8rem; color: #a7f3d0;">
          <strong>Actionable Takeaway:</strong> ${escapeHtml(tip.actionable_tip)}
        </div>
      </div>
    `).join("");
  }

  // 3. Render Canvas Improvement Trend Chart
  renderProgressTrendChart(summary.session_trend || []);
}

function renderProgressTrendChart(sessions) {
  const canvas = document.getElementById("progress-trend-canvas");
  if (!canvas) return;

  const ctx = canvas.getContext("2d");
  const width = canvas.width;
  const height = canvas.height;

  // Clear canvas
  ctx.clearRect(0, 0, width, height);

  if (!sessions || sessions.length === 0) {
    sessions = [
      { session: "S1", readiness: 54, coding: 45, interview: 60 },
      { session: "S2", readiness: 62, coding: 60, interview: 65 },
      { session: "S3", readiness: 71, coding: 70, interview: 75 },
      { session: "S4", readiness: 82, coding: 80, interview: 84 }
    ];
  }

  const paddingLeft = 45;
  const paddingRight = 30;
  const paddingTop = 20;
  const paddingBottom = 35;
  const plotWidth = width - paddingLeft - paddingRight;
  const plotHeight = height - paddingTop - paddingBottom;

  // Background Grid
  ctx.strokeStyle = "#f1f5f9";
  ctx.lineWidth = 1;
  ctx.fillStyle = "#94a3b8";
  ctx.font = "10px Inter, sans-serif";
  ctx.textAlign = "right";

  for (let s = 0; s <= 100; s += 25) {
    const y = paddingTop + plotHeight - (s / 100) * plotHeight;
    ctx.beginPath();
    ctx.moveTo(paddingLeft, y);
    ctx.lineTo(width - paddingRight, y);
    ctx.stroke();
    ctx.fillText(`${s}%`, paddingLeft - 8, y + 3);
  }

  const stepX = sessions.length > 1 ? plotWidth / (sessions.length - 1) : plotWidth;

  // Helper to draw series
  function drawLine(key, color) {
    ctx.beginPath();
    ctx.strokeStyle = color;
    ctx.lineWidth = 2.5;

    sessions.forEach((pt, i) => {
      const val = pt[key] || 0;
      const x = paddingLeft + (i * stepX);
      const y = paddingTop + plotHeight - (val / 100) * plotHeight;
      if (i === 0) ctx.moveTo(x, y);
      else ctx.lineTo(x, y);
    });
    ctx.stroke();

    // Draw dots
    sessions.forEach((pt, i) => {
      const val = pt[key] || 0;
      const x = paddingLeft + (i * stepX);
      const y = paddingTop + plotHeight - (val / 100) * plotHeight;
      ctx.beginPath();
      ctx.fillStyle = "#ffffff";
      ctx.arc(x, y, 4.5, 0, Math.PI * 2);
      ctx.fill();
      ctx.beginPath();
      ctx.fillStyle = color;
      ctx.arc(x, y, 3, 0, Math.PI * 2);
      ctx.fill();
    });
  }

  // Draw X labels
  ctx.textAlign = "center";
  ctx.fillStyle = "#64748b";
  sessions.forEach((pt, i) => {
    const x = paddingLeft + (i * stepX);
    ctx.fillText(pt.session || `S${i+1}`, x, height - 10);
  });

  // Draw Lines: Readiness (Indigo), Coding (Emerald), Interview (Violet)
  drawLine("coding", "#10b981");
  drawLine("interview", "#8b5cf6");
  drawLine("readiness", "#4f46e5");
}

function renderReadinessAndSkills(assessment) {
  // Gauge Score
  const scoreVal = document.getElementById("readiness-score-val");
  const tierBadge = document.getElementById("readiness-tier-badge");
  const tierDesc = document.getElementById("readiness-tier-desc");

  if (scoreVal) {
    scoreVal.innerHTML = `${assessment.overall_readiness_score}<span style="font-size: 1.1rem; color: var(--text-muted); font-weight: 500;"> / 100</span>`;
  }
  if (tierBadge) {
    tierBadge.innerHTML = `${escapeHtml(assessment.status_tier)} <i class="fa-solid fa-rocket"></i>`;
    tierBadge.className = `badge ${assessment.tier_badge || 'badge-success'}`;
  }
  if (tierDesc) {
    tierDesc.textContent = assessment.tier_description || "Transparent weighted preparation index calculated from 5 performance dimensions.";
  }

  // 5 Pillars
  const b = assessment.readiness_breakdown || {};
  if (document.getElementById("pillar-aptitude") && b.aptitude) {
    document.getElementById("pillar-aptitude").textContent = `${b.aptitude.score}%`;
  }
  if (document.getElementById("pillar-coding") && b.coding) {
    document.getElementById("pillar-coding").textContent = `${b.coding.score}% (${b.coding.solved_count || 0} solved)`;
  }
  if (document.getElementById("pillar-technical") && b.technical) {
    document.getElementById("pillar-technical").textContent = `${b.technical.score}%`;
  }
  if (document.getElementById("pillar-interview") && b.interview) {
    document.getElementById("pillar-interview").textContent = `${b.interview.score}%`;
  }
  if (document.getElementById("pillar-resume") && b.resume) {
    document.getElementById("pillar-resume").textContent = `${b.resume.score}%`;
  }

  // 3-Tier Skill Matrix
  const strongList = document.getElementById("matrix-strong-list");
  const devList = document.getElementById("matrix-developing-list");
  const weakList = document.getElementById("matrix-weak-list");

  if (strongList && assessment.strong_competencies) {
    strongList.innerHTML = assessment.strong_competencies.map(s => `<span class="badge" style="background: #dcfce7; color: #166534;">${escapeHtml(s)}</span>`).join("");
  }
  if (devList && assessment.developing_skills) {
    devList.innerHTML = assessment.developing_skills.map(s => `<span class="badge" style="background: #fef9c3; color: #854d0e;">${escapeHtml(s)}</span>`).join("");
  }
  if (weakList && assessment.priority_focus_areas) {
    weakList.innerHTML = assessment.priority_focus_areas.map(s => `<span class="badge" style="background: #fee2e2; color: #991b1b;">${escapeHtml(s)}</span>`).join("");
  }
}

function renderDailyPlan(planData, employeeId) {
  const dateEl = document.getElementById("daily-plan-date");
  const tasksContainer = document.getElementById("daily-plan-tasks");

  if (dateEl && planData.plan_date) {
    dateEl.textContent = planData.plan_date;
  }

  if (tasksContainer && planData.tasks) {
    const completedSet = new Set(planData.completed_tasks || []);
    tasksContainer.innerHTML = planData.tasks.map(task => {
      const isDone = completedSet.has(task.id);
      return `
        <div style="display: flex; align-items: center; justify-content: space-between; padding: 10px 14px; background: ${isDone ? '#f0fdf4' : 'var(--bg-subtle)'}; border: 1px solid ${isDone ? '#bbf7d0' : 'var(--border-color)'}; border-radius: 6px; transition: all 0.2s;">
          <div style="display: flex; align-items: center; gap: 10px;">
            <input type="checkbox" id="task-${task.id}" ${isDone ? 'checked' : ''} style="width: 18px; height: 18px; cursor: pointer; accent-color: var(--emerald-600);" onchange="toggleDailyTask('${task.id}', ${employeeId})">
            <div>
              <label for="task-${task.id}" style="font-weight: 600; font-size: 0.9rem; cursor: pointer; text-decoration: ${isDone ? 'line-through' : 'none'}; color: ${isDone ? '#15803d' : 'var(--text-main)'};">
                ${escapeHtml(task.title)}
              </label>
              <div style="font-size: 0.78rem; color: var(--text-muted);">${escapeHtml(task.description)}</div>
            </div>
          </div>
          <div style="display: flex; align-items: center; gap: 8px;">
            <span class="badge" style="font-size: 0.72rem; background: rgba(99,102,241,0.1); color: var(--primary-700);">${task.category}</span>
            <span style="font-size: 0.75rem; color: var(--text-muted);"><i class="fa-solid fa-stopwatch"></i> ${task.estimated_minutes}m</span>
          </div>
        </div>
      `;
    }).join("");
  }
}

async function toggleDailyTask(taskId, employeeId) {
  try {
    const res = await fetch(`${API_BASE}/api/skills/daily-plan/toggle`, {
      method: "POST",
      headers: getAuthHeaders(),
      body: JSON.stringify({ employee_id: employeeId, task_id: taskId })
    });
    const data = await res.json();
    if (data.success) {
      showToast("Daily task updated! +15 XP", "success");
      await loadDashboardAnalytics(employeeId);
    }
  } catch (err) {
    showToast("Error updating task status.", "error");
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

/* =========================================================================
   NOTICE PERIOD PLANNER CONTROLLER
   ========================================================================= */

let currentSavedNoticePlan = null;

function setupNoticePlan(employee) {
  const form = document.getElementById("form-notice-planner");
  const btnRegenerate = document.getElementById("btn-notice-regenerate");
  const btnEdit = document.getElementById("btn-edit-notice-plan");
  const btnCopy = document.getElementById("btn-copy-notice-plan");
  const formSection = document.getElementById("notice-planner-form-section");
  const resultSection = document.getElementById("notice-planner-result-section");
  const errorBox = document.getElementById("notice-form-error");
  const errorText = document.getElementById("notice-form-error-text");

  // Pre-fill target role and experience from employee profile if available
  const roleInput = document.getElementById("notice-target-role");
  const expSelect = document.getElementById("notice-experience-years");
  const daysInput = document.getElementById("notice-period-days");

  if (roleInput && !roleInput.value) {
    roleInput.value = employee.target_role || employee.job_role || "Software Engineer";
  }
  if (expSelect && !expSelect.value) {
    expSelect.value = employee.experience || "1-3";
  }

  // Switch to edit/regenerate view
  function switchToFormView() {
    if (formSection) formSection.style.display = "block";
    if (resultSection) resultSection.style.display = "none";
    if (errorBox) errorBox.style.display = "none";
    if (btnRegenerate) btnRegenerate.style.display = "none";
  }

  if (btnRegenerate) btnRegenerate.addEventListener("click", switchToFormView);
  if (btnEdit) btnEdit.addEventListener("click", switchToFormView);

  // Copy plan to clipboard
  if (btnCopy) {
    btnCopy.addEventListener("click", () => {
      if (currentSavedNoticePlan && currentSavedNoticePlan.plan_text) {
        navigator.clipboard.writeText(currentSavedNoticePlan.plan_text)
          .then(() => showToast("Preparation plan copied to clipboard!", "success"))
          .catch(() => showToast("Could not copy to clipboard.", "warning"));
      }
    });
  }

  // Form submission with validation and loading state
  if (form) {
    form.addEventListener("submit", async (e) => {
      e.preventDefault();
      if (errorBox) errorBox.style.display = "none";

      const targetRole = roleInput ? roleInput.value.trim() : "";
      const experience = expSelect ? expSelect.value : "1-3";
      const noticeDaysVal = daysInput ? parseInt(daysInput.value, 10) : 30;

      // Basic form validation
      if (!targetRole) {
        if (errorBox && errorText) {
          errorText.textContent = "Please enter your target job role.";
          errorBox.style.display = "block";
        }
        if (roleInput) roleInput.focus();
        return;
      }

      if (isNaN(noticeDaysVal) || noticeDaysVal < 1 || noticeDaysVal > 365) {
        if (errorBox && errorText) {
          errorText.textContent = "Please enter a valid notice period (1 to 365 days).";
          errorBox.style.display = "block";
        }
        if (daysInput) daysInput.focus();
        return;
      }

      // Collect checked weak areas
      const weakAreas = [];
      document.querySelectorAll("input[name='notice_weak_areas']:checked").forEach(cb => {
        weakAreas.push(cb.value);
      });

      // Loading state
      const submitBtn = document.getElementById("btn-submit-notice-plan");
      const spinner = document.getElementById("notice-submit-spinner");
      const label = document.getElementById("notice-submit-label");

      if (submitBtn) submitBtn.disabled = true;
      if (spinner) spinner.style.display = "inline-block";
      if (label) label.textContent = "Generating your personalized plan...";

      try {
        const payload = {
          employee_id: employee.id,
          target_role: targetRole,
          experience: experience,
          notice_days: noticeDaysVal,
          weak_areas: weakAreas
        };

        const res = await fetch(`${API_BASE}/api/notice-plan/generate`, {
          method: "POST",
          headers: getAuthHeaders(),
          body: JSON.stringify(payload)
        });

        const result = await res.json();
        if (res.ok && result.success && result.data) {
          currentSavedNoticePlan = result.data;
          renderNoticePlanResult(result.data);
          showToast("🎉 Notice Period Preparation Plan generated successfully!", "success");
        } else {
          if (errorBox && errorText) {
            errorText.textContent = result.message || "Failed to generate plan. Please try again.";
            errorBox.style.display = "block";
          }
        }
      } catch (err) {
        console.error("Error generating notice plan:", err);
        if (errorBox && errorText) {
          errorText.textContent = "Service temporarily unavailable. Please try again.";
          errorBox.style.display = "block";
        }
      } finally {
        if (submitBtn) submitBtn.disabled = false;
        if (spinner) spinner.style.display = "none";
        if (label) label.innerHTML = `Generate Preparation Plan <i class="fa-solid fa-wand-magic-sparkles"></i>`;
      }
    });
  }
}

async function loadNoticePlan(employeeId) {
  try {
    const res = await fetch(`${API_BASE}/api/notice-plan/latest?employee_id=${employeeId}`);
    if (res.ok) {
      const data = await res.json();
      if (data.success && data.data && data.data.plan_text) {
        currentSavedNoticePlan = data.data;
        renderNoticePlanResult(data.data);
        return;
      }
    }
    // No saved plan: show empty form state
    renderNoticePlanFormState();
  } catch (err) {
    console.warn("Could not load latest notice plan:", err);
    renderNoticePlanFormState();
  }
}

function renderNoticePlanFormState() {
  const formSection = document.getElementById("notice-planner-form-section");
  const resultSection = document.getElementById("notice-planner-result-section");
  const daysBadge = document.getElementById("notice-days-left-badge");
  const btnRegenerate = document.getElementById("btn-notice-regenerate");

  if (formSection) formSection.style.display = "block";
  if (resultSection) resultSection.style.display = "none";
  if (daysBadge) daysBadge.style.display = "none";
  if (btnRegenerate) btnRegenerate.style.display = "none";
}

function renderNoticePlanResult(plan) {
  const formSection = document.getElementById("notice-planner-form-section");
  const resultSection = document.getElementById("notice-planner-result-section");
  const daysBadge = document.getElementById("notice-days-left-badge");
  const daysCount = document.getElementById("notice-days-left-count");
  const btnRegenerate = document.getElementById("btn-notice-regenerate");

  // Metadata pills
  const resRole = document.getElementById("notice-res-role");
  const resExp = document.getElementById("notice-res-exp");
  const resDays = document.getElementById("notice-res-days");
  const resWeak = document.getElementById("notice-res-weak");
  const contentBox = document.getElementById("notice-plan-content");
  const savedAt = document.getElementById("notice-plan-saved-at");

  // Pre-fill inputs in form for easy adjustment
  const roleInput = document.getElementById("notice-target-role");
  const expSelect = document.getElementById("notice-experience-years");
  const daysInput = document.getElementById("notice-period-days");
  if (roleInput && plan.target_role) roleInput.value = plan.target_role;
  if (expSelect && plan.experience) expSelect.value = plan.experience;
  if (daysInput && plan.notice_days) daysInput.value = plan.notice_days;

  // Weak area checkboxes
  const weakList = Array.isArray(plan.weak_areas)
    ? plan.weak_areas
    : (typeof plan.weak_areas === "string" ? plan.weak_areas.split(",").map(s => s.trim()) : []);
  const weakSet = new Set(weakList);
  document.querySelectorAll("input[name='notice_weak_areas']").forEach(cb => {
    cb.checked = weakSet.has(cb.value);
  });

  // Days left badge
  const daysLeft = (plan.days_left !== undefined && plan.days_left !== null) ? plan.days_left : (plan.notice_days || 30);
  if (daysCount) daysCount.textContent = daysLeft;
  if (daysBadge) daysBadge.style.display = "inline-flex";

  // Metadata labels
  if (resRole) resRole.textContent = plan.target_role || "Software Engineer";
  if (resExp) resExp.textContent = `${plan.experience || '1-3'} yrs`;
  if (resDays) resDays.textContent = `${plan.notice_days || 30} Days`;
  if (resWeak) resWeak.textContent = weakList.length > 0 ? weakList.join(", ") : "General Technical";

  if (savedAt && plan.created_at) {
    savedAt.innerHTML = `<i class="fa-solid fa-check-double text-success"></i> Plan active • Saved on: ${escapeHtml(String(plan.created_at).split('.')[0])}`;
  }

  // Format and render plan content
  if (contentBox) {
    contentBox.innerHTML = formatMarkdownToPlanHtml(plan.plan_text || "");
  }

  // Show result, hide form
  if (formSection) formSection.style.display = "none";
  if (resultSection) resultSection.style.display = "block";
  if (btnRegenerate) btnRegenerate.style.display = "inline-flex";
}

function formatMarkdownToPlanHtml(text) {
  if (!text) return "<p>No plan content available.</p>";

  // Clean and convert markdown
  let html = escapeHtml(text);

  // Headers: ##, ###, ####
  html = html.replace(/^##\s+(.*$)/gim, '<h4 style="color:var(--text-main); font-size:1.15rem; margin-top:14px; margin-bottom:8px; font-weight:700;">$1</h4>');
  html = html.replace(/^###\s+(.*$)/gim, '<h5 style="color:var(--primary-700); font-size:1.02rem; margin-top:16px; margin-bottom:6px; font-weight:600; border-bottom:1px solid var(--border-color); padding-bottom:4px;">$1</h5>');
  html = html.replace(/^####\s+(.*$)/gim, '<h6 style="color:var(--emerald-600); font-size:0.92rem; margin-top:12px; margin-bottom:4px; font-weight:600;">$1</h6>');

  // Bold text: **text**
  html = html.replace(/\*\*(.*?)\*\*/gim, '<strong style="color:var(--text-main);">$1</strong>');

  // Inline code: `code`
  html = html.replace(/`([^`]+)`/gim, '<code style="background:var(--bg-subtle); padding:2px 6px; border-radius:4px; font-size:0.85rem;">$1</code>');

  // Bullet items: - or *
  html = html.replace(/^\s*[-*]\s+(.*$)/gim, '<li style="margin-bottom:4px; color:var(--text-main);">$1</li>');

  // Wrap lists
  html = html.replace(/(<li.*<\/li>)/gms, '<ul style="margin:6px 0 10px 20px; padding:0; line-height:1.6;">$1</ul>');

  // Replace double newlines with spacing
  html = html.replace(/\n\n/g, '<div style="height:8px;"></div>');

  return html;
}

async function toggleNoticePlanTask(taskId, employeeId) {
  try {
    const res = await fetch(`${API_BASE}/api/notice-plan/task/toggle`, {
      method: "POST",
      headers: getAuthHeaders(),
      body: JSON.stringify({ employee_id: employeeId, task_id: taskId })
    });
    const data = await res.json();
    if (data.success) {
      showToast(data.is_completed ? "Task completed! +15 XP" : "Task marked pending.", "success");
      await loadNoticePlan(employeeId);
      // Sync full modal if open
      const fullModal = document.getElementById("notice-plan-full-modal");
      if (fullModal && fullModal.style.display === "flex") {
        const activeFilter = document.querySelector(".filter-plan-btn.active")?.dataset?.filter || "all";
        renderFullNoticePlanTimeline(currentActiveNoticePlan, activeFilter, employeeId);
      }
    } else {
      showToast(data.message || "Could not update task.", "error");
    }
  } catch (err) {
    showToast("Error updating notice task status.", "error");
  }
}

function openNoticeFullModal(employeeId) {
  const modal = document.getElementById("notice-plan-full-modal");
  if (!modal || !currentActiveNoticePlan) return;

  const titleEl = document.getElementById("full-modal-title");
  const subtitleEl = document.getElementById("full-modal-subtitle");
  const daysBadge = document.getElementById("full-modal-days-left-badge");
  const footerProg = document.getElementById("full-modal-footer-progress");

  if (titleEl) titleEl.textContent = `${currentActiveNoticePlan.target_role} Countdown Schedule`;
  if (subtitleEl) subtitleEl.textContent = `Last Working Date: ${currentActiveNoticePlan.last_working_date} • Daily ${currentActiveNoticePlan.daily_study_time}`;
  if (daysBadge) daysBadge.textContent = `${currentActiveNoticePlan.days_left} Days Left`;
  if (footerProg) footerProg.textContent = `${currentActiveNoticePlan.completed_tasks} of ${currentActiveNoticePlan.total_tasks} tasks completed (${currentActiveNoticePlan.progress_percent}%)`;

  // Update filter count badge
  const countAll = document.getElementById("count-filter-all");
  if (countAll && currentActiveNoticePlan.days) {
    countAll.textContent = currentActiveNoticePlan.days.length;
  }

  // Reset to 'all' filter
  document.querySelectorAll(".filter-plan-btn").forEach(b => {
    b.classList.remove("active", "btn-primary");
    if (b.dataset.filter === "all") b.classList.add("active", "btn-primary");
  });

  renderFullNoticePlanTimeline(currentActiveNoticePlan, "all", employeeId);
  modal.style.display = "flex";
}

function closeNoticeFullModal() {
  const modal = document.getElementById("notice-plan-full-modal");
  if (modal) modal.style.display = "none";
}

function renderFullNoticePlanTimeline(plan, filter = "all", employeeId) {
  const container = document.getElementById("full-plan-timeline-container");
  if (!container || !plan || !plan.days) return;

  let filteredDays = plan.days;
  if (filter === "today") {
    filteredDays = plan.days.filter(d => d.day_number === plan.current_day);
  } else if (filter === "interviews") {
    filteredDays = plan.days.filter(d => d.is_interview_prep);
  } else if (filter === "pending") {
    filteredDays = plan.days.filter(d => (d.tasks || []).some(t => !t.is_completed));
  }

  if (filteredDays.length === 0) {
    container.innerHTML = `
      <div style="text-align: center; padding: 30px; color: var(--text-muted); font-size: 0.9rem;">
        <i class="fa-solid fa-list-check" style="font-size: 2rem; margin-bottom: 8px; display: block; opacity: 0.5;"></i>
        No schedule items match the selected filter.
      </div>
    `;
    return;
  }

  container.innerHTML = filteredDays.map(day => {
    const isToday = (day.day_number === plan.current_day);
    const isInterview = Boolean(day.is_interview_prep);
    const allDone = Boolean(day.all_completed);

    let headerBg = "var(--bg-subtle)";
    let borderCol = "var(--border-color)";
    if (isToday) {
      headerBg = "rgba(79, 70, 229, 0.08)";
      borderCol = "var(--primary-600)";
    } else if (isInterview) {
      headerBg = "#fff1f2";
      borderCol = "#fecdd3";
    }

    return `
      <div class="card" style="padding: 16px; border: 1px solid ${borderCol}; border-radius: 8px; background: var(--bg-card); box-shadow: var(--shadow-xs);">
        
        <!-- Day Header -->
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; flex-wrap: wrap; gap: 8px; padding-bottom: 8px; border-bottom: 1px solid var(--border-color);">
          <div style="display: flex; align-items: center; gap: 10px; flex-wrap: wrap;">
            <span style="font-weight: 800; font-size: 0.98rem; color: var(--text-main);">
              ${escapeHtml(day.date_label || `Day ${day.day_number}`)}
            </span>
            ${isToday ? `<span class="badge badge-primary" style="font-size: 0.72rem;"><i class="fa-solid fa-star"></i> TODAY</span>` : ''}
            ${isInterview ? `<span class="badge" style="background: #fee2e2; color: #991b1b; font-size: 0.72rem;"><i class="fa-solid fa-bullseye"></i> REVISION & MOCK</span>` : ''}
            ${allDone ? `<span class="badge badge-success" style="font-size: 0.72rem;"><i class="fa-solid fa-check"></i> ALL DONE</span>` : ''}
          </div>
          <span style="font-size: 0.8rem; font-weight: 600; color: var(--text-muted);">${escapeHtml(day.theme || '')}</span>
        </div>

        ${day.interview_alert ? `
          <div style="background: #fff1f2; border: 1px solid #fecdd3; border-radius: 6px; padding: 6px 12px; margin-bottom: 10px; font-size: 0.8rem; color: #9f1239; font-weight: 600;">
            <i class="fa-solid fa-bell"></i> ${escapeHtml(day.interview_alert)}
          </div>
        ` : ''}

        <!-- Day Tasks List -->
        <div style="display: flex; flex-direction: column; gap: 8px;">
          ${(day.tasks || []).map(t => {
            const isDone = Boolean(t.is_completed);
            return `
              <div style="display: flex; align-items: center; justify-content: space-between; padding: 8px 12px; background: ${isDone ? '#f0fdf4' : 'var(--bg-subtle)'}; border: 1px solid ${isDone ? '#bbf7d0' : 'var(--border-color)'}; border-radius: 6px; font-size: 0.85rem; flex-wrap: wrap; gap: 8px;">
                <div style="display: flex; align-items: center; gap: 10px; flex: 1; min-width: 220px;">
                  <input type="checkbox" id="full-task-${t.id}" ${isDone ? 'checked' : ''} style="width: 17px; height: 17px; accent-color: var(--emerald-600); cursor: pointer;" onchange="toggleNoticePlanTask(${t.id}, ${employeeId})">
                  <div>
                    <span style="font-weight: 600; text-decoration: ${isDone ? 'line-through' : 'none'}; color: ${isDone ? '#15803d' : 'var(--text-main)'};">
                      ${escapeHtml(t.title)}
                    </span>
                    <div style="font-size: 0.78rem; color: var(--text-muted);">${escapeHtml(t.description)}</div>
                  </div>
                </div>

                <div style="display: flex; align-items: center; gap: 8px;">
                  <span class="badge" style="font-size: 0.7rem; background: rgba(99,102,241,0.08); color: var(--primary-700);">${escapeHtml(t.category)}</span>
                  <span style="font-size: 0.74rem; color: var(--text-muted);"><i class="fa-solid fa-stopwatch"></i> ${t.estimated_minutes}m</span>
                  ${t.link_url ? `
                    <a href="${t.link_url}" class="btn btn-sm btn-outline-primary" style="padding: 2px 8px; font-size: 0.74rem;">
                      Go <i class="fa-solid fa-arrow-up-right-from-square"></i>
                    </a>
                  ` : ''}
                </div>
              </div>
            `;
          }).join("")}
        </div>
      </div>
    `;
  }).join("");
}