import sqlite3
from config import DATABASE_PATH


connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()


try:

    cursor.execute("""
    CREATE UNIQUE INDEX idx_unique_email
    ON employees(email)
    """)


    connection.commit()

    print("Unique index created successfully")


except sqlite3.Error as error:

    print(error)


connection.close()