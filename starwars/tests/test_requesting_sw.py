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
from starship import Starships
from model import StarshipsModel
from main import *


class StarshipsTest(unittest.TestCase):
    starships = Starships()

    def test_response(self):
        self.assertEquals(self.starships(""), 200)
        self.assertEquals(self.starships(""), 404)
    
    def  test_json(self):
        self.assertIsInstance(self.starships(""), json)
