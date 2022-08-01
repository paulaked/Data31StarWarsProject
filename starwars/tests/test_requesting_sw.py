# Unit Testing Plan
import unittest
import sys
from bson import ObjectId

import requests

sys.path.insert(0,"..")
from ..app.requesting_sw import *

# Test function that pulls all available starships from api

class Apitests(unittest.TestCase):

    api_test = GetApi()

    def test_get_api(self):
        '''test to see if connection is ok'''
        self.assertEqual(self.api_test.get_api().status_code,200)

    def test_db(self):
        '''test to see if database is there'''
        self.assertEqual(type(self.api_test.set_up_db()), pymongo.database.Database)

    dict_test = {"a": "1", "created": "34"}
    def test_api_type(self):
        self.assertEqual(type(self.api_test.get_from_api("https://swapi.dev/api/starships/?page=1")), type(self.dict_test))

    '''
    y = ObjectId()
    def test_object_id(self):
        for sublist in self.api_test.get_pilots():
            if sublist['pilots'] is None:
                pass
            else:
                self.assertEqual(type(self.api_test.get_pilots(ships)), type(self.y))
    '''

    def test_drop_keys(self):
        '''test to see if the drop function works'''
        self.assertEqual(self.api_test.drop_columns(self.dict_test), self.dict_test)
