-- Lesson 12 of 24 | EXISTS Operator
-- EXISTS asks one yes or no question: does the inner query find at least one row?
-- It is a good way to ask "has this department got any employees?"

SELECT d.dept_id, d.dept_name
FROM departments AS d
WHERE EXISTS (SELECT 1 FROM employees AS e WHERE e.dept_id = d.dept_id)
ORDER BY d.dept_id;

SELECT d.dept_id, d.dept_name
FROM departments AS d
WHERE NOT EXISTS (SELECT 1 FROM employees AS e WHERE e.dept_id = d.dept_id);