/**
 * AI Employee Preparation Platform - Secure AI Aptitude Engine
 * Anti-Cheating & Security Suite:
 * - 1-Attempt enforcement per candidate
 * - Multi-tab collision prevention via session tab tokens
 * - Server-authoritative timer & in-flight session recovery on reload
 * - Browser back-button & page unload protection
 * - Server-side grading & zero client-side answer leakage
 */

let currentSessionId = null;
let questions = [];
let currentIndex = 0;
let userAnswers = []; // selected option index for each question [0..3 or null]
let timerSeconds = 900;
let timerInterval = null;
let testSubmitted = false;
let serverReviewData = [];
let currentCompanySlug = "";
let currentRoleParam = "";

function getActiveCompanySlug() {
  const urlParams = new URLSearchParams(window.location.search);
  return (currentCompanySlug || urlParams.get("company") || "").trim();
}

function getActiveRole() {
  const urlParams = new URLSearchParams(window.location.search);
  return (currentRoleParam || urlParams.get("role") || "Software Engineer").trim();
}

// Unique tab token stored in sessionStorage (isolated per browser tab)
let tabToken = sessionStorage.getItem("aptitude_tab_token");
if (!tabToken) {
  tabToken = "tab_" + Math.random().toString(36).substr(2, 9);
  sessionStorage.setItem("aptitude_tab_token", tabToken);
}

document.addEventListener("DOMContentLoaded", async () => {
  const employee = requireAuth();
  if (!employee) return;

  // Personalize test title and company context
  const urlParams = new URLSearchParams(window.location.search);
  currentCompanySlug = (urlParams.get("company") || "").trim();
  currentRoleParam = (urlParams.get("role") || employee.target_role || employee.job_role || "Software Engineer").trim();

  const testCategoryBadge = document.getElementById("test-category-badge");
  const testTitle = document.getElementById("test-title");
  if (currentCompanySlug) {
    const compUpper = currentCompanySlug.toUpperCase();
    if (testCategoryBadge) testCategoryBadge.textContent = `${compUpper} • ${currentRoleParam}`;
    if (testTitle) testTitle.textContent = `${compUpper} Placement Assessment Simulation`;
  } else if (employee.job_role) {
    if (testCategoryBadge) testCategoryBadge.textContent = `${employee.job_role} Aptitude`;
    if (testTitle) testTitle.textContent = `${employee.job_role} Placement Assessment`;
  }

  // Trap back navigation while on active test
  window.history.pushState(null, null, window.location.href);
  window.addEventListener("popstate", () => {
    if (!testSubmitted && currentSessionId) {
      window.history.pushState(null, null, window.location.href);
      showToast("Back navigation is disabled during an active test session.", "warning");
    }
  });

  // Warn on page unload if test is running
  window.addEventListener("beforeunload", (e) => {
    if (!testSubmitted && currentSessionId) {
      e.preventDefault();
      e.returnValue = "You have an active test session in progress. Leaving will count against your attempt.";
    }
  });

  // Navigation button listeners
  const btnPrev = document.getElementById("btn-prev");
  const btnNext = document.getElementById("btn-next");
  const btnSubmit = document.getElementById("btn-submit-test");
  const btnRetake = document.getElementById("btn-retake-test");
  const btnReview = document.getElementById("btn-toggle-review");

  if (btnPrev) btnPrev.addEventListener("click", () => navigateQuestion(currentIndex - 1));
  if (btnNext) btnNext.addEventListener("click", () => navigateQuestion(currentIndex + 1));
  
  if (btnSubmit) {
    btnSubmit.addEventListener("click", () => {
      const answeredCount = userAnswers.filter(a => a !== null).length;
      if (answeredCount < questions.length) {
        if (confirm(`You have answered ${answeredCount} of ${questions.length} questions. Are you sure you want to submit your final attempt?`)) {
          submitTest();
        }
      } else {
        submitTest();
      }
    });
  }

  if (btnRetake) {
    btnRetake.style.display = "inline-block";
    btnRetake.addEventListener("click", async () => {
      await initOrResumeSecureTest(true);
      showToast("Starting a fresh assessment with new questions! 🚀", "success");
    });
  }

  const btnNewTest = document.getElementById("btn-new-aptitude");
  if (btnNewTest) {
    btnNewTest.addEventListener("click", async () => {
      const answered = userAnswers.filter(a => a !== null).length;
      if (answered > 0 && !confirm("Generate a fresh set of questions? Your current progress will reset.")) {
        return;
      }
      btnNewTest.disabled = true;
      btnNewTest.textContent = "🔄 Loading...";
      await initOrResumeSecureTest(true);
      btnNewTest.disabled = false;
      btnNewTest.textContent = "🔄 New Questions";
      showToast("Fresh randomized aptitude test loaded! ⏱️", "success");
    });
  }

  const selectDiff = document.getElementById("select-apt-difficulty");
  if (selectDiff) {
    selectDiff.addEventListener("change", async () => {
      const answered = userAnswers.filter(a => a !== null).length;
      if (answered > 0 && !confirm("Changing difficulty will start a fresh assessment. Continue?")) {
        return;
      }
      await initOrResumeSecureTest(true);
      showToast(`Questions loaded for ${selectDiff.options[selectDiff.selectedIndex].text}! 🚀`, "info");
    });
  }

  // Initialize or restore secure test session
  await initOrResumeSecureTest();
});

