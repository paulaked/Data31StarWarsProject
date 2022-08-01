import requests
import json
import pymongo

# Connect to 'starwars31' database from mongodb
def connect_db():
    client = pymongo.MongoClient()
    db = client['starwars31']

    try:
        db.create_collection("starship")

    except pymongo.errors.CollectionInvalid:
        print("Collection Startship already exists")
        db.drop_collection("starships")
        db.create_collection("starships")

    finally:
        print("The starship collection has been deleted and recreated")

    return db


def call_api():
    # Calling the API (getting)
    json_body = {"Content-Type": "application/json"}
    starships_req = requests.get("http://swapi.dev/api/starships", headers=json_body)
    print(starships_req.json())



def starships_db():
    results_lis
