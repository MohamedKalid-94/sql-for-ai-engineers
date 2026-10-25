-- UNION removes duplicates

SELECT dept_id
FROM employees
WHERE dept_id IN (1,2)

UNION

SELECT dept_id
FROM employees
WHERE dept_id IN (2,3);



-- UNION ALL keeps duplicates

SELECT dept_id
FROM employees
WHERE dept_id IN (1,2)

UNION ALL

SELECT dept_id
FROM employees
WHERE dept_id IN (2,3);