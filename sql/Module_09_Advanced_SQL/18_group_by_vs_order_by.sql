-- GROUP BY

SELECT
department_id,
COUNT(*) AS total_employees
FROM employees
GROUP BY department_id;

-- ORDER BY

SELECT
emp_id,
name,
salary
FROM employees
ORDER BY salary DESC;