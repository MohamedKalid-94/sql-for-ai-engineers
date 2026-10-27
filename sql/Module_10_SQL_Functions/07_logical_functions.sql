-- Lesson 7 of 11 | Logical Functions
-- Logical functions let a query make decisions. CASE is the full if / else if / else.
-- IIF is the short version with only two outcomes.
-- AND, OR and NOT give 1 for true and 0 for false, and NULL when the answer is unknown.
-- Module 9 showed COALESCE, NULLIF and IFNULL, so here we use decisions to grade the exam scores.

SELECT subject,
       score,
       CASE
           WHEN score >= 90 THEN 'A'
           WHEN score >= 75 THEN 'B'
           WHEN score >= 60 THEN 'C'
           ELSE 'F'
       END AS grade
FROM exam_scores
WHERE student = 'Asha'
ORDER BY score_id;

SELECT grade, COUNT(*) AS how_many
FROM (SELECT CASE
                 WHEN score >= 90 THEN 'A'
                 WHEN score >= 75 THEN 'B'
                 WHEN score >= 60 THEN 'C'
                 ELSE 'F'
             END AS grade
      FROM exam_scores)
GROUP BY grade
ORDER BY grade;

SELECT student,
       SUM(IIF(score >= 60, 1, 0)) AS subjects_passed,
       SUM(IIF(score < 60, 1, 0))  AS subjects_failed
FROM exam_scores
GROUP BY student
ORDER BY student;

SELECT (5 > 3)              AS true_is_1,
       (5 < 3)              AS false_is_0,
       (5 > 3 AND 2 > 1)    AS both,
       (5 < 3 OR 2 > 1)     AS either,
       NOT (5 < 3)          AS opposite,
       NULL AND 1           AS null_and_true,
       NULL AND 0           AS null_and_false,
       NULL OR 1            AS null_or_true;

SELECT name,
       CASE
           WHEN dept_id IN (1, 5) THEN 'AI team'
           WHEN dept_id = 2       THEN 'Python team'
           ELSE 'Other'
       END AS team
FROM employees
ORDER BY emp_id;