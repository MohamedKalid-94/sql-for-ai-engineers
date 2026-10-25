-- LIKE Operator

-- Names starting with S

SELECT *
FROM employees
WHERE name LIKE 'S%';


-- Names ending with a

SELECT *
FROM employees
WHERE name LIKE '%a';