import sqlite3
from config import DATABASE_PATH


connection = sqlite3.connect(DATABASE_PATH)

cursor = connection.cursor()


cursor.execute("""
SELECT *
FROM employees
WHERE joining_date IS NULL
""")


rows = cursor.fetchall()


print("Employees With NULL Joining Date")
print("--------------------------------")


for row in rows:
    print(row)


connection.close()