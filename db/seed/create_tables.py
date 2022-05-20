from time import gmtime, strftime

import mysql.connector
from decouple import config

db_config = {
    "host": config("TEST_DB_HOST", default="localhost"),
    "database": config("TEST_DB_NAME"),
    "user": config("TEST_DB_USER"),
    "password": config("TEST_DB_PASSWORD"),
    "raise_on_warnings": True,
}


def create_tables():
    cnx = mysql.connector.connect(**db_config)

    cursor = cnx.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS employees (emp_no INT NOT NULL AUTO_INCREMENT, birth_date DATE NOT NULL, 
        first_name VARCHAR(14) NOT NULL, last_name VARCHAR(16) NOT NULL, gender ENUM ('M','F') NOT NULL, 
        hire_date DATE NOT NULL, PRIMARY KEY (emp_no))"""
    )

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS departments (dept_no CHAR(4) NOT NULL, 
        dept_name VARCHAR(40) NOT NULL, PRIMARY KEY (dept_no), UNIQUE KEY dept_name (dept_name))"""
    )

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS salaries (emp_no INT NOT NULL, salary INT NOT NULL, 
        from_date DATE NOT NULL, to_date DATE NOT NULL, PRIMARY KEY (emp_no, from_date), KEY emp_no (emp_no), 
        CONSTRAINT salaries_ibfk_1 FOREIGN KEY (emp_no) REFERENCES employees (emp_no) ON DELETE CASCADE)"""
    )

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS dept_emp (emp_no INT NOT NULL, dept_no CHAR(4) NOT NULL, 
        from_date DATE NOT NULL,to_date DATE NOT NULL, PRIMARY KEY (emp_no, dept_no),KEY emp_no (emp_no),
        KEY dept_no (dept_no), CONSTRAINT dept_emp_ibfk_1 FOREIGN KEY (emp_no)
        REFERENCES employees (emp_no) ON DELETE CASCADE,
        CONSTRAINT dept_emp_ibfk_2 FOREIGN KEY (dept_no) REFERENCES departments (dept_no) ON DELETE CASCADE)"""
    )

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS dept_manager(emp_no INT NOT NULL, dept_no CHAR(4) NOT NULL, from_date DATE NOT NULL, "
        "to_date DATE NOT NULL, PRIMARY KEY (emp_no, dept_no), KEY emp_no (emp_no), KEY dept_no (dept_no), "
        "CONSTRAINT dept_manager_ibfk_1 FOREIGN KEY (emp_no) REFERENCES employees (emp_no) ON DELETE CASCADE, "
        "CONSTRAINT dept_manager_ibfk_2 FOREIGN KEY (dept_no) REFERENCES departments (dept_no) ON DELETE CASCADE)"
    )

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS titles(emp_no INT NOT NULL, title VARCHAR(50) NOT NULL, "
        "from_date DATE NOT NULL, to_date DATE DEFAULT NULL, PRIMARY KEY (emp_no, title, from_date), "
        "KEY emp_no (emp_no), CONSTRAINT titles_ibfk_1 FOREIGN KEY (emp_no) REFERENCES employees (emp_no) "
        "ON DELETE CASCADE)"
    )

    cursor.close()
    cnx.close()

    print("Logged:", strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
