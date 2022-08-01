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

        
    def test_replace_links(self):
        requesting_sw.new = []
        requesting_sw.get_starships(70, 76)
        result = requesting_sw.replace_links(0)
        self.assertEqual(result, [{'properties': {'model': 'Belbullab-22 starfighter', 'starship_class': 'starfighter', 'manufacturer': 'Feethan Ottraw Scalable Assemblies', 'cost_in_credits': '168000', 'length': '6.71', 'crew': '1', 'passengers': '0', 'max_atmosphering_speed': '1100', 'hyperdrive_rating': '6', 'MGLT': 'unknown', 'cargo_capacity': '140', 'consumables': '7 days', 'pilots': ["ObjectID('5f63a36eee9fd7000499be4b')", "ObjectID('5f63a36fee9fd7000499be8f')"], 'created': '2020-09-17T17:55:06.604Z', 'edited': '2020-09-17T17:55:06.604Z', 'name': 'Belbullab-22 starfighter', 'url': 'https://www.swapi.tech/api/starships/74'}, 'description': 'A Starship', '_id': '5f63a34fee9fd7000499be40', 'uid': '74', '__v': 0}, {'properties': {'model': 'Alpha-3 Nimbus-class V-wing starfighter', 'starship_class': 'starfighter', 'manufacturer': 'Kuat Systems Engineering', 'cost_in_credits': '102500', 'length': '7.9', 'crew': '1', 'passengers': '0', 'max_atmosphering_speed': '1050', 'hyperdrive_rating': '1.0', 'MGLT': 'unknown', 'cargo_capacity': '60', 'consumables': '15 hours', 'pilots': [], 'created': '2020-09-17T17:55:06.604Z', 'edited': '2020-09-17T17:55:06.604Z', 'name': 'V-wing', 'url': 'https://www.swapi.tech/api/starships/75'}, 'description': 'A Starship', '_id': '5f63a350ee9fd7000499be41', 'uid': '75', '__v': 0}])

