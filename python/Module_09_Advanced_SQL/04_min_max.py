from config import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.execute("""
SELECT MIN(salary)
FROM employees
""")

print("Minimum Salary")
print("--------------")
print(cursor.fetchone()[0])

cursor.execute("""
SELECT MAX(salary)
FROM employees
""")

print("\nMaximum Salary")
print("--------------")
print(cursor.fetchone()[0])

conn.close()