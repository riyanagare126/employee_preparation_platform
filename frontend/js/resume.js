/**
 * AI Employee Preparation Platform - Advanced Resume Builder & 2026 Trending Templates
 * Features:
 * - 3 Trending 2026 Templates (Modern Single-Column, Minimalist Accent, Classic Reverse-Chronological)
 * - Multi-Version Manager per employee_id (Save, Load, Delete versions)
 * - AI Metric-Driven Bullet Point Rewriter
 * - AI Resume Score (ATS Friendliness & JD Keyword Match)
 * - Real-Time Split-Screen Live Preview & PDF Download
 */

let activeTemplate = "modern-single";
const SECTION_IDS = [
  "objective",
  "contact",
  "education",
  "skills",
  "soft-skills",
  "projects",
  "internships",
  "experience",
  "certifications",
  "achievements",
  "languages",
  "hobbies",
  "strengths",
  "extracurricular",
  "github",
  "linkedin",
  "portfolio"
];

let lastRewrittenBullet = "";

document.addEventListener("DOMContentLoaded", async () => {
  const employee = requireAuth();
  if (!employee) return;

  setupTemplateSelector();
  setupSectionToggles();
  setupLiveSync();
  setupVersionManager(employee);
  setupAITools(employee);
  prefillResumeForm(employee);
  await loadSavedResume(employee);
  await loadSavedVersionsList(employee.id);

  // Setup Print / Download PDF
  const btnPrint = document.getElementById("btn-print-resume");
  if (btnPrint) {
    btnPrint.addEventListener("click", () => {
      updatePreviewFromForm();
      window.print();
    });
  }

  // Quick Save
  const btnSave = document.getElementById("btn-save-resume");
  if (btnSave) {
    btnSave.addEventListener("click", () => saveResumeToBackend(employee));
  }
});

function setupTemplateSelector() {
  const templateBtns = document.querySelectorAll(".template-btn");
  const resumeSheet = document.getElementById("resume-sheet");

  templateBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      templateBtns.forEach(b => b.classList.remove("active"));
      btn.classList.add("active");

      activeTemplate = btn.getAttribute("data-template") || "modern-single";
      if (resumeSheet) {
        resumeSheet.className = `resume-paper template-${activeTemplate}`;
      }
      updatePreviewFromForm();
      showToast(`Switched to ${btn.textContent.trim().split('\n')[0]} template!`, "info");
    });
  });
}

function setupSectionToggles() {
  SECTION_IDS.forEach(secKey => {
    const chk = document.getElementById(`chk-${secKey}`);
    if (chk) {
      chk.addEventListener("change", () => {
        const isVisible = chk.checked;
        const formGroup = document.getElementById(`group-input-${secKey}`);
        if (formGroup) formGroup.style.display = isVisible ? "block" : "none";

        const previewSec = document.getElementById(`sec-${secKey}`);
        if (previewSec) previewSec.style.display = isVisible ? "block" : "none";

        if (secKey === "github") {
          const el = document.getElementById("preview-github");
          if (el) el.style.display = isVisible ? "inline" : "none";
        }
        if (secKey === "linkedin") {
          const el = document.getElementById("preview-linkedin");
          if (el) el.style.display = isVisible ? "inline" : "none";
        }
        if (secKey === "portfolio") {
          const el = document.getElementById("preview-portfolio");
          if (el) el.style.display = isVisible ? "inline" : "none";
        }
      });
    }
  });
}

function setupLiveSync() {
  const form = document.getElementById("resume-form");
  if (!form) return;

  const inputs = form.querySelectorAll("input, textarea, select");
  inputs.forEach(input => {
    input.addEventListener("input", updatePreviewFromForm);
    input.addEventListener("change", updatePreviewFromForm);
  });
}

