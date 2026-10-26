-- Lesson 7 of 7 | ORDER BY
-- ORDER BY sorts the result. ASC is smallest first (the default). DESC is largest first.
-- When two rows tie, the next column in the list decides.
-- NULL counts as the smallest value, so it comes first in ASC order.

SELECT name, salary
FROM employees
ORDER BY salary DESC, name ASC;

SELECT name, dept_id, salary
FROM employees
ORDER BY dept_id ASC, salary DESC;

SELECT name, joining_date
FROM employees
ORDER BY joining_date ASC, name ASC;

SELECT name, salary
FROM employees
ORDER BY salary DESC
LIMIT 3;