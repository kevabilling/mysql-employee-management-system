from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import os

app = Flask(__name__)
app.secret_key = "employee_management_secret_key"


def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "localhost"),
        user=os.getenv("MYSQL_USER", "root"),
        password=os.getenv("MYSQL_PASSWORD", ""),
        database=os.getenv("MYSQL_DATABASE", "employee_db"),
        autocommit=True,
    )


def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS employees (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(120) NOT NULL UNIQUE,
            department VARCHAR(50),
            position VARCHAR(100),
            salary DECIMAL(10,2),
            joining_date DATE
        )
        """
    )
    conn.close()


@app.route("/")
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM employees ORDER BY id DESC")
    employees = cursor.fetchall()
    conn.close()
    return render_template("index.html", employees=employees)


@app.route("/employees/new")
def new_employee():
    return render_template("add_employee.html")


@app.route("/employees", methods=["POST"])
def create_employee():
    name = request.form["name"]
    email = request.form["email"]
    department = request.form["department"]
    position = request.form["position"]
    salary = request.form["salary"]
    joining_date = request.form["joining_date"]

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO employees (name, email, department, position, salary, joining_date)
        VALUES (%s, %s, %s, %s, %s, %s)
        """,
        (name, email, department, position, salary, joining_date),
    )
    conn.close()
    return redirect(url_for("index"))


@app.route("/employees/<int:employee_id>/edit")
def edit_employee(employee_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM employees WHERE id = %s", (employee_id,))
    employee = cursor.fetchone()
    conn.close()

    if employee is None:
        return redirect(url_for("index"))

    return render_template("edit_employee.html", employee=employee)


@app.route("/employees/<int:employee_id>", methods=["POST"])
def update_employee(employee_id):
    name = request.form["name"]
    email = request.form["email"]
    department = request.form["department"]
    position = request.form["position"]
    salary = request.form["salary"]
    joining_date = request.form["joining_date"]

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE employees
        SET name = %s,
            email = %s,
            department = %s,
            position = %s,
            salary = %s,
            joining_date = %s
        WHERE id = %s
        """,
        (name, email, department, position, salary, joining_date, employee_id),
    )
    conn.close()
    return redirect(url_for("index"))


@app.route("/employees/<int:employee_id>/delete", methods=["POST"])
def delete_employee(employee_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM employees WHERE id = %s", (employee_id,))
    conn.close()
    return redirect(url_for("index"))


if __name__ == "__main__":
    init_db()
    app.run(debug=True, host="0.0.0.0", port=5000)