function prefillResumeForm(employee) {
  setVal("res-input-name", employee.name || "Candidate Name");
  setVal("res-input-email", employee.email || "candidate@example.com");
  setVal("res-input-role", employee.target_role || employee.job_role || "Software Engineer");
  setVal("res-input-education", employee.qualification || "B.Tech in Computer Science and Engineering");
  setVal("res-input-skills", employee.skills || "Java, Spring Boot, SQL, Python, Git, Docker");
}

function setVal(id, val) {
  const el = document.getElementById(id);
  if (el && (!el.value || el.value.trim() === "")) {
    el.value = val;
  }
}

function getVal(id) {
  const el = document.getElementById(id);
  return el ? el.value.trim() : "";
}

function updatePreviewFromForm() {
  setText("preview-name", getVal("res-input-name") || "Your Name");
  setText("preview-role", getVal("res-input-role") || "Software Engineer");
  setText("preview-email", getVal("res-input-email") || "email@example.com");
  setText("preview-phone", getVal("res-input-phone") || "+91 98765 43210");
  setText("preview-location", getVal("res-input-location") || "City, Country");
  setText("preview-objective", getVal("res-input-objective") || "Driven software engineering professional committed to technical excellence and delivering high-value solutions.");
  setText("preview-education", getVal("res-input-education") || "B.Tech in Computer Science");
  setText("preview-skills", getVal("res-input-skills") || "Java, Python, SQL, REST APIs");
  setText("preview-soft-skills", getVal("res-input-soft-skills") || "Problem Solving, Communication, Ownership");

  renderFormattedList("preview-projects", getVal("res-input-projects"));
  renderFormattedList("preview-internships", getVal("res-input-internships"));
  renderFormattedList("preview-experience", getVal("res-input-experience"));
  renderFormattedList("preview-certifications", getVal("res-input-certifications"));
  renderFormattedList("preview-achievements", getVal("res-input-achievements"));
  renderFormattedList("preview-languages", getVal("res-input-languages"));
  renderFormattedList("preview-hobbies", getVal("res-input-hobbies"));
  renderFormattedList("preview-strengths", getVal("res-input-strengths"));
  renderFormattedList("preview-extracurricular", getVal("res-input-extracurricular"));

  setLink("preview-github", getVal("res-input-github"), "GitHub");
  setLink("preview-linkedin", getVal("res-input-linkedin"), "LinkedIn");
  setLink("preview-portfolio", getVal("res-input-portfolio"), "Portfolio");
}

function setText(id, text) {
  const el = document.getElementById(id);
  if (el) el.textContent = text;
}

function renderFormattedList(id, rawText) {
  const el = document.getElementById(id);
  if (!el) return;
  if (!rawText) {
    el.innerHTML = `<span style="color: #94a3b8; font-style: italic;">Not specified</span>`;
    return;
  }
  const lines = rawText.split("\n").filter(l => l.trim().length > 0);
  if (lines.length === 1) {
    el.textContent = lines[0];
  } else {
    el.innerHTML = `<ul style="padding-left: 18px; margin: 4px 0;">${lines.map(l => `<li>${escapeHtml(l.replace(/^[•\-\*]\s*/, ''))}</li>`).join("")}</ul>`;
  }
}

function setLink(id, url, label) {
  const el = document.getElementById(id);
  if (!el) return;
  if (url) {
    el.innerHTML = `<a href="${escapeHtml(url)}" target="_blank" style="color: inherit; text-decoration: underline;">${label}</a>`;
  } else {
    el.textContent = "";
  }
}

function gatherFormData() {
  return {
    full_name: getVal("res-input-name"),
    email: getVal("res-input-email"),
    phone: getVal("res-input-phone"),
    role: getVal("res-input-role"),
    location: getVal("res-input-location"),
    objective: getVal("res-input-objective"),
    qualification: getVal("res-input-education"),
    skills: getVal("res-input-skills"),
    soft_skills: getVal("res-input-soft-skills"),
    projects: getVal("res-input-projects"),
    internships: getVal("res-input-internships"),
    experience: getVal("res-input-experience"),
    certifications: getVal("res-input-certifications"),
    achievements: getVal("res-input-achievements"),
    languages: getVal("res-input-languages"),
    hobbies: getVal("res-input-hobbies"),
    strengths: getVal("res-input-strengths"),
    extracurricular: getVal("res-input-extracurricular"),
    github: getVal("res-input-github"),
    linkedin: getVal("res-input-linkedin"),
    portfolio: getVal("res-input-portfolio"),
    template: activeTemplate
  };
}

