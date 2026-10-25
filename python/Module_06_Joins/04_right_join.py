import sqlite3
from config import DATABASE_PATH


connection = sqlite3.connect(DATABASE_PATH)

cursor = connection.cursor()


cursor.execute("""
SELECT
    departments.department_name,
    employees.emp_name

FROM departments

LEFT JOIN employees

ON departments.department_id =
employees.department_id
""")


print("RIGHT JOIN Equivalent Result")
print("----------------------------")


for row in cursor.fetchall():
    print(row)


connection.close()