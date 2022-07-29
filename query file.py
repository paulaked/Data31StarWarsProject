import requests
import pymongo

starships = requests.get("https://swapi.dev/api/starships/"+str(2)).json()
#print(starships)
#print(starships.json())

client = pymongo.MongoClient()
db = client['starwars31']

#db.create_collection("ships")
#db.drop_collection("starships")

url = "https://swapi.dev/api/starships/"


def get_api_info():

    response = requests.get(url).json()
    return response

#starships = get_api_info()
#print(starships)

def get_ships():
    pg_num = 1

    ships=[]
    while not False:
        star_ships = requests.get("https://swapi.dev/api/starships/?page=" + str(pg_num)).json()

        for star_ship in star_ships['results']:
            ships.append(star_ship)

        if star_ships['next'] is None:
            return ships
        else:
            pg_num += 1
    return ships

ships = get_ships()



'''def transform(db):

    json_end = False
    page_num = 1

    while not json_end:

        starships = requests.get("https://swapi.dev/api/starships/?page="+str(page_num)).json()

        for starship in starships['results']:

            pilots = []

            for pilot in starship['pilots']:
                pilot_info = get_api_info(pilot).json()
                pilot_name = pilot_info['name']
                char_id = db.characters.find({"name": pilot_name}, {"_id": 1})

                for id_value in char_id:
                    pilots.append(id_value["_id"])

            pilots_info = {'pilots': pilots}
            starship.update(pilots_info)

            fields_to_remove = ['created', 'edited', 'url']
            for fields in fields_to_remove:
                starship.pop(fields)

            db.starships.insert_one(starship)

        if starships['next'] is None:
            print("Finished.")
            json_end = True

        else:
            page_num += 1

    return json_end

starwars31 = transform("starwars31")'''

