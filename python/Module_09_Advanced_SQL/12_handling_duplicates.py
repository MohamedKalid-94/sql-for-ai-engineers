import sqlite3
from config import DATABASE_PATH, read_statements

(create_table, insert_rows, read_all, find_duplicates, distinct_rows,
 preview_delete, delete_duplicates, create_unique, bad_insert,
 insert_ignore, read_final) = read_statements(__file__)

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()


def show(title, statement):
    print(title)
    print("-" * len(title))
    cursor.execute(statement)
    for row in cursor.fetchall():
        print(row)


cursor.execute(create_table)
cursor.execute(insert_rows)
connection.commit()

show("The table with repeated rows", read_all)

print()
show("Which emails repeat, and how many times", find_duplicates)

print()
show("DISTINCT shows each person once, but the table is unchanged", distinct_rows)

print()
show("Preview: the rows that would be deleted (everything but the first of each email)", preview_delete)

cursor.execute(delete_duplicates)
connection.commit()
print("\nDuplicate rows deleted:", cursor.rowcount)

cursor.execute(create_unique)
connection.commit()
print("A UNIQUE index on email now guards the table")

print("\nTry to add the same email again")
try:
    cursor.execute(bad_insert)
except sqlite3.IntegrityError as error:
    print("Rejected:", error)

cursor.execute(insert_ignore)
connection.commit()
print("INSERT OR IGNORE: rows inserted =", cursor.rowcount, "(skipped quietly)")

print()
show("The table after cleaning", read_final)

connection.close()