import unittest
from app import requesting_sw
import pymongo


# Test function that sets up databases.
class Tests(unittest.TestCase):
    db = requesting_sw.set_up_db()

    def test_set_up_db(self):
        self.assertIsInstance(self.db, pymongo.database.Database, "Database not returned")

    # Test function that pulls data from api.
    def test_get_from_api(self):
        status_code = requesting_sw.get_from_api("https://swapi.dev/api/people").status_code
        self.assertEqual(status_code, 200, "Incorrect response code")

        status_code = requesting_sw.get_from_api("https://swapi.dev/api/people5").status_code
        self.assertEqual(status_code, 404, "Incorrect response code")

    # Test function that downloads, transforms and inserts data.
    def test_dl_trans_ins(self):
        self.assertTrue(requesting_sw.dl_trans_ins(self.db), "Data could not be transformed.")

    # Test function that reads from transformed collection.
    def test_read_from_db(self):
        self.assertTrue(requesting_sw.dl_trans_ins(self.db), "Data could not be read.")


if __name__ == "__main__":
    unittest.main()
