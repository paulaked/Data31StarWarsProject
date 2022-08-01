# Unit Testing Plan
import pymongo.database
import pytest


from starwars.app.requesting_sw import *
# Test function that pulls all available starships from api
url = "https://swapi.dev/api/starships/"


def test_set_db():
    # See if the database exists
    assert(type(set_db('starwars')), pymongo.database.Database)


def test_get_api():
    # See if the api is valid.
    assert get_api().status_code == 200


def test_get_api_info():
    # Checking that the response from the API is in dictionary form.
    response = {"key": "value"}
    assert type(get_api_info(url)) == type(response)


def test_get_starships():
    # Ensuring that all ships have been extracted from the API.
    total_ships = get_api_info(url)['count']
    assert len(get_starships()) == total_ships
