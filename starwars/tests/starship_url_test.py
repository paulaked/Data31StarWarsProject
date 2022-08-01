import requests
import json
#making sure api functions well
def test_api():
    response = requests.get("https://swapi.dev/api/")
    assert response.status_code == 200
    return(response)
print(test_api())