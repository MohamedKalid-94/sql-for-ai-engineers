import sqlite3
from config import DATABASE_PATH


connection = sqlite3.connect(DATABASE_PATH)

cursor = connection.cursor()


cursor.execute("""
SELECT
    employees.emp_name,
    departments.department_name

FROM employees

LEFT JOIN departments

ON employees.department_id =
departments.department_id


UNION


SELECT
    employees.emp_name,
    departments.department_name

FROM departments

LEFT JOIN employees

ON departments.department_id =
employees.department_id
""")


print("FULL JOIN Equivalent Result")
print("---------------------------")


for row in cursor.fetchall():
    print(row)


connection.close()