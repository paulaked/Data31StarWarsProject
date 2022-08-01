import pymongo
import requests
import json


def connect_with_db(db_name="starwars"):
    client = pymongo.MongoClient()
    return client[db_name]


def create_collection(coll_name="starships"):
    db = connect_with_db()
    return db.create_collection(coll_name)


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


#
# ### git commit do tad
# def convert_people_url_to_name(url="https://swapi.dev/api/people/13/"):
#     api_json = api_connection(url)
#     name = api_json['name']
#     return name
#
#
# #### pilots extraction
# def change_pilot_to_name():
#     for starship in clean_ships_list:
#         pilots = starship.get("pilots")
#         if len(pilots) == 0:
#             continue
#         else:
#             pilots_names = []
#             for pilot in pilots:
#                 pilots_names.append(convert_people_url_to_name(pilot))
#             starship["pilots"] = pilots_names


url = "http://swapi.dev/api/starships"

# db = connect_with_db()
starships_collection = create_collection()
print(starships_collection)

# connection_dict = api_connection(url)

# ships_list = get_all_starships(connection_dict)
# clean_ships_list = clean_all_starships(ships_list)

# for el in clean_ships_list:
#     print(el["pilots"])


#### mongo


# characters = db.characters.find({"name":"Chewbacca"},{"name":1})

# for char in characters:
#     ch = char
#     print(char)
# print(type(ch["_id"]))
# for i, x in enumerate(clean_ships_list):
#     print(i+1, x)
