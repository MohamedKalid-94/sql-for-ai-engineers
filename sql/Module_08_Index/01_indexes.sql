-- Lesson 1 of 7 | SQL Indexes
-- An index is like the index at the back of a book.
-- Without it, finding one topic means reading every page. With it, you jump straight to the right page.
-- SQLite can explain how it plans to answer a query, using EXPLAIN QUERY PLAN.
-- SCAN means read every row. SEARCH means jump straight to the matching rows.
-- The PRIMARY KEY of a table is already a built-in fast lookup.
-- Below, no index exists on marks yet.

SELECT COUNT(*) AS pupils_with_77_marks
FROM pupils
WHERE marks = 77;

EXPLAIN QUERY PLAN
SELECT pupil_id, name
FROM pupils
WHERE marks = 77;

EXPLAIN QUERY PLAN
SELECT pupil_id, name
FROM pupils
WHERE pupil_id = 500;