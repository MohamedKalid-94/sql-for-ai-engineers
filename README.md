# SQL for AI Engineers 🚀

A hands-on SQL learning and implementation repository designed for AI Engineers to build strong database foundations required for Data Engineering, Machine Learning, Generative AI, RAG Systems, and AI Applications.

This repository contains hands-on SQL concepts implemented using **SQLite** and **Python (`sqlite3`)**, organized into modular lessons with SQL scripts, Python implementations, documentation, automated execution, and output logs.

Each module includes:

- SQL implementation
- Equivalent Python (`sqlite3`) implementation
- Documentation
- Automated execution using `run_module.py`
- Execution output logs

---

# 🎯 Project Goal

Modern AI Engineers need more than LLM knowledge. Strong database skills are required for:

- Storing application data
- Managing user information
- Building AI application backends
- Creating RAG pipelines
- Managing document metadata
- Tracking conversations and AI workflows
- Designing scalable AI systems

This project builds SQL skills from beginner to advanced level through practical implementation.

---

# 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Execute SQL operations programmatically |
| SQLite | Lightweight relational database |
| SQL | Database queries and management |
| VS Code | Development environment |
| Git & GitHub | Version control and portfolio |

---

# 📂 Repository Structure

```
sql-for-ai-engineers/

│
├── database/
│   └── SQLite database files
│
├── docs/
│   └── Module documentation
│
├── outputs/
│   └── Execution logs
│
├── python/
│   ├── config.py
│   └── Module implementations
│
├── sql/
│   └── SQL command examples
│
├── run_module.py
│
├── requirements.txt
│
└── README.md
```

---

# ⚙️ Setup Instructions

## 1. Clone Repository

```bash
git clone https://github.com/<username>/sql-for-ai-engineers.git
```

Move into project:

```bash
cd sql-for-ai-engineers
```

---

## 2. Create Virtual Environment

Windows:

```bash
python -m venv .venv
```

Activate:

```bash
.venv\Scripts\activate
```

---

## 3. Install Requirements

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

Run all examples through the automation script:

```bash
python run_module.py
```

Select the required module:

Example:

```
Available Modules

1. Module_01_Database

Select Module Number: 1
```

The execution output will be saved automatically:

```
outputs/
└── Module_01_Database/
    └── output.txt
```

---

# 📚 Learning Modules

## ✅ Module 01: SQL Database Management

- Create Database
- Show Database
- Select Database
- Rename Database
- Backup Database
- Drop Database

---

## ✅ Module 02: SQL Tables

- Create Table
- Show Tables
- Rename Table
- Truncate Table (SQLite Equivalent)
- Clone Tables
- Temporary Tables
- Alter Tables
- Constraints
- Delete Table Data
- Drop Tables

---

## ✅ Module 03: SQL Queries

- Insert Sample Data
- INSERT
- SELECT
- SELECT INTO (SQLite Equivalent)
- INSERT INTO SELECT
- UPDATE
- DELETE
- ORDER BY

---

## ✅ Module 04: SQL Views

- Create Views
- Update Views (SQLite Equivalent)
- Drop Views
- Rename Views (SQLite Equivalent)

---

## ✅ Module 05: SQL Operators and Clauses 

- WHERE Clause
- TOP / LIMIT Clause
- DISTINCT Clause
- ORDER BY Clause
- GROUP BY Clause
- HAVING Clause
- AND & OR Operators
- BOOLEAN Operator
- LIKE Operator
- IN Operator
- ANY / ALL Operators
- EXISTS Operator
- CASE Expression
- NOT Operator
- NOT EQUAL Operator
- IS NULL
- IS NOT NULL
- NOT NULL Constraint
- BETWEEN Operator
- UNION Operator
- UNION vs UNION ALL
- INTERSECT Operator
- EXCEPT Operator
- Aliases

---

## ✅ Module 06: SQL Joins 

- USING JOIN
- INNER JOIN
- LEFT JOIN
- RIGHT JOIN
- CROSS JOIN
- FULL JOIN
- SELF JOIN
- DELETE JOIN
- UPDATE JOIN
- LEFT JOIN vs RIGHT JOIN
- UNION vs JOIN

> *RIGHT JOIN and FULL JOIN are demonstrated using SQLite-compatible alternatives.

---

## ✅ Module 07: SQL Keys 

- UNIQUE Key
- PRIMARY Key
- FOREIGN Key
- Composite Key
- Alternate Key

---

## ⏳ Module 08: SQL Indexes

- Create Index
- Unique Index
- Composite Index
- Drop Index

---

## ⏳ Module 09: Advanced SQL

- Transactions
- Subqueries
- Common Table Expressions (CTE)
- Views
- Database Optimization

---

## ⏳ Module 10: SQL Functions

- Aggregate Functions
- String Functions
- Numeric Functions
- Date Functions
- Conversion Functions

---

# 🤖 Connection With AI Engineering

SQL knowledge is important for building:

## RAG Applications

Example:

```
User
 |
Application
 |
FastAPI
 |
SQL Database
 |
Document Metadata
 |
Vector Database
 |
LLM
```

SQL stores:

- Users
- Projects
- Documents
- Chat History
- Permissions
- AI Agent Tasks

---

# 🔥 Future Integration Goals

This repository will later connect with:

- Python Data Processing
- SQLAlchemy
- FastAPI
- LangChain
- LangGraph
- RAG Applications
- Agentic AI Systems
- Vector Databases

---

# 📈 Learning Progress

| Module | Status |
|---------|--------|
| Module 01 - SQL Database | ✅ Completed |
| Module 02 - SQL Tables | ✅ Completed |
| Module 03 - SQL Queries | ✅ Completed |
| Module 04 - SQL Views | ✅ Completed |
| Module 05 - SQL Operators | ✅ Completed |
| Module 06 - SQL Joins | ✅ Completed |
| Module 07 - SQL Keys | ✅ Completed |
| Module 08 - SQL Indexes | ⏳ Planned |
| Module 09 - Advanced SQL | ⏳ Planned |
| Module 10 - SQL Functions | ⏳ Planned |

---

# ✨ Features

- Modular SQL learning path
- SQLite-based examples
- Python (`sqlite3`) implementation for every SQL script
- Automated module execution (`run_module.py`)
- Module-wise documentation
- Output logs for every execution
- Beginner-friendly and AI Engineer focused

# 👨‍💻 Author

Mohamed Kalid

