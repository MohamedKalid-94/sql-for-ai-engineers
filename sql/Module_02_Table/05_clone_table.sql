-- ============================================
-- Module 02
-- Clone Table
-- ============================================

DROP TABLE IF EXISTS employees_backup;

CREATE TABLE employees_backup AS
SELECT *
FROM employees;