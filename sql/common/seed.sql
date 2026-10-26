INSERT INTO departments (dept_id, dept_name) VALUES
    (1, 'AI'),
    (2, 'Python'),
    (3, 'Data Science'),
    (4, 'Cloud'),
    (5, 'GenAI');

INSERT INTO employees
    (emp_id, name, email, salary, dept_id, manager_id, phone, joining_date, is_active)
VALUES
    (101, 'John',  'john@gmail.com',  75000, 1, NULL, '9876543210', '2025-01-15', 1),
    (102, 'Sara',  'sara@gmail.com',  85000, 2, 101,  NULL,         '2025-02-10', 1),
    (103, 'David', 'david@gmail.com', 65000, 3, 101,  NULL,         '2024-11-20', 1),
    (104, 'Priya', 'priya@gmail.com', 90000, 1, 102,  '9123456780', '2024-12-05', 1),
    (105, 'Alex',  'alex@gmail.com',  72000, 5, 102,  NULL,         '2025-03-01', 1);