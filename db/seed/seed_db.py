from time import gmtime, strftime

import mysql.connector
from decouple import config
from sample_data import *

db_config = {
    "host": config("TEST_DB_HOST", default="localhost"),
    "database": config("TEST_DB_NAME"),
    "user": config("TEST_DB_USER"),
    "password": config("TEST_DB_PASSWORD"),
    "raise_on_warnings": True,
}


def seed_db():
    cnx = mysql.connector.connect(**db_config)

    cursor = cnx.cursor()

    add_employee = (
        "INSERT INTO employees "
        "(first_name, last_name, hire_date, gender, birth_date) "
        "VALUES (%s, %s, %s, %s, %s)"
    )
    add_salary = (
        "INSERT INTO salaries "
        "(emp_no, salary, from_date, to_date) "
        "VALUES (%(emp_no)s, %(salary)s, %(from_date)s, %(to_date)s)"
    )

    add_departments = (
        "INSERT INTO departments "
        "( dept_no, dept_name) "
        "VALUES ( %(dept_no)s, %(dept_name)s)"
    )

    add_dept_manager = (
        "INSERT INTO dept_manager "
        "(emp_no, dept_no, from_date, to_date) "
        "VALUES (%(emp_no)s, %(dept_no)s, %(from_date)s, %(to_date)s)"
    )

    add_title = (
        "INSERT INTO titles "
        "(emp_no, title, from_date, to_date) "
        "VALUES (%(emp_no)s, %(title)s, %(from_date)s, %(to_date)s)"
    )

    add_dept_emp = (
        "INSERT INTO dept_emp "
        "(emp_no, dept_no, from_date, to_date) "
        "VALUES (%(emp_no)s, %(dept_no)s, %(from_date)s, %(to_date)s)"
    )

    # Insert employees
    cursor.execute(add_employee, data_employee1)
    cursor.execute(add_employee, data_employee2)
    cursor.execute(add_employee, data_employee3)
    cursor.execute(add_employee, data_employee4)
    cursor.execute(add_employee, data_employee5)
    cursor.execute(add_employee, data_employee6)
    cursor.execute(add_employee, data_employee7)
    cursor.execute(add_employee, data_employee8)
    cursor.execute(add_employee, data_employee9)
    cursor.execute(add_employee, data_employee10)

    # Insert salaries
    cursor.execute(add_salary, data_salary1)
    cursor.execute(add_salary, data_salary2)
    cursor.execute(add_salary, data_salary3)
    cursor.execute(add_salary, data_salary4)
    cursor.execute(add_salary, data_salary5)
    cursor.execute(add_salary, data_salary6)
    cursor.execute(add_salary, data_salary7)
    cursor.execute(add_salary, data_salary8)
    cursor.execute(add_salary, data_salary9)
    cursor.execute(add_salary, data_salary10)

    # Insert departments
    cursor.execute(add_departments, data_dept1)
    cursor.execute(add_departments, data_dept2)
    cursor.execute(add_departments, data_dept3)
    cursor.execute(add_departments, data_dept4)
    cursor.execute(add_departments, data_dept5)
    cursor.execute(add_departments, data_dept6)

    # Insert dept managers
    cursor.execute(add_dept_manager, data_manager1)
    cursor.execute(add_dept_manager, data_manager2)
    cursor.execute(add_dept_manager, data_manager3)
    cursor.execute(add_dept_manager, data_manager4)
    cursor.execute(add_dept_manager, data_manager5)
    cursor.execute(add_dept_manager, data_manager6)
    cursor.execute(add_dept_manager, data_manager7)
    cursor.execute(add_dept_manager, data_manager8)
    cursor.execute(add_dept_manager, data_manager9)
    cursor.execute(add_dept_manager, data_manager10)

    # Insert titles
    cursor.execute(add_title, data_title1)
    cursor.execute(add_title, data_title2)
    cursor.execute(add_title, data_title3)
    cursor.execute(add_title, data_title4)
    cursor.execute(add_title, data_title5)
    cursor.execute(add_title, data_title6)
    cursor.execute(add_title, data_title7)
    cursor.execute(add_title, data_title8)
    cursor.execute(add_title, data_title9)
    cursor.execute(add_title, data_title10)

    # Insert dept employed
    cursor.execute(add_dept_emp, data_dept_emp1)
    cursor.execute(add_dept_emp, data_dept_emp2)
    cursor.execute(add_dept_emp, data_dept_emp3)
    cursor.execute(add_dept_emp, data_dept_emp4)
    cursor.execute(add_dept_emp, data_dept_emp5)
    cursor.execute(add_dept_emp, data_dept_emp6)
    cursor.execute(add_dept_emp, data_dept_emp7)
    cursor.execute(add_dept_emp, data_dept_emp8)
    cursor.execute(add_dept_emp, data_dept_emp9)
    cursor.execute(add_dept_emp, data_dept_emp10)

    cnx.commit()
    cursor.close()
    cnx.close()

    print("Logged:", strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
