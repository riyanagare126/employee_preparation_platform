/**
 * AI Employee Preparation Platform - Global Utilities, Auth & Master Navigation
 */

// Dynamic API_BASE resolution:
// Automatically uses current origin when served by Flask on Render, Vercel, or locally
const API_BASE = (() => {
  if (typeof window !== "undefined" && window.location && window.location.origin && window.location.origin.startsWith("http")) {
    const port = window.location.port;
    if (port === "5500" || port === "3000" || port === "5173") {
      return "http://127.0.0.1:5000";
    }
    return window.location.origin;
  }
  return "";
})();

/**
 * Retrieve logged-in employee object from localStorage
 * @returns {Object|null}
 */
function getLoggedInEmployee() {
  try {
    const raw = localStorage.getItem("loggedInEmployee");
    if (!raw) return null;
    const employee = JSON.parse(raw);
    if (employee && employee.id && employee.name) {
      return employee;
    }
    return null;
  } catch (e) {
    console.error("Error parsing loggedInEmployee from localStorage:", e);
    return null;
  }
}

/**
 * Save logged-in employee object to localStorage
 * @param {Object} employee 
 */
function setLoggedInEmployee(employee) {
  if (!employee) return;
  localStorage.setItem("loggedInEmployee", JSON.stringify(employee));
}

/**
 * Get standardized authorization headers with token and employee ID
 */
function getAuthHeaders() {
  const emp = getLoggedInEmployee();
  const headers = { "Content-Type": "application/json" };
  if (emp && emp.token) {
    headers["Authorization"] = `Bearer ${emp.token}`;
  }
  if (emp && emp.id) {
    headers["X-Employee-Id"] = String(emp.id);
  }
  if (emp && emp.is_admin) {
    headers["X-Admin-Email"] = emp.email || "admin@prep.com";
  }
  return headers;
}

/**
 * Get active selected company from localStorage or employee profile
 */
function getSelectedCompany() {
  try {
    const raw = localStorage.getItem("selectedCompany");
    if (raw) return JSON.parse(raw);
  } catch (e) {}

  const emp = getLoggedInEmployee();
  if (emp && emp.target_company) {
    const slug = emp.target_company_slug || (emp.target_company.toLowerCase().includes("tcs") ? "tcs" : "tcs");
    return {
      slug: slug,
      name: emp.target_company,
      role: emp.target_role || emp.job_role || "Software Engineer"
    };
  }
  return { slug: "tcs", name: "Tata Consultancy Services (TCS)", role: "Software Engineer" };
}

/**
 * Set active target company & target role in localStorage and sync with server
 */
async function setSelectedCompany(slug, name, role) {
  const compData = { slug: slug.toLowerCase(), name: name || slug.toUpperCase(), role: role || "Software Engineer" };
  localStorage.setItem("selectedCompany", JSON.stringify(compData));

  const emp = getLoggedInEmployee();
  if (emp) {
    emp.target_company = compData.name;
    emp.target_company_slug = compData.slug;
    emp.target_role = compData.role;
    setLoggedInEmployee(emp);

    try {
      await fetch(`${API_BASE}/api/companies/${slug}/select`, {
        method: "POST",
        headers: getAuthHeaders(),
        body: JSON.stringify({ employee_id: emp.id, role: compData.role })
      });
    } catch (e) {
      console.warn("Failed to sync selected company to server:", e);
    }
  }
  return compData;
}

/**
 * Guard protected pages: redirect to login.html if not authenticated
 */
function requireAuth() {
  const employee = getLoggedInEmployee();
  if (!employee) {
    window.location.href = "login.html";
    return null;
  }
  return employee;
}

/**
 * Guard guest pages: redirect to dashboard.html if already authenticated
 */
function redirectIfLoggedIn() {
  const employee = getLoggedInEmployee();
  if (employee) {
    window.location.href = "dashboard.html";
  }
}

/**
 * Logout employee, clean session, and redirect to login page
 */
function logout() {
  localStorage.clear();
  showToast("You have been successfully logged out.", "info");
  setTimeout(() => {
    window.location.href = "login.html";
  }, 400);
}

/**
 * Display toast notification to user
 */
