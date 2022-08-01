from functions import *
import pymongo

client = pymongo.MongoClient()
db = client['starwars31']
db.starships.drop()             # Drops the starships collection if it already exists.
new_col = db["starships"]       # Creates a new starships collection

starships = get_starships()
for i in range(len(starships)):
    url_of_starship_i = starships[i]
    list_of_pilot_IDs_for_starship_i = pilot_ID_list(url_of_starship_i)
    data = combine_starships_and_pilotID(url_of_starship_i,list_of_pilot_IDs_for_starship_i)
    add_to_collection(data)






