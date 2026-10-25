import sqlite3
from config import DATABASE_PATH

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

cursor.execute("""
CREATE TEMP TABLE temp_employee_salary AS

SELECT
    emp_id,
    name,
    salary
FROM employees
""")

print("Temporary Table Created Successfully")

print("\nTemporary Table Data\n")

cursor.execute("""
SELECT *
FROM temp_employee_salary
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

connection.close()