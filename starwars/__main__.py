from app.requesting_sw import *


if __name__ == '__main__':
    get_api = GetApi()
    db = get_api.set_up_db()
    ships = get_api.get_starships()
    ships = get_api.drop_columns(ships)
    pilots = get_api.get_pilots(ships)
    get_api.update_data(ships)
    get_api.read_from_db()