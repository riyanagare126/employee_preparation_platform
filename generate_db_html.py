"""
Generates an interactive, beautiful HTML viewer for the SQLite database.
Includes 1-Click Toggle: "Show Only My Admin Data (Riya Nagare)" vs "Show All Data"
"""
import os
import sqlite3
import html

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "backend", "database", "employees.db")
OUTPUT_HTML = os.path.join(BASE_DIR, "VIEW_DATABASE.html")
FRONTEND_HTML = os.path.join(BASE_DIR, "frontend", "view_db.html")

def generate_html():
    if not os.path.exists(DB_PATH):
        print(f"Database not found at {DB_PATH}")
        return

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    # Tables list
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name;")
    tables = [r["name"] for r in cur.fetchall()]

    # Users
    cur.execute("SELECT id, name, email, target_company, target_role, is_admin, created_at FROM employees ORDER BY id DESC;")
    users = cur.fetchall()

    # Aptitude results
    cur.execute("SELECT r.id, r.employee_id, e.name as user_name, e.email as user_email, r.score, r.total, r.percentage, r.performance_message, r.created_at FROM aptitude_results r LEFT JOIN employees e ON r.employee_id = e.id ORDER BY r.id DESC;")
    tests = cur.fetchall()

    # Coding submissions
    cur.execute("SELECT c.id, c.employee_id, e.name as user_name, e.email as user_email, c.problem_title, c.language, c.difficulty, c.status FROM coding_progress c LEFT JOIN employees e ON c.employee_id = e.id ORDER BY c.id DESC;")
    codes = cur.fetchall()

    # Smart roadmaps
    cur.execute("SELECT r.id, r.employee_id, e.name as user_name, e.email as user_email, r.company_name, r.duration_days, r.completed_tasks, r.total_tasks, r.progress_percent FROM smart_roadmaps r LEFT JOIN employees e ON r.employee_id = e.id ORDER BY r.id DESC;")
    roadmaps = cur.fetchall()

    db_size = round(os.path.getsize(DB_PATH) / (1024 * 1024), 2)

    # Specific stats for Riya Nagare (id=2 or riyanagare126@gmail.com)
    cur.execute("SELECT COUNT(*) FROM aptitude_results WHERE employee_id = 2")
    riya_apt_count = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM coding_progress WHERE employee_id = 2")
    riya_code_count = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM smart_roadmaps WHERE employee_id = 2")
    riya_roadmap_count = cur.fetchone()[0]

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Live Database Explorer - AI Employee Platform (Admin Only)</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  <script>
    // Strict Admin Authorization Guard: Only Admin has access to Live Database
    (function enforceAdminOnly() {{
      const isFileProtocol = window.location.protocol === "file:";
      let isSuperAdmin = false;
      try {{
        const raw = localStorage.getItem("loggedInEmployee");
        if (raw) {{
          const employee = JSON.parse(raw);
          isSuperAdmin = Boolean(
            employee && (
              employee.is_admin === 1 ||
              employee.is_admin === true ||
              employee.is_admin === "1" ||
              (employee.email && employee.email.toLowerCase() === "riyanagare126@gmail.com")
            )
          );
        }}
      }} catch (e) {{}}

      if (!isSuperAdmin && !isFileProtocol) {{
        // Instantly replace DOM to prevent rendering any live database information
        document.documentElement.innerHTML = `
          <!DOCTYPE html>
          <html lang="en">
          <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Access Denied - Admin Only</title>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
            <style>
              * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }}
              body {{
                background: #0b1120;
                color: #f8fafc;
                display: flex;
                align-items: center;
                justify-content: center;
                min-height: 100vh;
                padding: 24px;
              }}
              .lock-box {{
                background: #1e293b;
                border: 1px solid rgba(239, 68, 68, 0.4);
                border-radius: 16px;
                padding: 44px 36px;
                max-width: 520px;
                text-align: center;
                box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7);
              }}
              .icon-shield {{
                width: 72px;
                height: 72px;
                line-height: 72px;
                border-radius: 50%;
                background: rgba(239, 68, 68, 0.15);
                color: #ef4444;
                font-size: 2.2rem;
                margin: 0 auto 20px auto;
                display: flex;
                align-items: center;
                justify-content: center;
              }}
              h1 {{ font-size: 1.6rem; margin-bottom: 12px; color: #fff; font-weight: 700; }}
              p {{ font-size: 0.95rem; color: #94a3b8; line-height: 1.6; margin-bottom: 26px; }}
              .badge-lock {{
                display: inline-block;
                background: rgba(239, 68, 68, 0.12);
                color: #fca5a5;
                border: 1px solid rgba(239, 68, 68, 0.3);
                padding: 4px 12px;
                border-radius: 9999px;
                font-size: 0.8rem;
                font-weight: 600;
                margin-bottom: 14px;
                text-transform: uppercase;
                letter-spacing: 0.5px;
              }}
              .btn-action {{
                display: inline-flex;
                align-items: center;
                gap: 8px;
                background: #4f46e5;
                color: #fff;
                padding: 12px 24px;
                border-radius: 8px;
                text-decoration: none;
                font-weight: 600;
                font-size: 0.95rem;
                transition: all 0.2s ease;
              }}
              .btn-action:hover {{ background: #4338ca; transform: translateY(-1px); }}
            </style>
          </head>
          <body>
            <div class="lock-box">
              <div class="icon-shield"><i class="fa-solid fa-shield-halved"></i></div>
              <span class="badge-lock"><i class="fa-solid fa-lock"></i> Restricted Database</span>
              <h1>Access Denied: Admin Only</h1>
              <p>
                Live database access is strictly restricted to platform administrators.<br>
                Candidate and student accounts do not have permission to view live database tables.
              </p>
              <a href="dashboard.html" class="btn-action"><i class="fa-solid fa-arrow-left"></i> Return to Candidate Dashboard</a>
            </div>
          </body>
          </html>
        `;
        setTimeout(function() {{
          window.location.replace("dashboard.html");
        }}, 2500);
        throw new Error("Access Denied: Live Database is restricted to administrators only.");
      }}
    }})();
  </script>
  <style>
    :root {{
      --primary: #4f46e5;
      --bg: #0f172a;
      --card-bg: #1e293b;
      --text: #f8fafc;
      --text-muted: #94a3b8;
      --border: #334155;
      --emerald: #10b981;
      --rose: #f43f5e;
      --amber: #f59e0b;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }}
    body {{ background: var(--bg); color: var(--text); padding: 25px 20px; }}
    .container {{ max-width: 1200px; margin: 0 auto; }}
    
    header {{ margin-bottom: 20px; border-bottom: 1px solid var(--border); padding-bottom: 18px; }}
    h1 {{ font-size: 1.8rem; margin-bottom: 6px; color: #fff; display: flex; align-items: center; gap: 10px; }}
    
    .badge {{ display: inline-block; padding: 4px 10px; border-radius: 999px; font-size: 0.78rem; font-weight: 600; text-transform: uppercase; }}
    .badge-admin {{ background: rgba(244, 63, 94, 0.2); color: #fda4af; border: 1px solid #f43f5e; }}
    .badge-student {{ background: rgba(79, 70, 229, 0.2); color: #a5b4fc; border: 1px solid #6366f1; }}
    .badge-success {{ background: rgba(16, 185, 129, 0.2); color: #6ee7b7; border: 1px solid #10b981; }}
    .badge-riya {{ background: rgba(16, 185, 129, 0.25); color: #10b981; border: 1px solid #10b981; font-weight: bold; }}
    
    /* Toggle Control Bar */
    .filter-bar {{ display: flex; gap: 12px; margin-bottom: 24px; flex-wrap: wrap; align-items: center; background: #162032; padding: 12px 18px; border-radius: 10px; border: 1px solid var(--border); }}
    .filter-btn {{ padding: 8px 16px; border-radius: 8px; border: 1px solid var(--border); font-size: 0.9rem; font-weight: 600; cursor: pointer; display: flex; align-items: center; gap: 8px; transition: all 0.2s; }}
    .filter-btn.active {{ background: #10b981; color: #fff; border-color: #10b981; box-shadow: 0 0 12px rgba(16,185,129,0.3); }}
    .filter-btn:not(.active) {{ background: var(--card-bg); color: var(--text-muted); }}
    .filter-btn:not(.active):hover {{ background: #26354a; color: #fff; }}
    
    /* Highlight Admin banner */
    .admin-banner {{ background: linear-gradient(135deg, rgba(16,185,129,0.12), rgba(79,70,229,0.12)); border: 1px solid rgba(16,185,129,0.3); border-radius: 10px; padding: 16px 20px; margin-bottom: 25px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 14px; }}
    
    .stats-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(210px, 1fr)); gap: 14px; margin-bottom: 25px; }}
    .stat-card {{ background: var(--card-bg); border: 1px solid var(--border); padding: 16px; border-radius: 10px; }}
    .stat-title {{ font-size: 0.8rem; color: var(--text-muted); text-transform: uppercase; margin-bottom: 6px; }}
    .stat-value {{ font-size: 1.5rem; font-weight: 700; color: #fff; }}
    
    .section-card {{ background: var(--card-bg); border: 1px solid var(--border); border-radius: 10px; padding: 20px; margin-bottom: 25px; }}
    .section-header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px; border-bottom: 1px solid var(--border); padding-bottom: 10px; }}
    .section-title {{ font-size: 1.15rem; font-weight: 600; display: flex; align-items: center; gap: 8px; }}
    
    table {{ width: 100%; border-collapse: collapse; font-size: 0.9rem; text-align: left; }}
    th {{ background: rgba(15, 23, 42, 0.6); padding: 12px; border-bottom: 1px solid var(--border); color: var(--text-muted); font-weight: 600; }}
    td {{ padding: 12px; border-bottom: 1px solid var(--border); }}
    tr:hover td {{ background: rgba(255,255,255,0.02); }}
    
    .row-riya {{ background: rgba(16, 185, 129, 0.08) !important; }}
    .row-riya td {{ border-bottom-color: rgba(16, 185, 129, 0.25); }}
    
    .db-location {{ background: #0b1120; border: 1px solid #1e293b; padding: 10px 14px; border-radius: 8px; font-family: monospace; font-size: 0.82rem; color: #38bdf8; margin-top: 8px; }}
  </style>
</head>
<body>
  <div class="container">
    <header>
      <h1><i class="fa-solid fa-database" style="color: #10b981;"></i> AI Employee Platform — Live Database Explorer</h1>
      <p style="color: var(--text-muted); font-size: 0.9rem;">Direct connection to local SQLite database: <code>backend/database/employees.db</code></p>
      <div class="db-location">
        <strong>📂 Database File:</strong> {html.escape(DB_PATH)} ({db_size} MB)
      </div>
    </header>

    <!-- Admin Personal Profile Banner -->
    <div class="admin-banner">
      <div>
        <div style="font-size: 0.8rem; color: #10b981; font-weight: 700; text-transform: uppercase;">
          <i class="fa-solid fa-shield-halved"></i> Active Platform Administrator
        </div>
        <h2 style="font-size: 1.3rem; margin-top: 4px;">Riya Nagare (riyanagare126@gmail.com)</h2>
        <p style="color: var(--text-muted); font-size: 0.85rem; margin-top: 2px;">
          Candidate ID: <strong>#2</strong> | Status: <strong>Super Admin & Candidate Profile Active</strong>
        </p>
      </div>
      <div style="display: flex; gap: 16px; font-size: 0.88rem;">
        <div><strong style="color: #10b981; font-size: 1.1rem;">{riya_apt_count}</strong> <span style="color: var(--text-muted);">Aptitude Tests</span></div>
        <div><strong style="color: #38bdf8; font-size: 1.1rem;">{riya_code_count}</strong> <span style="color: var(--text-muted);">Coding Solved</span></div>
        <div><strong style="color: #a855f7; font-size: 1.1rem;">{riya_roadmap_count}</strong> <span style="color: var(--text-muted);">Roadmaps</span></div>
      </div>
    </div>

    <!-- Toggle Buttons -->
    <div class="filter-bar">
      <span style="font-size: 0.85rem; color: var(--text-muted); font-weight: 600;">FILTER DATA VIEW:</span>
      <button id="btn-filter-riya" class="filter-btn active" onclick="setFilter('riya')">
        <i class="fa-solid fa-crown" style="color: #f59e0b;"></i> Show ONLY My Admin Data (Riya Nagare)
      </button>
      <button id="btn-filter-all" class="filter-btn" onclick="setFilter('all')">
        <i class="fa-solid fa-users"></i> Show All Platform Users ({len(users)})
      </button>
    </div>

    <!-- Overview Stats -->
    <div class="stats-grid">
      <div class="stat-card">
        <div class="stat-title">Database Engine</div>
        <div class="stat-value" style="color: #38bdf8;">SQLite 3</div>
      </div>
      <div class="stat-card">
        <div class="stat-title">Total Relational Tables</div>
        <div class="stat-value">{len(tables)} Tables</div>
      </div>
      <div class="stat-card">
        <div class="stat-title">Your Admin ID</div>
        <div class="stat-value" style="color: #10b981;">#2 (Riya Nagare)</div>
      </div>
      <div class="stat-card">
        <div class="stat-title">Platform Records</div>
        <div class="stat-value">{len(users)} Users | {len(tests)} Tests</div>
      </div>
    </div>

    <!-- USERS TABLE -->
    <div class="section-card">
      <div class="section-header">
        <div class="section-title"><i class="fa-solid fa-user-shield text-primary"></i> Table: `employees` (User Profile & Credentials)</div>
      </div>
      <div style="overflow-x: auto;">
        <table>
          <thead>
            <tr>
              <th>ID</th>
              <th>Name</th>
              <th>Email</th>
              <th>Target Company</th>
              <th>Target Role</th>
              <th>Role Status</th>
              <th>Registered At</th>
            </tr>
          </thead>
          <tbody id="tbody-users">
    """

    for u in users:
        is_riya = (u["id"] == 2 or str(u["email"]).lower() == "riyanagare126@gmail.com")
        row_cls = "row-riya" if is_riya else "row-other"
        riya_attr = "true" if is_riya else "false"
        tag = '<span class="badge badge-riya"><i class="fa-solid fa-crown"></i> Platform Admin</span>' if is_riya else ('<span class="badge badge-admin">Admin</span>' if u["is_admin"] else '<span class="badge badge-student">Candidate</span>')
        
        name_str = f"<strong>{html.escape(str(u['name']))} (YOU)</strong>" if is_riya else html.escape(str(u["name"]))
        email_str = f"<strong style='color:#10b981;'>{html.escape(str(u['email']))}</strong>" if is_riya else html.escape(str(u["email"]))
        
        html_content += f"""
            <tr class="{row_cls}" data-is-riya="{riya_attr}">
              <td>#{u["id"]}</td>
              <td>{name_str}</td>
              <td>{email_str}</td>
              <td>{html.escape(str(u["target_company"] or "Tata Consultancy Services"))}</td>
              <td>{html.escape(str(u["target_role"] or "Java Developer"))}</td>
              <td>{tag}</td>
              <td style="color: var(--text-muted); font-size: 0.8rem;">{str(u["created_at"])[:16]}</td>
            </tr>
        """

    html_content += """
          </tbody>
        </table>
      </div>
    </div>

    <!-- APTITUDE TESTS TABLE -->
    <div class="section-card">
      <div class="section-header">
        <div class="section-title"><i class="fa-solid fa-clipboard-check text-emerald"></i> Table: `aptitude_results` (Test Submissions & Marks)</div>
      </div>
      <div style="overflow-x: auto;">
        <table>
          <thead>
            <tr>
              <th>Test ID</th>
              <th>Candidate Name</th>
              <th>Score</th>
              <th>Percentage</th>
              <th>Performance Message</th>
              <th>Date</th>
            </tr>
          </thead>
          <tbody id="tbody-tests">
    """

    for t in tests:
        is_riya = (t["employee_id"] == 2 or str(t["user_email"] or "").lower() == "riyanagare126@gmail.com")
        row_cls = "row-riya" if is_riya else "row-other"
        riya_attr = "true" if is_riya else "false"
        cand_name = "<strong>Riya Nagare (YOU)</strong>" if is_riya else html.escape(str(t["user_name"] or f"Candidate #{t['employee_id']}"))

        html_content += f"""
            <tr class="{row_cls}" data-is-riya="{riya_attr}">
              <td>#{t["id"]}</td>
              <td>{cand_name}</td>
              <td><strong>{t["score"]}</strong> / {t["total"]}</td>
              <td><span class="badge badge-success">{t["percentage"]}%</span></td>
              <td style="color: var(--text-muted);">{html.escape(str(t["performance_message"] or "Completed"))}</td>
              <td style="color: var(--text-muted); font-size: 0.8rem;">{str(t["created_at"])[:16]}</td>
            </tr>
        """

    html_content += """
          </tbody>
        </table>
      </div>
    </div>

    <!-- CODING SUBMISSIONS TABLE -->
    <div class="section-card">
      <div class="section-header">
        <div class="section-title"><i class="fa-solid fa-code text-cyan"></i> Table: `coding_progress` (Code Submissions)</div>
      </div>
      <div style="overflow-x: auto;">
        <table>
          <thead>
            <tr>
              <th>ID</th>
              <th>Candidate</th>
              <th>Problem Title</th>
              <th>Language</th>
              <th>Difficulty</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody id="tbody-codes">
    """

    for c in codes:
        is_riya = (c["employee_id"] == 2 or str(c["user_email"] or "").lower() == "riyanagare126@gmail.com")
        row_cls = "row-riya" if is_riya else "row-other"
        riya_attr = "true" if is_riya else "false"
        cand_name = "<strong>Riya Nagare (YOU)</strong>" if is_riya else html.escape(str(c["user_name"] or f"Candidate #{c['employee_id']}"))

        html_content += f"""
            <tr class="{row_cls}" data-is-riya="{riya_attr}">
              <td>#{c["id"]}</td>
              <td>{cand_name}</td>
              <td><strong>{html.escape(str(c["problem_title"]))}</strong></td>
              <td><code>{html.escape(str(c["language"]))}</code></td>
              <td>{html.escape(str(c["difficulty"]))}</td>
              <td><span class="badge badge-success">{c["status"]}</span></td>
            </tr>
        """

    html_content += """
          </tbody>
        </table>
      </div>
    </div>

    <!-- ROADMAPS TABLE -->
    <div class="section-card">
      <div class="section-header">
        <div class="section-title"><i class="fa-solid fa-map-location-dot text-violet"></i> Table: `smart_roadmaps` (Candidate Prep Roadmaps)</div>
      </div>
      <div style="overflow-x: auto;">
        <table>
          <thead>
            <tr>
              <th>ID</th>
              <th>Candidate</th>
              <th>Target Company</th>
              <th>Duration</th>
              <th>Tasks Progress</th>
              <th>Progress</th>
            </tr>
          </thead>
          <tbody id="tbody-roadmaps">
    """

    for r in roadmaps:
        is_riya = (r["employee_id"] == 2 or str(r["user_email"] or "").lower() == "riyanagare126@gmail.com")
        row_cls = "row-riya" if is_riya else "row-other"
        riya_attr = "true" if is_riya else "false"
        cand_name = "<strong>Riya Nagare (YOU)</strong>" if is_riya else html.escape(str(r["user_name"] or f"Candidate #{r['employee_id']}"))

        html_content += f"""
            <tr class="{row_cls}" data-is-riya="{riya_attr}">
              <td>#{r["id"]}</td>
              <td>{cand_name}</td>
              <td><strong>{html.escape(str(r["company_name"]))}</strong></td>
              <td>{r["duration_days"]} Days</td>
              <td>{r["completed_tasks"]} / {r["total_tasks"]} Tasks</td>
              <td><span class="badge badge-success">{r["progress_percent"]}%</span></td>
            </tr>
        """

    html_content += """
          </tbody>
        </table>
      </div>
    </div>

  </div>

  <script>
    function setFilter(mode) {
      const btnRiya = document.getElementById('btn-filter-riya');
      const btnAll = document.getElementById('btn-filter-all');
      const rows = document.querySelectorAll('tr[data-is-riya]');

      if (mode === 'riya') {
        btnRiya.classList.add('active');
        btnAll.classList.remove('active');
        rows.forEach(r => {
          if (r.getAttribute('data-is-riya') === 'true') {
            r.style.display = '';
          } else {
            r.style.display = 'none';
          }
        });
      } else {
        btnAll.classList.add('active');
        btnRiya.classList.remove('active');
        rows.forEach(r => {
          r.style.display = '';
        });
      }
    }

    // Default to showing only Riya Nagare's data on initial load
    document.addEventListener('DOMContentLoaded', () => {
      setFilter('riya');
    });
  </script>
</body>
</html>
    """

    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(html_content)
    with open(FRONTEND_HTML, "w", encoding="utf-8") as f:
        f.write(html_content)

    print("Regenerated database viewers successfully!")
    conn.close()

if __name__ == "__main__":
    generate_html()
