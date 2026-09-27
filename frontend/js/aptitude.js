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
let securityManager = null; // Anti-cheating & proctoring manager

// Mode Selection & Per-Question Timer State
let currentTestMode = "mock"; // 'practice' or 'mock'
const PER_QUESTION_TIME_LIMIT = 60; // 60s limit per question in Mock mode
let questionTimerSeconds = 60;
let questionTimerInterval = null;
let practiceCheckedMap = {}; // Tracks checked questions in Practice mode

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

  if (btnPrev) btnPrev.addEventListener("click", () => navigateQuestion(currentIndex - 1));
  if (btnNext) btnNext.addEventListener("click", () => navigateQuestion(currentIndex + 1));
  
  if (btnSubmit) {
    btnSubmit.addEventListener("click", () => {
      if (securityManager) securityManager.beginInternalAction();
      const answeredCount = userAnswers.filter(a => a !== null).length;
      if (answeredCount < questions.length) {
        if (confirm(`You have answered ${answeredCount} of ${questions.length} questions. Are you sure you want to submit your final attempt?`)) {
          submitTest(false);
        } else {
          if (securityManager) securityManager.endInternalAction();
        }
      } else {
        submitTest(false);
      }
    });
  }

  if (btnRetake) {
    btnRetake.style.display = "inline-block";
    btnRetake.addEventListener("click", () => {
      testSubmitted = false;
      const resultScreen = document.getElementById("test-result-screen");
      const viewScreen = document.getElementById("test-view-screen");
      const modeScreen = document.getElementById("mode-selection-screen");
      if (resultScreen) resultScreen.style.display = "none";
      if (viewScreen) viewScreen.style.display = "none";
      if (modeScreen) modeScreen.style.display = "block";
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  }

  const btnNewTest = document.getElementById("btn-new-aptitude");
  if (btnNewTest) {
    btnNewTest.addEventListener("click", async () => {
      if (securityManager) securityManager.beginInternalAction();
      const answered = userAnswers.filter(a => a !== null).length;
      if (answered > 0 && !confirm("Generate a fresh set of questions? Your current progress will reset.")) {
        if (securityManager) securityManager.endInternalAction();
        return;
      }
      btnNewTest.disabled = true;
      btnNewTest.innerHTML = '<i class="fa-solid fa-arrows-rotate fa-spin"></i> Loading...';
      await initOrResumeSecureTest(true, currentTestMode);
      btnNewTest.disabled = false;
      btnNewTest.innerHTML = '<i class="fa-solid fa-arrows-rotate"></i> New Questions';
      showToast("Fresh randomized aptitude test loaded!", "success");
    });
  }

  const selectDiff = document.getElementById("select-apt-difficulty");
  if (selectDiff) {
    selectDiff.addEventListener("change", async () => {
      if (securityManager) securityManager.beginInternalAction();
      const answered = userAnswers.filter(a => a !== null).length;
      if (answered > 0 && !confirm("Changing difficulty will start a fresh assessment. Continue?")) {
        if (securityManager) securityManager.endInternalAction();
        return;
      }
      await initOrResumeSecureTest(true, currentTestMode);
      showToast(`Questions loaded for ${selectDiff.options[selectDiff.selectedIndex].text}!`, "info");
    });
  }

  // Mode Selection Screen Handlers
  const btnSelectPractice = document.getElementById("btn-select-practice");
  const btnSelectMock = document.getElementById("btn-select-mock");
  const btnCancelMock = document.getElementById("btn-cancel-mock");
  const modalInstructions = document.getElementById("modal-test-instructions");
  const checkAgree = document.getElementById("check-agree-security");
  const btnStartSecure = document.getElementById("btn-start-secure-test");

  if (btnSelectPractice) {
    btnSelectPractice.addEventListener("click", async () => {
      currentTestMode = "practice";
      const modeScreen = document.getElementById("mode-selection-screen");
      const viewScreen = document.getElementById("test-view-screen");
      if (modeScreen) modeScreen.style.display = "none";
      if (viewScreen) viewScreen.style.display = "block";
      updateModeHeaderUI("practice");
      await initOrResumeSecureTest(true, "practice");
      showToast("Practice Mode started. Learn without time pressure!", "success");
    });
  }

  if (btnSelectMock) {
    btnSelectMock.addEventListener("click", () => {
      currentTestMode = "mock";
      if (modalInstructions) {
        if (checkAgree) checkAgree.checked = false;
        if (btnStartSecure) {
          btnStartSecure.disabled = true;
          btnStartSecure.style.opacity = "0.5";
          btnStartSecure.style.cursor = "not-allowed";
        }
        modalInstructions.style.display = "flex";
      }
    });
  }

  if (btnCancelMock) {
    btnCancelMock.addEventListener("click", () => {
      if (modalInstructions) modalInstructions.style.display = "none";
    });
  }

  if (checkAgree && btnStartSecure) {
    checkAgree.addEventListener("change", () => {
      btnStartSecure.disabled = !checkAgree.checked;
      btnStartSecure.style.opacity = checkAgree.checked ? "1.0" : "0.5";
      btnStartSecure.style.cursor = checkAgree.checked ? "pointer" : "not-allowed";
    });

    btnStartSecure.addEventListener("click", async () => {
      if (modalInstructions) modalInstructions.style.display = "none";
      const modeScreen = document.getElementById("mode-selection-screen");
      const viewScreen = document.getElementById("test-view-screen");
      if (modeScreen) modeScreen.style.display = "none";
      if (viewScreen) viewScreen.style.display = "block";
      updateModeHeaderUI("mock");
      await initOrResumeSecureTest(true, "mock");
      if (securityManager) {
        await securityManager.requestFullscreen();
        securityManager.start(0);
      }
      showToast("Mock Assessment Mode active. Proctored examination started.", "info");
    });
  }

  // Check for in-flight active session on page load
  await checkInFlightSession();
});

