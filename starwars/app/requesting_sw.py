import requests
import json
import pymongo

# Connect to 'starwars31' database from mongodb
client = pymongo.MongoClient()
db = client['starwars31']

characters = db.characters.find()

for character in characters:
    print(character)

# Calling the API (getting)
json_body = {"Content-Type": "application/json"}
starships_req = requests.get("http://swapi.dev/api/starships", headers=json_body)
print(starships_req.json())

