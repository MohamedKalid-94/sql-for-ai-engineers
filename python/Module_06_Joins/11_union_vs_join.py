import sqlite3
from config import DATABASE_PATH


connection = sqlite3.connect(DATABASE_PATH)

cursor = connection.cursor()



print("UNION Result")
print("------------")


cursor.execute("""
SELECT emp_name
FROM employees

UNION

SELECT department_name
FROM departments
""")


for row in cursor.fetchall():
    print(row)



print("\nJOIN Result")
print("-----------")


cursor.execute("""
SELECT

employees.emp_name,
departments.department_name


FROM employees


JOIN departments


ON employees.department_id =
departments.department_id
""")


for row in cursor.fetchall():
    print(row)



connection.close()