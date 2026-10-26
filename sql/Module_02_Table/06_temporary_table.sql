-- Lesson 6 of 10 | Temporary Table
-- A temporary table is rough paper: it exists only while this connection is open.
-- When the connection closes, it disappears and is never saved in the database file.

CREATE TEMP TABLE temp_high_earners AS
SELECT name, salary
FROM employees
WHERE salary > 70000;

SELECT name, salary
FROM temp_high_earners
ORDER BY salary DESC;

SELECT name
FROM sqlite_temp_master
WHERE type = 'table';