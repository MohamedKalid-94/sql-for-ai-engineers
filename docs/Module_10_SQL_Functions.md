# Module 10: SQL Functions

The built-in functions for dates, text, numbers, groups, JSON and types.

Run: `python run_module.py 10` | Output: `outputs/Module_10_SQL_Functions/output.txt` | Starts from: the shared tables, plus an `exam_scores` table

## Lessons

| Script | Topic |
|---|---|
| 00 create_sample_tables | 12 exam scores for the maths lessons |
| 01 date_functions | `strftime`, `julianday`, modifiers, Unix time |
| 02 string_functions | `UPPER`, `SUBSTR`, `INSTR`, `TRIM`, `REPLACE`, `printf` |
| 03 aggregate_functions | `COUNT`, `SUM`, `AVG`, `GROUP_CONCAT`, `TOTAL` |
| 04 numeric_functions | `ROUND`, integer division, `%`, and the optional math functions |
| 05 text_image_functions | `TEXT` versus `BLOB`, storing a real PNG |
| 06 statistical_functions | median in SQL, standard deviation as a Python aggregate |
| 07 logical_functions | `CASE`, `IIF`, and three-valued logic with NULL |
| 08 cursor_functions | `description`, `rowcount`, `lastrowid`, `row_factory` |
| 09 json_functions | `json_extract`, `json_each`, `json_set`, `json_valid` |
| 10 conversion_functions | `CAST` and quiet conversions |
| 11 datatype_functions | `TYPEOF`, type affinity, and `STRICT` tables |

## SQLite notes

- JSON needs SQLite 3.38 and `STRICT` tables need 3.37.
- `CEIL`, `FLOOR`, `SQRT` and `POWER` exist only in builds with math functions. Lesson 04 prints a message if they are missing.
- SQLite has no median or standard deviation, so Lesson 06 builds them.