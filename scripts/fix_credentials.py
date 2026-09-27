import sqlite3
import os
from werkzeug.security import generate_password_hash, check_password_hash

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_path = os.path.join(BASE_DIR, "backend", "database", "employees.db")
conn = sqlite3.connect(db_path)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

admin_hash = generate_password_hash("AdminPassword123!")
student_hash = generate_password_hash("Student123!")

# Update admin
cur.execute("UPDATE employees SET password = ?, is_admin = 1 WHERE LOWER(email) = 'admin@prep.com'", (admin_hash,))
if cur.rowcount == 0:
    cur.execute("""
        INSERT INTO employees (name, email, password, qualification, skills, experience, job_role, target_company, target_role, is_admin)
        VALUES ('Platform Administrator', 'admin@prep.com', ?, 'MCA / M.Tech', 'Full Stack, Cloud Architecture, Python, Security', '5+ Years', 'System Administrator', 'Tata Consultancy Services (TCS)', 'Software Engineer', 1)
    """, (admin_hash,))
    print("Admin user created!")
else:
    print(f"Admin user password updated successfully to AdminPassword123! ({cur.rowcount} row updated)")

# Also ensure demo student is set
cur.execute("UPDATE employees SET password = ?, name = 'Madhuri Pathak' WHERE LOWER(email) = 'student@prep.com'", (student_hash,))
if cur.rowcount == 0:
    cur.execute("""
        INSERT INTO employees (name, email, password, qualification, skills, experience, job_role, target_company, target_role, is_admin)
        VALUES ('Madhuri Pathak', 'student@prep.com', ?, 'B.Tech Computer Science', 'Java, Spring Boot, SQL, Python, React, DSA', 'Fresher', 'Software Engineer', 'Tata Consultancy Services (TCS)', 'Java Developer', 0)
    """, (student_hash,))
    print("Student user created!")
else:
    print(f"Student user password and name updated successfully ({cur.rowcount} row updated)")

conn.commit()

# Verify
admin = cur.execute("SELECT id, email, password, is_admin FROM employees WHERE LOWER(email) = 'admin@prep.com'").fetchone()
print("Verification -> Admin ID:", admin["id"], "Email:", admin["email"], "is_admin:", admin["is_admin"])
print("Does 'AdminPassword123!' match?:", check_password_hash(admin["password"], "AdminPassword123!"))

conn.close()
