import pymongo
import requests
import json


def connect_with_db(local_db="starwars31"):
    client = pymongo.MongoClient()
    return client[local_db]


def create_collection(coll_name="starships"):
    db = connect_with_db()
    try:
        db.create_collection(coll_name)
    except:
        db.coll_name.drop()
        db.create_collection(coll_name)
    return db


def get_api(url):
    response = requests.get(url, headers={"Content-Type": "application/json"}).json()
    return response


def starships_db(api_db):
    results_list = []
    page = 1
    while api_db["next"] is not None:
        results_list += api_db["results"]
        page += 1
        api_db = get_api(f"https://swapi.dev/api/starships/?page={page}")
    api_db= get_api(f"https://swapi.dev/api/starships/?page={page}")
    results_list += api_db['results']
    return results_list


def clean_all_starships(starships_list):
    for item in starships_list:
        item.pop("created")
        item.pop("edited")
        item.pop("url")
    return starships_list


# ### git commit do tad
def convert_pilot_url_to_name(url):
    api_json = get_api(url)
    name = api_json['name']
    return name


def pilots_url_to_names(ships_list):
    for starship in ships_list:
        pilots_ids = []
        for pilot in starship.get("pilots"):
            pilot_name = convert_pilot_url_to_name(pilot)
            pilot_id = db.characters.find({"name": pilot_name}, {"_id": 1})
            for result in pilot_id:
                pilots_ids.append(result["_id"])
        starship["pilots"] = pilots_ids
    return ships_list


def add_to_starships_coll(documents):
    db = connect_with_db()
    return db.starships.insert_many(documents)


db = connect_with_db()
db.starships.drop()