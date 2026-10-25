-- GROUP BY Clause
-- Count employees department wise

SELECT
    dept_id,
    COUNT(*) AS employee_count
FROM employees
GROUP BY dept_id;