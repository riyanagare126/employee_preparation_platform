import sqlite3

conn = sqlite3.connect("backend/database/employees.db")
c = conn.cursor()
c.execute("UPDATE employees SET name = 'Madhuri Pathav' WHERE LOWER(email) = 'student@prep.com'")
print("Updated employees count:", c.rowcount)
c.execute("UPDATE resume_data SET full_name = 'Madhuri Pathav' WHERE email = 'student@prep.com'")
print("Updated resume_data count:", c.rowcount)
c.execute("UPDATE resume_versions SET resume_data_json = REPLACE(resume_data_json, 'Rahul Sharma', 'Madhuri Pathav')")
print("Updated resume_versions count:", c.rowcount)
conn.commit()

c.execute("SELECT id, name, email FROM employees WHERE LOWER(email) = 'student@prep.com'")
rows = c.fetchall()
print("Local employees table verification:", rows)
conn.close()
