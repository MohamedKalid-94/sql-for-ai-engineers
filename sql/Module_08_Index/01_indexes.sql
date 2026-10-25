-- SQL Indexes

-- Check employee data

SELECT *
FROM employees;


-- Searching without index

SELECT *
FROM employees
WHERE salary > 80000;