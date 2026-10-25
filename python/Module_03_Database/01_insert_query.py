import sqlite3
from config import DATABASE_PATH

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

cursor.execute("""
INSERT OR IGNORE INTO employees
(
    emp_id,
    name,
    email,
    salary,
    dept_id
)
VALUES
(
    111,
    'Robert',
    'robert@gmail.com',
    76000,
    4
)
""")

connection.commit()

print("One employee inserted successfully")

connection.close()