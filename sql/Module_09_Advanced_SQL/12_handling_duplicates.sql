-- Lesson 12 of 20 | Handling Duplicates
-- Duplicates are rows that repeat the same information.
-- Find them with GROUP BY and HAVING COUNT(*) > 1.
-- Remove them by keeping the first row of each group (the smallest id) and deleting the rest.
-- Prevent them for good with a UNIQUE index.
-- INSERT OR IGNORE skips a bad row quietly instead of raising an error.

CREATE TABLE signups (
    signup_id INTEGER PRIMARY KEY,
    name      TEXT NOT NULL,
    email     TEXT NOT NULL
);

INSERT INTO signups (name, email) VALUES
    ('Asha',  'asha@gmail.com'),
    ('Ravi',  'ravi@gmail.com'),
    ('Asha',  'asha@gmail.com'),
    ('Meena', 'meena@gmail.com'),
    ('Ravi',  'ravi@gmail.com'),
    ('Asha',  'asha@gmail.com');

SELECT signup_id, name, email
FROM signups
ORDER BY signup_id;

SELECT email, COUNT(*) AS times
FROM signups
GROUP BY email
HAVING COUNT(*) > 1
ORDER BY email;

SELECT DISTINCT name, email
FROM signups
ORDER BY name;

SELECT signup_id, name
FROM signups
WHERE signup_id NOT IN (SELECT MIN(signup_id) FROM signups GROUP BY email)
ORDER BY signup_id;

DELETE FROM signups
WHERE signup_id NOT IN (SELECT MIN(signup_id) FROM signups GROUP BY email);

CREATE UNIQUE INDEX idx_signups_email ON signups (email);

-- The next statement is REJECTED ON PURPOSE.
-- The email asha@gmail.com is already in the table.

INSERT INTO signups (name, email) VALUES ('Asha again', 'asha@gmail.com');

INSERT OR IGNORE INTO signups (name, email) VALUES ('Asha again', 'asha@gmail.com');

SELECT signup_id, name, email
FROM signups
ORDER BY signup_id;