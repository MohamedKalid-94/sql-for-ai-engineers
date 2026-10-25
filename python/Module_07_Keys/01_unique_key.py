import sqlite3
from config import DATABASE_PATH


connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()


cursor.execute("""
DROP TABLE IF EXISTS employees_unique
""")


cursor.execute("""
CREATE TABLE employees_unique
(
    emp_id INTEGER,
    email TEXT UNIQUE
)
""")


cursor.execute("""
INSERT INTO employees_unique
VALUES
(101,'john@gmail.com')
""")


cursor.execute("""
INSERT INTO employees_unique
VALUES
(102,'sara@gmail.com')
""")


connection.commit()


print("UNIQUE KEY Result")
print("-----------------")


for row in cursor.execute(
    "SELECT * FROM employees_unique"
):
    print(row)


connection.close()