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
from starwars.app.starship import Starships
import starwars.etl as etl


class StarshipsTest(unittest.TestCase):
    starships = Starships(sw_config.SWAPI_STARSHIPS)

    def test_response(self):
        response = starships.response
        self.assertEqual(response.status_code, 200, "Status code: OK")

    def test_list(self):
        self.assertIsInstance(etl.extract(), list)


class ModelTest(unittest.TestCase):
    def test_output_type(self):
        self.assertIsInstance(main.starship_dicts, dict)

    def test_output(self):
        self.assertIn("Death Star", main.starship_dict, msg="That's no moon")


StarshipsTest.test_response()
