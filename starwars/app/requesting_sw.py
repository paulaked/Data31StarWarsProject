import pymongo
import requests


def set_up_db():
    # Connect to 'starwars31' database.
    client = pymongo.MongoClient()
    db = client['starwars31']

    # Check if collection already exists.
    try:
        db.create_collection("starships")
    except:
        print("Starship collection exists. This collection has been deleted and a new one has been created.")
        db.starships.drop()
        db.create_collection("starships")
    return db


def get_from_api(url):
    response = requests.get(url)
    return response