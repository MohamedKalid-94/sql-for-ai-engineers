# Module 01: SQL Database

In SQLite a database is one file, so database commands become small SQL commands or file actions.

Run: `python run_module.py 1` | Output: `outputs/Module_01_Database/output.txt` | Starts from: an empty database

## Lessons

| Script | Topic |
|---|---|
| 01 create_database | the file appears on the first write |
| 02 show_databases | `PRAGMA database_list` and an in-memory database |
| 03 select_database | `ATTACH` and `database.table` names |
| 04 rename_database | renaming the file and checking the data survived |
| 05 backup_database | `VACUUM INTO` and `Connection.backup()` |
| 06 drop_database | `DETACH`, then deleting the file |

## SQLite notes

| Other databases | SQLite |
|---|---|
| `CREATE DATABASE` | connect to a new file name and write to it |
| `SHOW DATABASES` | `PRAGMA database_list` |
| `USE name` | open the file, or `ATTACH` it |
| rename, drop | rename or delete the file |

Lesson 06 deletes the database, so it runs last.