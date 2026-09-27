/**
 * ============================================================================
 * AI Employee Preparation Platform - Test Security & Anti-Cheating Module
 * File: js/test-security.js
 * ============================================================================
 * 
 * VIVA EXPLANATION SUMMARY:
 * ----------------------------------------------------------------------------
 * 1. Purpose: Ensures assessment integrity by detecting when a candidate
 *    switches tabs, moves focus away, exits fullscreen, or attempts copy-paste.
 * 2. Architecture:
 *    - Client-side Detection: Listens to browser lifecycle events (visibilitychange,
 *      window.blur, fullscreenchange, contextmenu, keyboard shortcuts).
 *    - Debouncing: Merges simultaneous events (e.g., visibilitychange + blur) into
 *      a single violation within a 1.2-second debounce window.
 *    - Server Authority: Violations are sent to POST /api/test/{attempt_id}/violation.
 *      The backend increments and validates the violation counter in the database.
 *    - Immediate Feedback: Shows an urgent modal alert, updates a persistent top
 *      warning banner, triggers a native browser notification, and plays an audio beep.
 *    - Auto-Submission: On the 3rd violation, the test is automatically submitted
 *      with whatever answers were given so far and tagged as auto-submitted.
 *    - Resiliency: Queues failed network requests if connection drops and syncs on reconnect.
 *      Preserves violation count across browser page reloads via server synchronization.
 * ============================================================================
 */

class TestSecurityManager {
  /**
   * @param {Object} options Configuration options
   * @param {string} options.attemptId Unique session/attempt ID
   * @param {number} options.employeeId Current employee ID
   * @param {number} [options.maxViolations=3] Maximum allowed violations before auto-submit
   * @param {Function} options.onAutoSubmit Callback triggered on 3rd violation
   * @param {Function} [options.onViolation] Callback triggered on any violation (count, max)
   * @param {string} [options.apiBase=""] Base URL for API calls
   */
  constructor(options = {}) {
    this.attemptId = options.attemptId || null;
    this.employeeId = options.employeeId || null;
    this.maxViolations = options.maxViolations || 3;
    this.onAutoSubmit = options.onAutoSubmit || (() => {});
    this.onViolation = options.onViolation || (() => {});
    this.apiBase = options.apiBase || (typeof API_BASE !== "undefined" ? API_BASE : "");

    // Internal State
    this.isActive = false;
    this.violationCount = 0;
    this.isAutoSubmitted = false;
    this.lastViolationTimestamp = 0;
    this.debounceWindowMs = 1200; // Merges simultaneous blur & visibilitychange events
    this.awayStartEpoch = null;
    this.isInternalAction = false; // Flag to prevent false alarms from internal dialogs

    // Offline event queue
    this.offlineQueue = [];
    this.isOnline = navigator.onLine !== false;

    // Audio Context for beep warning
    this.audioCtx = null;

    // Bound event handlers for clean removal
    this.handleVisibilityChange = this._onVisibilityChange.bind(this);
    this.handleWindowBlur = this._onWindowBlur.bind(this);
    this.handleWindowFocus = this._onWindowFocus.bind(this);
    this.handleFullscreenChange = this._onFullscreenChange.bind(this);
    this.handleContextMenu = this._onContextMenu.bind(this);
    this.handleKeyDown = this._onKeyDown.bind(this);
    this.handleClipboard = this._onClipboardAction.bind(this);
    this.handleSelectStart = this._onSelectStart.bind(this);
    this.handleOnline = this._onOnline.bind(this);
    this.handleOffline = this._onOffline.bind(this);
  }

