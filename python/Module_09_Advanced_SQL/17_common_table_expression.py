from config import get_connection

conn = get_connection()
cursor = conn.cursor()

print("Common Table Expression")
print("-----------------------")

cursor.execute("""
WITH HighSalaryEmployees AS
(
    SELECT *
    FROM employees
    WHERE salary > 75000
)

SELECT *
FROM HighSalaryEmployees
""")

for row in cursor.fetchall():
    print(row)

conn.close()