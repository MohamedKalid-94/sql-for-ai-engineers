import sqlite3
from config import DATABASE_PATH, read_statements

(journal_mode, page_size, encoding,
 integrity, wal_on, wal_off) = read_statements(__file__)

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()


def ask(statement):
    cursor.execute(statement)
    return cursor.fetchone()[0]


print("Database file      :", DATABASE_PATH.name)
print("Where it lives     : one ordinary file next to the project, no server needed")
print("Journal mode       :", ask(journal_mode))
print("Page size (bytes)  :", ask(page_size))
print("Text encoding      :", ask(encoding))
print("Integrity check    :", ask(integrity))

print("\nSwitch to WAL mode (many readers, one writer)")
print("Journal mode now   :", ask(wal_on))
print("Back to normal     :", ask(wal_off))

connection.close()