/**
 * Swaps out the currently active question with a fresh alternative from the master bank
 */
async function handleChangeCurrentQuestion() {
  if (testSubmitted || !questions.length || currentIndex < 0 || currentIndex >= questions.length) return;
  const currentQ = questions[currentIndex];
  const btnChangeQ = document.getElementById("btn-change-apt-q");
  const employee = getLoggedInEmployee();
  if (!employee) return;

  if (btnChangeQ) {
    btnChangeQ.disabled = true;
    btnChangeQ.innerHTML = "<span>🎲 Swapping...</span>";
  }

  try {
    const res = await fetch(`${API_BASE}/api/aptitude/session/change-question`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        session_id: currentSessionId,
        employee_id: employee.id,
        question_index: currentIndex,
        category: currentQ.category || "",
        current_id: currentQ.id,
        company: getActiveCompanySlug()
      })
    });

    if (res.ok) {
      const data = await res.json();
      if (data.success && data.question) {
        questions[currentIndex] = data.question;
        userAnswers[currentIndex] = null; // reset answer for changed question
        renderQuestion(currentIndex);
        showToast("Question changed! Fresh challenge loaded 🎲", "success");
      }
    } else {
      showToast("Could not change question right now.", "warning");
    }
  } catch (err) {
    console.error("Error changing aptitude question:", err);
    showToast("Server error changing question.", "error");
  } finally {
    if (btnChangeQ) {
      btnChangeQ.disabled = false;
      btnChangeQ.innerHTML = "<span>🎲 Change Question</span>";
    }
  }
}

/**
 * Initialize new or resume in-flight secure test session
 */
