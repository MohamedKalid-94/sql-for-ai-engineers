import sqlite3
from config import DATABASE_PATH, read_statements

(create_unique, plan_lookup, read_lookup,
 bad_insert, bad_unique_index, count_rows) = read_statements(__file__)

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

cursor.execute(create_unique)
connection.commit()
print("Unique index idx_pupils_roll_code created")

print("\nHow SQLite finds one roll code")
print("------------------------------")
cursor.execute(plan_lookup)
for row in cursor.fetchall():
    print("  ", row[3])

print("\nThe pupil with roll code R00123")
print("-------------------------------")
cursor.execute(read_lookup)
print(cursor.fetchone())

print("\nTry to add a pupil with a roll code that already exists")
try:
    cursor.execute(bad_insert)
except sqlite3.Error as error:
    print("Rejected:", error)

print("\nTry to make a unique index on city (it has many repeats)")
try:
    cursor.execute(bad_unique_index)
except sqlite3.Error as error:
    print("Rejected:", error)

connection.rollback()
cursor.execute(count_rows)
print("\nPupils in the table:", cursor.fetchone()[0], "<- neither bad change got in")

connection.close()