import requests
import pytest
from starwars.app.requesting_sw import*
# Test function that pulls all available starships from api

def test_conection_status_code():
    response = requests.get("http://swapi.dev/api/starships")
    assert response.status_code == 200

