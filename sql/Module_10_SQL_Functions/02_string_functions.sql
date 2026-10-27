-- Lesson 2 of 11 | String Functions
-- A string is a piece of text. String functions cut it, clean it, change its case and join pieces together.
-- || joins text. SUBSTR cuts out a part. INSTR finds where a part starts. TRIM removes unwanted edges.
-- printf formats text and numbers, like a template with gaps.
-- These tools prepare text for search, chatbots and any tool that reads names and emails.

SELECT name,
       UPPER(name)  AS upper_case,
       LOWER(name)  AS lower_case,
       LENGTH(name) AS letters
FROM employees
ORDER BY emp_id;

SELECT email,
       SUBSTR(email, 1, INSTR(email, '@') - 1) AS user_part,
       SUBSTR(email, INSTR(email, '@') + 1)    AS domain
FROM employees
ORDER BY emp_id;

SELECT name || ' works in department ' || dept_id  AS sentence,
       printf('%-6s earns %8.2f', name, salary)    AS aligned
FROM employees
ORDER BY emp_id;

SELECT '[' || TRIM('   hello   ')  || ']' AS trimmed,
       '[' || LTRIM('   hello   ') || ']' AS left_trimmed,
       '[' || RTRIM('   hello   ') || ']' AS right_trimmed,
       TRIM('xxhixx', 'x')                AS trimmed_x;

SELECT raw_name,
       UPPER(SUBSTR(TRIM(raw_name), 1, 1)) || LOWER(SUBSTR(TRIM(raw_name), 2)) AS clean_name
FROM (SELECT '  sARA ' AS raw_name
      UNION ALL SELECT 'DAVID'
      UNION ALL SELECT 'pRiYa  ')
ORDER BY clean_name;

SELECT REPLACE('hello world', 'world', 'SQL') AS replaced,
       UNICODE('A')                            AS code_of_A,
       CHAR(72, 105)                           AS text_from_codes,
       HEX('Hi')                               AS as_hex,
       INSTR('hello', 'l')                     AS position_of_first_l;

SELECT sentence,
       LENGTH(sentence) - LENGTH(REPLACE(sentence, ' ', '')) + 1 AS word_count
FROM (SELECT 'SQL is a skill every AI engineer needs' AS sentence);