-- Lesson 5 of 11 | CROSS JOIN
-- CROSS JOIN pairs EVERY row of one table with EVERY row of the other. There is no ON.
-- 6 employees x 5 departments = 30 pairs, so we show only two employees.
-- Useful for making a grid, such as a schedule of every department and every shift.

SELECT e.name, d.dept_name
FROM employees AS e
CROSS JOIN departments AS d
WHERE e.emp_id IN (101, 102)
ORDER BY e.name, d.dept_id;

SELECT COUNT(*) AS all_combinations
FROM employees
CROSS JOIN departments;

SELECT d.dept_name, s.shift
FROM departments AS d
CROSS JOIN (SELECT 'Morning' AS shift UNION ALL SELECT 'Evening') AS s
WHERE d.dept_id <= 2
ORDER BY d.dept_id, s.shift;