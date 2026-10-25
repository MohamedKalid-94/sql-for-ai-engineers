import sqlite3
from config import DATABASE_PATH


connection = sqlite3.connect(DATABASE_PATH)

cursor = connection.cursor()


cursor.execute("""
SELECT *
FROM employees
ORDER BY salary DESC
""")


rows = cursor.fetchall()


print("Employees Ordered By Salary")
print("---------------------------")


for row in rows:
    print(row)


connection.close()