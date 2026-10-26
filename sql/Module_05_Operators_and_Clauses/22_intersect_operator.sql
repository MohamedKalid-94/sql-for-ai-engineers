-- Lesson 22 of 24 | INTERSECT Operator
-- INTERSECT keeps only the rows that appear in BOTH results.

SELECT name FROM employees
INTERSECT
SELECT name FROM contractors;