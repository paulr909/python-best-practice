import requests


def delete_todo():
    api_url = "https://jsonplaceholder.typicode.com/todos/10"
    response = requests.delete(api_url)
    response.json()

    print(response.status_code, response.text)


if __name__ == "__main__":
    delete_todo()
