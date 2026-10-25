import sqlite3
from config import DATABASE_PATH


connection = sqlite3.connect(DATABASE_PATH)

cursor = connection.cursor()


print("AND Operator Result")
print("------------------")


cursor.execute("""
SELECT *
FROM employees
WHERE salary > 70000
AND dept_id = 1
""")


for row in cursor.fetchall():
    print(row)



print("\nOR Operator Result")
print("-----------------")


cursor.execute("""
SELECT *
FROM employees
WHERE dept_id = 1
OR dept_id = 2
""")


for row in cursor.fetchall():
    print(row)



connection.close()