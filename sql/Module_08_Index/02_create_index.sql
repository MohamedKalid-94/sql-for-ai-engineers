-- Lesson 2 of 7 | Create Index
-- CREATE INDEX builds a sorted lookup list for one column.
-- We make three indexes on pupils, for marks, city and name.
-- The same query then gives the same answer, but SQLite SEARCHES instead of scanning every row.
-- The cost of an index is disk space, and every INSERT and UPDATE must keep it up to date.

EXPLAIN QUERY PLAN
SELECT pupil_id, name
FROM pupils
WHERE marks = 77;

CREATE INDEX idx_pupils_marks ON pupils (marks);

CREATE INDEX idx_pupils_city ON pupils (city);

CREATE INDEX idx_pupils_name ON pupils (name);

EXPLAIN QUERY PLAN
SELECT pupil_id, name
FROM pupils
WHERE marks = 77;

SELECT COUNT(*) AS pupils_with_77_marks
FROM pupils
WHERE marks = 77;