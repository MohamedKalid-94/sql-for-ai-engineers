import sqlite3
from config import DATABASE_PATH


connection = sqlite3.connect(DATABASE_PATH)

cursor = connection.cursor()


cursor.execute("""
SELECT name
FROM employees
WHERE dept_id = 1

UNION

SELECT name
FROM employees
WHERE dept_id = 2
""")


rows = cursor.fetchall()


print("UNION Result")
print("-------------")


for row in rows:
    print(row)


connection.close()