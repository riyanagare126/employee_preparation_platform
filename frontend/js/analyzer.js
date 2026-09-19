/**
 * AI Employee Preparation Platform - Resume Analyzer Controller
 */

document.addEventListener("DOMContentLoaded", async () => {
  const employee = requireAuth();
  if (!employee) return;

  const roleInput = document.getElementById("analyzer-role-input");
  if (roleInput && employee.job_role) {
    roleInput.value = employee.job_role;
  }

  // Load prior analysis if exists
  await loadPriorAnalysis(employee.id);

  // Setup Button Handlers
  const btnRun = document.getElementById("btn-run-analysis");
  const btnAutofill = document.getElementById("btn-autofill-builder");

  if (btnAutofill) {
    btnAutofill.addEventListener("click", async () => {
      await autofillFromBuilder(employee.id);
    });
  }

  if (btnRun) {
    btnRun.addEventListener("click", async () => {
      await runAnalysis(employee.id);
    });
  }
});

async function autofillFromBuilder(employeeId) {
  try {
    const res = await fetch(`${API_BASE}/api/resume?employee_id=${employeeId}`);
    if (res.ok) {
      const data = await res.json();
      if (data.success && data.data) {
        const r = data.data;
        const text = `
Full Name: ${r.full_name || ''}
Target Role: ${r.role || ''}
Email: ${r.email || ''} | Phone: ${r.phone || ''}
GitHub: ${r.github || ''} | LinkedIn: ${r.linkedin || ''} | Portfolio: ${r.portfolio || ''}

CAREER OBJECTIVE:
${r.objective || ''}

EDUCATION:
${r.qualification || ''}

TECHNICAL SKILLS:
${r.skills || ''}

SOFT SKILLS:
${r.soft_skills || ''}

PROJECTS:
${r.projects || ''}

INTERNSHIPS & EXPERIENCE:
${r.internships || ''}
${r.experience || ''}

CERTIFICATIONS & ACHIEVEMENTS:
${r.certifications || ''}
${r.achievements || ''}
        `.trim();

        const ta = document.getElementById("analyzer-resume-text");
        if (ta) ta.value = text;
        showToast("Resume loaded from builder!", "success");
      } else {
        showToast("No saved builder resume found. Please paste text.", "info");
      }
    }
  } catch (err) {
    showToast("Error loading builder data.", "error");
  }
}

async function runAnalysis(employeeId) {
  const resumeText = document.getElementById("analyzer-resume-text")?.value || "";
  const role = document.getElementById("analyzer-role-input")?.value || "Software Engineer";
  const btnRun = document.getElementById("btn-run-analysis");

  if (!resumeText.trim()) {
    showToast("Please provide resume text to analyze.", "error");
    return;
  }

  if (btnRun) {
    btnRun.disabled = true;
    btnRun.textContent = "Scanning ATS Score & Keywords...";
  }

  try {
    const res = await fetch(`${API_BASE}/api/resume/analyze`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        employee_id: employeeId,
        resume_text: resumeText,
        target_role: role
      })
    });

    if (res.ok) {
      const data = await res.json();
      if (data.success && data.report) {
        renderAnalysisReport(data.report);
        showToast("Resume scan complete!", "success");
      }
    } else {
      showToast("Analysis failed. Please try again.", "error");
    }
  } catch (err) {
    console.error("Resume analysis error:", err);
    showToast("Server connection error.", "error");
  } finally {
    if (btnRun) {
      btnRun.disabled = false;
      btnRun.innerHTML = '<i class="fa-solid fa-magnifying-glass"></i> Analyze Resume & ATS Match';
    }
  }
}

async function loadPriorAnalysis(employeeId) {
  try {
    const res = await fetch(`${API_BASE}/api/resume/analysis-history?employee_id=${employeeId}`);
    if (res.ok) {
      const data = await res.json();
      if (data.success && data.data) {
        const d = data.data;
        renderAnalysisReport({
          overall_score: d.overall_score,
          readability_score: d.readability_score,
          relevance_score: d.relevance_score,
          strengths: d.strengths_json || [],
          missing: d.missing_json || [],
          recommended_keywords: d.keywords_json || [],
          suggestions: d.suggestions_json || []
        });
      }
    }
  } catch (err) {}
}

function renderAnalysisReport(report) {
  const placeholder = document.getElementById("analysis-empty-placeholder");
  const resultsBox = document.getElementById("analysis-results-box");

  if (placeholder) placeholder.style.display = "none";
  if (resultsBox) resultsBox.style.display = "block";

  const scoreVal = document.getElementById("res-score-val");
  const readVal = document.getElementById("res-readability-val");
  const relVal = document.getElementById("res-relevance-val");

  if (scoreVal) scoreVal.textContent = `${report.overall_score || 75}/100`;
  if (readVal) readVal.textContent = `${report.readability_score || 80}%`;
  if (relVal) relVal.textContent = `${report.relevance_score || 85}%`;

  // Strengths
  const strengthsList = document.getElementById("res-strengths-list");
  if (strengthsList) {
    strengthsList.innerHTML = (report.strengths || []).map(s => `
      <div style="background: #f0fdf4; border-left: 3px solid #22c55e; padding: 6px 10px; border-radius: 4px;">• ${s}</div>
    `).join("");
  }

  // Missing
  const missingList = document.getElementById("res-missing-list");
  if (missingList) {
    missingList.innerHTML = (report.missing || []).map(m => `
      <div style="background: #fef2f2; border-left: 3px solid #ef4444; padding: 6px 10px; border-radius: 4px;">• ${m}</div>
    `).join("");
  }

  // Keywords
  const keywordsCloud = document.getElementById("res-keywords-cloud");
  if (keywordsCloud) {
    keywordsCloud.innerHTML = (report.recommended_keywords || []).map(k => `
      <span style="background: var(--primary-50); border: 1px solid var(--primary-200); color: var(--primary-700); padding: 3px 10px; border-radius: 999px; font-size: 0.82rem; font-weight: 600;">
        + ${k}
      </span>
    `).join("");
  }

  // Suggestions
  const suggList = document.getElementById("res-suggestions-list");
  if (suggList) {
    suggList.innerHTML = (report.suggestions || []).map(sg => `
      <div style="background: var(--bg-subtle); padding: 6px 10px; border-radius: 4px; border: 1px solid var(--border-color);"><i class="fa-solid fa-lightbulb text-warning"></i> ${sg}</div>
    `).join("");
  }
}
