from pathlib import Path


# Project Root
PROJECT_ROOT = Path(__file__).resolve().parent.parent


# Database Location
DATABASE_DIR = PROJECT_ROOT / "database"
DATABASE_DIR.mkdir(exist_ok=True)


# Backup Location
BACKUP_DIR = DATABASE_DIR / "backup"
BACKUP_DIR.mkdir(exist_ok=True)


DATABASE_PATH = DATABASE_DIR / "company.db"
RENAMED_DATABASE_PATH = DATABASE_DIR / "company_new.db"
BACKUP_DATABASE_PATH = BACKUP_DIR / "company_backup.db"