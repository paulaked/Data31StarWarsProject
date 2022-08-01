from model import StarshipModel
import requests
import starwars.config_manager as sw_conf


class Starships():
    def __init__(self) -> None:
        self.url = sw_conf.SWAPI_STARSHIPS
        self.request = requests.get(self.url)
        self.response = self.request.json()

    def model_response(self):
        return StarshipModel(self.response)

