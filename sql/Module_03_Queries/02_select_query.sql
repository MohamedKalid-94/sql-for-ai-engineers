-- Lesson 2 of 7 | SELECT
-- SELECT reads rows. We choose the columns, choose the rows with WHERE,
-- and can calculate new values.
-- ORDER BY is Lesson 7. Here it only keeps the lines in a steady order.

SELECT *
FROM employees
ORDER BY emp_id
LIMIT 3;

SELECT name, salary
FROM employees
WHERE dept_id = 1
ORDER BY name;

SELECT name, salary, salary * 12 AS yearly_salary
FROM employees
WHERE emp_id = 101;

SELECT COUNT(*)    AS total_employees,
       MAX(salary) AS highest_salary,
       MIN(salary) AS lowest_salary
FROM employees;