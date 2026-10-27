-- Lesson 5 of 6 | ALTERNATE KEY
-- A table may have several columns that could each identify a row. These are candidate keys.
-- We pick ONE as the PRIMARY KEY. The others are called ALTERNATE keys.
-- In SQL an alternate key is written as UNIQUE NOT NULL.
-- Here member_id is the primary key, and username and email are alternate keys.

CREATE TABLE members (
    member_id INTEGER PRIMARY KEY,
    username  TEXT NOT NULL UNIQUE,
    email     TEXT NOT NULL UNIQUE,
    full_name TEXT NOT NULL
);

INSERT INTO members (username, email, full_name) VALUES
    ('kalid', 'kalid@gmail.com', 'Kalid M'),
    ('john',  'john@gmail.com',  'John D');

SELECT member_id, username, email, full_name
FROM members
WHERE member_id = 2;

SELECT member_id, username, email, full_name
FROM members
WHERE username = 'kalid';

SELECT member_id, username, email, full_name
FROM members
WHERE email = 'john@gmail.com';

-- REJECTED ON PURPOSE: the username kalid is taken.

INSERT INTO members (username, email, full_name)
VALUES ('kalid', 'new@gmail.com', 'Another Kalid');

-- REJECTED ON PURPOSE: the email john@gmail.com is taken.

INSERT INTO members (username, email, full_name)
VALUES ('maya', 'john@gmail.com', 'Maya P');