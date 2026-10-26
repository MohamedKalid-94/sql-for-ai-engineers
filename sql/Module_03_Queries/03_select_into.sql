-- Lesson 3 of 7 | SELECT INTO (SQLite equivalent)
-- SQL Server writes: SELECT columns INTO new_table FROM old_table
-- SQLite writes: CREATE TABLE new_table AS SELECT columns FROM old_table
-- The new table is a snapshot. It is not linked to the original afterwards.

CREATE TABLE high_earners AS
SELECT emp_id, name, salary
FROM employees
WHERE salary >= 80000;

SELECT emp_id, name, salary
FROM high_earners
ORDER BY emp_id;

PRAGMA table_info(high_earners);