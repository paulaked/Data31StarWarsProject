# Unit Testing Plan

# Test function that pulls all available starships from api

from starwars.app import requesting_sw
import unittest
import sys
import requests
import pymongo


class ApiTesting(unittest.TestCase):

    # Test function that pulls data from api.
    def test_get_from_api(self):
        status_code = requesting_sw.get_api("https://swapi.dev/api/people").status_code
        self.assertEqual(status_code, 200, "Incorrect response code")

    # Test Database set up function
    api_test = requesting_sw.db_link('starwars')

    def test_set_up_db(self):
        self.assertIsInstance(self.api_test, pymongo.database.Database, "DatabaseX not returned")
