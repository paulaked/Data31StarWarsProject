import requests
import json

#starships = requests.get("https://swapi.dev/api/starships/")
#print(starships)
#print(starships.json())


def get_api():
    url = "https://swapi.dev/api/starships/"
    request_api = requests.get(url)
    resp_json = request_api.json()

    return request_api


starship = get_api()

print(starship)
