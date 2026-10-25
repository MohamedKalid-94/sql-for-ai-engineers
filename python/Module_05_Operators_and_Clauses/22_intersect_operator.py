import sqlite3
from config import DATABASE_PATH


connection = sqlite3.connect(DATABASE_PATH)

cursor = connection.cursor()


cursor.execute("""
SELECT name
FROM employees
WHERE salary > 70000

INTERSECT

SELECT name
FROM employees
WHERE dept_id = 1
""")


rows = cursor.fetchall()


print("INTERSECT Result")
print("----------------")


for row in rows:
    print(row)


connection.close()