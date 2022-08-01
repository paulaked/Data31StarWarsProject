from app.starship import Starships
import starwars.config_manager as sw_conf


def extract():
    url = sw_conf.SWAPI_STARSHIPS
    starships: list = []
    isNext = True
    while isNext:
        starships_list = Starships(url)
        page = starships_list.model_response()
        starships.extend(page)
        if starships_list.response['next'] is None:
            isNext = False
        else:
            url = starships_list.response['next']
    return starships

def transform():
    pass


def load():
    pass

