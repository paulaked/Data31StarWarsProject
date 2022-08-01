import pymongo
import requests

client = pymongo.MongoClient() # Connect to MongoDB.
db = client["starwars"] # Connect to the starwars database.

# function to drop the star ship collection if it already exists in the database
def del_starships():
    if db.starships.find({}) != "":
        db.starships.delete_many({})
    db.starships.drop()

# function to take an api url as a parameter, then converts the response into a json format.
def get_data_api():
    starships = []
    data_api = requests.get("https://www.swapi.tech/api/starships/").json()
    starships.append(data_api["results"])
    while data_api["next"]:
        data_api = requests.get(data_api["next"]).json()
        starships.append(data_api["results"])
    return starships

# function to replace the pilots url in the pilot field, with the pilots object IDs.
# search for the pilot's name and characters db to find their ObjectID.
def replace_object_ids():
    starship_dets = []
    for item in pull_data():
        for elements in item:
            starship_dets.append(requests.get(elements["url"]).json()["result"]["properties"])
    replace_object_ids_data = []
    for starship in starship_dets:
        pilot_list = []
        for pilot in starship["pilots"]:
            name = requests.get(pilot).json()["result"]["properties"]["name"]
            pilot_id = db.characters.find_one({"name": name}, {"_id": 1})
            pilot_list.append(pilot_id)
        starship.update({'pilots': pilot_list})
        replace_object_ids_data.append(starship)
    return replace_object_ids_data

# function to add the starships into the database
# making sure to prevent any insertions of the pilots section for empty entries.
def starships_insert_data():
    del_starships()
    db.create_collection("starships")
    for value in replace_object_ids():
        if not value["pilots"]:
            del value["pilots"]
        db.starships.insert_one(value)

