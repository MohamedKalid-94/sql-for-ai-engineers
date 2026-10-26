-- Lesson 8 of 24 | BOOLEAN (BIT) Operator
-- SQLite has no BOOLEAN or BIT type. True is stored as 1 and false as 0.
-- The words TRUE and FALSE also work (SQLite 3.23 or newer).

SELECT TRUE AS true_value, FALSE AS false_value;

SELECT name, is_active
FROM employees
WHERE is_active = 1
ORDER BY name;

SELECT name, is_active
FROM employees
WHERE is_active = 0;