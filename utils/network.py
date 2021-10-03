import requests


def fetch(*, url, headers):
    """
    Send a GET request and return response as Python object
    """

    response = requests.get(url, headers=headers)
    return response.json()
