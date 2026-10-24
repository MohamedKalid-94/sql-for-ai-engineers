
import sqlite3
import sys
from pathlib import Path


# ============================================
# Add python folder into path
# ============================================

PYTHON_DIR = Path(__file__).resolve().parent.parent

sys.path.append(str(PYTHON_DIR))


from config import DATABASE_PATH


# ============================================
# Connect Database
# ============================================

connection = sqlite3.connect(DATABASE_PATH)

cursor = connection.cursor()


# ============================================
# Show Tables
# ============================================

cursor.execute("""
SELECT name
FROM sqlite_master
WHERE type='table'
AND name NOT LIKE 'sqlite_%'
ORDER BY name
""")


tables = cursor.fetchall()


print("Tables Available")
print("------------------------------")


for table in tables:
    print(table[0])


connection.close()