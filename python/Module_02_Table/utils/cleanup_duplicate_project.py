import sqlite3
import sys
from pathlib import Path


# ==================================================
# Add python folder to system path
# ==================================================

PYTHON_DIR = Path(__file__).resolve().parent.parent

sys.path.append(str(PYTHON_DIR))


# Import database path
from config import DATABASE_PATH


# ==================================================
# Connect Database
# ==================================================

connection = sqlite3.connect(DATABASE_PATH)

cursor = connection.cursor()


# ==================================================
# Remove duplicate old projects table
# ==================================================

cursor.execute("""
DROP TABLE IF EXISTS projects
""")


connection.commit()


connection.close()


print("Old projects table removed successfully")