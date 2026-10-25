import sqlite3
from config import DATABASE_PATH


connection = sqlite3.connect(DATABASE_PATH)

cursor = connection.cursor()


cursor.execute("""
SELECT *
FROM employees
LIMIT 5
""")


rows = cursor.fetchall()


print("Top 5 Employees")
print("----------------")


for row in rows:
    print(row)


connection.close()