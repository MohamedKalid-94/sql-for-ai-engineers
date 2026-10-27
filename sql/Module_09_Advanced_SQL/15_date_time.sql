-- Lesson 15 of 20 | Date and Time Functions
-- SQLite stores dates as text in the form year-month-day, and times as hour:minute:second.
-- date, time and datetime build or clean these values. Modifiers such as '+1 month' do calendar maths.
-- strftime formats a date any way we like. julianday counts days, so a subtraction gives a number of days.
-- We use fixed dates so the output never changes. date('now') changes every day, so we only check its shape.

SELECT date('2025-03-15')                  AS the_date,
       time('2025-03-15 14:30:45')         AS the_time,
       datetime('2025-03-15 14:30:45')     AS both_together;

SELECT date('2025-01-31', '+1 day')                                 AS tomorrow,
       date('2025-01-31', '+1 month')                               AS next_month,
       date('2025-01-31', '-7 days')                                AS week_ago,
       date('2025-01-31', 'start of month')                         AS month_start,
       date('2025-02-10', 'start of month', '+1 month', '-1 day')   AS month_end;

SELECT name,
       joining_date,
       CAST(julianday('2025-06-01') - julianday(joining_date) AS INTEGER) AS days_employed
FROM employees
WHERE joining_date IS NOT NULL
ORDER BY joining_date;

SELECT name,
       strftime('%Y', joining_date)       AS year,
       strftime('%m', joining_date)       AS month,
       strftime('%d/%m/%Y', joining_date) AS day_month_year
FROM employees
WHERE joining_date IS NOT NULL
ORDER BY joining_date;

SELECT d AS the_date,
       strftime('%w', d) AS weekday_number
FROM (SELECT '2025-03-15' AS d UNION ALL SELECT '2025-03-16' UNION ALL SELECT '2025-03-17')
ORDER BY d;

SELECT length(date('now'))             AS length_of_today,
       date('now') LIKE '____-__-__'   AS has_date_shape;