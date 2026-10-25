-- UNION Operator
-- Combines results from two SELECT queries
-- Removes duplicate records


SELECT name
FROM employees
WHERE dept_id = 1

UNION

SELECT name
FROM employees
WHERE dept_id = 2;