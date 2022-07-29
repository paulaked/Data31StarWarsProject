import requests
import pymongo

starships = requests.get("https://swapi.dev/api/starships/")
print(starships)
print(starships.json())

client = pymongo.MongoClient()
db = client['starwars']

#db.create_collection("ships")
db.drop_collection("ships")

