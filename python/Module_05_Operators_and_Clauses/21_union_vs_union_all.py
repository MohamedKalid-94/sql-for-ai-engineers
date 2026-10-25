import sqlite3
from config import DATABASE_PATH


connection = sqlite3.connect(DATABASE_PATH)

cursor = connection.cursor()


print("UNION Result")
print("------------")


cursor.execute("""
SELECT dept_id
FROM employees
WHERE dept_id IN (1,2)

UNION

SELECT dept_id
FROM employees
WHERE dept_id IN (2,3)
""")


for row in cursor.fetchall():
    print(row)



print("\nUNION ALL Result")
print("----------------")


cursor.execute("""
SELECT dept_id
FROM employees
WHERE dept_id IN (1,2)

UNION ALL

SELECT dept_id
FROM employees
WHERE dept_id IN (2,3)
""")


for row in cursor.fetchall():
    print(row)



connection.close()