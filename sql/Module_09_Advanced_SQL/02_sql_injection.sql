-- SQL Injection

-- Unsafe Example
-- SELECT * FROM employees
-- WHERE name = '" + user_input + "';

-- Safe Example (Parameterized Query)

SELECT *
FROM employees
WHERE name = ?;