-- Lesson 17 of 24 | IS NOT NULL
-- IS NOT NULL keeps the rows that do have a value.
-- COUNT(*) counts every row, but COUNT(column) skips the NULLs.

SELECT emp_id, name, joining_date
FROM employees
WHERE joining_date IS NOT NULL
ORDER BY joining_date;

SELECT COUNT(*)            AS all_employees,
       COUNT(joining_date) AS with_joining_date
FROM employees;