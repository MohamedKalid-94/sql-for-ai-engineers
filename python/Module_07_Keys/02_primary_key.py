import sqlite3
from config import DATABASE_PATH


connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()


cursor.execute("""
DROP TABLE IF EXISTS employees_primary
""")


cursor.execute("""
CREATE TABLE employees_primary
(
    emp_id INTEGER PRIMARY KEY,
    name TEXT,
    salary REAL
)
""")


cursor.execute("""
INSERT INTO employees_primary
VALUES
(101,'John',75000)
""")


cursor.execute("""
INSERT INTO employees_primary
VALUES
(102,'Sara',85000)
""")


connection.commit()


print("PRIMARY KEY Result")
print("------------------")


for row in cursor.execute(
    "SELECT * FROM employees_primary"
):
    print(row)


connection.close()