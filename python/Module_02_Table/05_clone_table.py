import sqlite3
from config import DATABASE_PATH

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

# Remove old backup table if it exists
cursor.execute("""
DROP TABLE IF EXISTS employees_backup
""")

# Clone employees table
cursor.execute("""
CREATE TABLE employees_backup AS
SELECT *
FROM employees
""")

connection.commit()
connection.close()

print("employees table cloned successfully")
print("New Table : employees_backup")