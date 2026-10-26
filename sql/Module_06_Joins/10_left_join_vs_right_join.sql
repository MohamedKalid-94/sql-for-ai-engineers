-- Lesson 10 of 11 | LEFT JOIN vs RIGHT JOIN
-- LEFT JOIN keeps every row of the FIRST table. RIGHT JOIN keeps every row of the SECOND table.
-- They are mirror images, so RIGHT JOIN a to b gives the same rows as LEFT JOIN b to a.
-- Most people write only LEFT JOIN and put the table they want to keep first.

SELECT e.name, d.dept_name
FROM employees AS e
LEFT JOIN departments AS d ON d.dept_id = e.dept_id
ORDER BY e.emp_id;

SELECT e.name, d.dept_name
FROM employees AS e
RIGHT JOIN departments AS d ON d.dept_id = e.dept_id
ORDER BY d.dept_id, e.name;

SELECT e.name, d.dept_name
FROM departments AS d
LEFT JOIN employees AS e ON e.dept_id = d.dept_id
ORDER BY d.dept_id, e.name;

SELECT 'employee without department' AS gap, e.name AS who
FROM employees AS e
LEFT JOIN departments AS d ON d.dept_id = e.dept_id
WHERE d.dept_id IS NULL
UNION ALL
SELECT 'department without employee', d.dept_name
FROM departments AS d
LEFT JOIN employees AS e ON e.dept_id = d.dept_id
WHERE e.emp_id IS NULL
ORDER BY 1;