# Database Schema

## employees Table

| Column | Type | Description |
|---|---|---|
| emp_id | INTEGER | Primary Key |
| name | TEXT | Employee Name |
| email | TEXT | Unique Email |
| salary | REAL | Employee Salary |
| department_id | INTEGER | Department Reference |
| phone | TEXT | Contact Number |
| joining_date | DATE | Joining Date |
| status | INTEGER | Active Status |


## departments Table

| Column | Type |
|---|---|
| department_id | INTEGER |
| department_name | TEXT |