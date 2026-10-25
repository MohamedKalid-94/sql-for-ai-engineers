import sqlite3
from config import DATABASE_PATH

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

cursor.execute("DROP VIEW IF EXISTS employee_details")

connection.commit()

print("View dropped successfully")

connection.close()