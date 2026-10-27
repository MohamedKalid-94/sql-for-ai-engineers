-- Lesson 9 of 20 | NULL Values
-- NULL means no value at all. It is not zero and not an empty text.
-- Any maths with NULL gives NULL, and NULL = NULL is not true. Use IS NULL instead.
-- COUNT(*) counts rows, but COUNT(column) skips the NULLs.
-- In SQLite, NULLs sort first. NULLS LAST moves them to the end.

SELECT 100 + NULL AS sum_with_null,
       NULL = NULL AS null_equals_null,
       NULL IS NULL AS null_is_null;

SELECT name
FROM employees
WHERE phone IS NULL
ORDER BY name;

SELECT name
FROM employees
WHERE phone IS NOT NULL
ORDER BY name;

SELECT COUNT(*)            AS all_rows,
       COUNT(phone)        AS with_phone,
       COUNT(joining_date) AS with_date
FROM employees;

SELECT name, joining_date
FROM employees
ORDER BY joining_date, name;

SELECT name, joining_date
FROM employees
ORDER BY joining_date NULLS LAST, name;