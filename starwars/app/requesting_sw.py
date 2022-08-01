# importing required packages and setting up connection to database
import pymongo
import requests

client = pymongo.MongoClient()
db = client['starwars31']
base_url = 'https://swapi.dev/api/'


# find all entries for pilot and replace the URL's with ObjectId's from character collection
def replace_pilots():
    # iterates through each starship in collection
    for starship in db.starships.find({}):
        pilot_ids = []
        # iterates through each pilot in pilots field of starship
        for pilot in starship["pilots"]:
            # return data on pilot
            resp = requests.get(pilot)
            data = resp.json()
            # find ObjectID of pilot from characters and add to a list
            pilot_object = db.characters.find_one({"name": data["name"]}, {"_id": 1})
            pilot_ids.append(pilot_object["_id"])
        # replace starships pilots list with list of pilot ObjectId's
        db.starships.update_one({"name": starship["name"]}, {"$set": {"pilots": pilot_ids}})