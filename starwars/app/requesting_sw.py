import pymongo
import requests
import json


# function connectiong to mongo database
def connect_with_db(db_name="starwars"):
    client = pymongo.MongoClient()
    return client[db_name]


# function creating new collection "starships" in starwars database
def create_collection(db_name = "starwars",coll_name="starships"):
    db = connect_with_db(db_name)

    try:
        db.create_collection(coll_name)
    except:
        print("Collection already exists, all collection date will be replaced!!!")
        db.starships.drop()
        db.create_collection(coll_name)
    return db


# function connecting to API and returning json object as a response result
def api_connection(url):
    headers = {"Content-Type": "application/json"}

    response = requests.get(url, headers=headers)
    return response.json()


# function saving all starships information from API into list
def get_all_starships(api_dict):
    results_list = []
    page = 1
    while api_dict["next"] is not None:
        results_list += api_dict["results"]
        page += 1
        api_dict = api_connection(f"https://swapi.dev/api/starships/?page={page}")
    api_dict = api_connection(f"https://swapi.dev/api/starships/?page={page}")
    results_list += api_dict['results']
    return results_list


# function which remove not needed fields from starships list
def clean_all_starships(starships_list):
    for item in starships_list:
        item.pop("created")
        item.pop("edited")
        item.pop("url")
    return starships_list


# function converting pilot url address to pilot name
def convert_pilot_url_to_name(url):
    api_json = api_connection(url)
    name = api_json['name']
    return name


# function converting pilots names to object ID from characters collection (foreign key link)
def pilots_url_to_names(ships_list, db_name= "starwars"):
    add_collection = create_collection(db_name)
    for starship in ships_list:
        pilots_ids = []
        for pilot in starship.get("pilots"):
            pilot_name = convert_pilot_url_to_name(pilot)
            pilot_id = add_collection.characters.find({"name": pilot_name}, {"_id": 1})
            for result in pilot_id:
                pilots_ids.append(result["_id"])
        starship["pilots"] = pilots_ids
    return ships_list


# function inserting all document into new collection
def add_to_starships_coll(documents):
    db = connect_with_db()
    return db.starships.insert_many(documents)