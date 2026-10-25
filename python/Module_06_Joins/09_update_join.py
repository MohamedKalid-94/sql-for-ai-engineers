import sqlite3
from config import DATABASE_PATH


connection = sqlite3.connect(DATABASE_PATH)

cursor = connection.cursor()


cursor.execute("""
UPDATE employees

SET salary = salary + 5000


WHERE department_id IN

(
    SELECT department_id
    FROM departments
    WHERE department_name='AI'
)
""")


connection.commit()


print("UPDATE JOIN Equivalent Completed")


cursor.execute("""
SELECT *
FROM employees
""")


print("\nEmployees After Update")
print("---------------------")


for row in cursor.fetchall():
    print(row)


connection.close()