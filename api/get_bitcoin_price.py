from time import gmtime, strftime

import requests


def get_price():
    base_url = "https://api.coinbase.com/v2/prices/BTC-USD/buy"

    headers = {
        "Content-Type": "application/json",
        # "Authorization": "Bearer Hy84l0brc4hJ8Y8Th3htybelosbr678aUyte73KDdft",
    }

    response = requests.get(
        f"{base_url}",
        headers=headers,
    )

    print(response.status_code, response.text)


if __name__ == "__main__":
    get_price()

print("Logged:", strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
