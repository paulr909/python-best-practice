import requests


def update_todo():
    api_url = "https://jsonplaceholder.typicode.com/todos/10"
    todo = {"title": "Mow lawn"}
    response = requests.patch(api_url, json=todo)
    response.json()

    print(response.status_code, response.text)


if __name__ == "__main__":
    update_todo()
