from model import StarshipModel
import requests
from config_manager import *

class Starships():
    def __init__(self) -> None:
        self.url = SWAPI_STARSHIPS
        self.request = requests.get(self.url)
        self.response = self.request.json()

    def model_response(self):
        return StarshipModel(self.response)
