-- CASE Expression

SELECT
    name,
    salary,

    CASE

        WHEN salary >= 90000
        THEN 'High Salary'

        WHEN salary >= 70000
        THEN 'Medium Salary'

        ELSE 'Low Salary'

    END AS salary_category

FROM employees;