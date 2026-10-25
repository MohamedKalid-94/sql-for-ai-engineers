from config import get_connection

conn = get_connection()
cursor = conn.cursor()

print("Conversion Functions")
print("-"*22)

cursor.execute("""
SELECT
emp_name,
CAST(salary AS INTEGER),
CAST(emp_id AS TEXT)
FROM employees
""")

for row in cursor.fetchall():
    print(row)

conn.close()