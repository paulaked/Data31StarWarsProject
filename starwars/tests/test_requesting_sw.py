from main import *
import unittest


class Unit_tests(unittest.TestCase):

    def test_api_request(self):
        try:
            request_api("https://swapi.dev/api/starships")
        except AssertionError:
            self.fail("api_request: An exception occurred")

    def test_character_id_search(self):
        try:
            character_id_search("Luke Skywalker")
        except AssertionError:
            self.fail("character_id_search: An exception occurred")

    