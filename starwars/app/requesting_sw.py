import pymongo
import requests
import json


def api_connection():
    url = "http://swapi.dev/api/starships"
    headers = {'Content-Type': 'application/json'}
    json_body = json.dumps(["starships"])

    response = requests.get(url, headers=headers, data=json_body)
    return response.json()


print(api_connection())
