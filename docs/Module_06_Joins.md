# Module 06: SQL Joins

Combine two tables by matching a column.

Run: `python run_module.py 6` | Output: `outputs/Module_06_Joins/output.txt` | Starts from: the shared tables

Lesson 00 adds Maria, who has no department. The Cloud department already has no employees. Together they make each join type show something different.

## Lessons

| Script | Topic |
|---|---|
| 01 using_joins | `JOIN ... USING` and `JOIN ... ON` |
| 02 inner_join | matching rows only (6 employees become 5) |
| 03 left_join | keep every employee, find unmatched ones with `IS NULL` |
| 04 right_join | native `RIGHT JOIN` and the swapped `LEFT JOIN` |
| 05 cross_join | every pairing (6 x 5 = 30) |
| 06 full_join | native `FULL JOIN` and `LEFT JOIN` plus `UNION ALL` |
| 07 self_join | employee and manager from one table |
| 08 delete_join | `DELETE` with a subquery, rolled back |
| 09 update_join | `UPDATE ... FROM` and the subquery way, rolled back |
| 10 left_join_vs_right_join | mirror images |
| 11 union_vs_join | a wider result versus a longer one |

## SQLite notes

- `RIGHT JOIN` and `FULL JOIN` work from SQLite 3.39. Lessons 04, 06 and 10 also show the older way.
- `UPDATE ... FROM` needs 3.33. There is no `DELETE ... JOIN`.