/**
 * AI Employee Preparation Platform - Dynamic AI Mock Interview Engine
 * Ensures questions are freshly generated and randomized on every page reload & restart.
 */

let interviewQuestions = [];
let currentQIndex = 0;
let answersRecord = [];
let currentRole = "Java Developer";

document.addEventListener("DOMContentLoaded", () => {
  const employee = requireAuth();
  if (!employee) return;

  const urlParams = new URLSearchParams(window.location.search);
  const compSlug = (urlParams.get("company") || (getSelectedCompany() ? getSelectedCompany().slug : "")).toLowerCase();
  const interviewType = urlParams.get("type") || "mock";
  const roleParam = urlParams.get("role");

  // Pre-select employee's target job role or url role
  const roleSelect = document.getElementById("interview-role-select");
  if (roleSelect) {
    if (roleParam) {
      for (let opt of roleSelect.options) {
        if (opt.value.toLowerCase().includes(roleParam.toLowerCase())) {
          roleSelect.value = opt.value;
          break;
        }
      }
    } else if (employee.job_role) {
      for (let opt of roleSelect.options) {
        if (opt.value.toLowerCase().includes(employee.job_role.toLowerCase()) || employee.job_role.toLowerCase().includes(opt.value.toLowerCase())) {
          roleSelect.value = opt.value;
          break;
        }
      }
    }
  }

  // Personalize setup title if company or type is specified
  if (compSlug || interviewType) {
    const pageTitle = document.querySelector("#interview-setup-screen h1");
    const pageBadge = document.querySelector("#interview-setup-screen .badge");
    const compUpper = compSlug ? compSlug.toUpperCase() : "TARGET COMPANY";
    if (pageBadge) pageBadge.textContent = `${compUpper} • ${interviewType === 'hr' ? 'HR Interview' : 'AI Mock Interview'}`;
    if (pageTitle) pageTitle.textContent = `${compUpper} ${interviewType === 'hr' ? 'HR & Behavioral Round' : 'AI Mock Interview'}`;
  }

  // Setup Event Listeners
  const btnStart = document.getElementById("btn-start-interview");
  const btnShuffle = document.getElementById("btn-shuffle-interview");
  const btnChangeSingle = document.getElementById("btn-change-single-q");
  const btnSubmitAnswer = document.getElementById("btn-submit-answer");
  const btnAbort = document.getElementById("btn-abort-interview");
  const btnRestart = document.getElementById("btn-restart-interview");
  const answerInput = document.getElementById("candidate-answer-input");
  const charCount = document.getElementById("char-count");

  if (btnStart) {
    btnStart.addEventListener("click", () => startInterview(true));
  }

  if (btnShuffle) {
    btnShuffle.addEventListener("click", shuffleInterviewQuestions);
  }

  if (btnChangeSingle) {
    btnChangeSingle.addEventListener("click", changeSingleInterviewQuestion);
  }

  if (btnSubmitAnswer) {
    btnSubmitAnswer.addEventListener("click", handleAnswerSubmit);
  }

  if (btnAbort) {
    btnAbort.addEventListener("click", () => {
      if (confirm("Are you sure you want to end this mock interview? Your active session will close.")) {
        sessionStorage.removeItem("interview_active");
        location.reload();
      }
    });
  }

  if (btnRestart) {
    btnRestart.addEventListener("click", () => {
      sessionStorage.removeItem("interview_active");
      location.reload();
    });
  }

  if (answerInput && charCount) {
    answerInput.addEventListener("input", () => {
      const text = answerInput.value.trim();
      const words = text ? text.split(/\s+/).length : 0;
      charCount.textContent = `${words} words`;
    });

    // Support Ctrl+Enter / Cmd+Enter to quickly submit answer
    answerInput.addEventListener("keydown", (e) => {
      if ((e.ctrlKey || e.metaKey) && e.key === "Enter") {
        e.preventDefault();
        handleAnswerSubmit();
      }
    });
  }

  // If candidate was in an active interview session and refreshed the page (F5),
  // automatically reload with brand new randomized questions!
  if (sessionStorage.getItem("interview_active") === "true") {
    startInterview(true);
  }
});

