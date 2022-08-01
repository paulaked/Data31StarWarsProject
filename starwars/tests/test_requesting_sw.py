import unittest
import pytest
from starwars.app import starship_api as sa
import pymongo


class ttd(unittest.TestCase):  # create a class to test everything
    client = pymongo.MongoClient()
    db = client['starwars']
    col = db["starships"]

    mongo_len = db.starships.count({})

    def test_api_connection(self):  # we need to test that we are getting a good response from api
        self.assertEqual(str(sa.api_call("https://swapi.dev/api/starships")), "<Response [200]>")  # 200 = good response

    # def api_output_correct(self):  # we need to make sure we are getting all of the starship data
    #     self.assertEqual(self.list_starships, 36)  # there are 36 starships - no more movies planned so should be good

    def test_crawl(self):
        self.assertEqual(str(sa.crawl_api("https://swapi.dev/api/starships/75/")), "<generator object crawl_api at 0x101627bd0>")