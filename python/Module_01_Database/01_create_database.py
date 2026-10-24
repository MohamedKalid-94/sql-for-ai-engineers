import sqlite3
from config import DATABASE_PATH

connection = sqlite3.connect(DATABASE_PATH)
print("Database Created")
connection.close()