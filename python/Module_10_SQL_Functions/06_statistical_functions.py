from config import get_connection

conn = get_connection()
cursor = conn.cursor()

print("Statistical Functions")
print("-"*24)

cursor.execute("""
SELECT
COUNT(*),
MIN(salary),
MAX(salary),
AVG(salary),
SUM(salary)
FROM employees
""")

print(cursor.fetchone())

conn.close()