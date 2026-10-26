-- Lesson 13 of 24 | CASE Expression
-- CASE is an if / else inside a query. It picks the first WHEN that is true.
-- ELSE is the answer when no WHEN is true.

SELECT name,
       salary,
       CASE
           WHEN salary >= 85000 THEN 'High'
           WHEN salary >= 72000 THEN 'Medium'
           ELSE 'Low'
       END AS salary_band
FROM employees
ORDER BY salary DESC;

SELECT name,
       CASE is_active
           WHEN 1 THEN 'Active'
           ELSE 'Inactive'
       END AS status
FROM employees
ORDER BY emp_id;