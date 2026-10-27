import sqlite3
from config import DATABASE_PATH, read_statements

(typeof_literals, typeof_expressions, create_flexible, insert_flexible,
 read_flexible, declared_types, create_strict, insert_strict,
 bad_strict, read_strict) = read_statements(__file__)

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()


def show(title, statement):
    print(title)
    print("-" * len(title))
    cursor.execute(statement)
    for row in cursor.fetchall():
        print(row)


show("The five storage classes", typeof_literals)
print()
show("What type does a calculation give?", typeof_expressions)

cursor.execute(create_flexible)
cursor.execute(insert_flexible)
connection.commit()

print()
show("A column typed INTEGER accepts almost anything (read amount_stored_as)", read_flexible)
print()
show("The declared types: a preference, not a rule", declared_types)

print("\nA STRICT table makes the declared type a real rule")
print("--------------------------------------------------")
try:
    cursor.execute(create_strict)
except sqlite3.OperationalError as error:
    print("This SQLite is too old for STRICT tables (needs 3.37 or newer):", error)
else:
    cursor.execute(insert_strict)
    connection.commit()
    print("Inserted 10 and '20' (the text '20' was converted to a number)")
    try:
        cursor.execute(bad_strict)
    except sqlite3.Error as error:
        print("Rejected:", error)
    print()
    show("Rows in the STRICT table", read_strict)

connection.close()