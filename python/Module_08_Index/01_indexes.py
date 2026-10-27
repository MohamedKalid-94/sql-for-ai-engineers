import sqlite3
from config import DATABASE_PATH, read_statements

count_marks, plan_marks, plan_primary_key = read_statements(__file__)

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()


def show_plan(title, statement):
    print(f"\n{title}")
    print("-" * len(title))
    cursor.execute(statement)
    for row in cursor.fetchall():
        print("  ", row[3])      # the fourth column holds the plan text


cursor.execute(count_marks)
print("Pupils with exactly 77 marks:", cursor.fetchone()[0])

show_plan("No index on marks: SQLite must read every row (SCAN)", plan_marks)
show_plan("Search by the primary key: already fast (SEARCH)", plan_primary_key)

connection.close()