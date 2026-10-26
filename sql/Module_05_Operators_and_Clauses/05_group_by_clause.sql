-- Lesson 5 of 24 | GROUP BY Clause
-- GROUP BY puts rows into groups, such as one group for each department.
-- An aggregate such as COUNT, AVG or SUM then works on each group separately.

SELECT dept_id,
       COUNT(*)    AS employee_count,
       AVG(salary) AS avg_salary
FROM employees
GROUP BY dept_id
ORDER BY dept_id;

SELECT dept_id,
       SUM(salary) AS total_salary
FROM employees
GROUP BY dept_id
ORDER BY dept_id;