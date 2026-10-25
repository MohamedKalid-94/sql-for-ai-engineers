-- Wildcards

SELECT *
FROM employees
WHERE name LIKE 'S%';

SELECT *
FROM employees
WHERE email LIKE '%gmail%';

SELECT *
FROM employees
WHERE name LIKE '_o%';