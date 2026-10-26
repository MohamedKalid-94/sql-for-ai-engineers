-- Lesson 6 of 11 | FULL JOIN
-- FULL JOIN keeps EVERY row from BOTH tables.
-- Matches are joined, and unmatched rows get NULL on the missing side.
-- SQLite understands FULL JOIN from version 3.39 onwards.
-- On any SQLite version, a LEFT JOIN plus the unmatched rows of the other side
-- (joined with UNION ALL) gives the same answer.

SELECT e.name, d.dept_name
FROM employees AS e
FULL JOIN departments AS d ON d.dept_id = e.dept_id
ORDER BY d.dept_name, e.name;

SELECT e.name, d.dept_name
FROM employees AS e
LEFT JOIN departments AS d ON d.dept_id = e.dept_id
UNION ALL
SELECT e.name, d.dept_name
FROM departments AS d
LEFT JOIN employees AS e ON e.dept_id = d.dept_id
WHERE e.emp_id IS NULL
ORDER BY 2, 1;