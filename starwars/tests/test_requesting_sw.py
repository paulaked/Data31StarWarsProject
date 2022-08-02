# Unit Testing Plan
import requests
from app.requesting_sw import *

# the 200 status code means the requests works
def check_api_request():
    check_starwars_api = requests.get("https://swapi.dev/api/")
    assert check_starwars_api.status_code == 200

# checking order_id's is a string
def test_get_from_order_ids():
    for i in replace_order_ids():
        assert type(i['name']) is str    

# checking get_data is a string
def test_get_data():
    for i in get_data():
        assert type(i['name']) is str

# checking drop_starships is a dictionary
def test_drop_starships():
    for i in drop_starships():
        for j in i['pilots']:
            assert type(j) is str

    x = 0
    for i in db.starships.find({}):
        assert type(i) is dict

# checking add_starships is a dictionary
def test_add_starships():
    for i in test_add_starships().find({}):
        for j in i['pilots']:
            assert type(j) is dict