/**
 * Updates header badges and timer pills according to active mode
 */
function updateModeHeaderUI(mode) {
  const badge = document.getElementById("active-mode-badge");
  const qTimerBox = document.getElementById("q-timer-box");
  const timerBox = document.getElementById("timer-box");
  const timerDisplay = document.getElementById("timer-display");

  if (badge) {
    badge.style.display = "inline-block";
    if (mode === "practice") {
      badge.className = "badge badge-success";
      badge.innerHTML = '<i class="fa-solid fa-graduation-cap"></i> Practice Mode';
    } else {
      badge.className = "badge badge-purple";
      badge.innerHTML = '<i class="fa-solid fa-shield-halved"></i> Mock Assessment';
    }
  }

  if (mode === "practice") {
    if (qTimerBox) qTimerBox.style.display = "none";
    if (timerBox) {
      timerBox.style.background = "#dcfce7";
      timerBox.style.color = "#15803d";
      timerBox.style.borderColor = "#bbf7d0";
    }
    if (timerDisplay) timerDisplay.textContent = "Self-Paced";
  } else {
    if (qTimerBox) qTimerBox.style.display = "inline-flex";
    if (timerBox) {
      timerBox.style.background = "#fef2f2";
      timerBox.style.color = "#dc2626";
      timerBox.style.borderColor = "#fecaca";
    }
  }
}

/**
 * Checks if candidate has an existing active in-flight session on page load/reload
 */
