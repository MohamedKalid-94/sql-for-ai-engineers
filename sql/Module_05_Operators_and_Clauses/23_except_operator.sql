-- Lesson 23 of 24 | EXCEPT Operator
-- EXCEPT keeps the rows of the first result that are NOT in the second result.
-- Order matters: employees EXCEPT contractors is not the same as contractors EXCEPT employees.

SELECT name FROM employees
EXCEPT
SELECT name FROM contractors
ORDER BY name;

SELECT name FROM contractors
EXCEPT
SELECT name FROM employees
ORDER BY name;