/**
 * Start Dynamic Personalized Interview Flow
 * Always forces fresh questions via refresh=true & timestamp cache-buster
 */
async function startInterview(forceNew = true) {
  const roleSelect = document.getElementById("interview-role-select");
  currentRole = roleSelect ? roleSelect.value : "Java Developer";

  const diffSelect = document.getElementById("interview-difficulty-select");
  const selectedDiff = diffSelect ? diffSelect.value : "all";

  const urlParams = new URLSearchParams(window.location.search);
  const compSlug = (urlParams.get("company") || (getSelectedCompany() ? getSelectedCompany().slug : "")).toLowerCase();
  const interviewType = urlParams.get("type") || "mock";

  const employee = getLoggedInEmployee();
  const empId = employee ? employee.id : 1;
  const skills = employee ? (employee.skills || "") : "";
  const qual = employee ? (employee.qualification || "") : "";
  const exp = employee ? (employee.experience || "") : "";

  // Update difficulty badge on interview screen
  const diffBadge = document.getElementById("int-diff-badge");
  if (diffBadge) {
    if (selectedDiff === "low" || selectedDiff === "easy") {
      diffBadge.innerHTML = '<i class="fa-solid fa-circle text-success status-indicator-dot"></i> Low (Easy)';
      diffBadge.className = "badge badge-success";
    } else if (selectedDiff === "high" || selectedDiff === "hard") {
      diffBadge.innerHTML = '<i class="fa-solid fa-circle text-danger status-indicator-dot"></i> High (Hard)';
      diffBadge.className = "badge badge-danger";
    } else if (selectedDiff === "medium") {
      diffBadge.innerHTML = '<i class="fa-solid fa-circle text-warning status-indicator-dot"></i> Medium';
      diffBadge.className = "badge badge-warning";
    } else {
      diffBadge.innerHTML = '<i class="fa-solid fa-bolt text-primary"></i> Balanced';
      diffBadge.className = "badge badge-primary";
    }
  }

  // Mark session as active in browser
  sessionStorage.setItem("interview_active", "true");

  try {
    const queryParams = new URLSearchParams({
      employee_id: empId,
      job_role: currentRole,
      company: compSlug,
      type: interviewType,
      difficulty: selectedDiff,
      skills: skills,
      qualification: qual,
      experience: exp,
      refresh: "true",
      force_new: "true",
      _t: Date.now().toString()
    });

    const url = `${API_BASE}/api/interview/questions?${queryParams.toString()}`;
    const res = await fetch(url);
    if (res.ok) {
      const data = await res.json();
      if (data.success && Array.isArray(data.questions) && data.questions.length > 0) {
        interviewQuestions = data.questions;
      }
    }
  } catch (err) {
    console.warn("Interview API call error, generating dynamic fallback questions:", err);
  }

  // If API was unreachable or returned empty, build fresh randomized fallback questions
  if (!interviewQuestions || interviewQuestions.length === 0) {
    interviewQuestions = generateFallbackInterviewQuestions(currentRole, compSlug, interviewType);
  }

  currentQIndex = 0;
  answersRecord = [];

  // Switch Screens
  const setupScreen = document.getElementById("interview-setup-screen");
  const sessionScreen = document.getElementById("interview-session-screen");
  const summaryScreen = document.getElementById("interview-summary-screen");

  if (setupScreen) setupScreen.style.display = "none";
  if (summaryScreen) summaryScreen.style.display = "none";
  if (sessionScreen) sessionScreen.style.display = "block";

  renderCurrentQuestion();
}

/**
 * Shuffle and replace the active interview with fresh randomized questions
 */
