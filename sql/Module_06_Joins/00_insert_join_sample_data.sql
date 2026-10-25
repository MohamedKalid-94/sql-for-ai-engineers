DROP TABLE IF EXISTS projects;
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS departments;


CREATE TABLE departments(
    department_id INTEGER PRIMARY KEY,
    department_name TEXT NOT NULL
);


CREATE TABLE employees(
    emp_id INTEGER PRIMARY KEY,
    emp_name TEXT NOT NULL,
    email TEXT,
    salary REAL,
    department_id INTEGER,
    manager_id INTEGER,
    FOREIGN KEY(department_id)
    REFERENCES departments(department_id)
);


CREATE TABLE projects(
    project_id INTEGER PRIMARY KEY,
    project_name TEXT,
    emp_id INTEGER,
    FOREIGN KEY(emp_id)
    REFERENCES employees(emp_id)
);



INSERT INTO departments VALUES
(1,'AI'),
(2,'Python'),
(3,'Data Science'),
(4,'Cloud'),
(5,'GenAI');


INSERT INTO employees VALUES
(101,'John','john@gmail.com',75000,1,NULL),
(102,'Sara','sara@gmail.com',85000,2,101),
(103,'David','david@gmail.com',65000,3,101),
(104,'Priya','priya@gmail.com',90000,1,102),
(105,'Alex','alex@gmail.com',72000,5,102);


INSERT INTO projects VALUES
(1,'RAG Application',101),
(2,'AI Agent',102),
(3,'Chatbot',103);


SELECT 'Sample Data Inserted Successfully';