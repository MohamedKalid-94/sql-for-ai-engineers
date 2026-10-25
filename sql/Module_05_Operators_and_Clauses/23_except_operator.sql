-- EXCEPT
-- Returns records from first query
-- which are not present in second query


SELECT name
FROM employees

EXCEPT

SELECT name
FROM employees
WHERE dept_id = 1;