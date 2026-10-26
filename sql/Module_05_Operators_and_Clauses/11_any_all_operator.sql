-- Lesson 11 of 24 | ANY and ALL Operators
-- SQLite has no ANY and ALL. MIN and MAX in a subquery do the same job.
-- Above ANY of a list means above the SMALLEST value in the list.
-- Above ALL of a list means above the LARGEST value in the list.

SELECT name, salary
FROM employees
WHERE salary > (SELECT MIN(salary) FROM employees WHERE dept_id IN (3, 5))
ORDER BY salary;

SELECT name, salary
FROM employees
WHERE salary > (SELECT MAX(salary) FROM employees WHERE dept_id IN (3, 5))
ORDER BY salary;