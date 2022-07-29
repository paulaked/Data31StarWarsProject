import json
import requests


#url = requests.get("https://swapi.dev/")

class GetApi:

    def get_api(self):
        status_code = requests.get("https://swapi.dev/")
        return status_code