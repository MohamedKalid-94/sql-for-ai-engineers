import sqlite3
from config import DATABASE_PATH


connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()


print("Available Indexes")
print("-----------------")


cursor.execute("""
PRAGMA index_list('employees')
""")


for row in cursor.fetchall():
    print(row)


connection.close()