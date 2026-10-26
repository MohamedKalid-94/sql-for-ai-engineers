-- Lesson 9 of 11 | UPDATE JOIN (SQLite equivalent)
-- MySQL writes UPDATE ... JOIN ... SET. SQLite writes UPDATE ... FROM.
-- UPDATE ... FROM needs SQLite 3.33 or newer.
-- Older SQLite versions use a subquery in the WHERE part, shown second.
-- We do not save the updates. A rollback at the end puts the salaries back.

SELECT e.name, d.dept_name, e.salary
FROM employees AS e
JOIN departments AS d ON d.dept_id = e.dept_id
WHERE d.dept_name IN ('AI', 'Python')
ORDER BY e.name;

UPDATE employees
SET salary = ROUND(employees.salary * 1.10, 2)
FROM departments AS d
WHERE d.dept_id = employees.dept_id
  AND d.dept_name = 'AI';

UPDATE employees
SET salary = salary + 1000
WHERE dept_id = (SELECT dept_id FROM departments WHERE dept_name = 'Python');