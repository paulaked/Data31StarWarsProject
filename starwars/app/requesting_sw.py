import requests
import pymongo
import json


# noinspection PyUnresolvedReferences
def set_db():
    # Connecting to the starwars database
    client = pymongo.MongoClient()
    db = client['starwars31']

    # Creating the starships collections

    try:
        db.create_collection("starships")
        # noinspection PyUnresolvedReferences

    except pymongo.errors.CollectionInvalid:
        return "Starships collection already exists and will be deleted."
        db.drop_collection("starships")
        db.create_collection("starships")

    finally:
        return db



def api_status():
    # Checking the status code of the API
    url = "https://swapi.dev/api/starships/"
    code = requests.get(url)

    return code


def get_api_info(url):
    # Exploring the Star ships information from the API
    response = requests.get(url).json()
    return response


def get_starships():
    # Creating a list of the Star ships.
    pg_number = 1
    ships = []
    while not False:

        starships = get_api_info("https://swapi.dev/api/starships/?page=" + str(pg_number))

        for starship in starships['results']:
            ships.append(starship)

        if starships['next'] is None:
            return ships
        else:
            pg_number += 1


def drop_unwanted_columns(ships):
    # deleting the 'created', 'edited' and 'url' details from the starship information.
    for ship in ships:
        try:
            del ship['url']
        except:
            return "Url Key has been removed."

        try:
            del ship['edited']
        except:
            return "Edited Key has been removed."

        try:
            del ship['created']
        except:
            return "Created Key has been removed."

    return ships


def get_pilots(ships):
    # Creating a list of the pilots found in the Star ships list.
    pilots = []
    for ship in ships:
        if ship['pilots']:
            for pilot in ship['pilots']:
                pilots.append(get_api_info(pilot))
    return pilots


def insert_data(ships):
    # Inserting the Pilot ID referenced from the Characters Collection into the Star ships collection.
    for ship in ships:
        pilot_list = []
        for pilots in ship['pilots']:
            pilot_info = get_api_info(pilots)['name']
            get_id = db.characters.find_one({"name": pilot_info})
            pilot_id = get_id.get('_id')
            pilot_list.append(pilot_id)
            ship.pop('pilots')
            ship['pilots'] = pilot_list
        db.starships.insert_one(ship)


def read_from_db(starship):
    # Reading the name and pilot list from the newly transformed data from the Star Wars database.
    try:
        for ships in db.starships.find({"name": starship}, {"_id": 0}):
            return ships
    except:
        return "Collection doesn't exist"


db = set_db()
'''ships = get_starships()
ships = drop_unwanted_columns(ships)
pilots = get_pilots(ships)
insert_data(ships)
read_from_db("X-wing")'''
