import requests
import pytest


def test_api_connection():
    url = "http://swapi.dev/api/starships"
    response = requests.get(url)
    assert response.status_code == 200


