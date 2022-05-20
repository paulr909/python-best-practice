from db.csv_json import csv_json
from db.export_sql import connect_db

csv_file_path = "data/employees.csv"
json_file_path = "data/employees.json"


def main():
    connect_db()
    csv_json(csv_file_path, json_file_path)


if __name__ == "__main__":
    main()
