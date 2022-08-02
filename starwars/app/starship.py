from app.model import StarshipModel
import requests


def convert_to_dict(starship):
    return {"name": starship.name,
            "model": starship.model,
            "starship_class": starship.starship_class,
            "manufacturer": starship.manufacturer,
            "cost_in_credits": starship.cost_in_credits,
            "length": starship.length,
            "crew": starship.crew,
            "passengers": starship.passengers,
            "max_atmosphering_speed": starship.max_atmosphering_speed,
            "mglt": starship.mglt,
            "cargo_capacity": starship.cargo_capacity,
            "consumables": starship.consumables,
            "films": starship.films,
            "pilots": starship.pilots
            }

class Starships:
    def __init__(self, url: object) -> None:
        self.url: str = url
        self.request = requests.get(self.url)
        self.response = self.request.json()
        self.sw_list: list = []

    def model_response(self):
        starships = self.response
        for starship in starships['results']:
            starship = StarshipModel(starship)
            starship = convert_to_dict(starship)
            self.sw_list.append(starship)
        return self.sw_list


