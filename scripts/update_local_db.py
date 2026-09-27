import sqlite3

conn = sqlite3.connect("backend/database/employees.db")
c = conn.cursor()
c.execute("UPDATE employees SET name = 'Madhuri Pathak' WHERE LOWER(email) = 'student@prep.com'")
print("Updated employees count:", c.rowcount)
c.execute("UPDATE resume_data SET full_name = 'Madhuri Pathak' WHERE email = 'student@prep.com'")
print("Updated resume_data count:", c.rowcount)
c.execute("UPDATE resume_versions SET resume_data_json = REPLACE(REPLACE(resume_data_json, 'Rahul Sharma', 'Madhuri Pathak'), 'Madhuri Pathav', 'Madhuri Pathak')")
print("Updated resume_versions count:", c.rowcount)
conn.commit()

c.execute("SELECT id, name, email FROM employees WHERE LOWER(email) = 'student@prep.com'")
rows = c.fetchall()
print("Local employees table verification:", rows)
conn.close()
