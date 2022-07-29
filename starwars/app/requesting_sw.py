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

        ships = []
        while not False:

            starships = self.get_from_api("https://swapi.dev/api/starships/?page=" + str(page_number))

            for starship in starships['results']:
                ships.append(starship)

            if starships['next'] is None:
                return ships
            else:
                page_number += 1

        #return ships

    def drop_columns(self,ships):
        '''to delete the keys as stated'''
        #print(ships)
        for ship in ships:
            try:
                del ship['url']
            except:
                print("url key doesn't exist")

            try:
                del ship["created"]
            except:
                print("created key doesn't exist")

            try:
                del ship["edited"]
            except:
                print("edited key doesn't exist")

        return ships

    def get_pilots(self, ships):

        #print(ships)
        for ship in ships:
            if ship['pilots']:
                for pilot in ship['pilots']:
                    print(self.get_from_api(pilot))
                    pilot_data = self.get_from_api(pilot)
                    


    def read_from_db(self):
        pass


get_api = GetApi()
db = get_api.set_up_db()
ships = get_api.get_starships()
ships = get_api.drop_columns(ships)
get_api.get_pilots(ships)