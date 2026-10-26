-- Lesson 2 of 24 | TOP / LIMIT Clause
-- SQL Server writes SELECT TOP 3. SQLite writes LIMIT 3 at the end.
-- OFFSET skips rows first, which is how page 2 of a list is made.

SELECT name, salary
FROM employees
ORDER BY salary DESC
LIMIT 3;

SELECT name, salary
FROM employees
ORDER BY salary DESC
LIMIT 2 OFFSET 2;