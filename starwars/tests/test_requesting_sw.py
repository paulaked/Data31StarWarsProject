import requests
import pytest
from starwars.app.requesting_sw import *

url = "http://swapi.dev/api/starships"


def test_connection_status_code():
    response = requests.get(url)
    assert response.status_code == 200


def test_api_connection():
    assert isinstance(api_connection(url), dict)


def test_get_all_starships():
    response_json = requests.get(url).json()
    all_starships = response_json['count']
    assert len(get_all_starships(api_connection(url))) == all_starships
