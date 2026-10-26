-- Lesson 24 of 24 | Aliases
-- An alias is a short or friendly nickname, given with the word AS.
-- A column alias renames a result column. A table alias shortens a table name.
-- The nickname exists only for this one query. Nothing is renamed in the database.

SELECT e.name                    AS employee,
       d.dept_name               AS department,
       ROUND(e.salary * 1.10, 2) AS salary_after_raise
FROM employees   AS e
JOIN departments AS d ON d.dept_id = e.dept_id
ORDER BY e.name;

SELECT name,
       salary * 12 AS yearly_salary
FROM employees
ORDER BY yearly_salary DESC
LIMIT 2;

SELECT COUNT(*) AS total_staff
FROM employees AS staff;