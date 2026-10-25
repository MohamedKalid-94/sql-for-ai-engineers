import sqlite3
from config import DATABASE_PATH

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

cursor.execute("DROP VIEW IF EXISTS employee_details")

cursor.execute("""
CREATE VIEW employee_details AS

SELECT
    e.emp_id,
    e.name,
    e.email,
    e.salary,
    d.department_name
FROM employees e
INNER JOIN departments d
ON e.dept_id = d.dept_id
""")

connection.commit()

print("View created successfully")

connection.close()