async function initOrResumeSecureTest(forceNew = false) {
  testSubmitted = false;
  currentIndex = 0;
  serverReviewData = [];

  const employee = getLoggedInEmployee();
  if (!employee) return;

  const viewScreen = document.getElementById("test-view-screen");
  const resultScreen = document.getElementById("test-result-screen");
  const questionTextEl = document.getElementById("question-text");

  if (viewScreen) viewScreen.style.display = "block";
  if (resultScreen) resultScreen.style.display = "none";
  if (questionTextEl) questionTextEl.textContent = "⚙️ Connecting to test server & generating questions...";

  try {
    const activeCompany = getActiveCompanySlug();
    const activeRole = getActiveRole();
    const selectDiff = document.getElementById("select-apt-difficulty");
    const selectedDifficulty = selectDiff ? selectDiff.value : "all";

    const res = await fetch(`${API_BASE}/api/aptitude/start`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        employee_id: employee.id,
        tab_token: tabToken,
        job_role: activeRole,
        qualification: employee.qualification || "",
        skills: employee.skills || "",
        company: activeCompany,
        difficulty: selectedDifficulty,
        force_new: forceNew,
        refresh: forceNew,
        retake: forceNew
      })
    });

    const data = await res.json();

    // Check if user already completed this test (enforced only if strict lock)
    if (!forceNew && (res.status === 403 || data.already_completed)) {
      testSubmitted = true;
      if (viewScreen) viewScreen.style.display = "none";
      if (resultScreen) resultScreen.style.display = "block";

      showCompletedLockScreen(data.completed_result || {
        score: "-",
        total: 15,
        percentage: "-",
        performance_message: "Completed"
      });
      return;
    }

    // Check multi-tab collision
    if (res.status === 409 || data.tab_collision) {
      if (viewScreen) {
        viewScreen.innerHTML = `
          <div class="card" style="text-align: center; padding: 40px; border: 2px solid var(--danger-color);">
            <span style="font-size: 3rem;">⚠️</span>
            <h2 style="color: var(--danger-color); margin: 12px 0;">Multi-Tab Session Detected</h2>
            <p style="color: var(--text-muted); font-size: 1rem; margin-bottom: 20px;">
              This test is already active in another browser tab/session. To maintain test security, duplicate tabs are disabled.
            </p>
            <a href="dashboard.html" class="btn btn-secondary">Return to Dashboard</a>
          </div>
        `;
      }
      return;
    }

    if (data.success && data.questions && data.questions.length > 0) {
      currentSessionId = data.session_id;
      questions = data.questions;
      timerSeconds = data.remaining_seconds !== undefined ? data.remaining_seconds : (data.duration_seconds || 900);

      // Initialize answers array
      userAnswers = new Array(questions.length).fill(null);

      // If session was restored, fill previously selected draft answers
      if (data.draft_answers && typeof data.draft_answers === "object") {
        for (const [k, v] of Object.entries(data.draft_answers)) {
          const idx = parseInt(k, 10);
          if (!isNaN(idx) && idx >= 0 && idx < questions.length) {
            userAnswers[idx] = v;
          }
        }
        if (data.restored) {
          showToast("Active test session resumed seamlessly ⏱️", "info");
        }
      }

      renderPalette();
      renderQuestion(currentIndex);
      startTimer();
    } else {
      throw new Error(data.message || "Failed to initialize test session.");
    }
  } catch (err) {
    console.error("Test initialization error:", err);
    showToast(err.message || "Could not connect to test server.", "error");
  }
}

/**
 * Display locked result screen when 1-attempt has been completed
 */
function showCompletedLockScreen(resultData) {
  const resultScreen = document.getElementById("test-result-screen");
  if (!resultScreen) return;

  const scoreText = document.getElementById("result-score-text");
  const percentText = document.getElementById("result-percentage-text");
  const badgeEl = document.getElementById("result-badge");
  const msgEl = document.getElementById("result-message");
  const btnRetake = document.getElementById("btn-retake-test");

  if (btnRetake) btnRetake.style.display = "none";

  if (scoreText) scoreText.textContent = `${resultData.score || 0} / ${resultData.total || 15}`;
  if (percentText) percentText.textContent = `${resultData.percentage || 0}%`;
  if (badgeEl) badgeEl.textContent = "Attempt Verified ✓";
  if (msgEl) {
    msgEl.innerHTML = `
      <div style="background: #eff6ff; border: 1px solid #bfdbfe; color: #1e40af; padding: 12px 16px; border-radius: 8px; margin-top: 10px;">
        <strong>🔒 Single-Attempt Security Policy:</strong><br>
        You have already completed this test. A second attempt is not allowed. Your verified score has been permanently recorded to your employee profile.
      </div>
    `;
  }
}

/**
 * Start the authoritative countdown timer
 */
