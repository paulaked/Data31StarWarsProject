# Unit Testing Plan

# Test function that pulls all available starships from api

import unittest
import starwars

class TestStarwars(unittest.TestCase):

    def test_get_starships(self):
        length = len(starwars.get_starships(7,15))
        result = length
        self.assertEqual(result, 5)
