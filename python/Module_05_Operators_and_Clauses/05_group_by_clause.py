import sqlite3
from config import DATABASE_PATH


connection = sqlite3.connect(DATABASE_PATH)

cursor = connection.cursor()


cursor.execute("""
SELECT
    dept_id,
    COUNT(*) AS employee_count
FROM employees
GROUP BY dept_id
""")


rows = cursor.fetchall()


print("Employee Count Department Wise")
print("------------------------------")


for row in rows:
    print(row)


connection.close()