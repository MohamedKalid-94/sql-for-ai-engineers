import sqlite3
from config import DATABASE_PATH


connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()


print("Employees")
print("----------------")


cursor.execute("""
SELECT *
FROM employees
WHERE salary > 80000
""")


for row in cursor.fetchall():
    print(row)


connection.close()