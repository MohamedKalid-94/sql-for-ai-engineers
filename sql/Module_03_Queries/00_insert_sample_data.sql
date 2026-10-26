-- Lesson 0 of 7 | Insert Sample Data
-- The shared setup already gave this module 5 employees.
-- Here we add 2 more so the later lessons have more variety.
-- We name every column on purpose, so each value lands in the right place.

SELECT COUNT(*) AS employees_before
FROM employees;

INSERT INTO employees (emp_id, name, email, salary, dept_id, manager_id, phone, joining_date, is_active)
VALUES
    (106, 'Maria', 'maria@gmail.com', 68000, 2, 101, NULL,         '2025-04-01', 1),
    (107, 'Kumar', 'kumar@gmail.com', 95000, 4, 102, '9000000001', '2025-04-15', 1);

SELECT emp_id, name, salary, dept_id
FROM employees
ORDER BY emp_id;