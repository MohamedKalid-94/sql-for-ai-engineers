-- Lesson 6 of 20 | CHECK Constraint
-- A CHECK constraint is a rule that every value must pass, such as price above zero.
-- A CHECK can sit on one column, or on the whole row (the name rule below).
-- The database refuses any INSERT or UPDATE that breaks the rule.

CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    name       TEXT NOT NULL,
    price      REAL NOT NULL CHECK (price > 0),
    stock      INTEGER NOT NULL DEFAULT 0 CHECK (stock >= 0),
    CHECK (length(name) >= 3)
);

INSERT INTO products (name, price, stock) VALUES
    ('Laptop', 65000, 5),
    ('Mouse',    500, 40);

SELECT product_id, name, price, stock
FROM products
ORDER BY product_id;

-- The next four statements are REJECTED ON PURPOSE.
-- Each one breaks a different rule.

INSERT INTO products (name, price, stock) VALUES ('Free pen', 0, 10);

INSERT INTO products (name, price, stock) VALUES ('Phone', 30000, -1);

INSERT INTO products (name, price, stock) VALUES ('TV', 20000, 2);

UPDATE products SET price = -5 WHERE product_id = 1;