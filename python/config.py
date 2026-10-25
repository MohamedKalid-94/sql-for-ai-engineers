from pathlib import Path
import sqlite3

# ==========================
# Project Root
# ==========================
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# ==========================
# Database Paths
# ==========================
DATABASE_DIR = PROJECT_ROOT / "database"
DATABASE_DIR.mkdir(exist_ok=True)

BACKUP_DIR = DATABASE_DIR / "backup"
BACKUP_DIR.mkdir(exist_ok=True)

DATABASE_PATH = DATABASE_DIR / "company.db"
RENAMED_DATABASE_PATH = DATABASE_DIR / "company_archive.db"
BACKUP_DATABASE_PATH = BACKUP_DIR / "company_backup.db"

# ==========================
# Table Names
# ==========================
DEPARTMENTS_TABLE = "departments"
EMPLOYEES_TABLE = "employees"
PROJECTS_TABLE = "company_projects"

# ==========================
# Database Connection
# ==========================
def get_connection():
    """Return SQLite database connection."""
    return sqlite3.connect(DATABASE_PATH)