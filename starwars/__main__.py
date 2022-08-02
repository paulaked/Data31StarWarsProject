from app.Update import * # Calling my code from another file within the folder

# Extra
# user_URL = input(What sourse of api would you like to you)

'''
URL that will be connected to in order to get starwars starship information from
'''
url = "http://swapi.dev/api/starships"


# Calling on this function will get all the api data
connection_dict = get_api(url)
# Calling this function will call on the get_api function and create a list of starships db
ships_list = starships_db(connection_dict)
# using pop to drop information not needed to original starship data
clean_ships_list = clean_all_starships(ships_list)

# Getting the url in json form and replacing it
clean_ships_with_names = pilots_url_to_names(clean_ships_list)
# replacing names with ObjectId
add_to_starships_coll(clean_ships_with_names)

# Printing out the ships in a loop
ships = db.starships.find({})
for num, s in enumerate(ships):
    print(num+1, f"{s['name']} : {s['pilots']}")