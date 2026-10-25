from config import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.executescript("""
DROP TABLE IF EXISTS users;

CREATE TABLE users(
    user_id INTEGER PRIMARY KEY,
    username TEXT,
    status TEXT DEFAULT 'Active'
);

INSERT INTO users(user_id,username)
VALUES
(1,'Kalid');
""")

conn.commit()

print("DEFAULT Constraint Result")
print("-------------------------")

cursor.execute("SELECT * FROM users")

for row in cursor.fetchall():
    print(row)

conn.close()