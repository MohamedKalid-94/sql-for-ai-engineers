-- Lesson 1 of 11 | Date Functions
-- SQLite keeps dates as text in the form year-month-day, so there is no special date type.
-- strftime picks a date apart or formats it. date, time and datetime clean a value.
-- Modifiers such as '+1 month' or 'start of year' do calendar maths.
-- julianday counts days, so subtracting two of them gives a number of days.
-- We use fixed dates, so the output is the same on every run.
-- Module 9 introduced these functions. Here we use them to answer real questions.

SELECT name, joining_date, strftime('%Y-%m', joining_date) AS joined_month
FROM employees
ORDER BY joining_date;

SELECT name,
       CAST(julianday('2025-06-01') - julianday(joining_date) AS INTEGER) AS days_employed,
       (strftime('%Y', '2025-06-01') - strftime('%Y', joining_date)) * 12
         + (strftime('%m', '2025-06-01') - strftime('%m', joining_date))    AS calendar_months
FROM employees
ORDER BY joining_date;

SELECT name,
       joining_date,
       CASE strftime('%w', joining_date)
           WHEN '0' THEN 'Sunday'
           WHEN '1' THEN 'Monday'
           WHEN '2' THEN 'Tuesday'
           WHEN '3' THEN 'Wednesday'
           WHEN '4' THEN 'Thursday'
           WHEN '5' THEN 'Friday'
           ELSE 'Saturday'
       END AS joined_on_a
FROM employees
ORDER BY joining_date;

SELECT date('2025-03-15', 'weekday 1')                             AS next_monday,
       date('2025-03-15', 'start of year')                         AS year_start,
       date('2025-03-15', 'start of month', '+1 month', '-1 day')  AS month_end,
       date('2025-03-15', 'start of year', '+1 year', '-1 day')    AS year_end,
       strftime('%j', '2025-03-15')                                AS day_of_year;

SELECT strftime('%s', '2025-01-01')                AS seconds_since_1970,
       datetime(1735689600, 'unixepoch')           AS back_to_a_date,
       date(1735689600 + 86400 * 30, 'unixepoch')  AS thirty_days_later;

SELECT strftime('%Y', joining_date) AS year,
       COUNT(*)                     AS joined
FROM employees
GROUP BY year
ORDER BY year;