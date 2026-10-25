import sqlite3
from config import DATABASE_PATH


connection = sqlite3.connect(DATABASE_PATH)

cursor = connection.cursor()



print("LEFT JOIN Result")
print("----------------")


cursor.execute("""
SELECT

employees.emp_name,
departments.department_name


FROM employees


LEFT JOIN departments


ON employees.department_id =
departments.department_id
""")


for row in cursor.fetchall():
    print(row)



print("\nRIGHT JOIN Equivalent Result")
print("----------------------------")


cursor.execute("""
SELECT

departments.department_name,
employees.emp_name


FROM departments


LEFT JOIN employees


ON departments.department_id =
employees.department_id
""")


for row in cursor.fetchall():
    print(row)



connection.close()