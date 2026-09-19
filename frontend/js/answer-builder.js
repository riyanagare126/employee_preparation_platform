/**
 * AI Employee Preparation Platform - 2026 Present-Past-Future Answer Builder Controller
 * Live speaking cadence gauge (120-165 words / 60 seconds), AI flow analysis, and pitch library.
 */

document.addEventListener("DOMContentLoaded", async () => {
  const employee = requireAuth();
  if (!employee) return;

  // DOM Elements
  const selectQuestion = document.getElementById("select-pitch-question");
  const inputRole = document.getElementById("input-target-role");
  const inputCompany = document.getElementById("input-target-company");
  const questionHintBox = document.getElementById("question-hint-box");

  const inputPresent = document.getElementById("input-present-text");
  const inputPast = document.getElementById("input-past-text");
  const inputFuture = document.getElementById("input-future-text");

  const presentCount = document.getElementById("present-count-badge");
  const pastCount = document.getElementById("past-count-badge");
  const futureCount = document.getElementById("future-count-badge");

  const gaugeWords = document.getElementById("gauge-word-count");
  const gaugeTime = document.getElementById("gauge-speaking-time");
  const gaugeBadge = document.getElementById("gauge-status-badge");
  const meterFill = document.getElementById("speaking-meter-fill");

  const btnLoadSample = document.getElementById("btn-load-sample");
  const btnReset = document.getElementById("btn-reset-draft");
  const btnAnalyze = document.getElementById("btn-analyze-pitch");

  const resultsSection = document.getElementById("analysis-results-section");
  const resultScore = document.getElementById("result-structure-score");
  const resultWords = document.getElementById("result-words");
  const resultSeconds = document.getElementById("result-seconds");
  const resultRatio = document.getElementById("result-ratio");
  const resultCritique = document.getElementById("result-critique");
  const resultPitch = document.getElementById("result-optimized-pitch");

  const btnCopyPitch = document.getElementById("btn-copy-pitch");
  const btnSavePitch = document.getElementById("btn-save-pitch");
  const savedPitchesList = document.getElementById("saved-pitches-list");
  const savedPitchCount = document.getElementById("saved-pitch-count");
  const btnRefreshSaved = document.getElementById("btn-refresh-saved");

  let questionsBank = [];
  let currentAnalysis = null;

  // 1. Initialize Questions & Saved Library
  await loadPresetQuestions();
  await loadSavedPitches(employee.id);

  // 2. Real-time Word Counter & Speaking Gauge
  function updateSpeakingGauge() {
    const presText = (inputPresent.value || "").trim();
    const pastText = (inputPast.value || "").trim();
    const futText = (inputFuture.value || "").trim();

    const pWords = presText ? presText.split(/\s+/).filter(w => w.length > 0).length : 0;
    const paWords = pastText ? pastText.split(/\s+/).filter(w => w.length > 0).length : 0;
    const fWords = futText ? futText.split(/\s+/).filter(w => w.length > 0).length : 0;

    presentCount.textContent = `${pWords} words`;
    pastCount.textContent = `${paWords} words`;
    futureCount.textContent = `${fWords} words`;

    const totalWords = pWords + paWords + fWords;
    const estSeconds = Math.round(totalWords / 2.33); // ~140 wpm spoken cadence

    gaugeWords.textContent = `${totalWords} words`;
    gaugeTime.textContent = `~${estSeconds}s`;

    if (totalWords === 0) {
      gaugeBadge.textContent = "Ready to Type";
      gaugeBadge.className = "badge badge-secondary";
      meterFill.style.width = "0%";
      meterFill.style.backgroundColor = "var(--primary-500)";
    } else if (estSeconds < 40 || totalWords < 90) {
      gaugeBadge.textContent = "Too Short (<40s)";
      gaugeBadge.className = "badge badge-warning";
      const pct = Math.min(50, Math.round((estSeconds / 40) * 50));
      meterFill.style.width = `${pct}%`;
      meterFill.style.backgroundColor = "#f59e0b"; // amber
    } else if (estSeconds > 75 || totalWords > 185) {
      gaugeBadge.textContent = "Too Long (>75s)";
      gaugeBadge.className = "badge badge-danger";
      meterFill.style.width = "100%";
      meterFill.style.backgroundColor = "#ef4444"; // red
    } else {
      gaugeBadge.innerHTML = 'Sweet Spot <i class="fa-solid fa-bullseye"></i> (50-70s)';
      gaugeBadge.className = "badge badge-success";
      const pct = Math.min(95, 50 + Math.round(((estSeconds - 40) / 35) * 45));
      meterFill.style.width = `${pct}%`;
      meterFill.style.backgroundColor = "#22c55e"; // green
    }
  }

  [inputPresent, inputPast, inputFuture].forEach(input => {
    input.addEventListener("input", updateSpeakingGauge);
  });

  // 3. Question Selector Change
  selectQuestion.addEventListener("change", () => {
    const selectedKey = selectQuestion.value;
    const matched = questionsBank.find(q => q.key === selectedKey);
    if (matched && matched.hint) {
      questionHintBox.innerHTML = `<i class="fa-solid fa-lightbulb text-warning"></i> <strong>Recruiter Benchmark:</strong> ${escapeHtml(matched.hint)}`;
    } else {
      questionHintBox.innerHTML = `<i class="fa-solid fa-lightbulb text-warning"></i> <strong>Recruiter Benchmark:</strong> Start with your active technical focus, back it up with past metrics, and end with company impact.`;
    }
  });

  // 4. Load Sample High-Impact Pitch
  btnLoadSample.addEventListener("click", () => {
    inputRole.value = "Full Stack Software Engineer";
    inputCompany.value = "Google";
    inputPresent.value = "Currently, I am a software engineer specializing in scalable backend services with Python FastAPI and distributed architectures. Right now, I'm developing high-throughput REST APIs and optimizing asynchronous worker queues.";
    inputPast.value = "Previously, during my engineering residency, I re-architected an enterprise query cache that reduced 95th percentile database latency by 44% and successfully sustained 120,000 daily active requests without failure. I also automated test coverage to 92%.";
    inputFuture.value = "Looking forward, I want to join Google's Cloud Platform team because of your relentless focus on zero-trust reliability. In my first 90 days, I plan to leverage my API optimization expertise to ship microservice latency enhancements from day one.";
    updateSpeakingGauge();
    showToast("Loaded high-impact 60-second pitch sample!", "info");
  });

  // 5. Reset Draft
  btnReset.addEventListener("click", () => {
    if (confirm("Reset current draft? All text in the 3 boxes will be cleared.")) {
      inputPresent.value = "";
      inputPast.value = "";
      inputFuture.value = "";
      updateSpeakingGauge();
      resultsSection.style.display = "none";
      currentAnalysis = null;
      showToast("Draft cleared", "info");
    }
  });

  // 6. Analyze Pitch via AI
  btnAnalyze.addEventListener("click", async () => {
    const pres = (inputPresent.value || "").trim();
    const past = (inputPast.value || "").trim();
    const fut = (inputFuture.value || "").trim();

    if (!pres && !past && !fut) {
      showToast("Please fill in at least one section of your pitch first.", "warning");
      inputPresent.focus();
      return;
    }

    const questionTitle = selectQuestion.options[selectQuestion.selectedIndex]?.text || "Tell me about yourself";
    const role = (inputRole.value || "Software Engineer").trim();
    const company = (inputCompany.value || "Target Enterprise").trim();

    btnAnalyze.disabled = true;
    btnAnalyze.innerHTML = `<span>Analyzing flow & pacing... <i class="fa-solid fa-hourglass-half fa-spin"></i></span>`;

    try {
      const response = await fetch(`${API_BASE}/api/answer-builder/analyze`, {
        method: "POST",
        headers: getAuthHeaders(),
        body: JSON.stringify({
          employee_id: employee.id,
          question_title: questionTitle,
          present_text: pres,
          past_text: past,
          future_text: fut,
          target_role: role,
          target_company: company
        })
      });

      const res = await response.json();

      if (!response.ok || !res.success) {
        throw new Error(res.message || "Failed to analyze pitch.");
      }

      currentAnalysis = {
        ...res,
        question_key: selectQuestion.value || "tell-me-about-yourself",
        question_title: questionTitle,
        target_role: role,
        target_company: company,
        present_text: pres,
        past_text: past,
        future_text: fut,
        combined_text: `${pres} ${past} ${fut}`.trim()
      };

      // Populate Results UI
      resultScore.textContent = `${res.structure_score}/100`;
      resultWords.textContent = `${res.word_count} words`;
      resultSeconds.textContent = `~${res.speaking_time_seconds}s (${res.length_status})`;
      resultRatio.textContent = `Present (${res.present_words}w) | Past (${res.past_words}w) | Future (${res.future_words}w)`;
      resultCritique.textContent = res.critique;
      resultPitch.textContent = res.ai_optimized_pitch;

      resultsSection.style.display = "block";
      resultsSection.scrollIntoView({ behavior: "smooth", block: "start" });
      showToast("Pitch analyzed and polished by AI!", "success");

    } catch (err) {
      console.error("Error analyzing pitch:", err);
      showToast(err.message || "Network error while analyzing pitch.", "error");
    } finally {
      btnAnalyze.disabled = false;
      btnAnalyze.innerHTML = `Analyze & Polish with AI <i class="fa-solid fa-wand-magic-sparkles"></i>`;
    }
  });

  // 7. Copy AI-Optimized Pitch
  btnCopyPitch.addEventListener("click", async () => {
    const pitchText = resultPitch.textContent;
    if (!pitchText) return;
    try {
      await navigator.clipboard.writeText(pitchText);
      showToast("60-second pitch copied to clipboard!", "success");
    } catch (e) {
      showToast("Could not access clipboard automatically.", "info");
    }
  });

  // 8. Save Pitch to Library
  btnSavePitch.addEventListener("click", async () => {
    if (!currentAnalysis) {
      showToast("Please analyze your pitch before saving.", "warning");
      return;
    }

    btnSavePitch.disabled = true;
    btnSavePitch.innerHTML = 'Saving... <i class="fa-solid fa-floppy-disk fa-spin"></i>';

    try {
      const response = await fetch(`${API_BASE}/api/answer-builder/save`, {
        method: "POST",
        headers: getAuthHeaders(),
        body: JSON.stringify({
          employee_id: employee.id,
          question_key: currentAnalysis.question_key,
          question_title: currentAnalysis.question_title,
          target_role: currentAnalysis.target_role,
          target_company: currentAnalysis.target_company,
          present_text: currentAnalysis.present_text,
          past_text: currentAnalysis.past_text,
          future_text: currentAnalysis.future_text,
          combined_text: currentAnalysis.combined_text,
          speaking_time_seconds: currentAnalysis.speaking_time_seconds,
          structure_score: currentAnalysis.structure_score,
          ai_optimized_pitch: currentAnalysis.ai_optimized_pitch
        })
      });

      const res = await response.json();
      if (!response.ok || !res.success) {
        throw new Error(res.message || "Failed to save pitch.");
      }

      showToast("Saved pitch to your library!", "success");
      await loadSavedPitches(employee.id);

    } catch (err) {
      console.error("Error saving pitch:", err);
      showToast(err.message || "Error saving pitch.", "error");
    } finally {
      btnSavePitch.disabled = false;
      btnSavePitch.innerHTML = '<i class="fa-solid fa-floppy-disk"></i> Save to My Library';
    }
  });

  // 9. Refresh Saved Library
  btnRefreshSaved.addEventListener("click", () => {
    loadSavedPitches(employee.id);
  });

  // Load Preset Questions Helper
  async function loadPresetQuestions() {
    try {
      const res = await fetch(`${API_BASE}/api/answer-builder/questions`);
      const data = await res.json();
      if (data.success && Array.isArray(data.questions)) {
        questionsBank = data.questions;
        selectQuestion.innerHTML = questionsBank.map(q => 
          `<option value="${q.key}">${escapeHtml(q.title)}</option>`
        ).join("");

        if (questionsBank[0] && questionsBank[0].hint) {
          questionHintBox.innerHTML = `<i class="fa-solid fa-lightbulb text-warning"></i> <strong>Recruiter Benchmark:</strong> ${escapeHtml(questionsBank[0].hint)}`;
        }
      }
    } catch (e) {
      console.error("Error loading questions bank:", e);
      selectQuestion.innerHTML = `<option value="tell-me-about-yourself">Tell me about yourself / Walk me through your resume</option>`;
    }
  }

  // Load Saved Pitches Helper
  async function loadSavedPitches(employeeId) {
    try {
      const res = await fetch(`${API_BASE}/api/answer-builder/saved?employee_id=${employeeId}`, {
        headers: getAuthHeaders()
      });
      const data = await res.json();

      if (!data.success || !Array.isArray(data.data) || data.data.length === 0) {
        savedPitchCount.textContent = "0";
        savedPitchesList.innerHTML = `
          <div style="text-align: center; padding: 28px; background: var(--bg-subtle); border-radius: var(--radius-md); color: var(--text-muted);">
            <div style="font-size: 2rem; margin-bottom: 8px; color: var(--primary-600);"><i class="fa-solid fa-folder-open"></i></div>
            <div style="font-weight: 600; margin-bottom: 4px;">No saved elevator pitches yet</div>
            <div style="font-size: 0.85rem;">Draft your Present-Past-Future narrative above and click "Save to My Library".</div>
          </div>
        `;
        return;
      }

      savedPitchCount.textContent = String(data.data.length);
      savedPitchesList.innerHTML = data.data.map(item => `
        <div class="card" style="padding: 16px 20px; border: 1px solid var(--border-color); border-radius: var(--radius-md); background: var(--bg-card); display: flex; flex-direction: column; gap: 10px;">
          <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 10px;">
            <div>
              <div style="display: flex; align-items: center; gap: 8px; flex-wrap: wrap;">
                <span class="badge badge-primary">${escapeHtml(item.target_company || 'Enterprise')}</span>
                <span style="font-size: 0.82rem; font-weight: 700; color: var(--text-main);">${escapeHtml(item.target_role || 'SDE')}</span>
                <span style="font-size: 0.75rem; color: var(--text-muted);">&bull; ${escapeHtml(item.question_title || 'Self Intro')}</span>
              </div>
            </div>

            <div style="display: flex; align-items: center; gap: 12px;">
              <span class="badge badge-success">Score: ${item.structure_score || 90}/100</span>
              <span class="badge badge-secondary">~${item.speaking_time_seconds || 60}s</span>
              <button class="btn btn-outline-primary btn-sm btn-load-saved" data-id="${item.id}" style="padding: 3px 10px; font-size: 0.78rem;">Load <i class="fa-solid fa-pencil"></i></button>
              <button class="btn btn-ghost btn-sm btn-delete-saved" data-id="${item.id}" style="padding: 3px 8px; font-size: 0.78rem; color: var(--danger-600);"><i class="fa-solid fa-trash-can"></i></button>
            </div>
          </div>

          <div style="font-size: 0.88rem; color: #334155; line-height: 1.5; background: var(--bg-subtle); padding: 10px 14px; border-radius: var(--radius-sm);">
            ${escapeHtml(item.ai_optimized_pitch || item.combined_text || '')}
          </div>

          <div style="font-size: 0.72rem; color: var(--text-muted); display: flex; justify-content: space-between;">
            <span>Saved on: ${item.created_at ? new Date(item.created_at).toLocaleDateString() : 'Recent'}</span>
          </div>
        </div>
      `).join("");

      // Wire up Load and Delete buttons
      document.querySelectorAll(".btn-load-saved").forEach(btn => {
        btn.addEventListener("click", () => {
          const id = parseInt(btn.dataset.id);
          const item = data.data.find(x => x.id === id);
          if (item) {
            inputRole.value = item.target_role || "";
            inputCompany.value = item.target_company || "";
            inputPresent.value = item.present_text || "";
            inputPast.value = item.past_text || "";
            inputFuture.value = item.future_text || "";

            if (item.question_key) {
              selectQuestion.value = item.question_key;
            }

            updateSpeakingGauge();
            window.scrollTo({ top: 0, behavior: "smooth" });
            showToast(`Loaded saved pitch for ${item.target_company}!`, "info");
          }
        });
      });

      document.querySelectorAll(".btn-delete-saved").forEach(btn => {
        btn.addEventListener("click", async () => {
          const id = parseInt(btn.dataset.id);
          if (confirm("Delete this saved pitch from your library?")) {
            try {
              const res = await fetch(`${API_BASE}/api/answer-builder/saved/${id}?employee_id=${employee.id}`, {
                method: "DELETE",
                headers: getAuthHeaders()
              });
              if (res.ok) {
                showToast("Pitch deleted from library.", "info");
                loadSavedPitches(employee.id);
              }
            } catch (err) {
              console.error("Error deleting pitch:", err);
            }
          }
        });
      });

    } catch (e) {
      console.error("Error loading saved pitches:", e);
      savedPitchesList.innerHTML = `<div style="color: var(--danger-600); padding: 14px;">Error loading saved pitches.</div>`;
    }
  }

  function escapeHtml(text) {
    if (!text) return "";
    return text.toString()
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#039;");
  }
});
