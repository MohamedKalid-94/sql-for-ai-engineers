-- Lesson 17 of 20 | Common Table Expression (CTE)
-- A CTE gives a name to a small query, written with WITH, so the main query can use that name.
-- It makes long queries easier to read, like naming a step in a recipe.
-- A RECURSIVE CTE calls itself again and again, which is how we count or walk up and down a family tree.
-- Here manager_id points to the boss of each employee, so the tree is John, then Sara and David, then Priya and Alex.

WITH high_earners AS (
    SELECT emp_id, name, salary, dept_id
    FROM employees
    WHERE salary >= 80000
)
SELECT name, salary
FROM high_earners
ORDER BY salary DESC;

WITH dept_avg AS (
    SELECT dept_id, AVG(salary) AS avg_salary
    FROM employees
    GROUP BY dept_id
)
SELECT e.name, e.salary, d.dept_name, ROUND(a.avg_salary, 2) AS dept_average
FROM employees AS e
JOIN dept_avg AS a    ON a.dept_id = e.dept_id
JOIN departments AS d ON d.dept_id = e.dept_id
ORDER BY e.emp_id;

WITH RECURSIVE counter(n) AS (
    SELECT 1
    UNION ALL
    SELECT n + 1 FROM counter WHERE n < 5
)
SELECT n
FROM counter;

WITH RECURSIVE org_chart(emp_id, name, level, path) AS (
    SELECT emp_id, name, 0, name
    FROM employees
    WHERE manager_id IS NULL
    UNION ALL
    SELECT e.emp_id, e.name, o.level + 1, o.path || ' > ' || e.name
    FROM employees AS e
    JOIN org_chart AS o ON e.manager_id = o.emp_id
)
SELECT level, name, path
FROM org_chart
ORDER BY path;