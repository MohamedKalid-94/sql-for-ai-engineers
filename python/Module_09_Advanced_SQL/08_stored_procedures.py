from config import get_connection

conn = get_connection()
cursor = conn.cursor()


def get_high_salary():
    cursor.execute("""
    SELECT *
    FROM employees
    WHERE salary > 80000
    """)

    return cursor.fetchall()


print("Stored Procedure Equivalent")
print("---------------------------")

for row in get_high_salary():
    print(row)

conn.close()