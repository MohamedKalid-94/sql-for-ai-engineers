import sqlite3
from config import DATABASE_PATH


connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()
cursor.execute("PRAGMA database_list")

for row in cursor.fetchall():
    print(row)

connection.close()