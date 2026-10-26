-- Lesson 19 of 24 | BETWEEN Operator
-- BETWEEN a AND b keeps values from a to b. BOTH ends are included.
-- Dates written as year-month-day text sort and compare correctly.

SELECT name, salary
FROM employees
WHERE salary BETWEEN 72000 AND 85000
ORDER BY salary;

SELECT name, joining_date
FROM employees
WHERE joining_date BETWEEN '2025-01-01' AND '2025-02-28'
ORDER BY joining_date;

SELECT name, salary
FROM employees
WHERE salary NOT BETWEEN 72000 AND 85000
ORDER BY salary;