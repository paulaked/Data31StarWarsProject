# Unit Testing Plan
import requests


# Test function that pulls all available starships from api
from starwars.app.requesting_sw import *


def test_get_api():

    assert get_api().status_code == 200
