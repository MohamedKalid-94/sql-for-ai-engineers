-- Lesson 10 of 24 | IN Operator
-- IN is a short way to write many OR tests on the same column.

SELECT name, dept_id
FROM employees
WHERE dept_id IN (1, 2)
ORDER BY dept_id, name;

SELECT name, dept_id
FROM employees
WHERE dept_id NOT IN (1, 2)
ORDER BY dept_id;