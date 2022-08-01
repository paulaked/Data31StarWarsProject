import requests
import json

# Calling the API
json_body = {"Content-Type": "application/json"}
starships_req = requests.get("http://swapi.dev/api/starships", headers=json_body)
print(starships_req.json())

