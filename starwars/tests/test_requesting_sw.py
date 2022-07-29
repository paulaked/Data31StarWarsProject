# Unit Testing Plan

from starwars.app.requesting_sw import *
# Test function that pulls all available starships from api


def test_get_api():

    assert get_api().status_code == 200

def test_get_api_info():

    pass

def test_get_starships():

    pass

def test_drop_unwanted_columns():

    pass