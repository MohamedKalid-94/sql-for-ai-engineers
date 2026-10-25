import sqlite3
from config import DATABASE_PATH

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

# SQLite does not support ALTER VIEW ... RENAME TO
# Equivalent: Drop old view and create a new one.

cursor.execute("DROP VIEW IF EXISTS employee_details")

cursor.execute("DROP VIEW IF EXISTS employee_information")

cursor.execute("""
CREATE VIEW employee_information AS

SELECT
    emp_id,
    name,
    salary
FROM employees
""")

connection.commit()

print("View renamed successfully (SQLite equivalent)")

connection.close()