  /**
   * Initializes security monitoring for an active test session
   * @param {number} [initialCount=0] Persisted violation count from server (mid-test reload)
   */
  start(initialCount = 0) {
    if (this.isActive) return;
    this.isActive = true;
    this.violationCount = initialCount || 0;
    this.awayStartEpoch = null;

    // Request polite browser notification permission
    this._requestNotificationPermission();

    // Attach lifecycle listeners
    document.addEventListener("visibilitychange", this.handleVisibilityChange);
    window.addEventListener("blur", this.handleWindowBlur);
    window.addEventListener("focus", this.handleWindowFocus);
    document.addEventListener("fullscreenchange", this.handleFullscreenChange);
    document.addEventListener("webkitfullscreenchange", this.handleFullscreenChange);

    // Prevent copy, cut, paste, right-click, and select-all shortcuts
    document.addEventListener("contextmenu", this.handleContextMenu);
    document.addEventListener("keydown", this.handleKeyDown);
    document.addEventListener("copy", this.handleClipboard);
    document.addEventListener("cut", this.handleClipboard);
    document.addEventListener("paste", this.handleClipboard);
    document.addEventListener("selectstart", this.handleSelectStart);

    // Network resilience listeners
    window.addEventListener("online", this.handleOnline);
    window.addEventListener("offline", this.handleOffline);

    // Update banner with initial state if restored after reload
    this.updateBanner();

    console.log(`[TestSecurity] Monitoring active for attempt ${this.attemptId}. Initial count: ${this.violationCount}`);
  }

  /**
   * Stops security monitoring (called when test is submitted or completed)
   */
  stop() {
    this.isActive = false;

    document.removeEventListener("visibilitychange", this.handleVisibilityChange);
    window.removeEventListener("blur", this.handleWindowBlur);
    window.removeEventListener("focus", this.handleWindowFocus);
    document.removeEventListener("fullscreenchange", this.handleFullscreenChange);
    document.removeEventListener("webkitfullscreenchange", this.handleFullscreenChange);
    document.removeEventListener("contextmenu", this.handleContextMenu);
    document.removeEventListener("keydown", this.handleKeyDown);
    document.removeEventListener("copy", this.handleClipboard);
    document.removeEventListener("cut", this.handleClipboard);
    document.removeEventListener("paste", this.handleClipboard);
    document.removeEventListener("selectstart", this.handleSelectStart);
    window.removeEventListener("online", this.handleOnline);
    window.removeEventListener("offline", this.handleOffline);

    // Hide security banner when test finishes
    const banner = document.getElementById("test-security-banner");
    if (banner) banner.style.display = "none";

    console.log("[TestSecurity] Monitoring stopped.");
  }

  /**
   * Temporarily marks an action as internal (e.g., clicking platform's submit confirmation)
   * to avoid raising false violation alarms.
   */
  beginInternalAction() {
    this.isInternalAction = true;
  }

  endInternalAction() {
    setTimeout(() => {
      this.isInternalAction = false;
    }, 500);
  }

  /**
   * Attempts to request fullscreen mode with graceful mobile fallback
   */
  async requestFullscreen() {
    try {
      const el = document.documentElement;
      if (el.requestFullscreen) {
        await el.requestFullscreen();
      } else if (el.webkitRequestFullscreen) {
        await el.webkitRequestFullscreen();
      } else if (el.msRequestFullscreen) {
        await el.msRequestFullscreen();
      }
    } catch (err) {
      // Graceful fallback for mobile or browsers blocking automatic fullscreen
      console.warn("[TestSecurity] Fullscreen request not supported or denied by policy:", err);
    }
  }

  /**
   * Exits fullscreen mode if active
   */
  exitFullscreen() {
    try {
      if (document.fullscreenElement && document.exitFullscreen) {
        document.exitFullscreen().catch(() => {});
      }
    } catch (e) {}
  }

  // ==========================================================================
  // EVENT DETECTION HANDLERS
  // ==========================================================================

  _onVisibilityChange() {
    if (!this.isActive || this.isInternalAction) return;

    if (document.hidden) {
      // Tab hidden, minimized, or phone app switched
      this.awayStartEpoch = Date.now();
      this._showBrowserNotification("Assessment Warning", "You switched tabs! Return to your test immediately to avoid auto-submission.");
      this._triggerViolation("tab_switch");
    } else {
      // Returned back to test tab
      this._onUserReturned("tab_switch");
    }
  }

  _onWindowBlur() {
    if (!this.isActive || this.isInternalAction) return;

    // Window lost focus (another application or devtools focused)
    if (!this.awayStartEpoch) {
      this.awayStartEpoch = Date.now();
    }
    this._triggerViolation("window_blur");
  }

  _onWindowFocus() {
    if (!this.isActive || this.isInternalAction) return;
    this._onUserReturned("window_focus");
  }

