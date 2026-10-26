import sqlite3
from config import DATABASE_PATH, read_statements

attach, show_databases, detach, show_databases_again = read_statements(__file__)

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

cursor.execute(attach)
cursor.execute(show_databases)
print("Databases before DETACH:", [row[1] for row in cursor.fetchall()])

cursor.execute(detach)
cursor.execute(show_databases_again)
print("Databases after DETACH :", [row[1] for row in cursor.fetchall()])

connection.close()      # a file can only be deleted once it is closed

print("\nDROP DATABASE equivalent: delete the file")
print("Exists before:", DATABASE_PATH.exists())
DATABASE_PATH.unlink()
print("Exists after :", DATABASE_PATH.exists())