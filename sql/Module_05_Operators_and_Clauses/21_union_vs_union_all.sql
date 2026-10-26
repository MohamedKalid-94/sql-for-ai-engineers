-- Lesson 21 of 24 | UNION vs UNION ALL
-- UNION removes repeated rows. UNION ALL keeps every row, so it is faster and shows repeats.
-- Sara is in both tables, so she shows once with UNION and twice with UNION ALL.

SELECT name FROM employees
UNION
SELECT name FROM contractors
ORDER BY name;

SELECT name FROM employees
UNION ALL
SELECT name FROM contractors
ORDER BY name;