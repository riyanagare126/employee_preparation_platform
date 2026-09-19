/**
 * AI Employee Preparation Platform - Skill Assessment Controller
 */

document.addEventListener("DOMContentLoaded", async () => {
  const employee = requireAuth();
  if (!employee) return;

  await loadSkillAssessment(employee.id);

  const btnReEval = document.getElementById("btn-re-evaluate");
  if (btnReEval) {
    btnReEval.addEventListener("click", async () => {
      btnReEval.disabled = true;
      btnReEval.textContent = "Analyzing...";
      await loadSkillAssessment(employee.id);
      btnReEval.disabled = false;
      btnReEval.innerHTML = '<i class="fa-solid fa-arrows-rotate"></i> Re-Evaluate Skills';
      showToast("Skill competencies updated successfully!", "success");
    });
  }
});

async function loadSkillAssessment(employeeId) {
  try {
    const res = await fetch(`${API_BASE}/api/skills/assessment?employee_id=${employeeId}`);
    if (!res.ok) throw new Error("Failed to load skill assessment");

    const data = await res.json();
    if (data.success && data.data) {
      renderSkillAssessment(data.data);
    }
  } catch (err) {
    console.error("Skill assessment load error:", err);
    showToast("Could not retrieve skill assessment data.", "error");
  }
}

function renderSkillAssessment(data) {
  const readinessVal = document.getElementById("overall-readiness-val");
  const roleBadge = document.getElementById("target-role-badge");
  const strongCount = document.getElementById("strong-count");
  const avgCount = document.getElementById("avg-count");
  const weakCount = document.getElementById("weak-count");

  if (readinessVal) readinessVal.textContent = `${data.overall_readiness_score || 0}%`;
  if (roleBadge) roleBadge.textContent = `Target Role: ${data.target_role || "Software Engineer"}`;
  if (strongCount) strongCount.textContent = (data.strong_skills || []).length;
  if (avgCount) avgCount.textContent = (data.average_skills || []).length;
  if (weakCount) weakCount.textContent = (data.weak_skills || []).length;

  // Render Strong Skills
  renderSkillCards("strong-skills-list", data.strong_skills, '<i class="fa-solid fa-circle text-success status-indicator-dot"></i>', "#166534", "#dcfce7");
  // Render Average Skills
  renderSkillCards("average-skills-list", data.average_skills, '<i class="fa-solid fa-circle text-warning status-indicator-dot"></i>', "#854d0e", "#fef9c3");
  // Render Weak Skills
  renderSkillCards("weak-skills-list", data.weak_skills, '<i class="fa-solid fa-circle text-danger status-indicator-dot"></i>', "#991b1b", "#fee2e2");

  // Render Recommendations
  const recsContainer = document.getElementById("recommendations-list");
  if (recsContainer) {
    if (data.recommendations && data.recommendations.length > 0) {
      recsContainer.innerHTML = data.recommendations.map(rec => `
        <div style="background: var(--bg-subtle); border-left: 4px solid var(--primary-600); padding: 14px 18px; border-radius: var(--radius-sm); display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 10px;">
          <div style="display: flex; align-items: center; gap: 10px; font-weight: 500; font-size: 0.95rem;">
            <span><i class="fa-solid fa-lightbulb text-warning"></i></span>
            <span>${rec}</span>
          </div>
          <a href="preparation.html" class="btn btn-secondary btn-sm" style="font-size: 0.8rem;">Practice Now <i class="fa-solid fa-arrow-right"></i></a>
        </div>
      `).join("");
    } else {
      recsContainer.innerHTML = `<div style="color: var(--text-muted);">No urgent gaps identified. Keep maintaining your preparation streak!</div>`;
    }
  }
}

function renderSkillCards(containerId, skillsList, icon, textColor, bgColor) {
  const container = document.getElementById(containerId);
  if (!container) return;

  if (!skillsList || skillsList.length === 0) {
    container.innerHTML = `<div style="color: var(--text-muted); font-size: 0.88rem; font-style: italic;">No items in this category.</div>`;
    return;
  }

  container.innerHTML = skillsList.map(s => `
    <div style="background: ${bgColor}; border-radius: var(--radius-sm); padding: 12px 16px; display: flex; align-items: center; justify-content: space-between;">
      <div style="font-weight: 600; color: ${textColor}; font-size: 0.92rem; display: flex; align-items: center; gap: 8px;">
        <span>${icon}</span>
        <span>${s.name}</span>
      </div>
      <span style="font-size: 0.82rem; font-weight: 700; color: ${textColor}; background: rgba(255,255,255,0.7); padding: 2px 8px; border-radius: 999px;">
        ${s.score ? `${s.score}%` : s.badge}
      </span>
    </div>
  `).join("");
}
