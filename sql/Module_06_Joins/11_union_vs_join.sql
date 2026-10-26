-- Lesson 11 of 11 | UNION vs JOIN
-- A JOIN puts two tables side by side. It makes the result WIDER, with more columns.
-- A UNION stacks two lists on top of each other. It makes the result LONGER, with more rows.
-- JOIN needs a column to match on. UNION needs the same number of columns on both sides.

SELECT e.name, d.dept_name
FROM employees AS e
JOIN departments AS d ON d.dept_id = e.dept_id
ORDER BY e.name;

SELECT name AS value
FROM employees
UNION
SELECT dept_name
FROM departments
ORDER BY 1;

SELECT
    (SELECT COUNT(*)
     FROM employees AS e
     JOIN departments AS d ON d.dept_id = e.dept_id) AS rows_from_join,
    (SELECT COUNT(*) FROM employees) + (SELECT COUNT(*) FROM departments) AS rows_from_union;