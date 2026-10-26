-- Lesson 4 of 10 | Truncate Table
-- SQLite has no TRUNCATE TABLE command. DELETE FROM table with no WHERE does the same job.
-- AUTOINCREMENT remembers the last id in a hidden table called sqlite_sequence.
-- To start again from 1, we also clear that memory.

CREATE TABLE log_entries (
    log_id  INTEGER PRIMARY KEY AUTOINCREMENT,
    message TEXT NOT NULL
);

INSERT INTO log_entries (message) VALUES ('first'), ('second'), ('third');

SELECT COUNT(*) AS rows_in_table FROM log_entries;

-- TRUNCATE equivalent: remove every row

DELETE FROM log_entries;

INSERT INTO log_entries (message) VALUES ('new row');

SELECT log_id, message FROM log_entries;

-- Reset the id counter (the hidden memory)

DELETE FROM sqlite_sequence WHERE name = 'log_entries';