import requests
import pytest
from starwars.app.requesting_sw import *


def test_connection_status_code():
    url = "http://swapi.dev/api/starships"
    response = requests.get(url)
    assert response.status_code == 200


def test_api_connection():
    assert isinstance(api_connection("http://swapi.dev/api/starships"), dict)

