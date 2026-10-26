-- Lesson 14 of 24 | NOT Operator
-- NOT turns a test upside down. True becomes false and false becomes true.

SELECT name, dept_id
FROM employees
WHERE NOT dept_id = 1
ORDER BY name;

SELECT name
FROM employees
WHERE name NOT LIKE 'S%'
ORDER BY name;