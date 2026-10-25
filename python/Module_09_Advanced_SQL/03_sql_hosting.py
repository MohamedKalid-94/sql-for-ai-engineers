from config import get_connection

print("SQLite Hosting Example")
print("----------------------")
print("Database is running locally using SQLite.")

conn = get_connection()
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM employees")

print("Total Employees :", cursor.fetchone()[0])

conn.close()