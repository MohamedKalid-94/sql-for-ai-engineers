-- Lesson 6 of 11 | Statistical Functions
-- Statistics describe a set of numbers: the middle, the spread, and how far each one is from the middle.
-- SQLite has AVG, MIN, MAX and COUNT, but no median and no standard deviation.
-- The median is worked out in pure SQL below.
-- stddev_population and stddev_sample are written in Python, and the .py file registers them for SQL to call.
-- Population means these numbers are everything, and sample means they are a small part of a bigger group.

SELECT COUNT(score)             AS scores,
       ROUND(AVG(score), 2)     AS mean,
       MIN(score)               AS lowest,
       MAX(score)               AS highest,
       MAX(score) - MIN(score)  AS spread
FROM exam_scores;

SELECT AVG(score) AS median
FROM (
    SELECT score
    FROM exam_scores
    ORDER BY score
    LIMIT 2 - (SELECT COUNT(*) FROM exam_scores) % 2
    OFFSET (SELECT (COUNT(*) - 1) / 2 FROM exam_scores)
);

SELECT ROUND(stddev_population(score), 2) AS population_std,
       ROUND(stddev_sample(score), 2)     AS sample_std
FROM exam_scores;

SELECT subject,
       ROUND(AVG(score), 2)           AS mean,
       ROUND(stddev_sample(score), 2) AS sample_std
FROM exam_scores
GROUP BY subject
ORDER BY subject;

SELECT student,
       subject,
       score,
       ROUND((score - (SELECT AVG(score) FROM exam_scores))
             / (SELECT stddev_sample(score) FROM exam_scores), 1) AS z_score
FROM exam_scores
ORDER BY score DESC
LIMIT 3;