from config import get_connection

conn = get_connection()
cursor = conn.cursor()

print("Before Transaction")
print("------------------")

cursor.execute("""
SELECT emp_id,name,salary
FROM employees
""")

for row in cursor.fetchall():
    print(row)

cursor.execute("BEGIN TRANSACTION")

cursor.execute("""
UPDATE employees
SET salary = salary + 5000
WHERE department_id = 1
""")

conn.commit()

print("\nAfter Transaction")
print("-----------------")

cursor.execute("""
SELECT emp_id,name,salary
FROM employees
""")

for row in cursor.fetchall():
    print(row)

conn.close()