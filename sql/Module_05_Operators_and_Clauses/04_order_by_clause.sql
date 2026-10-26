-- Lesson 4 of 24 | ORDER BY Clause
-- ORDER BY sorts the result. ASC is smallest first (the default). DESC is largest first.
-- When two rows tie, the next column in the list decides.

SELECT name, salary
FROM employees
ORDER BY salary DESC;

SELECT dept_id, name
FROM employees
ORDER BY dept_id ASC, name ASC;