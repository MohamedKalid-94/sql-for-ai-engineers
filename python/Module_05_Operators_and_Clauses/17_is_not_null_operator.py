import sqlite3
from config import DATABASE_PATH


connection = sqlite3.connect(DATABASE_PATH)

cursor = connection.cursor()


# Update joining date
cursor.execute("""
UPDATE employees
SET joining_date = '2026-01-01'
WHERE emp_id IN (101,102,103)
""")


print("Employees With Joining Date")
print("---------------------------")


cursor.execute("""
SELECT *
FROM employees
WHERE joining_date IS NOT NULL
""")


rows = cursor.fetchall()

for row in rows:
    print(row)


connection.commit()
connection.close()