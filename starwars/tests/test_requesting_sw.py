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

import starwars.config_manager as sw_config
from starship import Starships
from model import StarshipsModel
import main


class StarshipsTest(unittest.TestCase):
    starships = Starships()
    starship_url = sw_config.SWAPI_STARSHIPS
    def test_response(self, url=starship_url):
        self.assertEquals(self.starships(url), 200)
        
    def test_fake_response(self):
        fake_url = sw_config.FAKE_URL
        self.assertEquals(self.starships(fake_url), 404)

    def  test_json(self, url=starship_url):

        self.assertIsInstance(self.starships(url), json)

class ModelTest(unittest.TestCase):
    def test_output_type(self):
        self.assertIsInstance(starwars_dict, dict)
    def test_output(self):
        self.assertIn("Death Star", starship_dict, msg="That's no moon")
