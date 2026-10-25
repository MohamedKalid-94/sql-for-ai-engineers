import sqlite3
from config import DATABASE_PATH

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

cursor.execute("""
DELETE FROM company_projects
""")

connection.commit()
connection.close()

print("Table Truncated Successfully (SQLite uses DELETE)")