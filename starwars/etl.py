from app.starship import Starships
import starwars.config_manager as sw_conf
import requests
import pymongo

connect = pymongo.MongoClient()
db = connect['starwars']
characters = db.characters


def get_pilot(pilot_url):
    response = requests.get(pilot_url)
    pilot_data = response.json()
    pilot_name = pilot_data['name']
    pilot_record = characters.find({"name": pilot_name})
    return pilot_record['_id']


def get_film(film_url):
    response = requests.get(film_url)
    film_data = response.json()
    return film_data['title']


def replace_pilots(starship_pilots):
    for index, pilot in enumerate(starship_pilots):
        pilot_name = get_pilot(pilot)
        starship_pilots[index] = pilot_name
    return starship_pilots


def replace_films(starship_films):
    for index, film in enumerate(starship_films):
        film_title = get_film(film)
        starship_films[index] = film_title
    return starship_films


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


def transform(starship_data):
    for index, starship in enumerate(starship_data):
        if len(starship['pilots']) > 0:
            starship_pilots = starship['pilots']
            starship[index] = replace_pilots(starship_pilots)
        if len(starship['films']) > 0:
            starship_films = starship['films']
            starship[index] = replace_films(starship_films)
    return starship_data


def load():
    pass
