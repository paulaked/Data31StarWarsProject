from starwars.app.requesting_sw import *

db = set_db()
ships = get_starships()
ships = drop_unwanted_columns(ships)
pilots = get_pilots(ships)
insert_data(ships)
print(read_from_db("X-wing"))
