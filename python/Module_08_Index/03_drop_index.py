import sqlite3
from config import DATABASE_PATH, read_statements

(plan_with_index, drop_index, plan_without_index,
 drop_if_exists, drop_missing, count_rows) = read_statements(__file__)

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()


def show_plan(title, statement):
    print(f"\n{title}")
    print("-" * len(title))
    cursor.execute(statement)
    for row in cursor.fetchall():
        print("  ", row[3])


show_plan("With the index idx_pupils_name", plan_with_index)

cursor.execute(drop_index)
connection.commit()
print("\nDROP INDEX idx_pupils_name done")

show_plan("Without the index (back to reading every row)", plan_without_index)

cursor.execute(drop_if_exists)
print("\nDROP INDEX IF EXISTS on a missing index: no error")

try:
    cursor.execute(drop_missing)
except sqlite3.Error as error:
    print("DROP INDEX on a missing index: rejected ->", error)

cursor.execute(count_rows)
print("\nPupils still in the table:", cursor.fetchone()[0], "<- dropping an index never touches the data")

connection.close()