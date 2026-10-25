import sqlite3
from config import DATABASE_PATH

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

cursor.execute("""
INSERT INTO employees_backup

SELECT *

FROM employees
""")

connection.commit()

print("employees copied into employees_backup")

connection.close()