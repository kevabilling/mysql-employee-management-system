# MySQL Employee Management System

A simple employee management website built with Python, Flask, and MySQL. It allows you to add, view, update, and delete employee records.

## Features

- Add employee records
- Display all employees in a table
- Edit existing employee information
- Delete employee entries
- MySQL database integration
- Clean, responsive web interface

## Tech Stack

- Python
- Flask
- MySQL
- HTML/CSS
- mysql-connector-python

## Project Structure

- `app.py` — Flask application and database logic
- `templates/` — HTML pages
- `static/` — CSS styling
- `requirements.txt` — Python dependencies

## Setup Instructions

1. Install MySQL on your machine or use a MySQL server.
2. Create a database:

```sql
CREATE DATABASE employee_db;
```

3. Create a `.env` file or export environment variables:

```bash
export MYSQL_HOST=localhost
export MYSQL_USER=root
export MYSQL_PASSWORD=your_password
export MYSQL_DATABASE=employee_db
```

Or create a `.env` file if you choose to add a dotenv loader later.

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Run the application:

```bash
python app.py
```

6. Open your browser at:

```text
http://localhost:5000
```

## Database Schema

The app creates this table automatically if it does not exist:

```sql
CREATE TABLE IF NOT EXISTS employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(120) NOT NULL UNIQUE,
    department VARCHAR(50),
    position VARCHAR(100),
    salary DECIMAL(10,2),
    joining_date DATE
);
```

## Example of Employee Record

- Name: John Doe
- Email: john.doe@example.com
- Department: Engineering
- Position: Software Engineer
- Salary: 75000.00
- Joining Date: 2024-01-15

## License

This project is open source and available under the MIT License.
