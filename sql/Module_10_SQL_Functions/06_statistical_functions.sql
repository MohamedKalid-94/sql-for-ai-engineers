-- Statistical Functions

SELECT
COUNT(*) AS total_employees,
AVG(salary) AS average_salary,
MIN(salary) AS minimum_salary,
MAX(salary) AS maximum_salary,
SUM(salary) AS total_salary
FROM employees;