import sqlite3
from config import DATABASE_PATH


connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()


cursor.execute("DROP TABLE IF EXISTS employees")
cursor.execute("DROP TABLE IF EXISTS departments")


cursor.execute("""
CREATE TABLE departments
(
    dept_id INTEGER,
    dept_name TEXT
)
""")


cursor.execute("""
CREATE TABLE employees
(
    emp_id INTEGER,
    name TEXT,
    email TEXT,
    salary REAL,
    dept_id INTEGER
)
""")


departments = [
    (1, "AI"),
    (2, "Python"),
    (3, "Data Science")
]


employees = [
    (101, "John", "john@gmail.com", 75000, 1),
    (102, "Sara", "sara@gmail.com", 85000, 2),
    (103, "David", "david@gmail.com", 65000, 3)
]


cursor.executemany(
    "INSERT INTO departments VALUES (?,?)",
    departments
)


cursor.executemany(
    "INSERT INTO employees VALUES (?,?,?,?,?)",
    employees
)


connection.commit()

print("Sample tables created successfully")

connection.close()