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
        url = requests.get("https://swapi.dev/")
        self.assertEqual(url.status_code,200)





