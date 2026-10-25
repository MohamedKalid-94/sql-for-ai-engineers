-- NULL Values

SELECT *
FROM employees
WHERE phone IS NULL;

SELECT *
FROM employees
WHERE phone IS NOT NULL;