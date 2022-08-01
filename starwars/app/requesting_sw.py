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


def tform_in(db):  # Checks if last page of JSON data has been reached
    final = False
    page = 1

    print("continue")

    while not final:

        starships = get_api("https://swapi.dev/api/starships/?page=" + str(page)).json()

        for starship in starships['results']:

            list_of_pilots = []  # store pilot IDs

            for pilot in starship['pilots']:  # get all Object IDs for pilots

                details_of_pilots = get_api(pilot).json()
                name_of_pilot = details_of_pilots['name']
                person_id = db.characters.find({"name": name_of_pilot}, {"_id": 1})  # get pilot name

                for id_value in person_id:  # append list of URLs in pilots with Object IDs
                    list_of_pilots.append(id_value["_id"])

            pilots = {'pilots': list_of_pilots}
            starship.update(pilots)

            remove_field = ['url', 'edited', 'created']  # remove additional objects
            for fields in remove_field:
                starship.pop(fields)

            db.starships.insert_one(starship)  # insert new objects into 'starships'

        if starships['next'] is None:  # iterate over all pages
            print("Finish")
            final = True
        else:
            page += 1

    return final


def read_db(db):  # Loop through starships collection and give the names and pilots

    try:
        for name_pilots in db.starships.find({}, {"_id": 0, "name": 1, "pilots": 1}):
            print(name_pilots)
    except:
        return False

    return True
