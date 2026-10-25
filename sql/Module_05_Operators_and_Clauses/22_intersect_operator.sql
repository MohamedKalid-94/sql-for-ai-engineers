-- INTERSECT
-- Returns common records from both queries


SELECT name
FROM employees
WHERE salary > 70000

INTERSECT

SELECT name
FROM employees
WHERE dept_id = 1;