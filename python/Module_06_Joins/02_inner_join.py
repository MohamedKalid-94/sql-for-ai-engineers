import sqlite3
from config import DATABASE_PATH


connection = sqlite3.connect(DATABASE_PATH)

cursor = connection.cursor()


cursor.execute("""
SELECT
employees.emp_name,
employees.salary,
departments.department_name

FROM employees

INNER JOIN departments

ON employees.department_id =
departments.department_id
""")


print("INNER JOIN Result")
print("-----------------")


for row in cursor.fetchall():
    print(row)


connection.close()