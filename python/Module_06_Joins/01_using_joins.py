import sqlite3
from config import DATABASE_PATH


connection = sqlite3.connect(DATABASE_PATH)

cursor = connection.cursor()


cursor.execute("""
SELECT
employees.emp_name,
departments.department_name

FROM employees

JOIN departments

USING(department_id)
""")


print("USING JOIN Result")
print("-----------------")

for row in cursor.fetchall():
    print(row)


connection.close()