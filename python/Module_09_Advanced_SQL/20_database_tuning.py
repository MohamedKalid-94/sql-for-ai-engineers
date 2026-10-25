from config import get_connection

conn = get_connection()
cursor = conn.cursor()

print("Database Query Plan")
print("-------------------")

cursor.execute("""
EXPLAIN QUERY PLAN
SELECT *
FROM employees
WHERE salary > 80000
""")

for row in cursor.fetchall():
    print(row)

conn.close()