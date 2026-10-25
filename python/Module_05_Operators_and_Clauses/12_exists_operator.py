import sqlite3
from config import DATABASE_PATH


connection = sqlite3.connect(DATABASE_PATH)

cursor = connection.cursor()


cursor.execute("""
SELECT *
FROM employees e
WHERE EXISTS
(
    SELECT 1
    FROM departments d
    WHERE d.dept_id = e.dept_id
)
""")


rows = cursor.fetchall()


print("Employees With Valid Departments")
print("--------------------------------")


for row in rows:
    print(row)


connection.close()