async function checkInFlightSession() {
  const employee = getLoggedInEmployee();
  if (!employee) return;

  try {
    const res = await fetch(`${API_BASE}/api/aptitude/session/active?employee_id=${employee.id}&tab_token=${tabToken}`);
    if (res.ok) {
      const data = await res.json();
      if (data.has_active && data.questions && data.questions.length > 0) {
        currentTestMode = (data.mode || "mock").toLowerCase();
        const modeScreen = document.getElementById("mode-selection-screen");
        const viewScreen = document.getElementById("test-view-screen");
        if (modeScreen) modeScreen.style.display = "none";
        if (viewScreen) viewScreen.style.display = "block";
        updateModeHeaderUI(currentTestMode);
        await initOrResumeSecureTest(false, currentTestMode);
        return;
      }
    }
  } catch (e) {
    console.warn("Could not check active session:", e);
  }

  // No active session: show mode selection screen
  const modeScreen = document.getElementById("mode-selection-screen");
  const viewScreen = document.getElementById("test-view-screen");
  const resultScreen = document.getElementById("test-result-screen");
  if (modeScreen) modeScreen.style.display = "block";
  if (viewScreen) viewScreen.style.display = "none";
  if (resultScreen) resultScreen.style.display = "none";
}

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
    btnChangeQ.innerHTML = '<span><i class="fa-solid fa-dice fa-spin"></i> Swapping...</span>';
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
        showToast("Question changed! Fresh challenge loaded", "success");
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
      btnChangeQ.innerHTML = '<span><i class="fa-solid fa-dice"></i> Change Question</span>';
    }
  }
}

/**
 * Initialize new or resume in-flight secure test session
 */
async function initOrResumeSecureTest(forceNew = false, mode = null) {
  testSubmitted = false;
  currentIndex = 0;
  serverReviewData = [];
  practiceCheckedMap = {};

  if (mode) {
    currentTestMode = mode;
  } else if (!currentTestMode) {
    currentTestMode = "mock";
  }

  const employee = getLoggedInEmployee();
  if (!employee) return;

  const modeScreen = document.getElementById("mode-selection-screen");
  const viewScreen = document.getElementById("test-view-screen");
  const resultScreen = document.getElementById("test-result-screen");
  const questionTextEl = document.getElementById("question-text");

  if (modeScreen) modeScreen.style.display = "none";
  if (viewScreen) viewScreen.style.display = "block";
  if (resultScreen) resultScreen.style.display = "none";
  if (questionTextEl) questionTextEl.innerHTML = '<i class="fa-solid fa-gear fa-spin"></i> Connecting to test server & generating questions...';

  updateModeHeaderUI(currentTestMode);

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
        retake: forceNew,
        mode: currentTestMode
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
            <span style="font-size: 3rem; color: #f59e0b;"><i class="fa-solid fa-triangle-exclamation"></i></span>
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
      currentTestMode = (data.mode || currentTestMode || "mock").toLowerCase();
      updateModeHeaderUI(currentTestMode);

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
          showToast(`Active ${currentTestMode === 'practice' ? 'Practice' : 'Mock'} session resumed seamlessly`, "info");
        }
      }

      renderPalette();
      renderQuestion(currentIndex);

      if (currentTestMode === "mock") {
        startTimer();
        startPerQuestionTimer();

        // Initialize security & anti-cheating manager
        if (securityManager) {
          securityManager.stop();
        }

        securityManager = new TestSecurityManager({
          attemptId: currentSessionId,
          employeeId: employee.id,
          maxViolations: 3,
          onAutoSubmit: () => {
            submitTest(true);
          },
          onViolation: (count, max, type) => {
            console.warn(`[AntiCheat] Violation recorded: ${count}/${max} (${type})`);
          }
        });

        // Start monitoring (passing restored violation count if restored)
        securityManager.start(data.violation_count || 0);
      } else {
        // Practice Mode: completely deactivate proctoring and timers
        if (securityManager) {
          securityManager.stop();
          securityManager.exitFullscreen();
          securityManager = null;
        }
        if (timerInterval) clearInterval(timerInterval);
        if (questionTimerInterval) clearInterval(questionTimerInterval);
        const qTimerBox = document.getElementById("q-timer-box");
        if (qTimerBox) qTimerBox.style.display = "none";
      }
    } else {
      throw new Error(data.message || "Failed to initialize test session.");
    }
  } catch (err) {
    console.error("Test initialization error:", err);
    showToast(err.message || "Could not connect to test server.", "error");
  }
}

