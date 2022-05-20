import json

import requests

# def post_todo():
# api_url = "https://jsonplaceholder.typicode.com/todos"
# todo = {"userId": 1, "title": "Buy milk", "completed": False}
# response = requests.post(api_url, json=todo)
# response.json()

# print(response.status_code, response.text)

# With Headers


def post_todo():
    api_url = "https://jsonplaceholder.typicode.com/todos"
    todo = {"userId": 1, "title": "Buy milk", "completed": False}
    headers = {"Content-Type": "application/json"}
    response = requests.post(api_url, data=json.dumps(todo), headers=headers)
    response.json()

    print(response.status_code, response.text)


if __name__ == "__main__":
    post_todo()
