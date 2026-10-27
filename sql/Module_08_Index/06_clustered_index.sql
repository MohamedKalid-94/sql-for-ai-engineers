-- Lesson 6 of 7 | Clustered Index (SQLite equivalent)
-- In SQL Server a clustered index decides how the rows of a table are physically sorted.
-- A table can have only one, because rows can be sorted in only one way.
-- SQLite has no CREATE CLUSTERED INDEX, but it has two equivalents.
-- 1) An ordinary table is already stored sorted by its hidden rowid. INTEGER PRIMARY KEY is that rowid.
-- 2) A WITHOUT ROWID table is stored sorted by its PRIMARY KEY, whatever type that key is.
-- Below we copy pupils into a WITHOUT ROWID table that is sorted by roll_code.

CREATE TABLE pupils_by_code (
    roll_code TEXT PRIMARY KEY,
    pupil_id  INTEGER NOT NULL,
    name      TEXT NOT NULL,
    city      TEXT NOT NULL,
    marks     INTEGER NOT NULL
) WITHOUT ROWID;

INSERT INTO pupils_by_code (roll_code, pupil_id, name, city, marks)
SELECT roll_code, pupil_id, name, city, marks
FROM pupils;

SELECT COUNT(*) AS rows_copied
FROM pupils_by_code;

EXPLAIN QUERY PLAN
SELECT name
FROM pupils
WHERE pupil_id = 500;

EXPLAIN QUERY PLAN
SELECT pupil_id, name
FROM pupils_by_code
WHERE roll_code = 'R00500';

SELECT roll_code, name
FROM pupils_by_code
WHERE roll_code BETWEEN 'R00010' AND 'R00013'
ORDER BY roll_code;

EXPLAIN QUERY PLAN
SELECT roll_code, name
FROM pupils_by_code
WHERE roll_code BETWEEN 'R00010' AND 'R00013'
ORDER BY roll_code;