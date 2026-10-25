import sqlite3
from config import DATABASE_PATH

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS employee_copy")

cursor.execute("""
CREATE TABLE employee_copy AS

SELECT *

FROM employees
""")

connection.commit()

print("employee_copy table created")

connection.close()