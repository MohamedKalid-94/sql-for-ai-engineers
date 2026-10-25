import sqlite3
from config import DATABASE_PATH


connection = sqlite3.connect(DATABASE_PATH)

cursor = connection.cursor()


cursor.execute("""
SELECT *
FROM employees
WHERE dept_id != 1
""")


rows = cursor.fetchall()


print("Employees Not In Department 1")
print("-----------------------------")


for row in rows:
    print(row)


connection.close()