async function saveResumeToBackend(employee) {
  const payload = {
    employee_id: employee.id,
    ...gatherFormData()
  };

  try {
    const res = await fetch(`${API_BASE}/api/resume`, {
      method: "POST",
      headers: getAuthHeaders(),
      body: JSON.stringify(payload)
    });
    const data = await res.json();
    if (data.success) {
      showToast("Resume saved successfully!", "success");
    } else {
      showToast(data.message || "Failed to save resume.", "error");
    }
  } catch (err) {
    showToast("Error connecting to server to save resume.", "error");
  }
}

async function loadSavedResume(employee) {
  try {
    const res = await fetch(`${API_BASE}/api/resume?employee_id=${employee.id}`);
    if (res.ok) {
      const data = await res.json();
      if (data.success && data.data) {
        populateFormFromData(data.data);
      }
    }
  } catch (err) {
    console.error("Error loading resume:", err);
  }
  updatePreviewFromForm();
}

function populateFormFromData(d) {
  if (d.full_name) document.getElementById("res-input-name").value = d.full_name;
  if (d.email) document.getElementById("res-input-email").value = d.email;
  if (d.phone) document.getElementById("res-input-phone").value = d.phone;
  if (d.role) document.getElementById("res-input-role").value = d.role;
  if (d.location) document.getElementById("res-input-location").value = d.location;
  if (d.objective) document.getElementById("res-input-objective").value = d.objective;
  if (d.qualification) document.getElementById("res-input-education").value = d.qualification;
  if (d.skills) document.getElementById("res-input-skills").value = d.skills;
  if (d.soft_skills) document.getElementById("res-input-soft-skills").value = d.soft_skills;
  if (d.projects) document.getElementById("res-input-projects").value = d.projects;
  if (d.internships) document.getElementById("res-input-internships").value = d.internships;
  if (d.experience) document.getElementById("res-input-experience").value = d.experience;
  if (d.certifications) document.getElementById("res-input-certifications").value = d.certifications;
  if (d.achievements) document.getElementById("res-input-achievements").value = d.achievements;
  if (d.languages) document.getElementById("res-input-languages").value = d.languages;
  if (d.hobbies) document.getElementById("res-input-hobbies").value = d.hobbies;
  if (d.strengths) document.getElementById("res-input-strengths").value = d.strengths;
  if (d.extracurricular) document.getElementById("res-input-extracurricular").value = d.extracurricular;
  if (d.github) document.getElementById("res-input-github").value = d.github;
  if (d.linkedin) document.getElementById("res-input-linkedin").value = d.linkedin;
  if (d.portfolio) document.getElementById("res-input-portfolio").value = d.portfolio;

  if (d.template) {
    activeTemplate = d.template;
    const btns = document.querySelectorAll(".template-btn");
    btns.forEach(b => {
      if (b.getAttribute("data-template") === activeTemplate) {
        btns.forEach(x => x.classList.remove("active"));
        b.classList.add("active");
      }
    });
    const resumeSheet = document.getElementById("resume-sheet");
    if (resumeSheet) resumeSheet.className = `resume-paper template-${activeTemplate}`;
  }
}

