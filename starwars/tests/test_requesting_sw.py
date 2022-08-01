# Unit Testing Plan

# Test function that pulls all available starships from api

import unittest
import requesting_sw

class TestStarwars(unittest.TestCase):

    def test_get_starships(self):
        requesting_sw.new = []
        self.assertEqual(len(requesting_sw.get_starships(7, 15)), 5)
        requesting_sw.new = []
        self.assertEqual(len(requesting_sw.get_starships(29, 37)), 3)
        requesting_sw.new = []
        self.assertEqual(len(requesting_sw.get_starships(53, 57)), 0)

