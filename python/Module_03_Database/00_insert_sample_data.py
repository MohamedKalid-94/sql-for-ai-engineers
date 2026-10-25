import sqlite3
from config import DATABASE_PATH

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

# ------------------------
# Departments
# ------------------------

departments = [
    (1, "Artificial Intelligence"),
    (2, "Human Resources"),
    (3, "Finance"),
    (4, "Sales"),
    (5, "IT")
]

cursor.executemany("""
INSERT OR IGNORE INTO departments
VALUES (?,?)
""", departments)

print("Departments inserted")

# ------------------------
# Employees
# ------------------------

employees = [
(101,"John","john@gmail.com",70000,1),
(102,"Sara","sara@gmail.com",85000,2),
(103,"David","david@gmail.com",65000,3),
(104,"Priya","priya@gmail.com",90000,1),
(105,"Alex","alex@gmail.com",72000,5),
(106,"Maria","maria@gmail.com",78000,4),
(107,"Ahmed","ahmed@gmail.com",68000,1),
(108,"Sophia","sophia@gmail.com",95000,2),
(109,"James","james@gmail.com",61000,3),
(110,"Emma","emma@gmail.com",82000,5)
]

cursor.executemany("""
INSERT OR IGNORE INTO employees
(emp_id,name,email,salary,dept_id)
VALUES (?,?,?,?,?)
""", employees)

print("Employees inserted")

# ------------------------
# Projects
# ------------------------

projects = [
(1,"RAG Chatbot",101),
(2,"Recruitment AI",102),
(3,"AI Search Engine",104),
(4,"Payroll System",103),
(5,"Sales Dashboard",106),
(6,"HR Portal",108)
]

cursor.executemany("""
INSERT OR IGNORE INTO company_projects
VALUES (?,?,?)
""", projects)

print("Projects inserted")

connection.commit()
connection.close()

print("\nSample Data Inserted Successfully")