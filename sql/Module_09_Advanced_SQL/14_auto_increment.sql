-- Lesson 14 of 20 | AUTO INCREMENT
-- In SQLite, a column typed INTEGER PRIMARY KEY fills itself in with the next free number.
-- It takes the biggest number now in the table and adds 1.
-- So if we delete the biggest row, the next new row REUSES that number.
-- Adding the word AUTOINCREMENT keeps a hidden counter, so a number is never used twice.

CREATE TABLE plain_ids (
    id    INTEGER PRIMARY KEY,
    label TEXT NOT NULL
);

CREATE TABLE safe_ids (
    id    INTEGER PRIMARY KEY AUTOINCREMENT,
    label TEXT NOT NULL
);

INSERT INTO plain_ids (label) VALUES ('first'), ('second'), ('third');

INSERT INTO safe_ids (label) VALUES ('first'), ('second'), ('third');

DELETE FROM plain_ids WHERE id = 3;

DELETE FROM safe_ids WHERE id = 3;

INSERT INTO plain_ids (label) VALUES ('new');

INSERT INTO safe_ids (label) VALUES ('new');

SELECT id, label
FROM plain_ids
ORDER BY id;

SELECT id, label
FROM safe_ids
ORDER BY id;

SELECT name, seq
FROM sqlite_sequence
ORDER BY name;