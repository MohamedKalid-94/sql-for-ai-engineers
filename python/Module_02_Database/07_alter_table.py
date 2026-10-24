import sqlite3
from config import DATABASE_PATH

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()


def column_exists(column_name):

    cursor.execute("PRAGMA table_info(employees)")

    columns = [column[1] for column in cursor.fetchall()]

    return column_name in columns


if not column_exists("phone"):

    cursor.execute("""
        ALTER TABLE employees
        ADD COLUMN phone TEXT
    """)

    print("Column 'phone' added")

else:

    print("Column 'phone' already exists")


if not column_exists("joining_date"):

    cursor.execute("""
        ALTER TABLE employees
        ADD COLUMN joining_date TEXT
    """)

    print("Column 'joining_date' added")

else:

    print("Column 'joining_date' already exists")


if not column_exists("is_active"):

    cursor.execute("""
        ALTER TABLE employees
        ADD COLUMN is_active INTEGER DEFAULT 1
    """)

    print("Column 'is_active' added")

else:

    print("Column 'is_active' already exists")


connection.commit()
connection.close()

print("\nALTER TABLE completed successfully")