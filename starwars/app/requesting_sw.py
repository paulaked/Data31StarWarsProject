import pymongo
import requests
import json


def api_connection(url):
    headers = {"Content-Type": "application/json"}
    response = requests.get(url, headers=headers)
    return response.json()


def get_all_starships(api_dict):
    results_list = []
    page = 1
    while api_dict["next"] is not None:
        results_list += api_dict["results"]
        page += 1
        api_dict = api_connection(f"https://swapi.dev/api/starships/?page={page}")
    api_dict = api_connection(f"https://swapi.dev/api/starships/?page={page}")
    results_list += api_dict['results']
    return results_list


url = "http://swapi.dev/api/starships"

connection_dict = api_connection(url)
ships_list = get_all_starships(connection_dict)

print(connection_dict)
print(ships_list)