function showToast(message, type = "info") {
  let container = document.getElementById("toast-container");
  if (!container) {
    container = document.createElement("div");
    container.id = "toast-container";
    container.className = "toast-container";
    document.body.appendChild(container);
  }

  const toast = document.createElement("div");
  toast.className = `toast toast-${type}`;

  const icon = type === "success" ? "✔" : (type === "error" ? "✖" : "ℹ");
  toast.innerHTML = `<span>${icon}</span> <span>${message}</span>`;
  container.appendChild(toast);

  setTimeout(() => {
    toast.style.opacity = "0";
    toast.style.transform = "translateX(100%)";
    toast.style.transition = "all 0.3s ease";
    setTimeout(() => toast.remove(), 300);
  }, 4000);
}

/**
 * Enrich Navigation Bar with Gamification Pills & Admin Links
 */
async function setupGlobalNavbar() {
  const employee = getLoggedInEmployee();
  if (!employee) return;

  const navMenu = document.getElementById("nav-menu");
  if (!navMenu) return;

  // Highlight active link based on window.location
  const currentPath = window.location.pathname.split("/").pop() || "dashboard.html";
  const links = navMenu.querySelectorAll(".nav-link");
  links.forEach(l => {
    const href = l.getAttribute("href");
    if (href === currentPath) {
      l.classList.add("active");
    }
  });

  // Inject Gamification Points Pill & Admin Link if not present
  if (!document.getElementById("nav-gamification-pill")) {
    const pill = document.createElement("li");
    pill.id = "nav-gamification-pill";
    pill.innerHTML = `
      <a href="achievements.html" class="badge badge-purple" style="display: inline-flex; align-items: center; gap: 6px; padding: 6px 12px; font-weight: 700; text-decoration: none;">
        <span>🔥 <span id="nav-streak-count">1</span>d</span>
        <span>•</span>
        <span>⚡ <span id="nav-points-count">50</span> XP</span>
      </a>
    `;
    navMenu.insertBefore(pill, navMenu.firstChild);
  }

  // Fetch gamification stats
  try {
    const res = await fetch(`${API_BASE}/api/gamification/stats?employee_id=${employee.id}`);
    if (res.ok) {
      const data = await res.json();
      if (data.success && data.stats) {
        const streakEl = document.getElementById("nav-streak-count");
        const ptsEl = document.getElementById("nav-points-count");
        if (streakEl) streakEl.textContent = data.stats.streak_days || 1;
        if (ptsEl) ptsEl.textContent = data.stats.points || 50;
      }
    }
  } catch (e) {}

  // Check admin status
  if (employee.is_admin) {
    if (!document.getElementById("nav-admin-link")) {
      const adminLi = document.createElement("li");
      adminLi.id = "nav-admin-link";
      adminLi.innerHTML = `<a href="admin.html" class="nav-link" style="color: #f43f5e; font-weight: 700;">🛡️ Admin</a>`;
      navMenu.appendChild(adminLi);
    }
  }
}

// Global DOM setup
document.addEventListener("DOMContentLoaded", () => {
  const navToggle = document.getElementById("nav-toggle");
  const navMenu = document.getElementById("nav-menu");
  if (navToggle && navMenu) {
    const toggleNav = (forceState) => {
      const isOpen = typeof forceState === "boolean" ? forceState : !navMenu.classList.contains("open");
      navMenu.classList.toggle("open", isOpen);
      navToggle.setAttribute("aria-expanded", isOpen ? "true" : "false");
      navToggle.innerHTML = isOpen ? "✕" : "☰";
    };

    navToggle.addEventListener("click", (e) => {
      e.stopPropagation();
      toggleNav();
    });

    // Auto-close nav when clicking a link or button inside the menu
    navMenu.addEventListener("click", (e) => {
      const link = e.target.closest("a, button");
      if (link && !link.classList.contains("dropdown-toggle")) {
        toggleNav(false);
      }
    });

    // Close when tapping outside the navbar
    document.addEventListener("click", (e) => {
      if (navMenu.classList.contains("open") && !e.target.closest(".navbar")) {
        toggleNav(false);
      }
    });

    // Close on Escape key
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape" && navMenu.classList.contains("open")) {
        toggleNav(false);
      }
    });
  }

  const logoutBtns = document.querySelectorAll(".btn-logout, [data-action='logout']");
  logoutBtns.forEach(btn => {
    btn.addEventListener("click", (e) => {
      e.preventDefault();
      logout();
    });
  });

  setupGlobalNavbar();
});
