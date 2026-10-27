-- Lesson 10 of 11 | Conversion Functions
-- Conversion means changing a value from one type to another.
-- CAST(value AS type) does it on purpose. SQLite also converts quietly when it must.
-- CAST never raises an error. Text that is not a number becomes 0, and a REAL cut to INTEGER loses its decimals.
-- A plus sign makes SQLite treat both sides as numbers, but || joins them as text.
-- printf formats a number as text, which is useful for padding and decimals.

SELECT CAST('42' AS INTEGER)   AS text_to_integer,
       CAST('3.75' AS REAL)    AS text_to_real,
       CAST(3.99 AS INTEGER)   AS real_to_integer,
       CAST(65 AS TEXT)        AS integer_to_text,
       CAST(5 AS REAL)         AS integer_to_real;

SELECT CAST('12abc' AS INTEGER)       AS digits_then_letters,
       CAST('abc' AS INTEGER)         AS only_letters,
       CAST('' AS INTEGER)            AS empty_text,
       CAST(NULL AS INTEGER)          AS null_stays_null,
       CAST('2025-03-15' AS INTEGER)  AS date_text;

SELECT '10' + 5    AS text_plus_number,
       '10' || 5   AS text_joined_with_number,
       '3' * '4'   AS text_times_text,
       10 / 4      AS integer_division,
       10 / 4.0    AS decimal_division,
       '10' = 10   AS text_equals_number;

SELECT emp_id, name
FROM employees
WHERE emp_id = '101';

SELECT printf('%05d', 42)                          AS padded_with_zeros,
       printf('%.2f', 3.14159)                     AS two_decimals,
       printf('%x', 255)                           AS as_hex,
       printf('%s has %d letters', 'Asha', LENGTH('Asha')) AS sentence,
       printf('%5.1f%%', 87.456)                   AS percent;

SELECT CAST(X'48656C6C6F' AS TEXT)      AS bytes_to_text,
       HEX(CAST('Hello' AS BLOB))       AS text_to_hex;

SELECT name,
       'Rs ' || printf('%.2f', salary)  AS salary_text,
       CAST(salary AS INTEGER)          AS salary_whole
FROM employees
ORDER BY emp_id;