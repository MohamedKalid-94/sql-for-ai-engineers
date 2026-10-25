-- COALESCE

SELECT
name,
COALESCE(phone,'Not Available')
FROM employees;

-- IFNULL

SELECT
name,
IFNULL(joining_date,'Not Joined')
FROM employees;

-- NULLIF

SELECT
NULLIF(75000,75000);

SELECT
NULLIF(75000,90000);