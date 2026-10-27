-- Lesson 19 of 20 | IN vs EXISTS
-- IN checks whether a value is found in a list that a subquery builds.
-- EXISTS checks whether the subquery finds at least one row, and it stops at the first one.
-- For plain questions they give the same answer.
-- THE TRAP: if the list built for NOT IN contains even one NULL, NOT IN returns NO rows at all.
-- NOT EXISTS has no such problem, so it is the safer choice.

SELECT dept_id, dept_name
FROM departments
WHERE dept_id IN (SELECT dept_id FROM employees)
ORDER BY dept_id;

SELECT d.dept_id, d.dept_name
FROM departments AS d
WHERE EXISTS (SELECT 1 FROM employees AS e WHERE e.dept_id = d.dept_id)
ORDER BY d.dept_id;

SELECT dept_id, dept_name
FROM departments
WHERE dept_id NOT IN (SELECT dept_id FROM employees)
ORDER BY dept_id;

SELECT d.dept_id, d.dept_name
FROM departments AS d
WHERE NOT EXISTS (SELECT 1 FROM employees AS e WHERE e.dept_id = d.dept_id)
ORDER BY d.dept_id;

SELECT name
FROM employees
WHERE emp_id NOT IN (SELECT manager_id FROM employees)
ORDER BY name;

SELECT name
FROM employees AS e
WHERE NOT EXISTS (SELECT 1 FROM employees AS x WHERE x.manager_id = e.emp_id)
ORDER BY name;