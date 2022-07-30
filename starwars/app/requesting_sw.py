import pymongo
import requests
import json


def api_connection(url):
    headers = {"Content-Type": "application/json"}
    response = requests.get(url, headers=headers)
    return response.json()


def get_all_starships(api_dict):
    pass


