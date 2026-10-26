-- Lesson 2 of 11 | INNER JOIN
-- INNER JOIN keeps only the rows that have a match on BOTH sides.
-- The word INNER is optional, so JOIN alone means INNER JOIN.
-- Maria has no department and Cloud has no employees, so neither of them appears.

SELECT e.name, e.salary, d.dept_name
FROM employees AS e
INNER JOIN departments AS d ON d.dept_id = e.dept_id
ORDER BY e.name;

SELECT
    (SELECT COUNT(*) FROM employees) AS employees_in_table,
    (SELECT COUNT(*)
     FROM employees AS e
     INNER JOIN departments AS d ON d.dept_id = e.dept_id) AS rows_after_inner_join;

SELECT e.name, d.dept_name
FROM employees AS e
INNER JOIN departments AS d ON d.dept_id = e.dept_id
WHERE d.dept_name = 'AI'
ORDER BY e.name;