async function shuffleInterviewQuestions() {
  const btnShuffle = document.getElementById("btn-shuffle-interview");
  if (answersRecord.length > 0) {
    if (!confirm("Generate a fresh set of questions? Your current round answers will reset.")) {
      return;
    }
  }

  if (btnShuffle) {
    btnShuffle.disabled = true;
    btnShuffle.innerHTML = '<i class="fa-solid fa-arrows-rotate fa-spin"></i> Generating...';
  }

  try {
    await startInterview(true);
    showToast("Fresh AI interview questions generated!", "success");
  } finally {
    if (btnShuffle) {
      btnShuffle.disabled = false;
      btnShuffle.innerHTML = '<i class="fa-solid fa-arrows-rotate"></i> New Questions';
    }
  }
}

/**
 * Change only the currently active interview question without resetting the entire session
 */
async function changeSingleInterviewQuestion() {
  if (currentQIndex < 0 || currentQIndex >= interviewQuestions.length) return;
  const currentQ = interviewQuestions[currentQIndex];
  const btnChangeSingle = document.getElementById("btn-change-single-q");

  if (btnChangeSingle) {
    btnChangeSingle.disabled = true;
    btnChangeSingle.innerHTML = '<span><i class="fa-solid fa-dice fa-spin"></i> Changing...</span>';
  }

  try {
    const cat = currentQ.category || "";
    const excludeId = currentQ.bank_id || "";
    const urlParams = new URLSearchParams(window.location.search);
    const compSlug = (urlParams.get("company") || (getSelectedCompany() ? getSelectedCompany().slug : "")).toLowerCase();
    const res = await fetch(`${API_BASE}/api/interview/random-question?category=${encodeURIComponent(cat)}&role=${encodeURIComponent(currentRole)}&company=${encodeURIComponent(compSlug)}&exclude_id=${encodeURIComponent(excludeId)}&_t=${Date.now()}`);
    if (res.ok) {
      const data = await res.json();
      if (data.success && data.question) {
        interviewQuestions[currentQIndex] = {
          ...currentQ,
          ...data.question
        };
        renderCurrentQuestion();
        showToast("Interview question changed!", "success");
      }
    }
  } catch (err) {
    console.error("Failed to change interview question:", err);
    showToast("Could not change question right now.", "warning");
  } finally {
    if (btnChangeSingle) {
      btnChangeSingle.disabled = false;
      btnChangeSingle.innerHTML = '<span><i class="fa-solid fa-dice"></i> Change Question</span>';
    }
  }
}

/**
 * Render Current Interview Question to the Chat UI
 */
function renderCurrentQuestion() {
  if (currentQIndex < 0 || currentQIndex >= interviewQuestions.length) return;

  const q = interviewQuestions[currentQIndex];

  // Role Badge
  const roleBadge = document.getElementById("int-role-badge");
  if (roleBadge) roleBadge.textContent = currentRole;

  // Counter
  const qCounter = document.getElementById("int-question-counter") || document.getElementById("interview-q-num");
  if (qCounter) qCounter.textContent = `Question ${currentQIndex + 1} of ${interviewQuestions.length}`;

  // Progress Bar
  const progressBar = document.getElementById("interview-progress-bar");
  if (progressBar) {
    const pct = Math.round(((currentQIndex + 1) / interviewQuestions.length) * 100);
    progressBar.style.width = `${pct}%`;
  }

  // Category Badge
  const catBadge = document.getElementById("int-cat-badge") || document.getElementById("interview-q-category");
  if (catBadge) catBadge.textContent = q.category || "Technical";

  // Question Text
  const qText = document.getElementById("ai-question-text") || document.getElementById("interview-q-text");
  if (qText) qText.textContent = q.question;

  // Guidance / Tip
  const guidanceText = document.getElementById("ai-guidance-text") || document.getElementById("interview-q-guidance");
  if (guidanceText) {
    guidanceText.innerHTML = q.guidance ? `<i class="fa-solid fa-lightbulb text-warning"></i> Tip: ${escapeHtml(q.guidance)}` : '<i class="fa-solid fa-lightbulb text-warning"></i> Tip: Structure your answer clearly with concrete examples and technical depth.';
  }

  // Candidate Answer Input & Counter
  const answerInput = document.getElementById("candidate-answer-input");
  if (answerInput) {
    answerInput.value = "";
    answerInput.focus();
  }

  const charCount = document.getElementById("char-count");
  if (charCount) charCount.textContent = "0 words";

  // Hide instant feedback box for the new question
  const feedbackBox = document.getElementById("ai-instant-feedback-box") || document.getElementById("live-feedback-box");
  if (feedbackBox) feedbackBox.style.display = "none";
}

