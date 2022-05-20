import mysql.connector
import pytest
from decouple import config


@pytest.fixture(scope="module")
def connect():
    cnx = mysql.connector.connect(
        host="localhost",
        database="employees_test_db",
        user="root",
        password="root",
    )
    yield cnx
    cnx.close()


@pytest.fixture
def cursor(connect):
    cursor = connect.cursor()
    yield cursor
    connect.rollback()
