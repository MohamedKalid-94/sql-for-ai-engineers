from config import get_connection

conn = get_connection()
cursor = conn.cursor()

print("Cursor Functions (SQLite Equivalent)")
print("-"*38)

cursor.execute("""
SELECT emp_id,emp_name,salary
FROM employees
""")

for row in cursor:
    print(row)

conn.close()