import csv
import os
from time import gmtime, strftime

import mysql.connector
from decouple import config
from mysql.connector import errorcode

db_config = {
    "host": config("DB_HOST", default="localhost"),
    "database": config("DB_NAME"),
    "user": config("DB_USER"),
    "password": config("DB_PASSWORD"),
    "raise_on_warnings": True,
}


def connect_db():
    file_path = "data/employees.csv"
    cnx = None

    if os.path.exists(file_path):

        try:
            cnx = mysql.connector.connect(**db_config)

        except mysql.connector.Error as e:
            if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif e.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(e.args[1])
                print("Database connection unsuccessful")

        cursor = cnx.cursor()

        sql_select = "SELECT * FROM employees"

        try:
            cursor.execute(sql_select)
            # Fetch the data
            results = cursor.fetchall()
            # Extract the table headers
            headers = [i[0] for i in cursor.description]

            csv_from_sql = csv.writer(
                open(file_path, "w", newline=""),
                delimiter=",",
                lineterminator="\r\n",
                quoting=csv.QUOTE_NONE,
                escapechar="\\",
            )

            csv_from_sql.writerow(headers)
            csv_from_sql.writerows(results)
            print("Data export successful")

        except mysql.connector.Error as e:
            print(e.errno)
            print("Data export unsuccessful")

        finally:
            cursor.close()
            cnx.close()

    else:
        print("File path does not exist")

    print("Logged:", strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
