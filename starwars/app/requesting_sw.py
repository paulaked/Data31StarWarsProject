import requests
import json
import pymongo


def set_db(dbname):
    # Connect to the starwars database
    client = pymongo.MongoClient()
    db = client[dbname]

    # Checking if the starships collections exists

    try:
        db.create_collection("starships")

    except pymongo.errors.CollectionInvalid:
        print("Collection Starships already exists")
        db.drop_collection("starships")
        db.create_collection("starships")

    finally:
        print("The Starships collection has been deleted and recreated")

    return db


def get_api():
    url = "https://swapi.dev/api/starships/"
    request_api = requests.get(url)

    return request_api

#def

