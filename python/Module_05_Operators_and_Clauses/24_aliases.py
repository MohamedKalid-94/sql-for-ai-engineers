import sqlite3
from config import DATABASE_PATH


connection = sqlite3.connect(DATABASE_PATH)

cursor = connection.cursor()


cursor.execute("""
SELECT
name AS employee_name,
salary AS monthly_salary

FROM employees
""")


rows = cursor.fetchall()


print("Column Alias Result")
print("-------------------")


for row in rows:
    print(row)



print("\nTable Alias Result")
print("------------------")


cursor.execute("""
SELECT
e.name,
e.salary

FROM employees AS e
""")


for row in cursor.fetchall():
    print(row)


connection.close()