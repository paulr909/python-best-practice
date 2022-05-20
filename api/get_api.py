import requests


def get_todo():
    api_url = "https://jsonplaceholder.typicode.com/todos/1"
    response = requests.get(api_url)
    response.json()

    print(response.status_code, response.text)


if __name__ == "__main__":
    get_todo()
