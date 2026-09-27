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

  // =========================================================================
  // HONEST-TO-PROFESSIONAL ANSWER CONVERTER CONTROLLER
  // =========================================================================
  
  // Tab Switcher Elements
  const tabBtnPitch = document.getElementById("tab-btn-pitch");
  const tabBtnConverter = document.getElementById("tab-btn-converter");
  const pitchSection = document.getElementById("pitch-builder-section");
  const converterSection = document.getElementById("honest-converter-section");

  // Converter Form Elements
  const formConverter = document.getElementById("form-honest-converter");
  const selectConvQType = document.getElementById("select-conv-qtype");
  const inputConvRole = document.getElementById("input-conv-role");
  const inputConvCompany = document.getElementById("input-conv-company");
  const inputHonestRaw = document.getElementById("input-honest-raw");
  const rawCharCount = document.getElementById("raw-char-count");
  const convErrorBox = document.getElementById("conv-error-box");
  const btnSampleHonest = document.getElementById("btn-sample-honest");
  const btnClearHonest = document.getElementById("btn-clear-honest");
  const btnConvertHonest = document.getElementById("btn-convert-honest");
  const convSpinner = document.getElementById("conv-spinner");
  const convBtnLabel = document.getElementById("conv-btn-label");

  // Converter Results Elements
  const converterResultsSection = document.getElementById("converter-results-section");
  const resProfAns = document.getElementById("res-prof-ans");
  const resShortAns = document.getElementById("res-short-ans");
  const profAnsMeta = document.getElementById("prof-ans-meta");
  const shortAnsMeta = document.getElementById("short-ans-meta");
  const resRedFlagsContainer = document.getElementById("res-red-flags-container");
  const resFollowupsContainer = document.getElementById("res-followups-container");
  const btnCopyProfAns = document.getElementById("btn-copy-prof-ans");
  const btnCopyShortAns = document.getElementById("btn-copy-short-ans");
  const btnSaveConverted = document.getElementById("btn-save-converted-answer");

  // Converter Saved Library Elements
  const savedConvCount = document.getElementById("saved-conv-count");
  const savedConvCountBadge = document.getElementById("saved-conv-count-badge");
  const savedConvertedList = document.getElementById("saved-converted-list");
  const btnRefreshConvSaved = document.getElementById("btn-refresh-conv-saved");

  let currentConvertedData = null;

  // Tab Switching Functionality
  function activateTab(tabName) {
    if (tabName === "converter") {
      pitchSection.style.display = "none";
      converterSection.style.display = "block";
      tabBtnPitch.className = "btn btn-secondary";
      tabBtnConverter.className = "btn btn-primary";
    } else {
      pitchSection.style.display = "block";
      converterSection.style.display = "none";
      tabBtnPitch.className = "btn btn-primary";
      tabBtnConverter.className = "btn btn-secondary";
    }
  }

  if (tabBtnPitch && tabBtnConverter) {
    tabBtnPitch.addEventListener("click", () => activateTab("pitch"));
    tabBtnConverter.addEventListener("click", () => activateTab("converter"));
  }

  // Check URL hash for direct navigation
  if (window.location.hash === "#converter" || window.location.hash === "#honest-converter") {
    activateTab("converter");
  }

  // Live Character Count for Raw Answer
  if (inputHonestRaw && rawCharCount) {
    inputHonestRaw.addEventListener("input", () => {
      const count = (inputHonestRaw.value || "").length;
      rawCharCount.textContent = `${count} characters`;
    });
  }

  // Sample Honest Answers Preset Dictionary
  const sampleHonestDict = {
    "Why are you leaving your current job?":
      "My manager is a micromanager who changes requirements daily and takes credit for our work. I haven't gotten a promotion or salary hike in over two years despite consistently working 60-hour weeks. The tech stack is outdated and there's nowhere for me to grow.",
    "Explain your employment gap":
      "I was completely burned out after 4 years of nonstop crunch time and late-night on-call. I quit without an offer to take 8 months off, rest, spend time with my family, and figure out what I actually want to do next.",
    "Why were you laid off?":
      "Our entire division was eliminated after the company missed revenue targets. They called an all-hands at 9 AM and locked our Slack accounts by noon. I was caught completely off guard and had to start interviewing suddenly.",
    "Why did you get laid off?":
      "Our entire division was eliminated after the company missed revenue targets. They called an all-hands at 9 AM and locked our Slack accounts by noon. I was caught completely off guard and had to start interviewing suddenly.",
    "Why so many job changes?":
      "I left my first job after 8 months because the pay was too low. At my second company, they changed the project to something I didn't want to do, so I left after 10 months. Now at my third company after a year, the leadership is unstable and team morale is terrible."
  };

  if (btnSampleHonest && inputHonestRaw && selectConvQType) {
    btnSampleHonest.addEventListener("click", () => {
      const qtype = selectConvQType.value;
      inputHonestRaw.value = sampleHonestDict[qtype] || sampleHonestDict["Why are you leaving your current job?"];
      rawCharCount.textContent = `${inputHonestRaw.value.length} characters`;
      if (convErrorBox) convErrorBox.style.display = "none";
      showToast("Loaded sample honest scenario!", "info");
    });

    selectConvQType.addEventListener("change", () => {
      if (!inputHonestRaw.value.trim()) {
        const qtype = selectConvQType.value;
        if (sampleHonestDict[qtype]) {
          inputHonestRaw.placeholder = `e.g. "${sampleHonestDict[qtype]}"`;
        }
      }
    });
  }

  // Clear Form
  if (btnClearHonest && inputHonestRaw) {
    btnClearHonest.addEventListener("click", () => {
      inputHonestRaw.value = "";
      rawCharCount.textContent = "0 characters";
      if (convErrorBox) convErrorBox.style.display = "none";
      if (converterResultsSection) converterResultsSection.style.display = "none";
      currentConvertedData = null;
    });
  }

  // Submit Form: Convert Honest to Professional
  if (formConverter) {
    formConverter.addEventListener("submit", async (e) => {
      e.preventDefault();

      const rawText = (inputHonestRaw.value || "").trim();
      const questionType = selectConvQType.value || "Why are you leaving your current job?";
      const targetRole = (inputConvRole.value || "").trim() || "Software Engineer";
      const targetCompany = (inputConvCompany.value || "").trim() || "Target Enterprise";

      if (!rawText) {
        if (convErrorBox) {
          convErrorBox.textContent = "Please provide your raw, honest answer to convert.";
          convErrorBox.style.display = "block";
        }
        inputHonestRaw.focus();
        return;
      }

      if (rawText.length < 10) {
        if (convErrorBox) {
          convErrorBox.textContent = "Please provide at least a short sentence describing your real situation.";
          convErrorBox.style.display = "block";
        }
        inputHonestRaw.focus();
        return;
      }

      if (convErrorBox) convErrorBox.style.display = "none";

      // UI Loading State
      btnConvertHonest.disabled = true;
      if (convSpinner) convSpinner.style.display = "inline-block";
      if (convBtnLabel) convBtnLabel.textContent = " Converting & Saving with AI...";

      try {
        const response = await fetch(`${API_BASE}/api/converted-answers/convert`, {
          method: "POST",
          headers: getAuthHeaders(),
          body: JSON.stringify({
            employee_id: employee ? employee.id : null,
            question_type: questionType,
            raw_answer: rawText,
            target_role: targetRole,
            target_company: targetCompany
          })
        });

        const res = await response.json();
        if (!response.ok || !res.success) {
          throw new Error(res.message || "Failed to convert answer.");
        }

        const data = res.data;
        currentConvertedData = {
          ...data,
          question_type: questionType,
          raw_answer: rawText,
          target_role: targetRole,
          target_company: targetCompany
        };

        // Render (A) Polished Answer
        resProfAns.textContent = data.professional_answer;
        const profWords = data.professional_answer ? data.professional_answer.split(/\s+/).filter(Boolean).length : 0;
        const profSentences = data.professional_answer ? (data.professional_answer.match(/[.!?]+/g) || []).length : 4;
        profAnsMeta.textContent = `~${profSentences} sentences (${profWords} words)`;

        // Render (B) Short 30s Answer
        resShortAns.textContent = data.short_answer;
        const shortWords = data.short_answer ? data.short_answer.split(/\s+/).filter(Boolean).length : 0;
        const shortSecs = Math.round(shortWords / 2.3);
        shortAnsMeta.textContent = `~${shortSecs}s (${shortWords} words)`;

        // Render (C) Red Flags
        if (Array.isArray(data.red_flags) && data.red_flags.length > 0) {
          resRedFlagsContainer.innerHTML = data.red_flags.map((rf, idx) => `
            <div style="background: #ffffff; border: 1px solid #fed7aa; border-radius: 8px; padding: 12px 16px; display: flex; flex-direction: column; gap: 6px;">
              <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 8px;">
                <span class="badge badge-danger" style="font-size: 0.76rem; font-weight: 700;">
                  <i class="fa-solid fa-ban"></i> Red-Flag Risk: "${escapeHtml(rf.flagged_phrase || 'Critical Phrase')}"
                </span>
                <span style="font-size: 0.74rem; color: #b45309; font-weight: 600;">Issue: ${escapeHtml(rf.risk || 'Perceived negatively')}</span>
              </div>
              <div style="font-size: 0.86rem; color: #15803d; background: #f0fdf4; border: 1px solid #bbf7d0; padding: 8px 12px; border-radius: 6px; margin-top: 4px;">
                <strong><i class="fa-solid fa-arrow-right"></i> Reframed Alternative:</strong> ${escapeHtml(rf.safer_alternative || '')}
              </div>
            </div>
          `).join("");
        } else {
          resRedFlagsContainer.innerHTML = `
            <div style="background: #f0fdf4; border: 1px solid #bbf7d0; color: #166534; padding: 12px 16px; border-radius: 8px; font-size: 0.88rem;">
              <i class="fa-solid fa-circle-check"></i> Great composure! No severe red-flag hostility detected in your honest explanation.
            </div>
          `;
        }

        // Render (D) Follow-Up Questions
        if (Array.isArray(data.follow_up_questions) && data.follow_up_questions.length > 0) {
          resFollowupsContainer.innerHTML = data.follow_up_questions.map((fq, idx) => `
            <div style="background: #ffffff; border: 1px solid #e0e7ff; border-radius: 8px; padding: 12px 16px; display: flex; flex-direction: column; gap: 4px;">
              <div style="font-size: 0.92rem; font-weight: 700; color: #1e1b4b; display: flex; align-items: flex-start; gap: 8px;">
                <span style="background: #4f46e5; color: #fff; border-radius: 50%; width: 20px; height: 20px; display: inline-flex; align-items: center; justify-content: center; font-size: 0.72rem; flex-shrink: 0;">${idx + 1}</span>
                <span>"${escapeHtml(fq.question || '')}"</span>
              </div>
              ${fq.recruiter_intent ? `
                <div style="font-size: 0.8rem; color: #4338ca; margin-left: 28px; line-height: 1.4;">
                  <strong>Recruiter Intent:</strong> ${escapeHtml(fq.recruiter_intent)}
                </div>
              ` : ''}
            </div>
          `).join("");
        } else {
          resFollowupsContainer.innerHTML = `
            <div style="background: #eef2ff; border: 1px solid #c7d2fe; color: #3730a3; padding: 10px 14px; border-radius: 8px; font-size: 0.86rem;">
              Standard follow-up questions will probe on technical project delivery and team dynamics.
            </div>
          `;
        }

        // Show Results Section & Scroll
        converterResultsSection.style.display = "block";
        converterResultsSection.scrollIntoView({ behavior: "smooth", block: "start" });
        showToast("Answer converted and saved to your library!", "success");

        // Immediately refresh the saved list below
        if (employee && employee.id) {
          loadSavedConvertedAnswers(employee.id);
        }

      } catch (err) {
        console.error("Error converting answer:", err);
        if (convErrorBox) {
          convErrorBox.textContent = err.message || "Failed to convert answer. Please try again.";
          convErrorBox.style.display = "block";
        }
        showToast(err.message || "Error converting answer.", "error");
      } finally {
        btnConvertHonest.disabled = false;
        if (convSpinner) convSpinner.style.display = "none";
        if (convBtnLabel) convBtnLabel.innerHTML = `<i class="fa-solid fa-wand-magic-sparkles"></i> Convert to Professional Answer`;
      }
    });
  }

  // Copy Buttons
  if (btnCopyProfAns && resProfAns) {
    btnCopyProfAns.addEventListener("click", async () => {
      const text = (resProfAns.textContent || "").trim();
      if (!text) return;
      try {
        if (navigator.clipboard && navigator.clipboard.writeText) {
          await navigator.clipboard.writeText(text);
        } else {
          const ta = document.createElement("textarea");
          ta.value = text;
          document.body.appendChild(ta);
          ta.select();
          document.execCommand("copy");
          document.body.removeChild(ta);
        }
        showToast("Polished professional answer copied to clipboard!", "success");
      } catch (e) {
        showToast("Polished professional answer copied!", "success");
      }
    });
  }

  if (btnCopyShortAns && resShortAns) {
    btnCopyShortAns.addEventListener("click", async () => {
      const text = resShortAns.textContent;
      if (!text) return;
      try {
        await navigator.clipboard.writeText(text);
        showToast("30-second elevator version copied to clipboard!", "success");
      } catch (e) {
        showToast("Could not access clipboard automatically.", "info");
      }
    });
  }

  // Save Converted Answer to Library
  if (btnSaveConverted) {
    btnSaveConverted.addEventListener("click", async () => {
      if (!currentConvertedData) {
        showToast("Please convert your answer before saving.", "warning");
        return;
      }

      btnSaveConverted.disabled = true;
      btnSaveConverted.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Saving...';

      try {
        const response = await fetch(`${API_BASE}/api/converted-answers/save`, {
          method: "POST",
          headers: getAuthHeaders(),
          body: JSON.stringify({
            employee_id: employee.id,
            question_type: currentConvertedData.question_type,
            raw_answer: currentConvertedData.raw_answer,
            professional_answer: currentConvertedData.professional_answer,
            short_answer: currentConvertedData.short_answer,
            red_flags: currentConvertedData.red_flags || [],
            follow_up_questions: currentConvertedData.follow_up_questions || [],
            target_role: currentConvertedData.target_role,
            target_company: currentConvertedData.target_company
          })
        });

        const res = await response.json();
        if (!response.ok || !res.success) {
          throw new Error(res.message || "Failed to save converted answer.");
        }

        showToast("+20 XP! Saved converted answer to your library.", "success");
        await loadSavedConvertedAnswers(employee.id);

      } catch (err) {
        console.error("Error saving converted answer:", err);
        showToast(err.message || "Error saving converted answer.", "error");
      } finally {
        btnSaveConverted.disabled = false;
        btnSaveConverted.innerHTML = '<i class="fa-solid fa-bookmark"></i> Save to My Answers (+20 XP)';
      }
    });
  }

  // Refresh Saved Converted Answers
  if (btnRefreshConvSaved) {
    btnRefreshConvSaved.addEventListener("click", () => {
      loadSavedConvertedAnswers(employee.id);
    });
  }

  // Load Saved Converted Answers Helper
  async function loadSavedConvertedAnswers(employeeId) {
    if (!savedConvertedList) return;

    try {
      const res = await fetch(`${API_BASE}/api/converted-answers?employee_id=${employeeId}`, {
        headers: getAuthHeaders()
      });
      const data = await res.json();

      if (!data.success || !Array.isArray(data.data) || data.data.length === 0) {
        if (savedConvCount) savedConvCount.textContent = "0";
        if (savedConvCountBadge) savedConvCountBadge.textContent = "0";
        savedConvertedList.innerHTML = `
          <div style="text-align: center; padding: 28px; background: var(--bg-subtle); border-radius: var(--radius-md); color: var(--text-muted);">
            <div style="font-size: 2rem; margin-bottom: 8px; color: #a855f7;"><i class="fa-solid fa-folder-open"></i></div>
            <div style="font-weight: 600; margin-bottom: 4px;">No saved converted answers yet</div>
            <div style="font-size: 0.85rem;">Input your honest reason above and click "Save to My Answers" to keep them handy for interviews.</div>
          </div>
        `;
        return;
      }

      const total = data.data.length;
      if (savedConvCount) savedConvCount.textContent = String(total);
      if (savedConvCountBadge) savedConvCountBadge.textContent = String(total);

      savedConvertedList.innerHTML = data.data.map(item => {
        let redFlags = [];
        try {
          redFlags = typeof item.red_flags === "string" ? JSON.parse(item.red_flags) : (item.red_flags || []);
        } catch (e) { redFlags = []; }

        let followUps = [];
        try {
          followUps = typeof item.follow_up_questions === "string" ? JSON.parse(item.follow_up_questions) : (item.follow_up_questions || []);
        } catch (e) { followUps = []; }

        return `
          <div class="card" style="padding: 18px 20px; border: 1px solid var(--border-color); border-radius: var(--radius-md); background: var(--bg-card); display: flex; flex-direction: column; gap: 12px;">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 10px;">
              <div>
                <div style="display: flex; align-items: center; gap: 8px; flex-wrap: wrap; margin-bottom: 4px;">
                  <span class="badge badge-primary" style="background: #4338ca;">${escapeHtml(item.question_type)}</span>
                  ${item.target_company ? `<span class="badge badge-secondary">${escapeHtml(item.target_company)}</span>` : ''}
                  ${item.target_role ? `<span style="font-size: 0.8rem; font-weight: 600; color: var(--text-main);">${escapeHtml(item.target_role)}</span>` : ''}
                </div>
              </div>

              <div style="display: flex; align-items: center; gap: 10px;">
                <button class="btn btn-outline-primary btn-sm btn-load-conv" data-id="${item.id}" style="padding: 3px 10px; font-size: 0.78rem;">
                  <i class="fa-solid fa-pencil"></i> Load
                </button>
                <button class="btn btn-secondary btn-sm btn-copy-saved-prof" data-id="${item.id}" style="padding: 3px 10px; font-size: 0.78rem;">
                  <i class="fa-regular fa-copy"></i> Copy
                </button>
                <button class="btn btn-ghost btn-sm btn-delete-conv" data-id="${item.id}" style="padding: 3px 8px; font-size: 0.78rem; color: var(--danger-600);">
                  <i class="fa-solid fa-trash-can"></i>
                </button>
              </div>
            </div>

            <!-- Professional Answer Preview -->
            <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 12px 14px;">
              <div style="font-size: 0.76rem; font-weight: 700; color: #1e40af; margin-bottom: 4px; text-transform: uppercase; letter-spacing: 0.04em;">
                <i class="fa-solid fa-star"></i> Polished Professional Answer (4-6 sentences):
              </div>
              <div style="font-size: 0.9rem; color: #1e293b; line-height: 1.55;">
                ${escapeHtml(item.professional_answer || '')}
              </div>
            </div>

            <!-- Short 30s Answer Preview -->
            ${item.short_answer ? `
              <div style="background: #faf5ff; border: 1px solid #f3e8ff; border-radius: 8px; padding: 10px 14px;">
                <div style="font-size: 0.74rem; font-weight: 700; color: #6b21a8; margin-bottom: 2px;">
                  <i class="fa-solid fa-bolt"></i> 30-Second Quick Pitch:
                </div>
                <div style="font-size: 0.86rem; color: #334155; line-height: 1.5;">
                  ${escapeHtml(item.short_answer)}
                </div>
              </div>
            ` : ''}

            <!-- Red Flags & Follow-ups Summary Badges -->
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px; font-size: 0.74rem; color: var(--text-muted);">
              <div style="display: flex; gap: 8px; align-items: center;">
                ${redFlags.length > 0 ? `
                  <span class="badge badge-warning" style="font-size: 0.72rem;">
                    <i class="fa-solid fa-shield"></i> ${redFlags.length} Red Flags Addressed
                  </span>
                ` : `
                  <span class="badge badge-success" style="font-size: 0.72rem;"><i class="fa-solid fa-check"></i> Clean</span>
                `}
                ${followUps.length > 0 ? `
                  <span class="badge badge-secondary" style="font-size: 0.72rem;">
                    <i class="fa-solid fa-clipboard-question"></i> ${followUps.length} Follow-ups Mapped
                  </span>
                ` : ''}
              </div>
              <span>Saved on: ${item.created_at ? new Date(item.created_at).toLocaleDateString() : 'Recent'}</span>
            </div>
          </div>
        `;
      }).join("");

      // Wire up Action Buttons in List
      document.querySelectorAll(".btn-load-conv").forEach(btn => {
        btn.addEventListener("click", () => {
          const id = parseInt(btn.dataset.id);
          const item = data.data.find(x => x.id === id);
          if (item) {
            activateTab("converter");
            selectConvQType.value = item.question_type || "Why are you leaving your current job?";
            if (item.target_role) inputConvRole.value = item.target_role;
            if (item.target_company) inputConvCompany.value = item.target_company;
            inputHonestRaw.value = item.raw_answer || "";
            rawCharCount.textContent = `${(item.raw_answer || "").length} characters`;

            // Display results in the result box directly
            let redFlags = [];
            try {
              redFlags = typeof item.red_flags === "string" ? JSON.parse(item.red_flags) : (item.red_flags || []);
            } catch (e) { redFlags = []; }

            let followUps = [];
            try {
              followUps = typeof item.follow_up_questions === "string" ? JSON.parse(item.follow_up_questions) : (item.follow_up_questions || []);
            } catch (e) { followUps = []; }

            currentConvertedData = {
              ...item,
              red_flags: redFlags,
              follow_up_questions: followUps
            };

            resProfAns.textContent = item.professional_answer;
            resShortAns.textContent = item.short_answer;
            
            const profWords = item.professional_answer ? item.professional_answer.split(/\s+/).filter(Boolean).length : 0;
            const profSentences = item.professional_answer ? (item.professional_answer.match(/[.!?]+/g) || []).length : 4;
            profAnsMeta.textContent = `~${profSentences} sentences (${profWords} words)`;

            const shortWords = item.short_answer ? item.short_answer.split(/\s+/).filter(Boolean).length : 0;
            const shortSecs = Math.round(shortWords / 2.3);
            shortAnsMeta.textContent = `~${shortSecs}s (${shortWords} words)`;

            // Red Flags
            if (redFlags.length > 0) {
              resRedFlagsContainer.innerHTML = redFlags.map(rf => `
                <div style="background: #ffffff; border: 1px solid #fed7aa; border-radius: 8px; padding: 12px 16px; display: flex; flex-direction: column; gap: 6px;">
                  <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 8px;">
                    <span class="badge badge-danger" style="font-size: 0.76rem; font-weight: 700;">
                      <i class="fa-solid fa-ban"></i> Red-Flag Risk: "${escapeHtml(rf.flagged_phrase || 'Critical Phrase')}"
                    </span>
                    <span style="font-size: 0.74rem; color: #b45309; font-weight: 600;">Issue: ${escapeHtml(rf.risk || 'Perceived negatively')}</span>
                  </div>
                  <div style="font-size: 0.86rem; color: #15803d; background: #f0fdf4; border: 1px solid #bbf7d0; padding: 8px 12px; border-radius: 6px; margin-top: 4px;">
                    <strong><i class="fa-solid fa-arrow-right"></i> Reframed Alternative:</strong> ${escapeHtml(rf.safer_alternative || '')}
                  </div>
                </div>
              `).join("");
            } else {
              resRedFlagsContainer.innerHTML = `<div style="padding: 10px; color: #166534;"><i class="fa-solid fa-circle-check"></i> No severe red-flag hostility detected.</div>`;
            }

            // Follow-ups
            if (followUps.length > 0) {
              resFollowupsContainer.innerHTML = followUps.map((fq, idx) => `
                <div style="background: #ffffff; border: 1px solid #e0e7ff; border-radius: 8px; padding: 12px 16px; display: flex; flex-direction: column; gap: 4px;">
                  <div style="font-size: 0.92rem; font-weight: 700; color: #1e1b4b; display: flex; align-items: flex-start; gap: 8px;">
                    <span style="background: #4f46e5; color: #fff; border-radius: 50%; width: 20px; height: 20px; display: inline-flex; align-items: center; justify-content: center; font-size: 0.72rem; flex-shrink: 0;">${idx + 1}</span>
                    <span>"${escapeHtml(fq.question || '')}"</span>
                  </div>
                  ${fq.recruiter_intent ? `
                    <div style="font-size: 0.8rem; color: #4338ca; margin-left: 28px; line-height: 1.4;">
                      <strong>Recruiter Intent:</strong> ${escapeHtml(fq.recruiter_intent)}
                    </div>
                  ` : ''}
                </div>
              `).join("");
            }

            converterResultsSection.style.display = "block";
            formConverter.scrollIntoView({ behavior: "smooth", block: "start" });
            showToast("Loaded saved answer into editor!", "info");
          }
        });
      });

      document.querySelectorAll(".btn-copy-saved-prof").forEach(btn => {
        btn.addEventListener("click", async () => {
          const id = parseInt(btn.dataset.id);
          const item = data.data.find(x => x.id === id);
          if (item && item.professional_answer) {
            try {
              await navigator.clipboard.writeText(item.professional_answer);
              showToast("Copied saved professional answer!", "success");
            } catch (e) {
              showToast("Could not access clipboard.", "info");
            }
          }
        });
      });

      document.querySelectorAll(".btn-delete-conv").forEach(btn => {
        btn.addEventListener("click", async () => {
          const id = parseInt(btn.dataset.id);
          if (confirm("Delete this converted answer from your saved library?")) {
            try {
              const res = await fetch(`${API_BASE}/api/converted-answers/${id}?employee_id=${employee.id}`, {
                method: "DELETE",
                headers: getAuthHeaders()
              });
              if (res.ok) {
                showToast("Converted answer deleted from library.", "info");
                loadSavedConvertedAnswers(employee.id);
              } else {
                showToast("Failed to delete answer.", "error");
              }
            } catch (err) {
              console.error("Error deleting converted answer:", err);
            }
          }
        });
      });

    } catch (e) {
      console.error("Error loading saved converted answers:", e);
      if (savedConvertedList) {
        savedConvertedList.innerHTML = `<div style="color: var(--danger-600); padding: 14px;">Error loading saved answers.</div>`;
      }
    }
  }

  // Initialize Saved Converted Answers
  await loadSavedConvertedAnswers(employee.id);

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
