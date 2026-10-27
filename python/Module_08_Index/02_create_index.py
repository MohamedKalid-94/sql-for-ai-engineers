import sqlite3
from config import DATABASE_PATH, read_statements

(plan_before, create_marks, create_city, create_name,
 plan_after, count_marks) = read_statements(__file__)

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()


def show_plan(title, statement):
    print(f"\n{title}")
    print("-" * len(title))
    cursor.execute(statement)
    for row in cursor.fetchall():
        print("  ", row[3])


show_plan("Before the index", plan_before)

cursor.execute(create_marks)
cursor.execute(create_city)
cursor.execute(create_name)
connection.commit()
print("\nThree indexes created: idx_pupils_marks, idx_pupils_city, idx_pupils_name")

show_plan("After the index (the very same query)", plan_after)

cursor.execute(count_marks)
print("\nSame answer as before:", cursor.fetchone()[0], "pupils with 77 marks")

connection.close()