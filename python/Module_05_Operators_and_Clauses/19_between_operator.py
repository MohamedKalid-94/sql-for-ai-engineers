import sqlite3
from config import DATABASE_PATH


connection = sqlite3.connect(DATABASE_PATH)

cursor = connection.cursor()


cursor.execute("""
SELECT *
FROM employees
WHERE salary BETWEEN 70000 AND 90000
""")


rows = cursor.fetchall()


print("Employees Salary Between 70000 and 90000")
print("----------------------------------------")


for row in rows:
    print(row)


connection.close()