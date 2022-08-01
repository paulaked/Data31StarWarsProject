# Unit Testing Plan
import pymongo.database
import unittest
from bson import ObjectId

from starwars.app.requesting_sw import *

# Test function that pulls all available starships from api
url = "https://swapi.dev/api/starships/"


class Tests(unittest.TestCase):
    def test_set_db(self):
        # See if the database exists
        assert (type(set_db()), pymongo.database.Database)

    def test_api_status(self):
        # See if the api is valid.
        assert api_status().status_code == 200

    def test_get_api_info(self):
        # Checking that the response from the API is in dictionary form.
        response = {"key": "value"}
        assert type(get_api_info(url)) == type(response)

    def test_get_starships(self):
        # Ensuring that all ships have been extracted from the API.
        total_ships = get_api_info(url)['count']
        assert len(get_starships()) == total_ships

    def test_read_from_db(self):
        # Testing the database output.
        actual = {'name': 'X-wing', 'model': 'T-65 X-wing', 'manufacturer': 'Incom Corporation',
                  'cost_in_credits': '149999', 'length': '12.5', 'max_atmosphering_speed': '1050',
                  'crew': '1', 'passengers': '0', 'cargo_capacity': '110', 'consumables': '1 week',
                  'hyperdrive_rating': '1.0', 'MGLT': '100', 'starship_class': 'Starfighter',
                  'films': ['https://swapi.dev/api/films/1/', 'https://swapi.dev/api/films/2/',
                            'https://swapi.dev/api/films/3/'],
                  'pilots': [ObjectId('62e40790a2a250f08d03fe60'), ObjectId('62e40777611cebce05f42f48'),
                             ObjectId('62e407a9c6f22f40f3b4c280'), ObjectId('62e4078afd3d0bda16a6fef9')]}

        self.assertEqual(read_from_db("X-wing"), actual, "The Pilot IDs aren't being inserted properly.")
