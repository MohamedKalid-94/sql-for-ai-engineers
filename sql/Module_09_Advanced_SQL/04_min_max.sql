-- Lesson 4 of 20 | MIN and MAX
-- MIN finds the smallest value and MAX finds the largest.
-- They work on numbers, text (A is smallest) and dates (oldest is smallest).
-- NULL values are ignored. On an empty set, both give NULL.

SELECT MIN(salary) AS lowest_salary,
       MAX(salary) AS highest_salary
FROM employees;

SELECT name, salary
FROM employees
WHERE salary = (SELECT MAX(salary) FROM employees);

SELECT dept_id,
       MIN(salary) AS lowest,
       MAX(salary) AS highest
FROM employees
GROUP BY dept_id
ORDER BY dept_id;

SELECT MIN(name)         AS first_name,
       MAX(name)         AS last_name,
       MIN(joining_date) AS earliest_date,
       MAX(joining_date) AS latest_date
FROM employees;

SELECT MAX(salary) AS highest_in_cloud
FROM employees
WHERE dept_id = 4;