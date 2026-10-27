-- Lesson 3 of 7 | Drop Index
-- DROP INDEX removes the lookup list. The table and its data are never touched.
-- Queries still give the right answer, but SQLite goes back to reading every row.
-- IF EXISTS makes the command safe when the index is already gone.

EXPLAIN QUERY PLAN
SELECT pupil_id, marks
FROM pupils
WHERE name = 'Pupil 500';

DROP INDEX idx_pupils_name;

EXPLAIN QUERY PLAN
SELECT pupil_id, marks
FROM pupils
WHERE name = 'Pupil 500';

DROP INDEX IF EXISTS idx_pupils_name;

-- The next statement is REJECTED ON PURPOSE.
-- The index is already gone, so there is nothing to drop.

DROP INDEX idx_pupils_name;

SELECT COUNT(*) AS pupils_still_in_table
FROM pupils;