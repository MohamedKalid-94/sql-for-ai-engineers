import sqlite3
from config import DATABASE_PATH, read_statements

(create_sequences, insert_sequences, next_value_sql, read_sequences,
 create_tokens, insert_tokens, read_sqlite_sequence, read_tokens) = read_statements(__file__)

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

cursor.execute(create_sequences)
cursor.execute(insert_sequences)
connection.commit()


def next_value(name, step):
    """The NEXT VALUE FOR equivalent: add the step and return the new number."""
    cursor.execute(next_value_sql, {"name": name, "step": step})
    value = cursor.fetchall()[0][0]
    connection.commit()
    return value


print("Counter table: invoice_number starts at 1000, steps of 1")
print("--------------------------------------------------------")
for _ in range(3):
    print("Next invoice number:", next_value("invoice_number", 1))

print("\nCounter table: ticket_number starts at 100, steps of 5")
print("------------------------------------------------------")
for _ in range(2):
    print("Next ticket number :", next_value("ticket_number", 5))

print("\nWhere each counter stands now")
print("-----------------------------")
cursor.execute(read_sequences)
for row in cursor.fetchall():
    print(row)

print("\nThe other equivalent: AUTOINCREMENT keeps a hidden counter")
print("----------------------------------------------------------")
cursor.execute(create_tokens)
cursor.execute(insert_tokens)
connection.commit()
cursor.execute(read_tokens)
for row in cursor.fetchall():
    print(row)
cursor.execute(read_sqlite_sequence)
print("Hidden counter (sqlite_sequence):", cursor.fetchall())

connection.close()