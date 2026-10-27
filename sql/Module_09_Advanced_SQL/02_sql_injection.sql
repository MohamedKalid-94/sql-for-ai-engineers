-- Lesson 2 of 20 | SQL Injection
-- SQL injection is when a person types SQL code into a text box, and careless code runs it.
-- UNSAFE: the program pastes the typed text straight into the query text.
-- SAFE: the program uses a ? placeholder, so the typed text is only ever treated as data.
-- The first query below is a template. Python fills in the name slot by pasting text, which is the unsafe habit.

SELECT emp_id, name, salary FROM employees WHERE name = '{name}' ORDER BY emp_id;

SELECT emp_id, name, salary FROM employees WHERE name = ? ORDER BY emp_id;