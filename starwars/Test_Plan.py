import unittest
from app import requesting_sw
import pymongo
# Unit Testing Plan

# Test function that sets up databases.
class Tests(unittest.TestCase):
    def test_set_up_db(self):

        db = requesting_sw.set_up_db()
        self.assertIsInstance(db,pymongo.database.Database , "Database not returned")


unittest.main()
# Test function that pulls data from api.
# Test function that downloads, transforms and inserts data.
# Test function that reads from transformed collection.
