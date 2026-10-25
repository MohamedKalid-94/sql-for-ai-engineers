import sqlite3
from config import DATABASE_PATH


connection = sqlite3.connect(DATABASE_PATH)

cursor = connection.cursor()


cursor.execute("""
SELECT

employee.emp_name AS Employee,

manager.emp_name AS Manager


FROM employees employee


LEFT JOIN employees manager


ON employee.manager_id =
manager.emp_id
""")


print("SELF JOIN Result")
print("----------------")


for row in cursor.fetchall():
    print(row)


connection.close()