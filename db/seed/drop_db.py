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


def drop_db():
    cnx = mysql.connector.connect(**db_config)

    cursor = cnx.cursor()
    cursor.execute("DROP DATABASE IF EXISTS employees_test_db")

    cursor.close()
    cnx.close()

    print("Logged:", strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))


if __name__ == "__main__":
    drop_db()
