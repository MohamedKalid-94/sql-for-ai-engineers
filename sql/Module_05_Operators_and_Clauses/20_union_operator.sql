-- Lesson 20 of 24 | UNION Operator
-- UNION stacks the results of two SELECT commands into one list.
-- Both SELECTs need the same number of columns. Repeated rows are removed.

SELECT name FROM employees
UNION
SELECT name FROM contractors
ORDER BY name;