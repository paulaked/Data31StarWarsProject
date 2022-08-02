from app.requesting_sw import *


if __name__ == '__main__':

    url = "http://swapi.dev/api/starships"

    db_name = "starwars"

    connection_dict = api_connection(url)
    ships_list = get_all_starships(connection_dict)
    clean_ships_list = clean_all_starships(ships_list)

    # add to collection
    clean_ships_with_names = pilots_url_to_names(clean_ships_list)
    add_to_starships_coll(clean_ships_with_names)

    ### list from db starships collection to check answer [uncomment code bellow to print list]
    
    # db = connect_with_db(db_name)
    # ships = db.starships.find({})
    # for num, s in enumerate(ships):
    #     print(num + 1, f"{s['name']} : {s['pilots']}")
