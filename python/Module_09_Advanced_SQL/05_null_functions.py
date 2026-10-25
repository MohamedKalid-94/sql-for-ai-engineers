from config import get_connection

conn = get_connection()
cursor = conn.cursor()

print("COALESCE Function")
print("-----------------")

cursor.execute("""
SELECT
name,
COALESCE(phone,'Not Available')
FROM employees
""")

for row in cursor.fetchall():
    print(row)

print("\nIFNULL Function")
print("----------------")

cursor.execute("""
SELECT
name,
IFNULL(joining_date,'Not Joined')
FROM employees
""")

for row in cursor.fetchall():
    print(row)

print("\nNULLIF Function")
print("----------------")

cursor.execute("SELECT NULLIF(75000,75000)")
print(cursor.fetchone()[0])

cursor.execute("SELECT NULLIF(75000,90000)")
print(cursor.fetchone()[0])

conn.close()