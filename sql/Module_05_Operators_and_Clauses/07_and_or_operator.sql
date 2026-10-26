-- Lesson 7 of 24 | AND and OR Operators
-- AND needs BOTH tests to pass. OR needs at least ONE test to pass.
-- Use brackets to say which test belongs together.

SELECT name, dept_id, salary
FROM employees
WHERE dept_id = 1 AND salary > 80000;

SELECT name, dept_id, salary
FROM employees
WHERE dept_id = 2 OR salary > 80000
ORDER BY name;

SELECT name, dept_id, salary
FROM employees
WHERE (dept_id = 1 OR dept_id = 5) AND salary > 72000
ORDER BY name;