import sqlite3
from config import DATABASE_PATH


connection = sqlite3.connect(DATABASE_PATH)

cursor = connection.cursor()


cursor.execute(
    "PRAGMA foreign_keys = ON"
)


cursor.execute("""
DROP TABLE IF EXISTS employees_fk
""")


cursor.execute("""
DROP TABLE IF EXISTS departments_fk
""")


cursor.execute("""
CREATE TABLE departments_fk
(
    dept_id INTEGER PRIMARY KEY,
    dept_name TEXT
)
""")


cursor.execute("""
CREATE TABLE employees_fk
(
    emp_id INTEGER PRIMARY KEY,
    name TEXT,
    dept_id INTEGER,

    FOREIGN KEY(dept_id)
    REFERENCES departments_fk(dept_id)
)
""")


cursor.executemany(
    """
    INSERT INTO departments_fk
    VALUES (?,?)
    """,
    [
        (1,"AI"),
        (2,"Python")
    ]
)


cursor.executemany(
    """
    INSERT INTO employees_fk
    VALUES (?,?,?)
    """,
    [
        (101,"John",1),
        (102,"Sara",2)
    ]
)


connection.commit()


print("FOREIGN KEY Result")
print("------------------")


query = """
SELECT
employees_fk.name,
departments_fk.dept_name

FROM employees_fk

JOIN departments_fk

ON employees_fk.dept_id =
departments_fk.dept_id
"""


for row in cursor.execute(query):
    print(row)


connection.close()