import json
import requests
import pymongo


#url = requests.get("https://swapi.dev/")

class GetApi:

    def get_api(self):
        '''get status code of the api'''
        status_code = requests.get("https://swapi.dev/")
        return status_code

    def set_up_db(self):
        '''set up database and make a starships collection'''
        client = pymongo.MongoClient()
        db = client['starwars']

        try:
            db.create_collection("starships")
        except:
            print("starship collection already exists, deleting old one and replacing it with new one")
            db.starships.drop()
            db.create_collection("starships")

        print(type(db))
        return db

    def get_from_api(self, url):
        resp = requests.get(url)
        return resp.json()

    def get_starships(self):
        '''gets the starships'''
        page_number = 1 ## referencing starships page number

        starships = self.get_from_api("https://swapi.dev/api/starships/?page=" + str(page_number))

        ships = []
        for starship in starships['results']:
            ships.append(starship)
        return ships

    def get_pilots(self):


    def read_from_db(self):
        pass


get_api = GetApi()
db = get_api.set_up_db()
get_api.get_starships()