  _onFullscreenChange() {
    if (!this.isActive || this.isInternalAction) return;

    const isFullscreen = !!(document.fullscreenElement || document.webkitFullscreenElement);
    if (!isFullscreen) {
      // User exited fullscreen
      this._triggerViolation("fullscreen_exit");
      this._showWarningModal("fullscreen_exit");
    }
  }

  _onContextMenu(e) {
    if (!this.isActive) return;
    e.preventDefault();
    this._triggerViolation("right_click", false); // Minor violation warning
    this._showToast("Right-click context menu is disabled during the test.", "warning");
  }

  _onKeyDown(e) {
    if (!this.isActive) return;

    // Block Ctrl+C, Ctrl+V, Ctrl+X, Ctrl+A, Ctrl+U, F12
    const isCtrlOrCmd = e.ctrlKey || e.metaKey;
    const key = (e.key || "").toLowerCase();

    if (
      (isCtrlOrCmd && ["c", "v", "x", "a", "u"].includes(key)) ||
      key === "f12" ||
      (isCtrlOrCmd && e.shiftKey && ["i", "j", "c"].includes(key))
    ) {
      e.preventDefault();
      this._triggerViolation("copy_paste_attempt", false);
      this._showToast("Copy, paste, inspect, and select shortcuts are strictly prohibited.", "warning");
    }
  }

  _onClipboardAction(e) {
    if (!this.isActive) return;
    e.preventDefault();
    this._triggerViolation("copy_paste_attempt", false);
    this._showToast("Clipboard actions (copy, cut, paste) are disabled during the test.", "warning");
  }

  _onSelectStart(e) {
    if (!this.isActive) return;
    // Allow selection only if inside an input or textarea (if any exist)
    const target = e.target;
    if (target && (target.tagName === "INPUT" || target.tagName === "TEXTAREA")) return;
    e.preventDefault();
  }

  _onUserReturned(source) {
    let durationAway = null;
    if (this.awayStartEpoch) {
      durationAway = Math.round((Date.now() - this.awayStartEpoch) / 1000);
      this.awayStartEpoch = null;
    }

    // Show warning modal on return if violation occurred
    if (this.violationCount > 0 && !this.isAutoSubmitted) {
      this._showWarningModal(source, durationAway);
    }
  }

  // ==========================================================================
  // CORE VIOLATION LOGIC & SERVER SYNC
  // ==========================================================================

  /**
   * Debounces and records a violation both locally and on the authoritative server
   * @param {string} eventType tab_switch | window_blur | fullscreen_exit | copy_paste_attempt | right_click
   * @param {boolean} [countAsMajor=true] Whether this increments the 3-strike counter
   */
  async _triggerViolation(eventType, countAsMajor = true) {
    const now = Date.now();

    // Debounce major tab switches and blurs that occur within 1.2s of each other
    if (countAsMajor) {
      if (now - this.lastViolationTimestamp < this.debounceWindowMs) {
        return; // Ignore duplicated trigger
      }
      this.lastViolationTimestamp = now;
      this.violationCount += 1;
    }

    // Play audible alert beep
    this._playWarningBeep();

    // Calculate duration away if available
    let durationAway = null;
    if (this.awayStartEpoch) {
      durationAway = Math.max(1, Math.round((now - this.awayStartEpoch) / 1000));
    }

    // Live update UI banner
    this.updateBanner();

    // Invoke client listener
    this.onViolation(this.violationCount, this.maxViolations, eventType);

    // Send payload to backend server
    const payload = {
      attempt_id: this.attemptId,
      employee_id: this.employeeId,
      event_type: eventType,
      duration_away_seconds: durationAway
    };

    if (this.isOnline) {
      await this._sendViolationToServer(payload);
    } else {
      // Queue offline for resilience
      this.offlineQueue.push(payload);
      console.warn("[TestSecurity] Network offline: Queued violation event for sync.");
    }

    // Auto-submission check on 3rd violation
    if (countAsMajor && this.violationCount >= this.maxViolations && !this.isAutoSubmitted) {
      this._handleStrikeOut();
    }
  }

