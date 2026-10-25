from config import get_connection

conn = get_connection()
cursor = conn.cursor()

user_name = "John"

cursor.execute("""
SELECT *
FROM employees
WHERE name=?
""", (user_name,))

print("Safe Parameterized Query")
print("------------------------")

for row in cursor.fetchall():
    print(row)

conn.close()