# Unit Testing Plan

# Test function that pulls all available starships from api
import requests
import json

json_body = json.dumps(["starships"])
headers = {'Content-Type':'application/json'}
starship_req = requests.get("https://swapi.dev/api/starships/",headers=headers, data=json_body)

print(starship_req)
