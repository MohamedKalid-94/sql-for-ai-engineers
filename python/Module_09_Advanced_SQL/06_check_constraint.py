from config import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.executescript("""
DROP TABLE IF EXISTS products;

CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    price REAL CHECK(price > 0)
);

INSERT INTO products VALUES
(1,'Laptop',65000);
""")

conn.commit()

print("CHECK Constraint Result")
print("-----------------------")

cursor.execute("SELECT * FROM products")

for row in cursor.fetchall():
    print(row)

conn.close()