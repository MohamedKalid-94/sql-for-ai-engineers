-- Lesson 18 of 20 | GROUP BY vs ORDER BY
-- ORDER BY only SORTS the rows. Every row stays, just in a new order.
-- GROUP BY FOLDS rows into groups, giving one row per group, usually with COUNT, SUM or AVG.
-- They can work together: group first, then sort the groups.

SELECT dept_id, name, salary
FROM employees
ORDER BY dept_id, salary DESC;

SELECT dept_id,
       COUNT(*)                AS staff,
       SUM(salary)             AS total_salary,
       ROUND(AVG(salary), 2)   AS avg_salary
FROM employees
GROUP BY dept_id
ORDER BY dept_id;

SELECT dept_id,
       SUM(salary) AS total_salary
FROM employees
GROUP BY dept_id
ORDER BY total_salary DESC;

SELECT (SELECT COUNT(*) FROM employees)                AS rows_with_order_by,
       (SELECT COUNT(DISTINCT dept_id) FROM employees) AS rows_with_group_by;

SELECT d.dept_name,
       COUNT(e.emp_id) AS staff
FROM departments AS d
LEFT JOIN employees AS e ON e.dept_id = d.dept_id
GROUP BY d.dept_id
ORDER BY d.dept_id;