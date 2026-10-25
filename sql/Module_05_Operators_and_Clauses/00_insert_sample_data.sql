-- Insert Departments

INSERT INTO departments
(dept_id, department_name)
VALUES
(1,'AI'),
(2,'Data Engineering'),
(3,'Software'),
(4,'Cloud'),
(5,'HR');


-- Insert Employees

INSERT INTO employees
(emp_id,name,email,salary,dept_id,is_active)
VALUES

(101,'John','john@gmail.com',70000,1,1),
(102,'Sara','sara@gmail.com',85000,2,1),
(103,'David','david@gmail.com',65000,3,1),
(104,'Priya','priya@gmail.com',90000,1,1),
(105,'Alex','alex@gmail.com',72000,5,1),
(106,'Maria','maria@gmail.com',78000,4,1),
(107,'Ahmed','ahmed@gmail.com',68000,1,1),
(108,'Sophia','sophia@gmail.com',95000,2,1),
(109,'James','james@gmail.com',61000,3,1),
(110,'Emma','emma@gmail.com',82000,5,1);