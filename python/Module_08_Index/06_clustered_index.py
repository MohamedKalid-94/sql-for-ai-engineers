import sqlite3
from config import DATABASE_PATH, read_statements

(create_table, copy_rows, count_rows, plan_rowid,
 plan_clustered, read_range, plan_range) = read_statements(__file__)

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()


def show_plan(title, statement):
    print(f"\n{title}")
    print("-" * len(title))
    cursor.execute(statement)
    for row in cursor.fetchall():
        print("  ", row[3])


cursor.execute(create_table)
cursor.execute(copy_rows)
connection.commit()
cursor.execute(count_rows)
print("Rows copied into the WITHOUT ROWID table:", cursor.fetchone()[0])

show_plan("Equivalent 1: pupils is sorted by its rowid (pupil_id)", plan_rowid)
show_plan("Equivalent 2: pupils_by_code is sorted by its PRIMARY KEY (roll_code)", plan_clustered)

print("\nA range of roll codes comes out already in order")
print("------------------------------------------------")
cursor.execute(read_range)
for row in cursor.fetchall():
    print("  ", row)

show_plan("Its plan has no extra sorting step, because the rows are stored in order", plan_range)

connection.close()