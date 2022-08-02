import pymongo
import requests

client = pymongo.MongoClient()
db = client["starwars31"]


# drop existing starships collections
def drop_starships():
    if db.starships.find({}) != "":
        db.starships.delete_many({})
        # drops the entire collection
    db.starships.drop()
    
def get_data():
    # Get starships data from API
    starships = []
    data = requests.get("https://www.swapi.tech/api/starships/").json()
    starships.append(data["results"])
    while data["next"]:
        data = requests.get(data["next"]).json()
        starships.append(data["results"])
    return starships
