-- AND Operator

SELECT *
FROM employees
WHERE salary > 70000
AND dept_id = 1;


-- OR Operator

SELECT *
FROM employees
WHERE dept_id = 1
OR dept_id = 2;