-- Lesson 3 of 11 | Aggregate Functions
-- An aggregate function folds many rows into ONE answer: a count, a total, an average, a smallest or a biggest.
-- GROUP BY gives one answer for each group. HAVING filters whole groups.
-- COUNT(*) counts rows, COUNT(column) skips NULLs, and COUNT(DISTINCT column) counts different values.
-- GROUP_CONCAT joins the values of a group into one piece of text.
-- On an empty set, SUM and AVG give NULL, but TOTAL gives 0.0 and COUNT gives 0.

SELECT COUNT(*)              AS scores,
       SUM(score)            AS total,
       ROUND(AVG(score), 2)  AS average,
       MIN(score)            AS lowest,
       MAX(score)            AS highest
FROM exam_scores;

SELECT subject,
       COUNT(*)              AS scores,
       SUM(score)            AS total,
       ROUND(AVG(score), 2)  AS average
FROM exam_scores
GROUP BY subject
ORDER BY subject;

SELECT student,
       COUNT(*)              AS subjects,
       SUM(score)            AS total,
       ROUND(AVG(score), 2)  AS average
FROM exam_scores
GROUP BY student
HAVING AVG(score) >= 70
ORDER BY average DESC;

SELECT COUNT(*)                AS rows_counted,
       COUNT(phone)            AS with_phone,
       COUNT(DISTINCT dept_id) AS departments_used
FROM employees;

SELECT dept_id,
       GROUP_CONCAT(name, ', ') AS people
FROM (SELECT dept_id, name FROM employees ORDER BY name)
GROUP BY dept_id
ORDER BY dept_id;

SELECT SUM(salary)    AS sum_of_nothing,
       TOTAL(salary)  AS total_of_nothing,
       COUNT(salary)  AS count_of_nothing,
       AVG(salary)    AS average_of_nothing
FROM employees
WHERE dept_id = 4;