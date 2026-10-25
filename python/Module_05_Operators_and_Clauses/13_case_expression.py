import sqlite3
from config import DATABASE_PATH


connection = sqlite3.connect(DATABASE_PATH)

cursor = connection.cursor()


cursor.execute("""
SELECT

name,
salary,

CASE

WHEN salary >= 90000
THEN 'High Salary'

WHEN salary >= 70000
THEN 'Medium Salary'

ELSE 'Low Salary'

END AS salary_category

FROM employees
""")


rows = cursor.fetchall()


print("Salary Category")
print("----------------")


for row in rows:
    print(row)


connection.close()