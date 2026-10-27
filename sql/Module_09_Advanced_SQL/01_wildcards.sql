-- Lesson 1 of 20 | Wildcards
-- LIKE searches with a pattern. % matches any number of characters. _ matches exactly one.
-- LIKE ignores upper and lower case for English letters.
-- GLOB is the strict cousin: it is case sensitive, uses * and ? instead, and understands [A-D] ranges.
-- To search for a real % sign, put an escape character in front of it and say ESCAPE.

SELECT name
FROM employees
WHERE name LIKE 'S%';

SELECT name, email
FROM employees
WHERE email LIKE '%a@gmail.com'
ORDER BY name;

SELECT name
FROM employees
WHERE name LIKE '_a%'
ORDER BY name;

SELECT name
FROM employees
WHERE name GLOB '[A-D]*'
ORDER BY name;

SELECT name
FROM employees
WHERE name LIKE 's%';

SELECT name
FROM employees
WHERE name GLOB 's%';

SELECT label
FROM (SELECT '50% off' AS label UNION ALL SELECT '500 items')
WHERE label LIKE '50%'
ORDER BY label;

SELECT label
FROM (SELECT '50% off' AS label UNION ALL SELECT '500 items')
WHERE label LIKE '50\%%' ESCAPE '\'
ORDER BY label;