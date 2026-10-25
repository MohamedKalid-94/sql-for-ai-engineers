import sqlite3
from config import DATABASE_PATH

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS employees")

cursor.execute("""
CREATE TABLE employees(
    emp_id INTEGER PRIMARY KEY,
    emp_name TEXT,
    email TEXT,
    salary REAL,
    department_id INTEGER,
    joining_date TEXT
)
""")

employees = [
    (101,"John","john@gmail.com",75000,1,"2025-01-15"),
    (102,"Sara","sara@gmail.com",85000,2,"2025-02-10"),
    (103,"David","david@gmail.com",65000,3,"2024-11-20"),
    (104,"Priya","priya@gmail.com",90000,1,"2024-12-05"),
    (105,"Alex","alex@gmail.com",72000,5,"2025-03-01")
]

cursor.executemany("""
INSERT INTO employees
VALUES(?,?,?,?,?,?)
""", employees)

connection.commit()

print("Sample employee table created successfully")

connection.close()