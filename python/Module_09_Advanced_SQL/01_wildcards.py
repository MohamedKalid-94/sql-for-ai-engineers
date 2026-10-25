from config import get_connection

conn = get_connection()
cursor = conn.cursor()

print("Names Starting With S")
print("----------------------")

cursor.execute("""
SELECT *
FROM employees
WHERE name LIKE 'S%'
""")

for row in cursor.fetchall():
    print(row)

print("\nEmail Contains gmail")
print("--------------------")

cursor.execute("""
SELECT *
FROM employees
WHERE email LIKE '%gmail%'
""")

for row in cursor.fetchall():
    print(row)

conn.close()