from config import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS documents(
id INTEGER PRIMARY KEY,
description TEXT,
image BLOB
)
""")

cursor.execute("DELETE FROM documents")

cursor.execute("""
INSERT INTO documents(description,image)
VALUES('AI Notes',X'89504E47')
""")

conn.commit()

print("TEXT & IMAGE Functions")
print("-"*25)

cursor.execute("""
SELECT id,
LENGTH(description),
LENGTH(image)
FROM documents
""")

for row in cursor.fetchall():
    print(row)

conn.close()