from app.model import StarshipModel
import requests


class Starships:
    def __init__(self, url) -> None:
        self.url: str = url
        self.request = requests.get(self.url)
        self.response = self.request.json()
        self.sw_list: list = []

    def model_response(self):
        starships = self.response
        for starship in starships['results']:
            StarshipModel(starship)
            self.sw_list.append(starship)
        return self.sw_list
