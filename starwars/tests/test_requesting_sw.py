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
