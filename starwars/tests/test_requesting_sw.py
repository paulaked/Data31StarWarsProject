# Unit Testing Plan
import unittest
import sys

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

    #dict_test = {"a": "1"}
    #def test_get_api(self):
        self.assertDictEqual(type(self.api_test.get_from_api()), type(self.dict_test))