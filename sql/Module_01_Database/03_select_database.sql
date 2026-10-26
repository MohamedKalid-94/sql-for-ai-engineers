-- Lesson 3 of 6 | Select Database
-- SQLite has no USE command.
-- Instead: open the file you want, or ATTACH a second database
-- and write database_name.table_name to say which notebook you mean.

ATTACH DATABASE ':memory:' AS scratch;

CREATE TABLE scratch.notes (
    note_id INTEGER PRIMARY KEY,
    note    TEXT NOT NULL
);

INSERT INTO scratch.notes (note)
VALUES ('I live in the scratch database');

SELECT purpose FROM main.database_info;

SELECT note FROM scratch.notes;