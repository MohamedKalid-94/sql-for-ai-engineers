-- Lesson 1 of 4 | Create Views
-- A view is a saved question. It stores the SELECT, not the data.
-- Every time we read the view, SQLite runs the question again on the real table,
-- so the view always shows the latest data.

CREATE VIEW high_salary_employees AS
SELECT emp_id, name, salary, dept_id
FROM employees
WHERE salary >= 80000;

CREATE VIEW employee_details AS
SELECT e.emp_id, e.name, e.salary, d.dept_name
FROM employees AS e
JOIN departments AS d ON d.dept_id = e.dept_id;

SELECT name
FROM sqlite_master
WHERE type = 'view'
ORDER BY name;

SELECT emp_id, name, salary
FROM high_salary_employees
ORDER BY emp_id;

SELECT emp_id, name, dept_name
FROM employee_details
ORDER BY emp_id;

-- Change the TABLE and watch the VIEW follow (we undo it with a rollback afterwards)

UPDATE employees
SET salary = 95000
WHERE emp_id = 103;