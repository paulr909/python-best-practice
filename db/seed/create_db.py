from time import gmtime, strftime

import mysql.connector
from create_tables import create_tables
from decouple import config
from seed_db import seed_db

db_config = {
    "host": config("TEST_DB_HOST", default="localhost"),
    # Missing "database": as we are creating a new test DB
    "user": config("TEST_DB_USER"),
    "password": config("TEST_DB_PASSWORD"),
    "raise_on_warnings": True,
}


def create_db():
    cnx = mysql.connector.connect(**db_config)

    cursor = cnx.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS employees_test_db")

    cursor.close()
    cnx.close()

    print("Logged:", strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))


if __name__ == "__main__":
    create_db()
    create_tables()
    seed_db()
