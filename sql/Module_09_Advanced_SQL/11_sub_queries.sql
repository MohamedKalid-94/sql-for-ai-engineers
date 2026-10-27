-- Lesson 11 of 20 | Sub Queries
-- A subquery is a SELECT placed inside another SELECT, in brackets.
-- It can give one value, a list of values, or a whole small table.
-- A correlated subquery looks at the current row of the outer query, so it re-runs for every row.

SELECT name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees)
ORDER BY salary DESC;

SELECT name, dept_id
FROM employees
WHERE dept_id IN (SELECT dept_id FROM departments WHERE dept_name IN ('AI', 'GenAI'))
ORDER BY name;

SELECT name,
       salary,
       ROUND(salary - (SELECT AVG(salary) FROM employees), 2) AS above_average
FROM employees
ORDER BY emp_id;

SELECT d.dept_name, t.avg_salary
FROM (SELECT dept_id, AVG(salary) AS avg_salary
      FROM employees
      GROUP BY dept_id) AS t
JOIN departments AS d ON d.dept_id = t.dept_id
WHERE t.avg_salary > 75000
ORDER BY t.avg_salary DESC;

SELECT e.name, e.dept_id, e.salary
FROM employees AS e
WHERE e.salary > (SELECT AVG(x.salary)
                  FROM employees AS x
                  WHERE x.dept_id = e.dept_id)
ORDER BY e.name;