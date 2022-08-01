import pymongo
import requests
import json


def connect_with_db(db_name="starwars"):
    client = pymongo.MongoClient()
    return client[db_name]


def create_collection(coll_name="starships"):
    db = connect_with_db()

    try:
        db.create_collection(coll_name)
    except:
        print("Collection already exists, all collection date will be replaced!!!")
        db.starships.drop()
        db.create_collection(coll_name)
    return db


def api_connection(url):
    headers = {"Content-Type": "application/json"}

    response = requests.get(url, headers=headers)
    return response.json()


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


def clean_all_starships(starships_list):
    for item in starships_list:
        item.pop("created")
        item.pop("edited")
        item.pop("url")
    return starships_list


# ### git commit do tad
def convert_pilot_url_to_name(url):
    api_json = api_connection(url)
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


#### transfer to main

url = "http://swapi.dev/api/starships"

db = connect_with_db()
db.starships.drop()

connection_dict = api_connection(url)
ships_list = get_all_starships(connection_dict)
clean_ships_list = clean_all_starships(ships_list)

# add to collection
clean_ships_with_names = pilots_url_to_names(clean_ships_list)
add_to_starships_coll(clean_ships_with_names)

### check db

ships = db.starships.find({})
for num, s in enumerate(ships):
    print(num+1, f"{s['name']} : {s['pilots']}")