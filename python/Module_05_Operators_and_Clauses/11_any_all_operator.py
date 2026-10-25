import sqlite3
from config import DATABASE_PATH


connection = sqlite3.connect(DATABASE_PATH)

cursor = connection.cursor()


print("ANY Equivalent Result")
print("--------------------")


cursor.execute("""
SELECT *
FROM employees
WHERE salary >
(
    SELECT MIN(salary)
    FROM employees
    WHERE dept_id = 3
)
""")


for row in cursor.fetchall():
    print(row)



print("\nALL Equivalent Result")
print("--------------------")


cursor.execute("""
SELECT *
FROM employees
WHERE salary >
(
    SELECT MAX(salary)
    FROM employees
    WHERE dept_id = 3
)
""")


for row in cursor.fetchall():
    print(row)



connection.close()