  /**
   * Transmits violation event to FastAPI / Flask backend
   */
  async _sendViolationToServer(payload) {
    if (!this.attemptId) return;

    try {
      const url = `${this.apiBase}/api/test/${encodeURIComponent(this.attemptId)}/violation`;
      const res = await fetch(url, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-Employee-Id": String(this.employeeId || "")
        },
        body: JSON.stringify(payload)
      });

      if (res.ok) {
        const data = await res.json();
        // Server-authoritative synchronization
        if (typeof data.violation_count === "number") {
          this.violationCount = data.violation_count;
          this.updateBanner();
        }
        if (data.auto_submit && !this.isAutoSubmitted) {
          this._handleStrikeOut();
        }
      } else {
        // Enqueue on HTTP failure
        this.offlineQueue.push(payload);
      }
    } catch (err) {
      console.warn("[TestSecurity] Error communicating with server, queueing:", err);
      this.offlineQueue.push(payload);
    }
  }

  /**
   * Strikes out candidate on reaching 3 violations: auto-submits immediately
   */
  _handleStrikeOut() {
    this.isAutoSubmitted = true;
    this.stop(); // Cease monitoring

    // Show auto-submission modal
    this._showAutoSubmitModal();

    // Call user-provided auto-submit callback after brief 1.5s delay so candidate sees alert
    setTimeout(() => {
      this.onAutoSubmit({
        violationCount: this.violationCount,
        maxViolations: this.maxViolations,
        reason: "auto_submitted_security_violation"
      });
    }, 1500);
  }

  // ==========================================================================
  // OFFLINE QUEUE RESILIENCE
  // ==========================================================================

  _onOnline() {
    this.isOnline = true;
    this._flushOfflineQueue();
  }

  _onOffline() {
    this.isOnline = false;
  }

  async _flushOfflineQueue() {
    if (!this.offlineQueue.length) return;
    console.log(`[TestSecurity] Back online. Flushing ${this.offlineQueue.length} queued violations...`);
    const queue = [...this.offlineQueue];
    this.offlineQueue = [];

    for (const item of queue) {
      await this._sendViolationToServer(item);
    }
  }

  // ==========================================================================
  // UI PRESENTATION & NOTIFICATIONS
  // ==========================================================================

  /**
   * Updates or mounts the top sticky red security banner
   */
  updateBanner() {
    let banner = document.getElementById("test-security-banner");
    if (!banner) {
      banner = document.createElement("div");
      banner.id = "test-security-banner";
      banner.className = "test-security-banner";
      document.body.prepend(banner);
    }

    if (this.violationCount === 0) {
      banner.style.display = "none";
      return;
    }

    banner.style.display = "flex";
    const remaining = Math.max(0, this.maxViolations - this.violationCount);

    if (this.violationCount >= this.maxViolations) {
      banner.className = "test-security-banner danger";
      banner.innerHTML = `
        <div class="banner-content">
          <i class="fa-solid fa-ban"></i>
          <span><strong>Maximum Violations Exceeded (${this.violationCount}/${this.maxViolations}):</strong> Test is being automatically submitted.</span>
        </div>
      `;
    } else {
      banner.className = "test-security-banner warning";
      banner.innerHTML = `
        <div class="banner-content">
          <i class="fa-solid fa-triangle-exclamation"></i>
          <span>
            <strong>Security Warning (${this.violationCount}/${this.maxViolations}):</strong>
            You left the test window. <strong>${remaining}</strong> more violation(s) will auto-submit your test.
          </span>
        </div>
      `;
    }
  }

  /**
   * Displays the popup warning modal when user returns to test
   */
  _showWarningModal(source, durationAway = null) {
    // Remove any existing warning modal
    const existing = document.getElementById("security-warning-modal");
    if (existing) existing.remove();

    const modal = document.createElement("div");
    modal.id = "security-warning-modal";
    modal.className = "security-modal-overlay";

    const awayText = durationAway ? ` You were away for approx <strong>${durationAway}s</strong>.` : "";
    const remaining = Math.max(0, this.maxViolations - this.violationCount);

    modal.innerHTML = `
      <div class="security-modal-dialog">
        <div class="modal-header-icon warning">
          <i class="fa-solid fa-triangle-exclamation"></i>
        </div>
        <h3>Warning: You Left the Test Screen</h3>
        <p class="modal-message">
          This activity has been recorded in your proctoring log.${awayText}
        </p>
        <div class="strike-counter-box">
          <div class="strike-label">Warning Level</div>
          <div class="strike-badges">
            <span class="strike-badge ${this.violationCount >= 1 ? 'active' : ''}">1</span>
            <span class="strike-badge ${this.violationCount >= 2 ? 'active' : ''}">2</span>
            <span class="strike-badge ${this.violationCount >= 3 ? 'active danger' : ''}">3</span>
          </div>
          <div class="strike-caption">
            <strong>Warning ${this.violationCount} of ${this.maxViolations}</strong> — ${remaining} remaining before auto-submit.
          </div>
        </div>
        <div class="modal-footer-action">
          <button id="btn-dismiss-security-warning" class="btn btn-warning btn-block">
            I Understand, Return to Test
          </button>
        </div>
      </div>
    `;

    document.body.appendChild(modal);

    const btn = document.getElementById("btn-dismiss-security-warning");
    if (btn) {
      btn.addEventListener("click", () => {
        modal.remove();
        // Re-request fullscreen if lost
        if (!document.fullscreenElement) {
          this.requestFullscreen().catch(() => {});
        }
      });
    }
  }

  /**
   * Displays the terminal auto-submit modal when 3rd violation occurs
   */
  _showAutoSubmitModal() {
    const existing = document.getElementById("security-warning-modal");
    if (existing) existing.remove();

    const modal = document.createElement("div");
    modal.id = "security-autosubmit-modal";
    modal.className = "security-modal-overlay";

    modal.innerHTML = `
      <div class="security-modal-dialog danger">
        <div class="modal-header-icon danger">
          <i class="fa-solid fa-ban"></i>
        </div>
        <h3>Test Auto-Submitted</h3>
        <p class="modal-message">
          Repeated security violations detected (<strong>${this.violationCount} of ${this.maxViolations}</strong>).
          Your assessment has been automatically frozen and submitted with answers recorded so far.
        </p>
        <div class="submitting-spinner">
          <i class="fa-solid fa-circle-notch fa-spin"></i> Finalizing assessment grading...
        </div>
      </div>
    `;

    document.body.appendChild(modal);
  }

  /**
   * Synthesizes an audio beep using Web Audio API
   */
  _playWarningBeep() {
    try {
      const AudioCtx = window.AudioContext || window.webkitAudioContext;
      if (!AudioCtx) return;
      if (!this.audioCtx) this.audioCtx = new AudioCtx();
      if (this.audioCtx.state === "suspended") {
        this.audioCtx.resume();
      }

      const osc = this.audioCtx.createOscillator();
      const gain = this.audioCtx.createGain();

      osc.type = "sawtooth";
      osc.frequency.setValueAtTime(440, this.audioCtx.currentTime); // 440 Hz (A4)
      osc.frequency.exponentialRampToValueAtTime(880, this.audioCtx.currentTime + 0.18); // rise to 880 Hz

      gain.gain.setValueAtTime(0.3, this.audioCtx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.01, this.audioCtx.currentTime + 0.25);

      osc.connect(gain);
      gain.connect(this.audioCtx.destination);

      osc.start();
      osc.stop(this.audioCtx.currentTime + 0.25);
    } catch (e) {
      // Audio playback non-critical
    }
  }

  /**
   * Requests polite notification permission
   */
  _requestNotificationPermission() {
    try {
      if ("Notification" in window && Notification.permission === "default") {
        Notification.requestPermission().catch(() => {});
      }
    } catch (e) {}
  }

  /**
   * Fires a native browser notification if user switched tabs
   */
  _showBrowserNotification(title, body) {
    try {
      if ("Notification" in window && Notification.permission === "granted") {
        new Notification(title, {
          body: body,
          icon: "favicon.ico",
          tag: "anti-cheat-alert"
        });
      }
    } catch (e) {}
  }

  _showToast(msg, type = "info") {
    if (typeof showToast === "function") {
      showToast(msg, type);
    }
  }
}

// Export globally for script tag consumption
window.TestSecurityManager = TestSecurityManager;
