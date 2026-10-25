-- ANY Equivalent
-- Employees earning more than at least one employee in department 3

SELECT *
FROM employees
WHERE salary >
(
    SELECT MIN(salary)
    FROM employees
    WHERE dept_id = 3
);


-- ALL Equivalent
-- Employees earning more than every employee in department 3

SELECT *
FROM employees
WHERE salary >
(
    SELECT MAX(salary)
    FROM employees
    WHERE dept_id = 3
);