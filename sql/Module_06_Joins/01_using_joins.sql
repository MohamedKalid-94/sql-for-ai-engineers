-- Lesson 1 of 11 | USING JOIN
-- A JOIN glues two tables together side by side, using a column they share.
-- Both employees and departments have a column called dept_id.
-- So JOIN ... USING (dept_id) is a short way to write ON e.dept_id = d.dept_id.
-- Only matching rows survive. Maria has no department, so she is missing here.

SELECT name, dept_name
FROM employees
JOIN departments USING (dept_id)
ORDER BY name;

SELECT e.name, d.dept_name
FROM employees AS e
JOIN departments AS d ON d.dept_id = e.dept_id
ORDER BY e.name;