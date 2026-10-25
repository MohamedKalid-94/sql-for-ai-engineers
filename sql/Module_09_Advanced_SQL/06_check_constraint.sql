-- CHECK Constraint

DROP TABLE IF EXISTS products;

CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    price REAL CHECK(price > 0)
);

INSERT INTO products VALUES
(1,'Laptop',65000);

SELECT * FROM products;