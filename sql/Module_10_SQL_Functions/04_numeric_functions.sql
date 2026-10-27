-- Lesson 4 of 11 | Numeric Functions
-- Numeric functions work on numbers: rounding, absolute value, remainders and so on.
-- Two things surprise beginners. A whole number divided by a whole number gives a whole number,
-- so 7 / 2 is 3. To get a decimal, make one side a decimal, as in 7 / 2.0.
-- ROUND always gives back a decimal number, such as 4568.0.
-- With several arguments, MAX and MIN pick the biggest or smallest of them. With one argument they are aggregates.
-- CEIL, FLOOR, SQRT and POWER are math functions. They exist only when SQLite was built with them.

SELECT ROUND(4567.891, 2)             AS two_decimals,
       ROUND(4567.891)                AS whole_number,
       ROUND(4567.891 / 100) * 100    AS nearest_hundred,
       ABS(-250)                      AS positive,
       ABS(-12.5)                     AS positive_decimal;

SELECT 7 / 2     AS whole_division,
       7 / 2.0   AS decimal_division,
       7 % 2     AS remainder,
       -7 / 2    AS negative_division,
       -7 % 2    AS negative_remainder;

SELECT name,
       salary,
       MAX(salary, 70000.0) AS at_least_70000,
       MIN(salary, 80000.0) AS at_most_80000
FROM employees
ORDER BY emp_id;

SELECT name,
       salary,
       ROUND(salary * 1.075, 2) AS after_raise,
       ROUND(salary / 12, 2)    AS per_month
FROM employees
ORDER BY emp_id;

SELECT CAST(CEIL(7.2) AS INTEGER)   AS round_up,
       CAST(FLOOR(7.8) AS INTEGER)  AS round_down,
       CAST(SQRT(144) AS INTEGER)   AS square_root,
       CAST(POWER(2, 10) AS INTEGER) AS two_to_the_ten,
       ROUND(SQRT(2), 4)            AS root_of_two;