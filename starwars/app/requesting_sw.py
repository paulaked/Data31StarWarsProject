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
        pilot_data = []
        for ship in ships:
            if ship['pilots']:
                for pilot in ship['pilots']:
                    pilot_data.append(self.get_from_api(pilot))
        return pilot_data

    def add_data(self,ships):
        for ship in ships:
            self.db.starships.insert_one(ship)

    def update_data(self, ships):
        for ship in ships:
            pilots_list = []
            for pilots in ship['pilots']:
                pilot_detail = self.get_from_api(pilots)['name']
                get_id = db.characters.find_one({"name": pilot_detail})
                pilot_id = get_id.get('_id')
                pilots_list.append(pilot_id)
                ship.pop('pilots')
                ship['pilots'] = pilots_list
            # starships.update_one(updated)
            #print(ship)
            db.starships.insert_one(ship)

    #def change_data(self, ships):
        #starships = db['starships']

        #for ship in ships:
        #    pilots_list = []
        #    for pilots in ship['pilots']:
        #        pilot_detail = get_api.get_from_api(pilots)['name']
        #        get_id = db.characters.find_one({"name": pilot_detail})
        #        pilot_id = get_id.get('_id')
        #        pilots_list.append(pilot_id)
        #        ships.pop('pilots')
        #        ships['pilots'] = pilots_list
            #starships.update_one(updated)
            #print(ships)
        #    db.starships.insert_one(ships)

            #pilots_list =[]
            #for key in ships['pilots']:
                    #print(key)
                #pilot_detail = self.get_api.get_from_api(key)['name']
                #get_id = db.characters.find_one({"name": pilot_detail})
                #pilot_id = get_id.get('_id')
                #pilots_list.append(pilot_id)
                #pilots_list.append(pilot_id)
                #ships['pilots'] = pilot_id
                #print(ships['pilots'])
            #pilots_new = {"$set": {'pilots':pilots_list}}
            #myquery = db.starships.find({},{"pilots":1})
            #starships.update_one(myquery, pilots_new)

            #starships['pilots'] = pilots_list[:]
            #starships.update_one({'pilots':pilots_list})
            #starships.save(['pilots'])

        #for ships in db.starships.find():
        #    pilots_list = []
        #    for pilot in ships['pilots']:
        #        pilot_detail = get_api.get_from_api(pilot)['name']
        #        get_id = db.characters.find_one({"name": pilot_detail})
        #        pilot_id = get_id.get('_id')
        #        pilots_list.append(pilot_id)
        #        pilot = pilot_id

        #for ship in ships:
        #    db.starships.insert_one(ship)
        #    if ship['pilots'] == []:
        #        pass
        #    else:
        #        pilot_id_list = []
        #        for pilot in ship['pilots']:
        #            pilot_detail = get_api.get_from_api(pilot)['name']
        #            get_id = db.characters.find_one({"name": pilot_detail})
        #            #print(get_id.get('_id'))
        #            pilot_id = get_id.get('_id')
        #            #print(pilot)
        #            pilot_id_list.append(pilot_id)

        #        for starship in db.starships.find():
        #            starship.update({'pilots':pilot_id_list})

        #for ship in ships:
        #    for pilot in ship['pilots']:
        #        if isinstance(ship['pilots'], pilot):
        #            pilot_detail = get_api.get_from_api(pilot)['name']
        #            get_id = db.characters.find_one({"name": pilot_detail})
        #    # print(get_id.get('_id'))
        #            ship['pilots'][pilot] = get_id.get('_id')
        #    db.starships.insert_one(ship)

                #pilot_detail = get_api.get_from_api(pilot)['name']
                #get_id = db.characters.find_one({"name": pilot_detail})
                #print(get_id.get('_id'))
                #pilot = get_id.get('_id')
            #db.starships.insert_one(ship)

        #print(pilot_data)
        #print(ships)
        #for ship in ships:
        #    for pilot_url in ship['pilots']:
        #        pilot_name = get_api.get_from_api(pilot_url)["name"]
        #        pilot_id = db.characters.find({"name": pilot_name}, {"_id": 1})
        #        print(pilot_id)
                #ship.update(get_api.get_from_api(pilot_url)["_id"])

        #print(ships)
                #print(get_api.get_from_api(pilot_url))

    def read_from_db(self):
        try:
            for ships in db.starships.find({},{"name":1, "pilots": 1}):
                print(ships)
        except:
            print("Collection doesn't exist")

get_api = GetApi()
db = get_api.set_up_db()
ships = get_api.get_starships()
ships = get_api.drop_columns(ships)
pilots = get_api.get_pilots(ships)
get_api.update_data(ships)
get_api.read_from_db()
#get_api.change_data(ships)
#get_api.add_data(ships)
#get_api.change_data(ships)
#get_api.read_from_db()