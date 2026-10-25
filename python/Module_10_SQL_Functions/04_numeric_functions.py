from config import get_connection

conn = get_connection()
cursor = conn.cursor()

print("Numeric Functions")
print("-" * 18)

cursor.execute("""
SELECT
ROUND(4567.8912,2),
ABS(-250),
CEIL(45.2),
FLOOR(45.9);
""")

print(cursor.fetchone())

conn.close()