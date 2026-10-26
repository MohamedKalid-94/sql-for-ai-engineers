-- Lesson 6 of 24 | HAVING Clause
-- WHERE filters single rows BEFORE grouping.
-- HAVING filters whole groups AFTER grouping, so it can use COUNT, AVG and SUM.

SELECT dept_id, AVG(salary) AS avg_salary
FROM employees
GROUP BY dept_id
HAVING AVG(salary) > 80000
ORDER BY dept_id;

SELECT dept_id, COUNT(*) AS employee_count
FROM employees
GROUP BY dept_id
HAVING COUNT(*) > 1;