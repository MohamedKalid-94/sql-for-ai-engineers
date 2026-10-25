import sqlite3
from config import DATABASE_PATH


connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()


cursor.execute("""
CREATE INDEX IF NOT EXISTS idx_department_id
ON employees(department_id);
""")


print("Non Clustered Index Created Successfully")


cursor.execute("""
SELECT *
FROM employees
WHERE department_id = 1;
""")


print("\nEmployees Department 1")
print("---------------------")


for row in cursor.fetchall():
    print(row)


connection.commit()
connection.close()