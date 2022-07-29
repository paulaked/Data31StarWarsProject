# Unit Testing Plan
# Test function that pulls all available starships from api
import unittest
import sys

sys.path.insert(0,"..")
from ..app.requesting_sw import *


class APIUnittests(unittest.TestCase):

    api_testing = GetStarwarsAPI()

    def test_get_api(self):
        '''
        Check to see if API is responding
        :return: checks if the status code matches the provided value
        '''
        self.assertEqual(self.api_testing.get_data_api().status_code, 200)
