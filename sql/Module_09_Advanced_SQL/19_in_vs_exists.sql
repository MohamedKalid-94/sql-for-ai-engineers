-- IN Operator

SELECT *
FROM employees
WHERE department_id IN
(
    SELECT department_id
    FROM employees
    WHERE salary > 80000
);

-- EXISTS Operator

SELECT *
FROM employees e
WHERE EXISTS
(
    SELECT 1
    FROM employees x
    WHERE x.department_id = e.department_id
      AND x.salary > 80000
);