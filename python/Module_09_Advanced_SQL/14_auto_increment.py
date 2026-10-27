import sqlite3
from config import DATABASE_PATH, read_statements

(create_plain, create_safe, insert_plain, insert_safe, delete_plain,
 delete_safe, insert_new_plain, insert_new_safe, read_plain, read_safe,
 read_sequence_table) = read_statements(__file__)

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()


def show(title, statement):
    print(title)
    print("-" * len(title))
    cursor.execute(statement)
    for row in cursor.fetchall():
        print(row)


cursor.execute(create_plain)
cursor.execute(create_safe)

cursor.execute(insert_plain)
print("Three rows added to plain_ids, last id:", cursor.lastrowid)
cursor.execute(insert_safe)
print("Three rows added to safe_ids , last id:", cursor.lastrowid)

cursor.execute(delete_plain)
cursor.execute(delete_safe)
print("\nRow with id 3 deleted from both tables")

cursor.execute(insert_new_plain)
print("New row in plain_ids gets id:", cursor.lastrowid, "<- the number 3 is REUSED")
cursor.execute(insert_new_safe)
print("New row in safe_ids  gets id:", cursor.lastrowid, "<- AUTOINCREMENT never reuses 3")
connection.commit()

print()
show("plain_ids (INTEGER PRIMARY KEY)", read_plain)
print()
show("safe_ids (AUTOINCREMENT)", read_safe)
print()
show("The hidden counters (tokens comes from the last lesson)", read_sequence_table)

connection.close()