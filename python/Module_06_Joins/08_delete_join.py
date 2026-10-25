import sqlite3
from config import DATABASE_PATH


connection = sqlite3.connect(DATABASE_PATH)

cursor = connection.cursor()


cursor.execute("""
DELETE FROM employees

WHERE department_id IN

(
    SELECT department_id
    FROM departments
    WHERE department_name='Cloud'
)
""")


connection.commit()


print("DELETE JOIN Equivalent Completed")


cursor.execute("""
SELECT *
FROM employees
""")


print("\nEmployees After Delete")
print("---------------------")


for row in cursor.fetchall():
    print(row)


connection.close()