import sqlite3
from config import DATABASE_PATH


connection = sqlite3.connect(DATABASE_PATH)

cursor = connection.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS employee_test
(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT
)
""")


cursor.execute("""
INSERT OR IGNORE INTO employee_test
(id,name,email)
VALUES
(1,'John','john@gmail.com')
""")


connection.commit()


print("NOT NULL constraint table created")
print("Sample record inserted successfully")


connection.close()