import sqlite3
from config import DATABASE_PATH

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

cursor.execute("""

DELETE

FROM employees

WHERE emp_id=111

""")

connection.commit()

print("Employee deleted")

connection.close()