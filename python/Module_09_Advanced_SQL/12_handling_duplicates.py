from config import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.executescript("""
DROP TABLE IF EXISTS duplicate_employees;

CREATE TABLE duplicate_employees(
    emp_id INTEGER,
    name TEXT
);

INSERT INTO duplicate_employees VALUES
(101,'John'),
(101,'John'),
(102,'Sara'),
(102,'Sara'),
(103,'David');
""")

conn.commit()

print("Duplicate Records")
print("-----------------")

cursor.execute("SELECT * FROM duplicate_employees")

for row in cursor.fetchall():
    print(row)

print("\nDistinct Records")
print("----------------")

cursor.execute("""
SELECT DISTINCT *
FROM duplicate_employees
""")

for row in cursor.fetchall():
    print(row)

conn.close()