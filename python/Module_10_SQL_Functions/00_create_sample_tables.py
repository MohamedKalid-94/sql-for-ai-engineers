import sqlite3
from config import DATABASE_PATH, read_statements

create_table, insert_scores, count_rows, first_rows = read_statements(__file__)

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

cursor.execute(create_table)
cursor.execute(insert_scores)
connection.commit()
print("Table exam_scores created and filled")

print("\nHow many scores")
print("---------------")
cursor.execute(count_rows)
print(cursor.fetchone())

print("\nThe first four scores")
print("---------------------")
cursor.execute(first_rows)
for row in cursor.fetchall():
    print(row)

connection.close()