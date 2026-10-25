import sqlite3
from config import DATABASE_PATH

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

# SQLite does not support CREATE OR REPLACE VIEW

cursor.execute("DROP VIEW IF EXISTS employee_details")

cursor.execute("""
CREATE VIEW employee_details AS

SELECT
    emp_id,
    name,
    salary
FROM employees
""")

connection.commit()

print("View updated successfully")

connection.close()