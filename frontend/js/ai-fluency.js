/**
 * AI Employee Preparation Platform - 2026 AI Fluency Round Controller
 * Evaluates candidate responses for natural AI-tool fluency, verification discipline, and velocity metrics.
 */

document.addEventListener("DOMContentLoaded", async () => {
  const employee = requireAuth();
  if (!employee) return;

  let questionBank = [];
  let currentQuestion = null;

  const selectQ = document.getElementById("select-fluency-question");
  const catBadge = document.getElementById("question-category-badge");
  const hintText = document.getElementById("question-hint-text");
  const idealList = document.getElementById("ideal-points-list");
  const answerInput = document.getElementById("input-candidate-answer");
  const wordCountEl = document.getElementById("answer-word-count");
  const btnEvaluate = document.getElementById("btn-evaluate-fluency");
  const btnRandom = document.getElementById("btn-random-question");
  const btnCopy = document.getElementById("btn-copy-rewrite");

  const resultsEmpty = document.getElementById("fluency-results-empty");
  const resultsCard = document.getElementById("fluency-results-card");

  // Track word count live
  if (answerInput && wordCountEl) {
    answerInput.addEventListener("input", () => {
      const words = answerInput.value.trim().split(/\s+/).filter(w => w.length > 0).length;
      wordCountEl.textContent = `${words} words`;
    });
  }

  // Load questions and history
  await loadQuestions();
  await loadFluencyHistory(employee.id);

  // Question selection change
  if (selectQ) {
    selectQ.addEventListener("change", () => {
      const qId = parseInt(selectQ.value);
      const q = questionBank.find(x => x.id === qId);
      if (q) {
        selectQuestion(q);
      }
    });
  }

  // Random Question
  if (btnRandom) {
    btnRandom.addEventListener("click", () => {
      if (questionBank.length > 0) {
        const randomIndex = Math.floor(Math.random() * questionBank.length);
        const q = questionBank[randomIndex];
        selectQ.value = q.id;
        selectQuestion(q);
        showToast("Loaded random practice question!", "info");
      }
    });
  }

  // Copy Rewrite Sample
  if (btnCopy) {
    btnCopy.addEventListener("click", () => {
      const sample = document.getElementById("eval-rewrite-sample").textContent;
      if (sample) {
        navigator.clipboard.writeText(sample);
        showToast("Rewritten pitch copied to clipboard!", "success");
      }
    });
  }

  // Evaluate Button
  if (btnEvaluate) {
    btnEvaluate.addEventListener("click", async () => {
      const text = answerInput.value.trim();
      const words = text.split(/\s+/).filter(w => w.length > 0).length;

      if (words < 15) {
        showToast("Please provide a more detailed response (at least 15-20 words) for evaluation.", "error");
        return;
      }

      btnEvaluate.disabled = true;
      btnEvaluate.innerHTML = `<span class="spinner-sm"></span> Evaluating AI Fluency...`;

      try {
        const res = await fetch(`${API_BASE}/api/ai-fluency/evaluate`, {
          method: "POST",
          headers: getAuthHeaders(),
          body: JSON.stringify({
            employee_id: employee.id,
            question_id: currentQuestion ? currentQuestion.id : 1,
            candidate_answer: text
          })
        });

        const data = await res.json();
        if (data.success) {
          renderEvaluationResults(data);
          showToast("Evaluation complete! +25 XP earned", "success");
          await loadFluencyHistory(employee.id);
        } else {
          showToast(data.message || "Evaluation failed.", "error");
        }
      } catch (err) {
        showToast("Error connecting to AI evaluation service.", "error");
      } finally {
        btnEvaluate.disabled = false;
        btnEvaluate.innerHTML = `Evaluate AI Fluency Score <i class="fa-solid fa-robot"></i>`;
      }
    });
  }

  async function loadQuestions() {
    try {
      const res = await fetch(`${API_BASE}/api/ai-fluency/questions`);
      if (res.ok) {
        const data = await res.json();
        if (data.success && data.questions && data.questions.length > 0) {
          questionBank = data.questions;
          selectQ.innerHTML = questionBank.map(q => `<option value="${q.id}">[${q.category}] ${escapeHtml(q.question_text.slice(0, 65))}...</option>`).join("");
          selectQuestion(questionBank[0]);
        }
      }
    } catch (e) {
      console.error("Error fetching fluency questions:", e);
    }
  }

  function selectQuestion(q) {
    currentQuestion = q;
    if (catBadge) catBadge.textContent = q.category || "General";
    if (hintText) hintText.textContent = q.context_hint || "Focus on describing your natural workflow while demonstrating code verification.";
    
    if (idealList && q.ideal_talking_points) {
      idealList.innerHTML = q.ideal_talking_points.map(p => `<span>• ${escapeHtml(p)}</span>`).join("");
    }
  }

  function renderEvaluationResults(res) {
    if (resultsEmpty) resultsEmpty.style.display = "none";
    if (resultsCard) resultsCard.style.display = "block";

    document.getElementById("eval-overall-score").textContent = `${res.overall_score}%`;
    const gradeBadge = document.getElementById("eval-overall-grade");
    if (gradeBadge) {
      if (res.overall_score >= 80) {
        gradeBadge.innerHTML = 'Fluent <i class="fa-solid fa-rocket"></i>';
        gradeBadge.className = "badge badge-success";
      } else if (res.overall_score >= 60) {
        gradeBadge.innerHTML = 'Developing <i class="fa-solid fa-bolt text-warning"></i>';
        gradeBadge.className = "badge badge-warning";
      } else {
        gradeBadge.innerHTML = 'Needs Practice <i class="fa-solid fa-triangle-exclamation text-warning"></i>';
        gradeBadge.className = "badge badge-danger";
      }
    }

    document.getElementById("pillar-tool").textContent = `${res.ai_tool_score}%`;
    document.getElementById("pillar-verif").textContent = `${res.verification_score}%`;
    document.getElementById("pillar-velo").textContent = `${res.velocity_score}%`;
    document.getElementById("pillar-comm").textContent = `${res.communication_score}%`;

    document.getElementById("eval-feedback-text").textContent = res.feedback || "Good response.";
    document.getElementById("eval-rewrite-sample").textContent = `"${res.rewrite_sample}"`;

    // Smooth scroll to results
    resultsCard.scrollIntoView({ behavior: "smooth", block: "nearest" });
  }

  async function loadFluencyHistory(employeeId) {
    const listEl = document.getElementById("fluency-history-list");
    if (!listEl) return;

    try {
      const res = await fetch(`${API_BASE}/api/ai-fluency/history?employee_id=${employeeId}`);
      if (res.ok) {
        const data = await res.json();
        if (data.success && data.data && data.data.attempts) {
          const attempts = data.data.attempts;
          if (attempts.length === 0) {
            listEl.innerHTML = `<div style="font-size: 0.82rem; color: var(--text-muted);">No attempts yet. Practice your first question above!</div>`;
            return;
          }

          listEl.innerHTML = attempts.map(att => `
            <div style="padding: 10px 12px; background: var(--bg-subtle); border-radius: 6px; border: 1px solid var(--border-color); display: flex; justify-content: space-between; align-items: center; gap: 10px;">
              <div style="flex: 1;">
                <div style="font-weight: 600; font-size: 0.85rem; color: var(--text-main);">${escapeHtml(att.question_text.slice(0, 50))}...</div>
                <div style="font-size: 0.74rem; color: var(--text-muted); margin-top: 2px;">
                  Tool: ${att.ai_tool_score}% • Verif: ${att.verification_score}% • Velocity: ${att.velocity_score}%
                </div>
              </div>
              <div style="text-align: right;">
                <div style="font-weight: 800; font-size: 1.1rem; color: ${att.overall_score >= 80 ? 'var(--emerald-600)' : 'var(--primary-600)'};">
                  ${att.overall_score}%
                </div>
              </div>
            </div>
          `).join("");
        }
      }
    } catch (e) {}
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
});
