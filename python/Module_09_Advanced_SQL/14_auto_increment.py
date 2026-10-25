from config import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.executescript("""
DROP TABLE IF EXISTS auto_increment_demo;

CREATE TABLE auto_increment_demo(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_name TEXT
);

INSERT INTO auto_increment_demo(employee_name)
VALUES
('Alex'),
('Maria'),
('Emma');
""")

conn.commit()

print("AUTO INCREMENT Result")
print("---------------------")

cursor.execute("""
SELECT *
FROM auto_increment_demo
""")

for row in cursor.fetchall():
    print(row)

conn.close()