// =========================================================================
// 2026 FEATURE: MULTI-VERSION MANAGER PER EMPLOYEE_ID
// =========================================================================
function setupVersionManager(employee) {
  const btnSaveModal = document.getElementById("btn-save-version-modal");
  const btnLoad = document.getElementById("btn-load-version");
  const btnDelete = document.getElementById("btn-delete-version");
  const selectVer = document.getElementById("select-resume-version");

  if (btnSaveModal) {
    btnSaveModal.addEventListener("click", async () => {
      const defaultName = `${employee.target_company || 'Enterprise'} - ${getVal('res-input-role') || 'Draft'} v${Date.now().toString().slice(-4)}`;
      const versionName = prompt("Enter a name for this resume version:", defaultName);
      if (!versionName || !versionName.trim()) return;

      const payload = {
        employee_id: employee.id,
        version_name: versionName.trim(),
        template_name: activeTemplate,
        target_role: getVal("res-input-role") || "Software Engineer",
        target_company: employee.target_company || "Enterprise",
        resume_data: gatherFormData(),
        score: 88
      };

      try {
        const res = await fetch(`${API_BASE}/api/resume/versions/save`, {
          method: "POST",
          headers: getAuthHeaders(),
          body: JSON.stringify(payload)
        });
        const data = await res.json();
        if (data.success) {
          showToast(`Saved version "${versionName}"!`, "success");
          await loadSavedVersionsList(employee.id);
        }
      } catch (e) {
        showToast("Error saving version.", "error");
      }
    });
  }

  if (btnLoad && selectVer) {
    btnLoad.addEventListener("click", async () => {
      const verId = selectVer.value;
      if (!verId) {
        showToast("Please select a saved version from the dropdown.", "info");
        return;
      }
      try {
        const res = await fetch(`${API_BASE}/api/resume/versions/${verId}?employee_id=${employee.id}`);
        const data = await res.json();
        if (data.success && data.data && data.data.resume_data) {
          populateFormFromData(data.data.resume_data);
          updatePreviewFromForm();
          const indicator = document.getElementById("version-status-indicator");
          if (indicator) indicator.textContent = `Active: ${data.data.version_name}`;
          showToast(`Loaded version: "${data.data.version_name}"`, "success");
        }
      } catch (e) {
        showToast("Error loading version.", "error");
      }
    });
  }

  if (btnDelete && selectVer) {
    btnDelete.addEventListener("click", async () => {
      const verId = selectVer.value;
      if (!verId) {
        showToast("Select a version to delete.", "info");
        return;
      }
      if (!confirm("Are you sure you want to delete this saved version?")) return;

      try {
        const res = await fetch(`${API_BASE}/api/resume/versions/${verId}?employee_id=${employee.id}`, {
          method: "DELETE"
        });
        const data = await res.json();
        if (data.success) {
          showToast("Version deleted.", "info");
          await loadSavedVersionsList(employee.id);
        }
      } catch (e) {
        showToast("Error deleting version.", "error");
      }
    });
  }
}

async function loadSavedVersionsList(employeeId) {
  const selectVer = document.getElementById("select-resume-version");
  if (!selectVer) return;

  try {
    const res = await fetch(`${API_BASE}/api/resume/versions?employee_id=${employeeId}`);
    if (res.ok) {
      const data = await res.json();
      if (data.success && data.versions) {
        selectVer.innerHTML = `<option value="">-- Select Saved Version to Load (${data.versions.length}) --</option>` +
          data.versions.map(v => `<option value="${v.id}">${escapeHtml(v.version_name)} (${escapeHtml(v.template_name)} - ${v.score || 85}%)</option>`).join("");
      }
    }
  } catch (e) {}
}

