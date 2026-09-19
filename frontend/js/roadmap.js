/**
 * AI Employee Preparation Platform - Smart Prep Roadmap Controller (2026 Core Feature)
 * Real DB persistence per employee_id, day-wise checklist, and auto-calibration
 */

document.addEventListener("DOMContentLoaded", async () => {
  const employee = requireAuth();
  if (!employee) return;

  let currentRoadmap = null;

  const selectCompany = document.getElementById("select-target-company");
  const customGroup = document.getElementById("custom-company-group");
  const customInput = document.getElementById("input-custom-company");
  const selectRole = document.getElementById("select-target-role");
  const selectDuration = document.getElementById("select-duration");
  const formGenerate = document.getElementById("form-generate-roadmap");
  const btnSubmit = document.getElementById("btn-generate-submit");
  const btnAutoAdjust = document.getElementById("btn-auto-adjust");

  // Sync initial dropdown values from employee profile if available
  if (employee.target_company) {
    const matchedOpt = Array.from(selectCompany.options).find(o => o.value.toLowerCase() === employee.target_company.toLowerCase());
    if (matchedOpt) {
      selectCompany.value = matchedOpt.value;
    } else {
      selectCompany.value = "Custom / Other Enterprise";
      if (customGroup && customInput) {
        customGroup.style.display = "block";
        customInput.value = employee.target_company;
      }
    }
  }

  if (employee.target_role) {
    const matchedRole = Array.from(selectRole.options).find(o => o.value.toLowerCase() === employee.target_role.toLowerCase());
    if (matchedRole) selectRole.value = matchedRole.value;
  }

  // Toggle custom company input visibility
  if (selectCompany) {
    selectCompany.addEventListener("change", () => {
      if (selectCompany.value === "Custom / Other Enterprise") {
        customGroup.style.display = "block";
        customInput.focus();
      } else {
        customGroup.style.display = "none";
      }
    });
  }

  // Load existing roadmap
  await loadSmartRoadmap(employee.id);

  // Handle Roadmap Generation Form
  if (formGenerate) {
    formGenerate.addEventListener("submit", async (e) => {
      e.preventDefault();

      let compName = selectCompany.value;
      let compSlug = selectCompany.selectedOptions[0]?.getAttribute("data-slug") || (compName ? getCompanySlugFromName(compName) : "");

      if (compName === "Custom / Other Enterprise") {
        compName = customInput.value.trim() || "Custom Enterprise";
        compSlug = compName.toLowerCase().replace(/[^a-z0-9]/g, "-");
      }

      const target_role = selectRole.value;
      const duration_days = parseInt(selectDuration.value) || 14;

      btnSubmit.disabled = true;
      btnSubmit.innerHTML = `<span class="spinner-sm"></span> Tailoring AI Roadmap...`;

      try {
        const res = await fetch(`${API_BASE}/api/roadmap/smart/generate`, {
          method: "POST",
          headers: getAuthHeaders(),
          body: JSON.stringify({
            employee_id: employee.id,
            company_name: compName,
            company_slug: compSlug,
            target_role: target_role,
            duration_days: duration_days
          })
        });

        const data = await res.json();
        if (data.success && data.data) {
          showToast(`Generated ${duration_days}-Day Roadmap for ${compName}!`, "success");
          currentRoadmap = data.data;
          renderRoadmap(currentRoadmap, employee.id);
        } else {
          showToast(data.message || "Failed to generate roadmap.", "error");
        }
      } catch (err) {
        showToast("Error connecting to server to generate roadmap.", "error");
      } finally {
        btnSubmit.disabled = false;
        btnSubmit.innerHTML = `Generate AI Roadmap <i class="fa-solid fa-rocket"></i>`;
      }
    });
  }

  // Auto-Calibrate with AI
  if (btnAutoAdjust) {
    btnAutoAdjust.addEventListener("click", async () => {
      if (!currentRoadmap || !currentRoadmap.id) {
        showToast("Please generate or select a roadmap first.", "info");
        return;
      }

      btnAutoAdjust.disabled = true;
      btnAutoAdjust.textContent = "Calibrating...";

      try {
        const res = await fetch(`${API_BASE}/api/roadmap/smart/adjust`, {
          method: "POST",
          headers: getAuthHeaders(),
          body: JSON.stringify({
            employee_id: employee.id,
            roadmap_id: currentRoadmap.id
          })
        });

        const data = await res.json();
        if (data.success) {
          showToast(data.message, "success");
          const alertBox = document.getElementById("calibration-alert");
          if (alertBox) {
            alertBox.style.display = "block";
            alertBox.innerHTML = `<strong><i class="fa-solid fa-robot"></i> AI Diagnostic Calibration:</strong> ${escapeHtml(data.ai_notes || '')}`;
          }
          const notesEl = document.getElementById("active-roadmap-notes");
          if (notesEl && data.ai_notes) notesEl.textContent = data.ai_notes;
        } else {
          showToast(data.message || "Could not calibrate roadmap.", "error");
        }
      } catch (err) {
        showToast("Error connecting to calibration engine.", "error");
      } finally {
        btnAutoAdjust.disabled = false;
        btnAutoAdjust.innerHTML = '<i class="fa-solid fa-bolt"></i> Auto-Calibrate with AI';
      }
    });
  }

  async function loadSmartRoadmap(employeeId) {
    try {
      const res = await fetch(`${API_BASE}/api/roadmap/smart?employee_id=${employeeId}`);
      if (res.ok) {
        const data = await res.json();
        if (data.success && data.data) {
          currentRoadmap = data.data;
          renderRoadmap(currentRoadmap, employeeId);
        }
      }
    } catch (err) {
      console.error("Error loading smart roadmap:", err);
    }
  }

  function renderRoadmap(roadmap, employeeId) {
    const titleEl = document.getElementById("active-roadmap-title");
    const roleBadge = document.getElementById("active-roadmap-role-badge");
    const notesEl = document.getElementById("active-roadmap-notes");
    const pctEl = document.getElementById("roadmap-pct-text");
    const ratioEl = document.getElementById("roadmap-tasks-ratio");
    const barFill = document.getElementById("roadmap-bar-fill");
    const streakEl = document.getElementById("roadmap-streak-val");
    const container = document.getElementById("roadmap-tasks-container");

    if (titleEl) titleEl.textContent = `${roadmap.company_name} — ${roadmap.duration_days} Days`;
    if (roleBadge) roleBadge.textContent = roadmap.target_role || "Software Engineer";
    if (notesEl) notesEl.textContent = roadmap.ai_notes || "Tailored to company interview pattern. Click task checkboxes as you complete daily goals.";

    const pct = Math.round(roadmap.progress_percent || 0);
    if (pctEl) pctEl.textContent = `${pct}%`;
    if (ratioEl) ratioEl.textContent = `${roadmap.completed_tasks || 0} of ${roadmap.total_tasks || 0} tasks completed`;
    if (barFill) barFill.style.width = `${pct}%`;
    if (streakEl) streakEl.innerHTML = `<i class="fa-solid fa-fire text-warning"></i> ${roadmap.streak_days || 5}d`;

    if (container && roadmap.tasks) {
      if (roadmap.tasks.length === 0) {
        container.innerHTML = `<div style="text-align: center; color: var(--text-muted); padding: 24px;">No tasks found. Click "Generate AI Roadmap" above to create your schedule.</div>`;
        return;
      }

      container.innerHTML = roadmap.tasks.map(task => {
        const isDone = Boolean(task.is_completed);
        const catClass = getCategoryBadge(task.category);

        return `
          <div class="roadmap-day-card ${isDone ? 'completed' : ''}" id="task-card-${task.id}">
            <div style="display: flex; align-items: flex-start; gap: 16px; flex: 1;">
              <input type="checkbox" class="roadmap-checkbox" id="chk-task-${task.id}" 
                ${isDone ? 'checked' : ''} 
                onchange="toggleTask(${task.id}, ${employeeId})">
              
              <div style="flex: 1;">
                <div style="display: flex; align-items: center; gap: 8px; flex-wrap: wrap; margin-bottom: 4px;">
                  <span style="font-size: 0.78rem; font-weight: 700; color: #64748b; text-transform: uppercase;">
                    ${escapeHtml(task.phase_name)}
                  </span>
                  <span class="badge ${catClass}" style="font-size: 0.72rem;">${escapeHtml(task.category)}</span>
                  <span style="font-size: 0.75rem; color: #94a3b8;"><i class="fa-solid fa-stopwatch"></i> ${task.estimated_minutes} mins</span>
                </div>

                <label for="chk-task-${task.id}" style="font-weight: 700; font-size: 1.05rem; cursor: pointer; color: ${isDone ? '#15803d' : 'var(--text-main)'}; text-decoration: ${isDone ? 'line-through' : 'none'};">
                  ${escapeHtml(task.title)}
                </label>
                <p style="font-size: 0.88rem; color: var(--text-muted); margin: 4px 0 0 0; line-height: 1.5;">
                  ${escapeHtml(task.description)}
                </p>
              </div>
            </div>

            <div style="text-align: right; flex-shrink: 0;">
              <span style="font-size: 0.8rem; font-weight: 600; color: ${isDone ? '#16a34a' : '#94a3b8'};">
                ${isDone ? '<i class="fa-solid fa-check text-success"></i> Completed' : 'Pending'}
              </span>
            </div>
          </div>
        `;
      }).join("");
    }
  }

  function getCategoryBadge(cat) {
    const c = (cat || "").toLowerCase();
    if (c.includes("coding")) return "badge-success";
    if (c.includes("aptitude")) return "badge-primary";
    if (c.includes("fluency")) return "badge-purple";
    if (c.includes("interview") || c.includes("mock")) return "badge-danger";
    if (c.includes("behavioral")) return "badge-warning";
    return "badge-primary";
  }
});

async function toggleTask(taskId, employeeId) {
  try {
    const res = await fetch(`${API_BASE}/api/roadmap/smart/task/toggle`, {
      method: "POST",
      headers: getAuthHeaders(),
      body: JSON.stringify({ employee_id: employeeId, task_id: taskId })
    });
    const data = await res.json();
    if (data.success) {
      const card = document.getElementById(`task-card-${taskId}`);
      if (card) {
        if (data.is_completed) {
          card.classList.add("completed");
          showToast("Task completed! +15 XP earned", "success");
        } else {
          card.classList.remove("completed");
          showToast("Task marked as pending.", "info");
        }
      }

      const pctEl = document.getElementById("roadmap-pct-text");
      const ratioEl = document.getElementById("roadmap-tasks-ratio");
      const barFill = document.getElementById("roadmap-bar-fill");

      if (pctEl) pctEl.textContent = `${Math.round(data.progress_percent)}%`;
      if (ratioEl) ratioEl.textContent = `${data.completed_tasks} of ${data.total_tasks} tasks completed`;
      if (barFill) barFill.style.width = `${data.progress_percent}%`;
    } else {
      showToast(data.message || "Failed to update task.", "error");
    }
  } catch (err) {
    showToast("Error updating task.", "error");
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
