-- HAVING Clause
-- Filter grouped data

SELECT
    dept_id,
    COUNT(*) AS employee_count
FROM employees
GROUP BY dept_id
HAVING COUNT(*) > 1;