// =========================================================================
// 2026 FEATURE: AI BULLET REWRITER & ATS SCORER
// =========================================================================
function setupAITools(employee) {
  // 1. AI Bullet Rewriter
  const btnRewrite = document.getElementById("btn-ai-rewrite-bullet");
  const rawBulletInput = document.getElementById("input-raw-bullet");
  const resultBox = document.getElementById("ai-bullet-result");
  const textEl = document.getElementById("ai-rewritten-text");
  const explEl = document.getElementById("ai-rewritten-expl");
  const btnApply = document.getElementById("btn-apply-bullet");

  if (btnRewrite && rawBulletInput) {
    btnRewrite.addEventListener("click", async () => {
      const raw = rawBulletInput.value.trim();
      if (!raw) {
        showToast("Please enter a bullet point to enhance.", "info");
        return;
      }

      btnRewrite.disabled = true;
      btnRewrite.textContent = "Enhancing...";

      try {
        const res = await fetch(`${API_BASE}/api/resume/rewrite-bullet`, {
          method: "POST",
          headers: getAuthHeaders(),
          body: JSON.stringify({
            bullet_text: raw,
            target_role: getVal("res-input-role") || "Software Engineer"
          })
        });
        const data = await res.json();
        if (data.success) {
          lastRewrittenBullet = data.rewritten_bullet;
          resultBox.style.display = "block";
          textEl.innerHTML = `<i class="fa-solid fa-wand-magic-sparkles text-primary"></i> "${escapeHtml(data.rewritten_bullet)}"`;
          explEl.textContent = `${data.score_boost} • ${data.explanation}`;
          showToast("Bullet point enhanced with STAR metrics!", "success");
        } else {
          showToast(data.message || "Failed to rewrite bullet.", "error");
        }
      } catch (e) {
        showToast("Error connecting to AI bullet rewriter.", "error");
      } finally {
        btnRewrite.disabled = false;
        btnRewrite.innerHTML = 'Rewrite <i class="fa-solid fa-wand-magic-sparkles"></i>';
      }
    });
  }

  if (btnApply) {
    btnApply.addEventListener("click", () => {
      if (!lastRewrittenBullet) return;
      const expArea = document.getElementById("res-input-experience");
      if (expArea) {
        if (expArea.value.trim()) {
          expArea.value += "\n" + lastRewrittenBullet;
        } else {
          expArea.value = lastRewrittenBullet;
        }
        updatePreviewFromForm();
        showToast("Applied rewritten bullet to Experience!", "success");
        rawBulletInput.value = "";
        resultBox.style.display = "none";
      }
    });
  }

  // 2. AI Resume ATS Score
  const btnCalcATS = document.getElementById("btn-calculate-ats");
  const jdInput = document.getElementById("input-jd-keywords");
  const atsBox = document.getElementById("ats-score-result");
  const scoreVal = document.getElementById("ats-score-val");
  const matchRatio = document.getElementById("ats-match-ratio");
  const summaryEl = document.getElementById("ats-keywords-summary");

  if (btnCalcATS) {
    btnCalcATS.addEventListener("click", async () => {
      btnCalcATS.disabled = true;
      btnCalcATS.textContent = "Scanning...";

      try {
        const res = await fetch(`${API_BASE}/api/resume/score-ats`, {
          method: "POST",
          headers: getAuthHeaders(),
          body: JSON.stringify({
            resume_data: gatherFormData(),
            target_role: getVal("res-input-role") || "Software Engineer",
            job_description: jdInput ? jdInput.value.trim() : ""
          })
        });
        const data = await res.json();
        if (data.success) {
          atsBox.style.display = "block";
          scoreVal.textContent = `${data.overall_score}%`;
          matchRatio.textContent = `${data.keyword_match_percentage}% Keyword Match`;
          summaryEl.innerHTML = `
            <div><strong>Detected Keywords:</strong> ${data.detected_keywords.join(", ") || "None"}</div>
            ${data.missing_keywords && data.missing_keywords.length ? `<div style="color: #b91c1c; margin-top: 2px;"><strong>Missing:</strong> ${data.missing_keywords.join(", ")}</div>` : ''}
            <div style="margin-top: 4px; color: #166534;"><strong>Tip:</strong> ${data.suggestions[0] || 'Clean ATS formatting'}</div>
          `;
          showToast(`ATS Analysis Complete: Score ${data.overall_score}%`, "success");
        }
      } catch (e) {
        showToast("Error calculating ATS score.", "error");
      } finally {
        btnCalcATS.disabled = false;
        btnCalcATS.innerHTML = 'Analyze <i class="fa-solid fa-robot"></i>';
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
