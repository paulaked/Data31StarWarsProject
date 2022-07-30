import pymongo
import requests
import json


def api_connection(url):
    headers = {"Content-Type": "application/json"}

    response = requests.get(url, headers=headers)
    return response.json()

