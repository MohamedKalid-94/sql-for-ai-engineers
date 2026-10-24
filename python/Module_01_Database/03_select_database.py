import sqlite3
from config import DATABASE_PATH

connection = sqlite3.connect(DATABASE_PATH)
print("Using Database:")

cursor = connection.cursor()

cursor.execute("PRAGMA database_list")
print(cursor.fetchall())

connection.close()