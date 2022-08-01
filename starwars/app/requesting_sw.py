import requests
import pymongo


def set_db():
    # Connecting to the starwars database
    client = pymongo.MongoClient()
    db = client['starwars31']

    # Creating the starships collections

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


def drop_unwanted_columns(ships):
    # deleting the 'created', 'edited' and 'url'
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


def get_pilots(ships):
    pilots = []
    for ship in ships:
        if ship['pilots']:
            for pilot in ship['pilots']:
                pilots.append(get_api_info(pilot))
    return pilots


def add_data(ships):
    for ship in ships:
        db.starships.insert_one(ship)


def update_data(ships):
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


def read_from_db():
    try:
        for ships in db.starships.find({},{"name": 1, "pilots": 1}):
            print(ships)
    except:
        print("Collection doesn't exist")


db = set_db()
ships = get_starships()
ships = drop_unwanted_columns(ships)
pilots = get_pilots(ships)
update_data(ships)
read_from_db()
