/**
 * AI Employee Preparation Platform - Preparation History Controller
 */

document.addEventListener("DOMContentLoaded", async () => {
  const employee = requireAuth();
  if (!employee) return;

  await loadHistory(employee.id);
});

async function loadHistory(employeeId) {
  try {
    const res = await fetch(`${API_BASE}/api/history/timeline?employee_id=${employeeId}`);
    if (!res.ok) throw new Error("Failed to load history");

    const data = await res.json();
    if (data.success) {
      renderCompanyProgress(data.company_progress || []);
      renderHistory(data.timeline || []);
    }
  } catch (err) {
    console.error("History load error:", err);
    showToast("Could not load history timeline.", "error");
  }
}

function renderCompanyProgress(companies) {
  const container = document.getElementById("company-progress-grid");
  if (!container) return;

  if (!companies || companies.length === 0) {
    container.innerHTML = `<div style="color: var(--text-muted); font-size: 0.88rem;">No company preparations started yet. Select a company on the Companies page to begin!</div>`;
    return;
  }

  container.innerHTML = companies.map(c => `
    <div style="background: var(--bg-subtle); padding: 14px 18px; border-radius: var(--radius-md); border: 1px solid var(--border-color);">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
        <strong style="color: var(--text-main); font-size: 1rem;">🏢 ${escapeHtml(c.company_name || c.company_slug.toUpperCase())}</strong>
        <span class="badge badge-primary">${Math.round(c.progress || 0)}%</span>
      </div>
      <div style="font-size: 0.82rem; color: var(--text-muted); margin-bottom: 8px;">Target Role: ${escapeHtml(c.role_name || 'Software Engineer')}</div>
      <div style="display: flex; gap: 8px; font-size: 0.78rem; flex-wrap: wrap;">
        <span class="badge" style="background: #e0f2fe; color: #0369a1;">Aptitude: ${Math.round(c.aptitude_progress || 0)}%</span>
        <span class="badge" style="background: #dcfce7; color: #166534;">Coding: ${Math.round(c.coding_progress || 0)}%</span>
        <span class="badge" style="background: #f3e8ff; color: #6b21a8;">Interview: ${Math.round(c.interview_progress || 0)}%</span>
      </div>
    </div>
  `).join("");
}

function renderHistory(timeline) {
  const container = document.getElementById("history-timeline-container");
  const countText = document.getElementById("history-count-text");

  if (countText) countText.textContent = `Total Activities: ${timeline.length}`;
  if (!container) return;

  if (!timeline || timeline.length === 0) {
    container.innerHTML = `<div style="color: var(--text-muted); text-align: center; padding: 40px 0;">No activities recorded yet. Complete an Aptitude Test, Coding Challenge, or Mock Interview to view your timeline!</div>`;
    return;
  }

  container.innerHTML = timeline.map(item => {
    let icon = item.icon || "📝";
    let badgeClass = "badge-info";

    if (item.type === "aptitude") {
      icon = "🧮";
      badgeClass = "badge-primary";
    } else if (item.type === "coding") {
      icon = "💻";
      badgeClass = "badge-success";
    } else if (item.type === "interview") {
      icon = "🎙️";
      badgeClass = "badge-purple";
    } else if (item.type === "resume") {
      icon = "📄";
      badgeClass = "badge-warning";
    }

    const dateFormatted = item.date ? new Date(item.date).toLocaleString(undefined, { dateStyle: "medium", timeStyle: "short" }) : "Recently";

    return `
      <div style="display: flex; align-items: center; justify-content: space-between; background: var(--bg-subtle); padding: 14px 18px; border-radius: var(--radius-sm); border: 1px solid var(--border-color); flex-wrap: wrap; gap: 12px;">
        <div style="display: flex; align-items: center; gap: 14px;">
          <span style="font-size: 1.6rem;">${icon}</span>
          <div>
            <div style="font-weight: 700; color: var(--text-main); font-size: 0.95rem;">${escapeHtml(item.title)}</div>
            <div style="font-size: 0.82rem; color: var(--text-muted);">Recorded: ${dateFormatted}</div>
          </div>
        </div>

        <div style="display: flex; align-items: center; gap: 12px;">
          <span style="font-weight: 600; font-size: 0.9rem; color: var(--primary-700);">${escapeHtml(item.score)}</span>
          <span class="badge ${badgeClass}">${escapeHtml(item.rating)}</span>
        </div>
      </div>
    `;
  }).join("");
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
