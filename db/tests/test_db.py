def test_departments_table_exists(cursor):
    cursor.execute("SELECT dept_no FROM departments")
    rs = cursor.fetchall()
    assert len(rs) == 6


def test_select_departments_item(cursor):
    cursor.execute("SELECT dept_no FROM departments")
    rs = cursor.fetchone()
    assert len(rs) == 1


def test_dept_emp_table_exists(cursor):
    cursor.execute("SELECT emp_no FROM dept_emp")
    rs = cursor.fetchall()
    assert len(rs) == 10


def test_select_get_dept_emp_item(cursor):
    cursor.execute("SELECT emp_no FROM dept_emp")
    rs = cursor.fetchone()
    assert len(rs) == 1


def test_dept_manager_table_exists(cursor):
    cursor.execute("SELECT emp_no FROM dept_manager")
    rs = cursor.fetchall()
    assert len(rs) == 10


def test_select_dept_manager_item(cursor):
    cursor.execute("SELECT emp_no FROM dept_manager")
    rs = cursor.fetchone()
    assert len(rs) == 1


def test_employees_table_exists(cursor):
    cursor.execute("SELECT emp_no FROM employees")
    rs = cursor.fetchall()
    assert len(rs) == 10


def test_select_employees_item(cursor):
    cursor.execute("SELECT emp_no FROM employees")
    rs = cursor.fetchone()
    assert len(rs) == 1


def test_salaries_table_exists(cursor):
    cursor.execute("SELECT emp_no FROM salaries")
    rs = cursor.fetchall()
    assert len(rs) == 10


def test_select_salaries_item(cursor):
    cursor.execute("SELECT emp_no FROM salaries")
    rs = cursor.fetchone()
    assert len(rs) == 1


def test_titles_table_exists(cursor):
    cursor.execute("SELECT emp_no FROM titles")
    rs = cursor.fetchall()
    assert len(rs) == 10


def test_select_title_item(cursor):
    cursor.execute("SELECT emp_no FROM titles")
    rs = cursor.fetchone()
    assert len(rs) == 1
