from config import get_connection

conn = get_connection()
cursor = conn.cursor()

print("Employees Above Average Salary")
print("------------------------------")

cursor.execute("""
SELECT *
FROM employees
WHERE salary >
(
    SELECT AVG(salary)
    FROM employees
)
""")

for row in cursor.fetchall():
    print(row)

conn.close()