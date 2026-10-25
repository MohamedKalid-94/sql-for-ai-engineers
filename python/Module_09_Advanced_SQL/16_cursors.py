from config import get_connection

conn = get_connection()
cursor = conn.cursor()

print("Cursor Equivalent")
print("-----------------")

cursor.execute("""
SELECT *
FROM employees
""")

for row in cursor.fetchall():
    print(row)

conn.close()