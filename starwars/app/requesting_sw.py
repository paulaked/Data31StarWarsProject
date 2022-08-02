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

def replace_order_ids():
    # Extract the starship URLs which link to the pilot details.
    starship_details = []
    for item in get_data():
        for elements in item:
            starship_details.append(requests.get(elements["url"]).json()["result"]["properties"])
            
    # Change pilot URLs with list of character OIDs.
    replaced_data = []
    for starship in starship_details:
        pilot_list = []
        for pilot in starship["pilots"]:
            # find the pilot's name and search characters db to find the objectID
            name = requests.get(pilot).json()["result"]["properties"]["name"]
            pilot_id = db.characters.find_one({"name": name}, {"_id": 1})
            pilot_list.append(pilot_id)
        starship.update({'pilots': pilot_list})
        replaced_data.append(starship)
    return replaced_data        
