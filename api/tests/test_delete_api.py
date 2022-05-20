import requests

base_url = "https://jsonplaceholder.typicode.com/todos/10"

data = {
    "package_id": "test-dataset",
    "name": "Test Package",
    "description": "A short description of my resource!",
    "owner_org": "company-name",
}


def test_status_code_equals_200():
    response = requests.delete(base_url, data=data)

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"


def test_status_code_equals_404():
    response = requests.delete(
        f"{base_url}/bad-path",
        data=data,
    )

    assert response.status_code == 404
