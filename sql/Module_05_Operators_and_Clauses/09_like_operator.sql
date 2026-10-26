-- Lesson 9 of 24 | LIKE Operator
-- LIKE searches for a pattern. % matches any number of characters. _ matches exactly one.
-- In SQLite, LIKE ignores upper and lower case for English letters.

SELECT name
FROM employees
WHERE name LIKE 'S%';

SELECT name
FROM employees
WHERE name LIKE '%a'
ORDER BY name;

SELECT name
FROM employees
WHERE name LIKE '____'
ORDER BY name;

SELECT name
FROM employees
WHERE name LIKE '%ri%';

SELECT name
FROM employees
WHERE name LIKE 's%';