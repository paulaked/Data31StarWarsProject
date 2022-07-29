import pymongo
import requests


def set_up_db():
    # Connect to 'starwars31' database.
    client = pymongo.MongoClient()
    db = client['starwars31']

    # Check if collection already exists.
    try:
        db.create_collection("starships")
    except:
        print("Starship collection exists. This collection has been deleted and a new one has been created.")
        db.starships.drop()
        db.create_collection("starships")
    return db


# Calls 'Star Wars' API.
def get_from_api(url):
    response = requests.get(url)
    return response


def dl_trans_ins(db):
    # Checks if last page of JSON data has been reached
    end_of_json = False
    page_no = 1

    print("Processing...")

    while not end_of_json:

        starships = get_from_api("https://swapi.dev/api/starships/?page=" + str(page_no)).json()

        for starship in starships['results']:

            # List to store Object IDs of pilots.
            pilots_list = []

            for pilot in starship['pilots']:

                # Get the Object IDs of each pilot in the list.
                pilot_details = get_from_api(pilot).json()
                pilot_name = pilot_details['name']
                person_id = db.characters.find({"name": pilot_name}, {"_id": 1})

                for id_value in person_id:
                    pilots_list.append(id_value["_id"])

            # Replace the list of URLs in 'pilots' key with Object IDs from 'characters' collection.
            pilots = {'pilots': pilots_list}
            starship.update(pilots)

            # The 'created', 'edited' and 'url' fields need to removed from the JSON objects.
            fields_to_be_removed = ['created', 'edited', 'url']
            for fields in fields_to_be_removed:
                starship.pop(fields)

            # Insert transformed JSON objects as documents in 'starships' collection.
            db.starships.insert_one(starship)

        # All data has been processed once last page of data has been reached.
        if starships['next'] is None:
            print("Done.")
            end_of_json = True
        else:
            page_no += 1

    return end_of_json


def read_from_db(db):
    # Loops through all documents in the 'starships' collection and displays their names and pilots.

    try:
        for name_pilots in db.starships.find({}, {"_id": 0, "name": 1, "pilots": 1}):
            print(name_pilots)
    except:
        return False

    return True


db = set_up_db()
dl_trans_ins(db)
read_from_db(db)
