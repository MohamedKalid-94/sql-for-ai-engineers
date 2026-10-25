from config import get_connection

conn = get_connection()
cursor = conn.cursor()

print("IN Operator Result")
print("------------------")

cursor.execute("""
SELECT *
FROM employees
WHERE department_id IN
(
    SELECT department_id
    FROM employees
    WHERE salary > 80000
)
""")

for row in cursor.fetchall():
    print(row)

print("\nEXISTS Operator Result")
print("----------------------")

cursor.execute("""
SELECT *
FROM employees e
WHERE EXISTS
(
    SELECT 1
    FROM employees x
    WHERE x.department_id=e.department_id
    AND x.salary>80000
)
""")

for row in cursor.fetchall():
    print(row)

conn.close()