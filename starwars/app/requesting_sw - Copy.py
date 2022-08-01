# importing required packages and setting up connection to database
import pymongo
import requests

client = pymongo.MongoClient()
db = client['starwars']
base_url = 'https://swapi.dev/api/'


# imports raw data from url to collection in database
def import_data():
    # deletes any pre-existing collections called starships
    db.drop_collection("starships")
    # creating new starships collection
    starships = db["starships"]
    # As long as next page exists go to next page
    valid_page = True
    i = 1
    while valid_page:
        # get data from page in json from
        resp = requests.get('https://swapi.dev/api/starships/?page=%i' % i)
        data = resp.json()
        # insert starship data from results key
        for starship in data["results"]:
            starships.insert_one(starship)
        i += 1
        if data['next'] is None:
            valid_page = False