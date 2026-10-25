import sqlite3
from config import DATABASE_PATH


connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()


cursor.execute("""
CREATE INDEX IF NOT EXISTS idx_employee_salary
ON employees(salary)
""")


connection.commit()


print("Index created successfully")


cursor.execute("""
SELECT *
FROM employees
WHERE salary > 80000
""")


print("\nEmployees Salary > 80000")
print("------------------------")


for row in cursor.fetchall():
    print(row)


connection.close()