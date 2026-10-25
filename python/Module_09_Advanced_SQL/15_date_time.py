from config import get_connection

conn = get_connection()
cursor = conn.cursor()

print("Current Date")
print("------------")

cursor.execute("SELECT DATE('now')")
print(cursor.fetchone()[0])

print("\nCurrent Time")
print("------------")

cursor.execute("SELECT TIME('now')")
print(cursor.fetchone()[0])

print("\nCurrent DateTime")
print("----------------")

cursor.execute("SELECT DATETIME('now')")
print(cursor.fetchone()[0])

print("\nEmployees With Joining Date")
print("---------------------------")

cursor.execute("""
SELECT emp_id,name,joining_date
FROM employees
WHERE joining_date IS NOT NULL
""")

for row in cursor.fetchall():
    print(row)

conn.close()