/**
 * Starts strict per-question countdown timer for Mock Assessment Mode (60s)
 */
function startPerQuestionTimer() {
  if (currentTestMode !== "mock" || testSubmitted) {
    const qTimerBox = document.getElementById("q-timer-box");
    if (qTimerBox) qTimerBox.style.display = "none";
    return;
  }

  if (questionTimerInterval) clearInterval(questionTimerInterval);
  questionTimerSeconds = PER_QUESTION_TIME_LIMIT;

  const qTimerBox = document.getElementById("q-timer-box");
  const qTimerDisplay = document.getElementById("q-timer-display");
  if (qTimerBox) {
    qTimerBox.style.display = "inline-flex";
    qTimerBox.classList.remove("timer-urgent");
  }
  if (qTimerDisplay) qTimerDisplay.textContent = `${questionTimerSeconds}s`;

  questionTimerInterval = setInterval(() => {
    if (testSubmitted) {
      clearInterval(questionTimerInterval);
      return;
    }
    questionTimerSeconds--;
    if (qTimerDisplay) qTimerDisplay.textContent = `${questionTimerSeconds}s`;

    if (questionTimerSeconds <= 15 && qTimerBox) {
      qTimerBox.classList.add("timer-urgent");
    }

    if (questionTimerSeconds <= 0) {
      clearInterval(questionTimerInterval);
      showToast(`Question ${currentIndex + 1} time limit reached. Moving to next question.`, "warning");
      if (currentIndex < questions.length - 1) {
        navigateQuestion(currentIndex + 1);
      } else {
        submitTest(false);
      }
    }
  }, 1000);
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
  if (badgeEl) badgeEl.innerHTML = 'Attempt Verified <i class="fa-solid fa-check"></i>';
  if (msgEl) {
    msgEl.innerHTML = `
      <div style="background: #eff6ff; border: 1px solid #bfdbfe; color: #1e40af; padding: 12px 16px; border-radius: 8px; margin-top: 10px;">
        <strong><i class="fa-solid fa-lock"></i> Single-Attempt Security Policy:</strong><br>
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
      diffEl.innerHTML = '<i class="fa-solid fa-circle text-success status-indicator-dot"></i> Low (Easy)';
      diffEl.className = "badge badge-success";
    } else if (d === "hard" || d === "high") {
      diffEl.innerHTML = '<i class="fa-solid fa-circle text-danger status-indicator-dot"></i> High (Hard)';
      diffEl.className = "badge badge-danger";
    } else {
      diffEl.innerHTML = '<i class="fa-solid fa-circle text-warning status-indicator-dot"></i> Medium';
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

    // In Practice Mode: render instant "Check Answer & Explanation" section
    if (currentTestMode === "practice") {
      const checkContainer = document.createElement("div");
      checkContainer.className = "practice-check-container";
      checkContainer.id = "practice-check-container";

      const isAnswered = (userAnswers[currentIndex] !== null && userAnswers[currentIndex] !== undefined);
      const hasChecked = !!practiceCheckedMap[currentIndex];

      checkContainer.innerHTML = `
        <div style="display: flex; gap: 10px; align-items: center; margin-top: 6px;">
          <button type="button" class="btn btn-sm btn-outline-primary" id="btn-check-answer" style="border-color: #16a34a; color: #16a34a; font-weight: 600; padding: 7px 16px;" ${!isAnswered ? 'disabled' : ''}>
            <i class="fa-solid fa-circle-check"></i> ${hasChecked ? 'Re-check Answer & Explanation' : 'Check Answer & Explanation'}
          </button>
        </div>
        <div id="practice-explanation-display"></div>
      `;
      optionsContainer.appendChild(checkContainer);

      const btnCheck = document.getElementById("btn-check-answer");
      if (btnCheck) {
        btnCheck.addEventListener("click", () => handlePracticeCheckAnswer(true));
      }

      // If user had previously checked this question in this session, re-render the explanation
      if (hasChecked && isAnswered) {
        handlePracticeCheckAnswer(false);
      }
    }
  }

  // In Mock Mode: start strict per-question timer
  if (currentTestMode === "mock") {
    startPerQuestionTimer();
  }

  updatePaletteHighlight();
}

/**
 * Validates selected answer against client-provided solution in Practice Mode
 */
function handlePracticeCheckAnswer(showToastAlert = true) {
  const q = questions[currentIndex];
  if (!q) return;
  const userAns = userAnswers[currentIndex];
  if (userAns === null || userAns === undefined) {
    showToast("Please choose an option first.", "info");
    return;
  }

  practiceCheckedMap[currentIndex] = true;
  const correctIdx = q.practice_correct_index;
  const isCorrect = (userAns === correctIdx);

  // Highlight options dynamically
  const optionsContainer = document.getElementById("options-container");
  if (optionsContainer) {
    const buttons = optionsContainer.querySelectorAll(".option-btn");
    buttons.forEach((btn, idx) => {
      btn.classList.remove("practice-correct", "practice-incorrect");
      if (idx === correctIdx) {
        btn.classList.add("practice-correct");
      }
      if (!isCorrect && idx === userAns) {
        btn.classList.add("practice-incorrect");
      }
    });
  }

  const explDisplay = document.getElementById("practice-explanation-display");
  if (explDisplay) {
    const letters = ["A", "B", "C", "D", "E", "F"];
    const correctLetter = letters[correctIdx] || (correctIdx + 1);
    explDisplay.innerHTML = `
      <div class="practice-explanation-card ${isCorrect ? 'correct-expl' : 'incorrect-expl'}">
        <div class="practice-explanation-title" style="color: ${isCorrect ? '#15803d' : '#b91c1c'}; font-size: 1rem;">
          <i class="${isCorrect ? 'fa-solid fa-circle-check' : 'fa-solid fa-circle-xmark'}"></i>
          ${isCorrect ? 'Correct! Excellent work.' : `Incorrect. The correct answer is Option ${correctLetter}.`}
        </div>
        <div style="font-size: 0.92rem; color: #334155; line-height: 1.55; margin-top: 6px;">
          <strong>Explanation:</strong> ${escapeHtml(q.explanation || "Standard analytical formula and reasoning applied.")}
        </div>
      </div>
    `;
  }

  if (showToastAlert) {
    if (isCorrect) {
      showToast("Correct answer! Great job.", "success");
    } else {
      showToast("Review the explanation above to learn the solution.", "info");
    }
  }
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

    // In Practice Mode: enable Check Answer button
    if (currentTestMode === "practice") {
      const btnCheck = document.getElementById("btn-check-answer");
      if (btnCheck) {
        btnCheck.disabled = false;
        btnCheck.style.opacity = "1";
        btnCheck.style.cursor = "pointer";
      }
    }
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
async function submitTest(isAutoSubmit = false) {
  if (testSubmitted) return;
  testSubmitted = true;

  if (timerInterval) clearInterval(timerInterval);
  if (questionTimerInterval) clearInterval(questionTimerInterval);

  // Stop security monitoring and exit fullscreen
  if (securityManager) {
    securityManager.stop();
    securityManager.exitFullscreen();
  }

  const employee = getLoggedInEmployee();
  if (!employee) return;

  const btnSubmit = document.getElementById("btn-submit-test");
  if (btnSubmit) {
    btnSubmit.disabled = true;
    btnSubmit.textContent = isAutoSubmit ? "Auto-Submitting Test..." : "Grading Assessment...";
  }

  try {
    const res = await fetch(`${API_BASE}/api/aptitude/submit`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        session_id: currentSessionId,
        employee_id: employee.id,
        user_answers: userAnswers,
        mode: currentTestMode,
        auto_submitted: isAutoSubmit
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

      if (isAutoSubmit) {
        showToast("Test auto-submitted due to repeated security violations.", "warning");
      } else {
        showToast("Aptitude test evaluated and permanently recorded!", "success");
      }
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

  if (btnRetake) btnRetake.style.display = "inline-block";

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
  renderSecurityReport(resultData);
}

/**
 * Render Anti-Cheating & Security Report on Result Screen
 */
function renderSecurityReport(resultData) {
  const card = document.getElementById("security-report-card");
  if (!card) return;

  // In Practice Mode, hide security report section completely
  if (resultData.mode === "practice" || currentTestMode === "practice" || !resultData.security_report) {
    card.style.display = "none";
    return;
  }

  card.style.display = "block";
  const badgeEl = document.getElementById("security-badge-status");
  const summaryEl = document.getElementById("security-summary-text");
  const eventsEl = document.getElementById("security-events-container");

  const vCount = resultData.violation_count !== undefined 
    ? resultData.violation_count 
    : (resultData.security_report?.total_violations || 0);
  const isAuto = Boolean(resultData.auto_submitted || resultData.security_report?.auto_submitted);
  const events = resultData.security_report?.events || [];

  if (isAuto) {
    if (badgeEl) {
      badgeEl.className = "badge badge-danger";
      badgeEl.innerHTML = '<i class="fa-solid fa-ban"></i> Auto-submitted (Security Violation)';
    }
    if (summaryEl) {
      summaryEl.innerHTML = `<span style="color: #dc2626; font-weight: 600;">Assessment was automatically terminated and submitted due to reaching ${vCount} security violations.</span>`;
    }
  } else if (vCount > 0) {
    if (badgeEl) {
      badgeEl.className = "badge badge-warning";
      badgeEl.innerHTML = `<i class="fa-solid fa-triangle-exclamation"></i> Flagged (${vCount} violations)`;
    }
    if (summaryEl) {
      summaryEl.textContent = `Warning flags were recorded during this session (${vCount} of 3 maximum allowed). Review the log below:`;
    }
  } else {
    if (badgeEl) {
      badgeEl.className = "badge badge-success";
      badgeEl.innerHTML = '<i class="fa-solid fa-shield-halved"></i> Clean Attempt (0 Violations)';
    }
    if (summaryEl) {
      summaryEl.textContent = "Excellent! Zero security or tab-switch violations detected. High integrity attempt verified.";
    }
  }

  if (eventsEl) {
    if (events.length > 0) {
      eventsEl.style.display = "flex";
      eventsEl.innerHTML = events.map((ev, i) => {
        const timeStr = ev.timestamp ? new Date(ev.timestamp).toLocaleTimeString() : `Event #${i+1}`;
        const typeLabels = {
          "tab_switch": "Tab Switched / Window Minimized",
          "window_blur": "Window Lost Focus",
          "fullscreen_exit": "Exited Fullscreen Mode",
          "copy_paste_attempt": "Prohibited Shortcut (Copy/Paste)",
          "right_click": "Disabled Context Menu Click"
        };
        const label = typeLabels[ev.event_type] || ev.event_type;
        const durStr = ev.duration_away_seconds ? ` (${ev.duration_away_seconds}s away)` : "";
        return `
          <div class="security-timeline-item">
            <span class="event-label">
              <i class="fa-solid fa-circle-exclamation"></i>
              <span>${escapeHtml(label)}${durStr}</span>
            </span>
            <span class="event-meta">${escapeHtml(timeStr)}</span>
          </div>
        `;
      }).join("");
    } else {
      eventsEl.style.display = "none";
    }
  }
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
        optTag = ' <i class="fa-solid fa-check text-success"></i> (Correct Answer)';
      }
      if (oIdx === userChoice && !isCorrect) {
        optClass = "user-wrong-choice";
        optTag = ' <i class="fa-solid fa-xmark text-danger"></i> (Your Choice)';
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
        <strong style="color: var(--primary-700);"><i class="fa-solid fa-lightbulb text-warning"></i> Detailed Solution & Explanation:</strong><br>
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
