-- EXISTS Operator

SELECT *
FROM employees e
WHERE EXISTS
(
    SELECT 1
    FROM departments d
    WHERE d.dept_id = e.dept_id
);