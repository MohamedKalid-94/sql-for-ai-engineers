-- Create Unique Index

CREATE UNIQUE INDEX idx_unique_email
ON employees(email);


-- Test unique constraint

INSERT INTO employees
(
emp_id,
name,
email,
salary,
department_id
)
VALUES
(
111,
'Robert',
'john@gmail.com',
70000,
1
);