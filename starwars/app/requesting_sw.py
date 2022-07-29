import pymongo
import requests


def get_api(url):  # get API
    response = requests.get(url)
    return response


def db_link(name):  # Connect to database 'starwars'
    client = pymongo.MongoClient()
    db = client[name]

    try:  # check if collection exists
        db.create_collection("starships")
    except:
        print("Starship collection already exists")
        db.starships.drop()
        db.create_collection("starships")
    return db
