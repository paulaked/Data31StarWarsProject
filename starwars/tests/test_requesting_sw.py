
from main import *
import unittest


class Tests(unittest.TestCase):

    def request_api_test(self):
        try:
            api_request("https://swapi.dev/api/starships")
        except AssertionError:
            self.fail("api_request raised an exception unexpectedly")

    def character_id_search_test(self):
        try:
            find_character_id("Luke Skywalker")
        except AssertionError:
            self.fail("find_character_id raised an exception unexpectedly")

    def test_add_pilot_id(self):
        try:
            add_pilot_id(api_request("https://swapi.dev/api/starships/2"))
        except AssertionError:
            self.fail("add_pilot_id raised an exception unexpectedly")

    def test_create_starships_list(self):
        try:
            create_starships_list()
        except AssertionError:
            self.fail("create_starships_list raised an exception unexpectedly")
