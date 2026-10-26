-- Lesson 16 of 24 | IS NULL
-- NULL means no value at all. It is not zero and not an empty text.
-- Comparing with = NULL never matches anything, because NULL is not equal to NULL.
-- The correct test is IS NULL.

SELECT emp_id, name, joining_date
FROM employees
WHERE joining_date IS NULL;

SELECT emp_id, name, joining_date
FROM employees
WHERE joining_date = NULL;