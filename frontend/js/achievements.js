/**
 * AI Employee Preparation Platform - Achievements Controller
 */

document.addEventListener("DOMContentLoaded", async () => {
  const employee = requireAuth();
  if (!employee) return;

  await loadAchievements(employee.id);
});

async function loadAchievements(employeeId) {
  try {
    const res = await fetch(`${API_BASE}/api/gamification/stats?employee_id=${employeeId}`);
    if (!res.ok) throw new Error("Failed to load gamification stats");

    const data = await res.json();
    if (data.success) {
      renderAchievements(data.stats, data.badges);
    }
  } catch (err) {
    console.error("Achievements load error:", err);
    showToast("Could not load achievements.", "error");
  }
}

function renderAchievements(stats, badges) {
  const ptsVal = document.getElementById("achieve-points-val");
  const lvlVal = document.getElementById("achieve-level-val");
  const streakVal = document.getElementById("achieve-streak-val");
  const unlockedCount = document.getElementById("achieve-unlocked-count");

  if (ptsVal) ptsVal.textContent = stats.points || 50;
  if (lvlVal) lvlVal.textContent = `Level ${stats.level || 1}`;
  if (streakVal) streakVal.textContent = `${stats.streak_days || 1} Day${stats.streak_days > 1 ? 's' : ''}`;

  const unlockedList = (badges || []).filter(b => b.unlocked);
  if (unlockedCount) unlockedCount.textContent = `${unlockedList.length} / ${(badges || []).length}`;

  const grid = document.getElementById("badges-grid");
  if (!grid) return;

  grid.innerHTML = (badges || []).map(b => {
    const isUnlocked = b.unlocked;

    return `
      <div style="background: ${isUnlocked ? 'var(--bg-card)' : 'var(--bg-subtle)'}; border: 1px solid ${isUnlocked ? 'var(--primary-200)' : 'var(--border-color)'}; border-radius: var(--radius-md); padding: 18px; display: flex; flex-direction: column; justify-content: space-between; opacity: ${isUnlocked ? '1' : '0.65'}; transition: var(--transition);">
        <div>
          <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 10px;">
            <span style="font-size: 2.2rem; color: ${isUnlocked ? 'var(--primary-600)' : 'var(--text-muted)'};">
              <i class="fa-solid ${{
                badge_aptitude_starter: 'fa-bullseye',
                badge_aptitude_master: 'fa-brain',
                badge_coding_beginner: 'fa-laptop-code',
                badge_coding_master: 'fa-rocket',
                badge_interview_ready: 'fa-microphone',
                badge_resume_ready: 'fa-file-lines',
                badge_streak_3: 'fa-fire',
                badge_streak_7: 'fa-bolt'
              }[b.id] || 'fa-award'}"></i>
            </span>
            <span class="badge ${isUnlocked ? 'badge-success' : 'badge-info'}" style="font-size: 0.75rem;">
              ${isUnlocked ? '<i class="fa-solid fa-check"></i> Unlocked' : '<i class="fa-solid fa-lock"></i> Locked'}
            </span>
          </div>

          <div style="font-weight: 700; color: var(--text-main); font-size: 1rem; margin-bottom: 4px;">${b.name}</div>
          <p style="font-size: 0.84rem; color: var(--text-muted); line-height: 1.4;">${b.desc}</p>
        </div>
      </div>
    `;
  }).join("");
}
