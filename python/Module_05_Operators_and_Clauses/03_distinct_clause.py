import sqlite3
from config import DATABASE_PATH


connection = sqlite3.connect(DATABASE_PATH)

cursor = connection.cursor()


cursor.execute("""
SELECT DISTINCT dept_id
FROM employees
""")


rows = cursor.fetchall()


print("Unique Departments")
print("------------------")


for row in rows:
    print(row)


connection.close()