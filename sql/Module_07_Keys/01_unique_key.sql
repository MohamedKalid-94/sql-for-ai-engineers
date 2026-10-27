-- Lesson 1 of 6 | UNIQUE Key
-- A UNIQUE key is a rule: no two rows may hold the same value in this column.
-- Think of a login name. Two people cannot share one.
-- A table can have many UNIQUE keys. Here both username and email are UNIQUE.
-- NULL means no value at all, so SQLite allows many NULLs in a UNIQUE column.

CREATE TABLE accounts (
    account_id INTEGER PRIMARY KEY,
    username   TEXT NOT NULL UNIQUE,
    email      TEXT UNIQUE
);

INSERT INTO accounts (username, email) VALUES
    ('kalid', 'kalid@gmail.com'),
    ('john',  'john@gmail.com');

-- REJECTED ON PURPOSE: the email john@gmail.com is already taken.

INSERT INTO accounts (username, email)
VALUES ('sara', 'john@gmail.com');

INSERT INTO accounts (username, email) VALUES ('guest1', NULL);

INSERT INTO accounts (username, email) VALUES ('guest2', NULL);

SELECT account_id, username, email
FROM accounts
ORDER BY account_id;