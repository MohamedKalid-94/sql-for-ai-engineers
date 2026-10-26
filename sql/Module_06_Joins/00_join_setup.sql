-- Lesson 0 of 11 | Join Setup
-- The shared setup gave this module 5 employees and 5 departments.
-- Every employee has a department, so most joins would look the same.
-- We add Maria, who has NO department yet, so the join types can show their differences.
-- Department 4 (Cloud) already has no employees, which helps too.

INSERT INTO employees (emp_id, name, email, salary, dept_id, manager_id, phone, joining_date, is_active)
VALUES (106, 'Maria', 'maria@gmail.com', 68000, NULL, 101, NULL, '2025-04-01', 1);

SELECT emp_id, name, dept_id, manager_id
FROM employees
ORDER BY emp_id;

SELECT dept_id, dept_name
FROM departments
ORDER BY dept_id;