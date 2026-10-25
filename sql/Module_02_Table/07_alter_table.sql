-- ============================================
-- Module 02
-- ALTER TABLE
-- ============================================

ALTER TABLE employees
ADD COLUMN phone TEXT;

ALTER TABLE employees
ADD COLUMN joining_date TEXT;

ALTER TABLE employees
ADD COLUMN is_active INTEGER DEFAULT 1;