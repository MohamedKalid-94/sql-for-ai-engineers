from config import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.executescript("""
DROP TABLE IF EXISTS sequence_demo;

CREATE TABLE sequence_demo(
    id INTEGER PRIMARY KEY,
    name TEXT
);

INSERT INTO sequence_demo(name)
VALUES
('John'),
('Sara'),
('David');
""")

conn.commit()

print("Sequence Equivalent")
print("-------------------")

cursor.execute("""
SELECT *
FROM sequence_demo
""")

for row in cursor.fetchall():
    print(row)

conn.close()