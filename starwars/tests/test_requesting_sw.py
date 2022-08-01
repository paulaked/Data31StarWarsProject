# Unit Testing Plan

# Test function that pulls all available starships from api

from starwars.app import requesting_sw
import unittest
import pymongo


class ApiTesting(unittest.TestCase):

    def test_get_from_api(self):  # Test for data pulled from api
        status_code = requesting_sw.get_api("https://swapi.dev/api/people").status_code
        self.assertEqual(status_code, 200, "Error")

    api_test = requesting_sw.db_link('starwars')  # set up db

    def test_set_up_db(self):  # check db returned
        self.assertIsInstance(self.api_test, pymongo.database.Database, "DatabaseX not returned")

    def test_num_starship(self):  # check num of db matches
        num_ships = (requesting_sw.get_api("https://swapi.dev/api/starships").json())['count']
        self.assertEqual(num_ships, 36, 'Wrong Number!')

    def test_get_api_info(self):  # check dictionary form
        dict_r = {"key": "value"}
        self.assertEqual(type(dict_r), type(requesting_sw.get_api("https://swapi.dev/api/starships").json()),
                         'Wrong Type!')