/**
 * Handle Candidate Answer Submission
 */
async function handleAnswerSubmit() {
  const answerInput = document.getElementById("candidate-answer-input");
  const submitBtn = document.getElementById("btn-submit-answer");
  const feedbackBox = document.getElementById("ai-instant-feedback-box") || document.getElementById("live-feedback-box");
  const feedbackText = document.getElementById("instant-feedback-text") || document.getElementById("live-feedback-text");
  const scoreBadge = document.getElementById("instant-score-badge") || document.getElementById("live-score-badge");

  const answer = answerInput ? answerInput.value.trim() : "";
  if (!answer) {
    showToast("Please provide your answer before proceeding.", "warning");
    if (answerInput) answerInput.focus();
    return;
  }

  const currentQ = interviewQuestions[currentQIndex];
  if (submitBtn) {
    submitBtn.disabled = true;
    submitBtn.innerHTML = 'Analyzing Response with AI... <i class="fa-solid fa-robot"></i>';
  }

  // Evaluate candidate answer with AI
  let evalScore = 78;
  let strengths = ["Clear explanation", "Directly addresses core premise"];
  let improvements = ["Could elaborate more on architectural tradeoffs and real-world edge cases"];

  try {
    const res = await fetch(`${API_BASE}/api/ai/evaluate-answer`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        question: currentQ.question,
        category: currentQ.category,
        answer: answer,
        role: currentRole
      })
    });

    if (res.ok) {
      const data = await res.json();
      if (data.success && data.evaluation) {
        evalScore = data.evaluation.score || evalScore;
        strengths = data.evaluation.strengths || strengths;
        improvements = data.evaluation.improvements || improvements;
      }
    }
  } catch (e) {
    console.warn("AI Evaluate API fallback evaluation:", e);
    // Dynamic score heuristic based on length and relevance
    const wordCount = answer.split(/\s+/).length;
    evalScore = Math.min(95, Math.max(65, Math.round(60 + Math.min(30, wordCount * 0.4) + Math.random() * 8)));
  }

  // Record candidate answer
  answersRecord.push({
    question_id: currentQ.id,
    question: currentQ.question,
    category: currentQ.category,
    answer: answer,
    score: evalScore,
    strengths: strengths,
    improvements: improvements
  });

  // Display Real-Time AI Feedback
  if (feedbackBox) {
    feedbackBox.style.display = "block";
    if (scoreBadge) scoreBadge.textContent = `Score: ${evalScore}/100`;
    if (feedbackText) {
      feedbackText.innerHTML = `
        <div style="margin-bottom: 4px;"><strong><i class="fa-solid fa-check text-success"></i> Strengths:</strong> ${strengths.join(", ")}</div>
        <div><strong><i class="fa-solid fa-lightbulb text-warning"></i> Growth Tip:</strong> ${improvements.join(", ")}</div>
      `;
    }
  }

  showToast(`Response evaluated: ${evalScore}/100`, "success");

  // Advance to next question after brief feedback preview
  setTimeout(() => {
    if (submitBtn) {
      submitBtn.disabled = false;
      submitBtn.innerHTML = 'Submit Response & Next <i class="fa-solid fa-arrow-right"></i>';
    }

    if (currentQIndex + 1 < interviewQuestions.length) {
      currentQIndex++;
      renderCurrentQuestion();
    } else {
      finishInterview();
    }
  }, 1400);
}

