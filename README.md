# Police Station Database CLI Application

This is a **Command-Line Interface (CLI)** application for managing a police station database. It allows you to add and view officers, badges, cases, suspects, and motorbikes using a simple menu-driven interface.

---

## Features

- **Add Entities**:
  - Add officers, badges, cases, suspects, and motorbikes.
- **View Entities**:
  - List all officers, badges, cases, suspects, and motorbikes.
- **Database Management**:
  - Uses **SQLAlchemy** for database operations.
  - Supports **SQLite** as the database backend.
- **Alembic Integration**:
  - Database schema migrations are managed using **Alembic**.

---

## Prerequisites

Before running the application, ensure you have the following installed:

- **Python 3.10 or higher**
- **SQLAlchemy**
- **Alembic**
- **SQLite** (included with Python)

## SETUP
1. Clone the Repository:
```bash
git clone https://github.com/Ali1-coder/Police-Python-Cli.git
cd police-python-cli
```
2. Install packages:
```bash
pipenv install
```
3. Start virtual environment:
```bash
pipenv shell
```
4. Initialize the Database:
    Run Alembic migrations to set up the database schema:
```bash
alembic upgrade head
```
5.Run the Application:
```bash
startfile.py
```

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

