-- Lesson 15 of 24 | NOT EQUAL Operator
-- Two spellings mean the same thing: <> and !=
-- Careful: a NULL value is never "not equal" to anything, so those rows are skipped.

SELECT name, dept_id
FROM employees
WHERE dept_id <> 1
ORDER BY name;

SELECT name, dept_id
FROM employees
WHERE dept_id != 1
ORDER BY name;

SELECT name, joining_date
FROM employees
WHERE joining_date <> '2025-01-15'
ORDER BY name;