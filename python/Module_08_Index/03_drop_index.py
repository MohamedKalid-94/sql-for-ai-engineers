import sqlite3
from config import DATABASE_PATH


connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()


cursor.execute("""
DROP INDEX IF EXISTS idx_employee_salary
""")


connection.commit()


print("Index dropped successfully")


connection.close()