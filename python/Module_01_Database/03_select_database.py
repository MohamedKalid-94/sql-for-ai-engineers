import sqlite3
from config import DATABASE_PATH, read_statements

attach, create_notes, insert_note, read_main, read_scratch = read_statements(__file__)

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

cursor.execute(attach)
cursor.execute(create_notes)
cursor.execute(insert_note)
connection.commit()

print("Using the main notebook")
print("-----------------------")
cursor.execute(read_main)
for row in cursor.fetchall():
    print(row)

print("\nUsing the scratch notebook")
print("--------------------------")
cursor.execute(read_scratch)
for row in cursor.fetchall():
    print(row)

connection.close()