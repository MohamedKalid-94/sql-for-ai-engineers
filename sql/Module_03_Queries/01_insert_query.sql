-- Lesson 1 of 7 | INSERT
-- INSERT adds new lines (rows) to a table. Always name the columns,
-- so the values cannot land in the wrong place.
-- A column we skip gets NULL, or its DEFAULT value (is_active defaults to 1).
-- Way 1: one row. Way 2: many rows in one command.
-- Way 3: placeholders (?), so Python can pass the values in safely.

INSERT INTO employees (emp_id, name, email, salary, dept_id)
VALUES (108, 'Neha', 'neha@gmail.com', 70000, 3);

INSERT INTO employees (emp_id, name, email, salary, dept_id)
VALUES
    (109, 'Omar', 'omar@gmail.com', 82000, 1),
    (110, 'Lena', 'lena@gmail.com', 61000, 5);

INSERT INTO employees (emp_id, name, email, salary, dept_id)
VALUES (?, ?, ?, ?, ?);

SELECT emp_id, name, salary, dept_id, phone, is_active
FROM employees
WHERE emp_id >= 108
ORDER BY emp_id;