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
  await loadCompanyPreparationBanner(employee);
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

    // 3. Fetch Daily Preparation Plan
    const resPlan = await fetch(`${API_BASE}/api/skills/daily-plan?employee_id=${employeeId}`);
    if (resPlan.ok) {
      const data = await resPlan.json();
      if (data.success && data.data) {
        renderDailyPlan(data.data, employeeId);
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