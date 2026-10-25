-- ============================================
-- Module 02
-- Constraints
-- ============================================

DROP TABLE IF EXISTS employee_constraints;

CREATE TABLE employee_constraints (

    emp_id INTEGER PRIMARY KEY,

    employee_code TEXT UNIQUE,

    name TEXT NOT NULL,

    salary REAL
        CHECK(salary >= 0),

    department TEXT
        DEFAULT 'General'
);