function startTimer() {
  if (timerInterval) clearInterval(timerInterval);
  const timerDisplay = document.getElementById("timer-display");
  const timerBox = document.getElementById("timer-box");

  function updateDisplay() {
    const mins = Math.floor(timerSeconds / 60);
    const secs = timerSeconds % 60;
    const formatted = `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
    if (timerDisplay) timerDisplay.textContent = formatted;
  }

  updateDisplay();

  timerInterval = setInterval(() => {
    if (timerSeconds <= 0) {
      clearInterval(timerInterval);
      showToast("Time expired! Submitting your test automatically.", "info");
      submitTest();
      return;
    }

    timerSeconds--;
    updateDisplay();

    if (timerSeconds < 120 && timerBox) {
      timerBox.style.background = "#fee2e2";
      timerBox.style.color = "#b91c1c";
    }
  }, 1000);
}

/**
 * Render current question and options
 */
function renderQuestion(index) {
  if (index < 0 || index >= questions.length) return;
  currentIndex = index;

  const q = questions[currentIndex];
  if (!q) return;

  const counterEl = document.getElementById("q-counter");
  const categoryEl = document.getElementById("q-category");
  const textEl = document.getElementById("question-text");
  const progressBar = document.getElementById("test-progress-bar");
  const optionsContainer = document.getElementById("options-container");
  const btnPrev = document.getElementById("btn-prev");
  const btnNext = document.getElementById("btn-next");

  if (counterEl) counterEl.textContent = `Question ${currentIndex + 1} of ${questions.length}`;
  if (categoryEl) categoryEl.textContent = q.category || "General Aptitude";
  if (textEl) textEl.textContent = `${currentIndex + 1}. ${q.question}`;

  const diffEl = document.getElementById("q-difficulty");
  if (diffEl) {
    const d = (q.difficulty || "Medium").toLowerCase();
    if (d === "easy" || d === "low") {
      diffEl.textContent = "🟢 Low (Easy)";
      diffEl.className = "badge badge-success";
    } else if (d === "hard" || d === "high") {
      diffEl.textContent = "🔴 High (Hard)";
      diffEl.className = "badge badge-danger";
    } else {
      diffEl.textContent = "🟡 Medium";
      diffEl.className = "badge badge-warning";
    }
  }

  if (progressBar) {
    const progressPercent = ((currentIndex + 1) / questions.length) * 100;
    progressBar.style.width = `${progressPercent}%`;
  }

  if (btnPrev) btnPrev.disabled = (currentIndex === 0);
  if (btnNext) btnNext.disabled = (currentIndex === questions.length - 1);

  if (optionsContainer) {
    optionsContainer.innerHTML = "";
    optionsContainer.className = "options-container";
    optionsContainer.style.display = "flex";
    optionsContainer.style.flexDirection = "column";
    optionsContainer.style.gap = "14px";
    optionsContainer.style.width = "100%";
    optionsContainer.style.marginBottom = "24px";

    const letters = ["A", "B", "C", "D", "E", "F"];
    const rawOptions = q.options || q.choices || [];
    const optionsList = Array.isArray(rawOptions) ? rawOptions : (typeof rawOptions === "string" ? JSON.parse(rawOptions) : []);

    if (!optionsList || optionsList.length === 0) {
      optionsContainer.innerHTML = `<div style="padding: 16px; color: var(--danger-color); border: 1px dashed var(--danger-color); border-radius: 8px;">No options available for this question.</div>`;
    } else {
      optionsList.forEach((optText, optIdx) => {
        const isSelected = (userAnswers[currentIndex] === optIdx);
        const optBtn = document.createElement("button");
        optBtn.type = "button";
        optBtn.className = `option-btn ${isSelected ? "selected" : ""}`;
        optBtn.setAttribute("data-option-index", optIdx);
        optBtn.style.display = "flex";
        optBtn.style.flexDirection = "row";
        optBtn.style.alignItems = "center";
        optBtn.style.width = "100%";
        optBtn.style.textAlign = "left";
        optBtn.style.padding = "16px 20px";
        optBtn.style.borderRadius = "12px";
        optBtn.style.border = isSelected ? "2px solid var(--primary-600, #2563eb)" : "1.5px solid var(--border-color, #e2e8f0)";
        optBtn.style.background = isSelected ? "var(--primary-50, #eff6ff)" : "var(--bg-card, #ffffff)";
        optBtn.style.color = "var(--text-main, #1e293b)";
        optBtn.style.cursor = "pointer";
        optBtn.style.gap = "16px";
        optBtn.style.transition = "all 0.2s ease";

        const labelText = typeof optText === "object" ? (optText.text || JSON.stringify(optText)) : String(optText);

        optBtn.innerHTML = `
          <span class="option-letter" style="display: inline-flex; align-items: center; justify-content: center; width: 36px; height: 36px; min-width: 36px; border-radius: 50%; font-weight: 700; font-size: 0.95rem; background: ${isSelected ? 'var(--primary-600, #2563eb)' : '#f1f5f9'}; color: ${isSelected ? '#ffffff' : '#334155'}; border: 1.5px solid ${isSelected ? 'var(--primary-600, #2563eb)' : '#cbd5e1'};">${letters[optIdx] || (optIdx + 1)}</span>
          <span class="option-label" style="flex: 1; font-size: 0.98rem; line-height: 1.5; color: inherit;">${escapeHtml(labelText)}</span>
        `;
        optBtn.addEventListener("click", (e) => {
          e.preventDefault();
          selectOption(optIdx);
        });
        optionsContainer.appendChild(optBtn);
      });
    }
  }

  updatePaletteHighlight();
}

/**
 * Handle Option Selection & Autosave Draft
 */
function selectOption(optionIndex) {
  if (testSubmitted) return;

  userAnswers[currentIndex] = optionIndex;

  const optionsContainer = document.getElementById("options-container");
  if (optionsContainer) {
    const buttons = optionsContainer.querySelectorAll(".option-btn");
    buttons.forEach((btn, idx) => {
      const isSelected = (idx === optionIndex);
      const letterSpan = btn.querySelector(".option-letter");
      if (isSelected) {
        btn.classList.add("selected");
        btn.style.borderColor = "var(--primary-600, #2563eb)";
        btn.style.background = "var(--primary-50, #eff6ff)";
        if (letterSpan) {
          letterSpan.style.background = "var(--primary-600, #2563eb)";
          letterSpan.style.color = "#ffffff";
          letterSpan.style.borderColor = "var(--primary-600, #2563eb)";
        }
      } else {
        btn.classList.remove("selected");
        btn.style.borderColor = "var(--border-color, #e2e8f0)";
        btn.style.background = "var(--bg-card, #ffffff)";
        if (letterSpan) {
          letterSpan.style.background = "#f1f5f9";
          letterSpan.style.color = "#334155";
          letterSpan.style.borderColor = "#cbd5e1";
        }
      }
    });
  }

  updatePaletteHighlight();

  // Autosave draft answers to backend
  autosaveDraft();
}

async function autosaveDraft() {
  const employee = getLoggedInEmployee();
  if (!employee || !currentSessionId) return;

  try {
    const draftMap = {};
    userAnswers.forEach((val, idx) => {
      if (val !== null) draftMap[idx] = val;
    });

    await fetch(`${API_BASE}/api/aptitude/session/save-draft`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        session_id: currentSessionId,
        employee_id: employee.id,
        answers: draftMap
      })
    });
  } catch (err) {
    // Non-blocking draft save
  }
}

/**
 * Render Question Palette
 */
function renderPalette() {
  const paletteContainer = document.getElementById("question-palette");
  if (!paletteContainer) return;

  paletteContainer.innerHTML = "";

  questions.forEach((_, idx) => {
    const btn = document.createElement("button");
    btn.className = "palette-btn";
    btn.id = `palette-btn-${idx}`;
    btn.textContent = idx + 1;
    btn.title = `Go to Question ${idx + 1}`;
    btn.addEventListener("click", () => renderQuestion(idx));
    paletteContainer.appendChild(btn);
  });
}

function updatePaletteHighlight() {
  questions.forEach((_, idx) => {
    const btn = document.getElementById(`palette-btn-${idx}`);
    if (!btn) return;

    btn.className = "palette-btn";
    if (idx === currentIndex) {
      btn.classList.add("current");
    }
    if (userAnswers[idx] !== null && userAnswers[idx] !== undefined) {
      btn.classList.add("answered");
    }
  });
}

function navigateQuestion(newIndex) {
  if (newIndex >= 0 && newIndex < questions.length) {
    renderQuestion(newIndex);
  }
}

/**
 * Final Server-Side Submission & Score Calculation
 */
async function submitTest() {
  if (testSubmitted) return;
  testSubmitted = true;

  if (timerInterval) clearInterval(timerInterval);

  const employee = getLoggedInEmployee();
  if (!employee) return;

  const btnSubmit = document.getElementById("btn-submit-test");
  if (btnSubmit) {
    btnSubmit.disabled = true;
    btnSubmit.textContent = "Grading Assessment...";
  }

  try {
    const res = await fetch(`${API_BASE}/api/aptitude/submit`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        session_id: currentSessionId,
        employee_id: employee.id,
        user_answers: userAnswers
      })
    });

    const data = await res.json();

    if (res.ok && data.success) {
      serverReviewData = data.review || [];
      showResultsScreen(data);

      // Award gamification points
      try {
        await fetch(`${API_BASE}/api/gamification/award-points`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            employee_id: employee.id,
            activity: "aptitude",
            points: 50
          })
        });
      } catch (e) {}

      showToast("Aptitude test evaluated and permanently recorded! 🎉", "success");
    } else {
      throw new Error(data.message || "Failed to grade assessment.");
    }
  } catch (err) {
    console.error("Submission error:", err);
    showToast(err.message || "Error submitting test. Please try again.", "error");
    if (btnSubmit) {
      btnSubmit.disabled = false;
      btnSubmit.textContent = "Submit Test";
      testSubmitted = false;
    }
  }
}

/**
 * Show the Scorecard and Detailed Review Screen
 */
function showResultsScreen(resultData) {
  const viewScreen = document.getElementById("test-view-screen");
  const resultScreen = document.getElementById("test-result-screen");

  if (viewScreen) viewScreen.style.display = "none";
  if (resultScreen) resultScreen.style.display = "block";

  const scoreText = document.getElementById("result-score-text");
  const percentText = document.getElementById("result-percentage-text");
  const badgeEl = document.getElementById("result-badge");
  const msgEl = document.getElementById("result-message");
  const btnRetake = document.getElementById("btn-retake-test");

  if (btnRetake) btnRetake.style.display = "none";

  if (scoreText) scoreText.textContent = `${resultData.score} / ${resultData.total}`;
  if (percentText) percentText.textContent = `${resultData.percentage}%`;

  if (badgeEl) {
    badgeEl.textContent = resultData.performance_message || "Assessment Completed";
    badgeEl.className = `badge ${resultData.percentage >= 70 ? 'badge-success' : (resultData.percentage >= 50 ? 'badge-warning' : 'badge-danger')}`;
  }

  if (msgEl) {
    if (resultData.percentage >= 80) {
      msgEl.textContent = "Outstanding Performance! Your analytical readiness is well above industry placement benchmarks.";
    } else if (resultData.percentage >= 50) {
      msgEl.textContent = "Good effort! Solid foundations demonstrated. Review the category breakdown below for target areas.";
    } else {
      msgEl.textContent = "Focus required. Strengthen your weak topics and practice targeted question sets.";
    }
  }

  renderCategoryBreakdown(resultData.category_breakdown || {});
  renderDetailedReview();
}

function renderCategoryBreakdown(breakdown) {
  const container = document.getElementById("category-breakdown-grid");
  if (!container) return;

  container.innerHTML = "";
  const entries = Object.entries(breakdown);

  if (entries.length === 0) {
    container.innerHTML = `<p style="color: var(--text-muted);">No category data available.</p>`;
    return;
  }

  entries.forEach(([catName, stats]) => {
    const pct = stats.total > 0 ? Math.round((stats.correct / stats.total) * 100) : 0;
    const card = document.createElement("div");
    card.className = "category-card";
    card.innerHTML = `
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
        <span style="font-weight: 600; font-size: 0.9rem; color: var(--text-main);">${escapeHtml(catName)}</span>
        <span style="font-weight: 700; font-size: 0.9rem; color: ${pct >= 75 ? '#16a34a' : (pct >= 50 ? '#d97706' : '#dc2626')};">${stats.correct}/${stats.total} (${pct}%)</span>
      </div>
      <div class="progress-bar-bg" style="height: 6px;">
        <div class="progress-bar-fill" style="width: ${pct}%; background: ${pct >= 75 ? '#16a34a' : (pct >= 50 ? '#d97706' : '#dc2626')};"></div>
      </div>
    `;
    container.appendChild(card);
  });
}

function renderDetailedReview() {
  const reviewList = document.getElementById("review-questions-list");
  if (!reviewList) return;

  reviewList.innerHTML = "";

  if (!serverReviewData || serverReviewData.length === 0) {
    reviewList.innerHTML = `<p style="color: var(--text-muted);">No review items available.</p>`;
    return;
  }

  const letters = ["A", "B", "C", "D", "E"];

  serverReviewData.forEach((item, idx) => {
    const isCorrect = item.is_correct;
    const userChoice = item.user_answer_index;
    const correctChoice = item.correct_answer_index;

    const itemEl = document.createElement("div");
    itemEl.className = `review-item ${isCorrect ? 'correct' : 'incorrect'}`;

    let optionsHtml = "";
    (item.options || []).forEach((opt, oIdx) => {
      let optClass = "";
      let optTag = "";

      if (oIdx === correctChoice) {
        optClass = "correct-choice";
        optTag = " ✔ (Correct Answer)";
      }
      if (oIdx === userChoice && !isCorrect) {
        optClass = "user-wrong-choice";
        optTag = " ✖ (Your Choice)";
      }

      optionsHtml += `
        <div class="review-option ${optClass}">
          <strong>${letters[oIdx]}.</strong> ${escapeHtml(opt)} ${optTag}
        </div>
      `;
    });

    itemEl.innerHTML = `
      <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 8px;">
        <div>
          <span class="badge ${isCorrect ? 'badge-success' : 'badge-danger'}" style="font-size: 0.75rem; margin-right: 8px;">
            ${isCorrect ? 'PASSED (+1)' : (userChoice === null ? 'SKIPPED (0)' : 'INCORRECT (0)')}
          </span>
          <span style="font-size: 0.8rem; color: var(--text-muted); font-weight: 600;">${escapeHtml(item.category)}</span>
        </div>
        <span style="font-size: 0.8rem; color: var(--text-muted);">Q${idx + 1}</span>
      </div>

      <p style="font-weight: 600; font-size: 0.95rem; color: var(--text-main); margin-bottom: 12px;">
        ${idx + 1}. ${escapeHtml(item.question)}
      </p>

      <div class="review-options-grid" style="display: flex; flex-direction: column; gap: 6px; margin-bottom: 12px;">
        ${optionsHtml}
      </div>

      <div class="review-explanation" style="background: #f8fafc; border-left: 3px solid var(--primary-500); padding: 10px 14px; border-radius: 4px; font-size: 0.85rem; color: var(--text-main);">
        <strong style="color: var(--primary-700);">💡 Detailed Solution & Explanation:</strong><br>
        ${escapeHtml(item.explanation || "Standard problem solving logic applied.")}
      </div>
    `;

    reviewList.appendChild(itemEl);
  });
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
