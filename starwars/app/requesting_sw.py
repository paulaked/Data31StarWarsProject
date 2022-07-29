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
    code = requests.get(url)

    return code


def get_api_info(url):

    response = requests.get(url)
    return response.json()


def get_starships():
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


def drop_unwated_columns(ships):
    # delete the 'created', 'edited' and 'url'
    for ship in ships:
        try:
            del ship['url']
        except:
            print("Url Key has been removed.")

        try:
            del ship['edited']
        except:
            print("Edited Key has been removed.")

        try:
            del ship['created']
        except:
            print("Created Key has been removed.")

    return ships

