from config import get_connection

conn = get_connection()
cursor = conn.cursor()

print("GROUP BY Result")
print("----------------")

cursor.execute("""
SELECT
department_id,
COUNT(*)
FROM employees
GROUP BY department_id
""")

for row in cursor.fetchall():
    print(row)

print("\nORDER BY Result")
print("----------------")

cursor.execute("""
SELECT
emp_id,
name,
salary
FROM employees
ORDER BY salary DESC
""")

for row in cursor.fetchall():
    print(row)

conn.close()