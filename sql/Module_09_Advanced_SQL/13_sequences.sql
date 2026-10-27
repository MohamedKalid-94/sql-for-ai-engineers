-- Lesson 13 of 20 | Sequences (SQLite equivalent)
-- Some databases have CREATE SEQUENCE, a counter that hands out the next number each time you ask.
-- SQLite has no sequences. Two equivalents:
-- 1) A small counter table. UPDATE adds the step, and RETURNING hands back the new number (needs SQLite 3.35).
-- 2) AUTOINCREMENT, which keeps its own counter in a hidden table called sqlite_sequence.

CREATE TABLE sequences (
    name          TEXT PRIMARY KEY,
    current_value INTEGER NOT NULL
);

INSERT INTO sequences (name, current_value) VALUES
    ('invoice_number', 1000),
    ('ticket_number',   100);

UPDATE sequences
SET current_value = current_value + :step
WHERE name = :name
RETURNING current_value;

SELECT name, current_value
FROM sequences
ORDER BY name;

CREATE TABLE tokens (
    token_no INTEGER PRIMARY KEY AUTOINCREMENT,
    holder   TEXT NOT NULL
);

INSERT INTO tokens (holder) VALUES ('Asha'), ('Ravi'), ('Meena');

SELECT name, seq
FROM sqlite_sequence;

SELECT token_no, holder
FROM tokens
ORDER BY token_no;