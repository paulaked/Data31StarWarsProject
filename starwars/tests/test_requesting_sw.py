# Unit Testing Plan
"""
classes
	Starships - to call starships list
		test response code
		test isinstance json
	StarshipsModel
		check returns only desired fields - mock entry

function:
	extract
		calls url
		function to store starships as dictionary
			check isValid dictionary ('Death Star')
"""
# Test function that pulls all available starships from api
import unittest
import json

from config_manager import *
from starship import Starships
from model import StarshipsModel
from main import *


class StarshipsTest(unittest.TestCase):
    starships = Starships()
    def test_response(self):
        starship_url = SWAPI_STARSHIPS
        self.assertEquals(self.starships(starship_url), 200)
        
    def test_fake_response(self):
        fake_url = FAKE_URL
        self.assertEquals(self.starships(fake_url), 404)

    def  test_json(self):
        self.assertIsInstance(self.starships(SWAPI_STARSHIPS), json)

class ModelTest(unittest.TestCase):
    pass
