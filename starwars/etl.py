from app.starship import Starships
import requests


def extract():
    json_response = Starships.model_response
    return json_response


def transform():
    pass


def load():
    pass