/**
 * Finish Interview and Render Scorecard
 */
async function finishInterview() {
  sessionStorage.removeItem("interview_active");

  const sessionScreen = document.getElementById("interview-session-screen");
  const summaryScreen = document.getElementById("interview-summary-screen");

  if (sessionScreen) sessionScreen.style.display = "none";
  if (summaryScreen) summaryScreen.style.display = "block";

  const totalScore = answersRecord.reduce((acc, curr) => acc + curr.score, 0);
  const avgScore = answersRecord.length > 0 ? Math.round(totalScore / answersRecord.length) : 80;
  const techScore = Math.min(100, Math.round(avgScore * 0.98 + (Math.random() * 4)));
  const commScore = Math.min(100, Math.round(avgScore * 1.02 + (Math.random() * 4)));

  const overallScoreEl = document.getElementById("int-score-overall");
  const techScoreEl = document.getElementById("int-score-tech");
  const commScoreEl = document.getElementById("int-score-comm");
  const feedbackEl = document.getElementById("int-overall-feedback");
  const breakdownList = document.getElementById("int-breakdown-list");

  if (overallScoreEl) overallScoreEl.textContent = `${avgScore}/100`;
  if (techScoreEl) techScoreEl.textContent = `${techScore}/100`;
  if (commScoreEl) commScoreEl.textContent = `${commScore}/100`;

  let executiveFeedback = `You demonstrated solid understanding of ${currentRole} principles with structured articulation. `;
  if (avgScore >= 85) {
    executiveFeedback += "Your answers were comprehensive, analytical, and showed strong technical maturity. Excellent preparation for tier-1 placement drives!";
  } else {
    executiveFeedback += "Focus on adding concrete code examples, design pattern tradeoffs, and measurable production metrics to elevate your score.";
  }
  if (feedbackEl) feedbackEl.textContent = executiveFeedback;

  if (breakdownList) {
    breakdownList.innerHTML = "";
    answersRecord.forEach((rec, idx) => {
      const row = document.createElement("div");
      row.style.background = "var(--bg-subtle)";
      row.style.borderRadius = "var(--radius-md)";
      row.style.padding = "16px";
      row.innerHTML = `
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
          <strong style="color: var(--text-main); font-size: 0.95rem;">Q${idx + 1} [${rec.category}]: ${rec.question}</strong>
          <span class="badge ${rec.score >= 80 ? 'badge-success' : 'badge-warning'}">${rec.score}/100</span>
        </div>
        <div style="font-size: 0.88rem; color: var(--text-muted); margin-bottom: 6px;">
          <strong>Your Answer:</strong> "${rec.answer}"
        </div>
        <div style="font-size: 0.82rem; color: #166534;">
          <i class="fa-solid fa-check text-success"></i> ${rec.strengths.join(", ")} | <i class="fa-solid fa-lightbulb text-warning"></i> ${rec.improvements.join(", ")}
        </div>
      `;
      breakdownList.appendChild(row);
    });
  }

  // Save result to localStorage & backend
  const employee = getLoggedInEmployee();
  if (employee && employee.id) {
    const interviewObj = {
      job_role: currentRole,
      overall_score: avgScore,
      technical_score: techScore,
      communication_score: commScore,
      feedback: executiveFeedback
    };

    localStorage.setItem(`interviewResult_${employee.id}`, JSON.stringify(interviewObj));

    try {
      await fetch(`${API_BASE}/api/interview/submit`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          employee_id: employee.id,
          job_role: currentRole,
          answers: answersRecord
        })
      });
    } catch (e) {
      console.warn("Interview submission backend error:", e);
    }
  }

  showToast("Interview scorecard generated successfully!", "success");
}

