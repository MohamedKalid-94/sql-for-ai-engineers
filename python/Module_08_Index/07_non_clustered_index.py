import sqlite3
from config import DATABASE_PATH, read_statements

(create_index, plan_normal, plan_covering,
 count_rows, list_indexes) = read_statements(__file__)

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()


def show_plan(title, statement):
    print(f"\n{title}")
    print("-" * len(title))
    cursor.execute(statement)
    for row in cursor.fetchall():
        print("  ", row[3])


cursor.execute(create_index)
connection.commit()
print("Index on two columns created: idx_pupils_city_marks (city, marks)")

show_plan("Uses city and marks together, then visits the table for the name", plan_normal)
show_plan("Asks only for city and marks: the index alone has everything (COVERING)", plan_covering)

cursor.execute(count_rows)
print("\nPune pupils with 77 marks:", cursor.fetchone()[0])

print("\nAll non-clustered indexes on pupils now")
print("---------------------------------------")
cursor.execute(list_indexes)
for index_name, is_unique, origin in cursor.fetchall():
    print(f"  {index_name:<24} unique: {is_unique} | origin: {origin}")

connection.close()