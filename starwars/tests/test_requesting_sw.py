# Unit Testing Plan
# Test function that pulls all available starships from api
import unittest
import sys
from unittest import TestCase

import pymongo.database
import requests
import mongomock
from ..app import requesting_sw

sys.path.insert(0, "..")
#from ..app.requesting_sw import *
#from ..app.requesting_sw import get_data_from_api


class APIUnittests(unittest.TestCase):


    def test_get_api(self):
        '''
        Check to see if API is responding
        :return: Passed or Failed (checks if the status code matches the provided value)
        '''
        response = requests.get("https://swapi.dev/api/starships/")
        assert response.status_code == 200

    def test_starship_count(self):
        '''
        Test to check the number of starships
        :return: Passed or Failed (if value matches)
        '''

        response = requests.get("https://swapi.dev/api/starships/") #requests data from given url
        response_body = response.json()
        assert response_body["count"] == 36  # value of number of starships

    def test_can_create_db(self):
        '''
        Test to check if mongodb database can be created
        :return:
        '''
        self.assertIsNotNone(mongomock.MongoClient())


#    def test_get_api_info(url):
#        # Checking that the response from the API is in dictionary form.
#        response = {"key": "value"}
#        assert type(get_data_from_api(url)) == type(response)

    #def test_
#    api_testing = GetStarwarsAPI()
#    db = requesting_sw.create_db_collection('starwars31')

#    def test_for_db(self):
#        '''
#        Test to check if the database created exists
#        :return: Passed or Failed (based on if database is found)
#        '''
#        self.assertIsInstance(type(self.db), pymongo.database.Database, "not exists")



