from app.model import StarshipModel
import requests
import starwars.config_manager as sw_conf


class Starships:
    def __init__(self) -> None:
        self.url: str = sw_conf.SWAPI_STARSHIPS
        self.request = requests.get(self.url)
        self.response = self.request.json()
        self.sw_dict: dict = {}

    def model_response(self):
        starships = self.response['results']
        for starship in starships:
            StarshipModel(starship)
            print(starship)
            self.sw_dict.update({starship['name']: starship})


Starships.model_response()
print(Starships.sw_dict)
