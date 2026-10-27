# Changelog

All notable changes to this project are listed here.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Planned
- Module 11: window functions
- Module 12: a complete SQL schema for an AI application

## [1.0.0] - 2026-10-27

### Added
- Modules 01 to 10 rebuilt: every lesson is a `.sql` file plus a `.py` file that runs it (112 scripts)
- Shared `employees` and `departments` data in `sql/common/`
- `run_module.py` options: interactive menu, module number, and `--all`
- Lessons that show rejected statements: constraints, keys, SQL injection, STRICT tables
- Query plans before and after creating an index (SCAN versus SEARCH)
- Documentation for every module in `docs/`

### Changed
- Each module runs on its own fresh database
- Output is deterministic: fixed dates, sorted rows, no local file paths
- README rewritten, and requirements reduced to the standard library

### Fixed
- The runner reported success even when a script failed
- The rename-database script failed on its second run
- The README wrongly said SQLite has no RIGHT JOIN or FULL JOIN
- Database backups now use `VACUUM INTO` and `Connection.backup()` instead of copying the file