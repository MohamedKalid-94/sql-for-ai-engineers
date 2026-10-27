import sqlite3
from config import DATABASE_PATH, read_statements

(create_table, insert_profiles, *reading,
 update_profile, read_updated, bad_insert) = read_statements(__file__)

titles = [
    "json_extract: pull single values out of the JSON text",
    "Lists: the first skill and how many skills",
    "json_each: one row for every skill, then filter for Python",
    "How many people have each skill",
    "json_object: build JSON from table columns",
    "json_group_array: roll many rows into one JSON list",
]
assert len(titles) == len(reading), "each title needs exactly one statement"

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

cursor.execute(create_table)
cursor.execute(insert_profiles)
connection.commit()
print("Table user_profiles created with", cursor.rowcount, "JSON profiles")

for title, statement in zip(titles, reading):
    print()
    print(title)
    print("-" * len(title))
    cursor.execute(statement)
    for row in cursor.fetchall():
        print(row)

print("\njson_set: change two values inside the JSON")
print("-------------------------------------------")
cursor.execute(update_profile)
connection.commit()
print("Rows changed:", cursor.rowcount)
cursor.execute(read_updated)
for row in cursor.fetchall():
    print(row)

print("\nTry to store text that is not valid JSON")
try:
    cursor.execute(bad_insert)
except sqlite3.IntegrityError as error:
    print("Rejected:", error)

connection.close()