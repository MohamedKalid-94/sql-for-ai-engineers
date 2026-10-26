-- Lesson 3 of 11 | LEFT JOIN
-- LEFT JOIN keeps EVERY row of the left table (the one written first).
-- When there is no match on the right, the right-hand columns are NULL.
-- WHERE ... IS NULL on the right side finds the left rows with no match.

SELECT e.name, d.dept_name
FROM employees AS e
LEFT JOIN departments AS d ON d.dept_id = e.dept_id
ORDER BY e.name;

SELECT e.name
FROM employees AS e
LEFT JOIN departments AS d ON d.dept_id = e.dept_id
WHERE d.dept_id IS NULL;