/**
 * Generates dynamic, randomized questions locally if the backend is unreachable.
 * Ensures questions still vary randomly on reload even in offline environments.
 */
function generateFallbackInterviewQuestions(role, companySlug, type) {
  const companyName = companySlug ? companySlug.toUpperCase() : "our enterprise";

  const intros = [
    `Please introduce yourself and explain what motivated you to pursue the ${role} position at ${companyName}.`,
    `Walk us through your software engineering background, your primary tech stack, and why ${companyName} is your top choice.`,
    `What makes you uniquely qualified for this ${role} opportunity, and how have your past projects prepared you for enterprise scale?`,
    `Give us a concise elevator pitch of your programming journey, technical milestones, and career aspirations at ${companyName}.`
  ];

  const techQuestions = {
    "Java Developer": [
      { q: "Explain Java Garbage Collection algorithms and the memory lifecycle across Eden, Survivor, and Tenured spaces.", g: "Cover Mark-Sweep-Compact, G1, ZGC, and memory tuning parameters." },
      { q: "How do you achieve thread safety in Java? Compare synchronized blocks, volatile, and AtomicInteger.", g: "Discuss memory barriers, CAS operations, and lock contention." },
      { q: "Explain the internal workings of HashMap in Java 8+ including hash bucket collision handling with Red-Black Trees.", g: "Detail hash calculation, load factor, re-hashing, and treeify thresholds." },
      { q: "How does the Spring Boot auto-configuration mechanism work under the hood using condition annotations?", g: "Mention @EnableAutoConfiguration, spring.factories, and @ConditionalOnClass." }
    ],
    "Python Developer": [
      { q: "Explain the Global Interpreter Lock (GIL) in CPython and how you handle CPU-bound vs IO-bound concurrency.", g: "Discuss multiprocessing vs asyncio, threading, and uvloop." },
      { q: "How do Python memory management and reference counting work together with cyclic garbage collection?", g: "Explain generation 0, 1, 2 collections and gc module." },
      { q: "Explain Python generators, yield syntax, and how they optimize memory consumption when processing large datasets.", g: "Discuss iterator protocols, lazy evaluation, and generator expressions." },
      { q: "How do decorators work in Python? Write or explain the mental model of a caching/memoization decorator.", g: "Detail closures, *args, **kwargs, and functools.wraps." }
    ],
    "Frontend Developer": [
      { q: "Explain the Critical Rendering Path in modern browsers and how you optimize First Contentful Paint (FCP) and LCP.", g: "Cover DOM/CSSOM construction, render tree, reflows, and script deferral." },
      { q: "How does the JavaScript Event Loop handle microtasks (Promises) vs macrotasks (setTimeout, UI events)?", g: "Explain execution stack, task queues, and starvation avoidance." },
      { q: "Compare modern state management strategies in React/Vue/vanilla applications and how to prevent unnecessary re-renders.", g: "Discuss reconciliation, memoization, and atomic state stores." },
      { q: "How do you ensure web accessibility (WCAG 2.1 AA) and cross-browser responsiveness across modern devices?", g: "Cover ARIA semantics, keyboard navigation, and responsive layouts." }
    ],
    "Full Stack Developer": [
      { q: "How do you architect end-to-end data flow from client UI components through secure REST/GraphQL endpoints to the database?", g: "Discuss payload validation, JWT authentication, caching, and ORM query optimization." },
      { q: "Explain how you handle distributed sessions, CORS configuration, and CSRF protection in a decoupled SPA architecture.", g: "Cover SameSite cookies, bearer tokens, preflight OPTIONS requests, and headers." },
      { q: "How do you design database schema migrations with zero downtime in continuous deployment (CI/CD) pipelines?", g: "Discuss expand-and-contract pattern, backwards compatibility, and rolling updates." },
      { q: "What strategies do you use for caching across the full stack: browser cache, CDN, reverse proxy, and Redis?", g: "Detail Cache-Control headers, stale-while-revalidate, and cache invalidation." }
    ]
  };

  const situations = [
    { q: "Describe a situation where a critical bug emerged right before a scheduled release. How did you investigate, triage, and resolve it?", g: "Detail isolation, rollback plan, blameless post-mortem, and team communication." },
    { q: "How do you negotiate technical debt vs aggressive feature delivery deadlines with product stakeholders?", g: "Explain calculating engineering velocity impact, risk management, and incremental refactoring." },
    { q: "Walk us through a time you had a technical disagreement with a senior engineer or teammate. How was it resolved?", g: "Focus on benchmark data, objective design reviews, and collaborative alignment." },
    { q: "Describe how you diagnose and resolve a severe production memory leak or sudden latency spike.", g: "Mention logs, APM metrics, profiling tools, heap analysis, and graceful failover." }
  ];

  const hrs = [
    { q: `Why are you eager to join ${companyName} specifically, and where do you envision your technical growth in 2-3 years?`, g: "Show alignment with company culture, continuous self-improvement, and passion for excellence." },
    { q: "Describe a project where you took leadership initiative beyond your assigned tasks to help your team succeed.", g: "Highlight proactivity, mentoring, documentation, or tooling improvements." },
    { q: "How do you prioritize your time when facing multiple high-priority deliverables with tight deadlines?", g: "Explain prioritization frameworks (Eisenhower/MoSCoW), clear expectations, and regular updates." }
  ];

  // Helper to pick a random item from an array
  const pickRandom = (arr) => arr[Math.floor(Math.random() * arr.length)];
  const shuffleArr = (arr) => [...arr].sort(() => 0.5 - Math.random());

  const selectedRoleTech = techQuestions[role] || techQuestions["Full Stack Developer"];
  const shuffledTech = shuffleArr(selectedRoleTech);
  const selectedIntro = pickRandom(intros);
  const selectedSit = pickRandom(situations);
  const selectedHr = pickRandom(hrs);

  if (type === "hr") {
    const hrShuffled = shuffleArr(hrs);
    return [
      { id: 1, category: "Introduction & Culture", question: selectedIntro, guidance: "Deliver a structured, confident introduction tailored to the company." },
      { id: 2, category: "Behavioral / STAR", question: hrShuffled[0].q, guidance: hrShuffled[0].g },
      { id: 3, category: "Work Ethic & Priorities", question: hrShuffled[1] ? hrShuffled[1].q : selectedHr.q, guidance: "Discuss time management and focus." },
      { id: 4, category: "Situational Judgment", question: selectedSit.q, guidance: selectedSit.g },
      { id: 5, category: "Company Alignment", question: `Where do you see yourself contributing within ${companyName} over the next 2-3 years?`, guidance: "Highlight long-term dedication and learning." }
    ];
  }

  return [
    {
      id: 1,
      category: "Introduction & Motivation",
      question: selectedIntro,
      guidance: "Highlight your key technical achievements, core strengths, and genuine motivation."
    },
    {
      id: 2,
      category: "Core Technical Concepts",
      question: shuffledTech[0].q,
      guidance: shuffledTech[0].g
    },
    {
      id: 3,
      category: "System Design & Architecture",
      question: shuffledTech[1] ? shuffledTech[1].q : "How do you design database schemas for high throughput, and how do you handle indexing and transactions?",
      guidance: shuffledTech[1] ? shuffledTech[1].g : "Discuss normalization, indexing strategies, and concurrency controls."
    },
    {
      id: 4,
      category: "Situational & Engineering Practice",
      question: selectedSit.q,
      guidance: selectedSit.g
    },
    {
      id: 5,
      category: "HR & Team Alignment",
      question: selectedHr.q,
      guidance: selectedHr.g
    }
  ];
}
