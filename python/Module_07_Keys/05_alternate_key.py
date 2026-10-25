import sqlite3
from config import DATABASE_PATH


connection = sqlite3.connect(DATABASE_PATH)

cursor = connection.cursor()


cursor.execute("""
DROP TABLE IF EXISTS users
""")


cursor.execute("""
CREATE TABLE users
(
    user_id INTEGER PRIMARY KEY,

    username TEXT UNIQUE,

    email TEXT UNIQUE
)
""")


users = [

(1,"kalid","kalid@gmail.com"),

(2,"john","john@gmail.com")

]


cursor.executemany(
"""
INSERT INTO users
VALUES (?,?,?)
""",
users
)


connection.commit()


print("ALTERNATE KEY Result")
print("--------------------")


for row in cursor.execute(
    "SELECT * FROM users"
):
    print(row)


connection.close()