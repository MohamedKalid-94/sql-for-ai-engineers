import sqlite3
from config import DATABASE_PATH


connection = sqlite3.connect(DATABASE_PATH)

cursor = connection.cursor()


cursor.execute("""
SELECT *
FROM employees
WHERE dept_id IN (1,2,5)
""")


rows = cursor.fetchall()


print("Employees From Departments 1,2,5")
print("--------------------------------")


for row in rows:
    print(row)


connection.close()