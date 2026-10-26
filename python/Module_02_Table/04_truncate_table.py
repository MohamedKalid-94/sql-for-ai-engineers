import sqlite3
from config import DATABASE_PATH, read_statements

(create_table, insert_three, count_rows, truncate,
 insert_one, read_rows, reset_counter) = read_statements(__file__)

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()


def show(title, statement):
    print(title)
    cursor.execute(statement)
    for row in cursor.fetchall():
        print("  ", row)


cursor.execute(create_table)
cursor.execute(insert_three)
connection.commit()
show("Rows after inserting three", count_rows)

cursor.execute(truncate)
connection.commit()
show("\nRows after the TRUNCATE equivalent", count_rows)

cursor.execute(insert_one)
connection.commit()
show("\nNew row (the id keeps counting from the old memory)", read_rows)

cursor.execute(truncate)
cursor.execute(reset_counter)
connection.commit()
cursor.execute(insert_one)
connection.commit()
show("\nNew row after resetting the counter (the id starts at 1 again)", read_rows)

connection.close()