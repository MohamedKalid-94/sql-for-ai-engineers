from config import get_connection

conn = get_connection()
cursor = conn.cursor()

print("Employees With NULL Phone")
print("-------------------------")

cursor.execute("""
SELECT *
FROM employees
WHERE phone IS NULL
""")

for row in cursor.fetchall():
    print(row)

print("\nEmployees With Phone")
print("--------------------")

cursor.execute("""
SELECT *
FROM employees
WHERE phone IS NOT NULL
""")

for row in cursor.fetchall():
    print(row)

conn.close()