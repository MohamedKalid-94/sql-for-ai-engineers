-- Logical Functions

SELECT
emp_name,
salary,
CASE
    WHEN salary>=90000 THEN 'High'
    WHEN salary>=75000 THEN 'Medium'
    ELSE 'Low'
END AS salary_grade
FROM employees;

SELECT
COALESCE(phone,'Not Available')
FROM employees;

SELECT
IFNULL(joining_date,'Not Joined')
FROM employees;

SELECT
NULLIF(100,100);

SELECT
NULLIF(100,200);