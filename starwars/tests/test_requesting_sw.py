import unittest

from bson import ObjectId
import pymongo

from starwars.app import requesting_sw


# Test function that sets up databases.
class Tests(unittest.TestCase):
    db = requesting_sw.set_up_db('starwars31')

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

    # Test function that removes fields from JSON object.
    def test_remove_fields(self):
        input = {'name': 'CR90 corvette', 'model': 'CR90 corvette',
                 'manufacturer': 'Corellian Engineering Corporation', 'cost_in_credits': '3500000',
                 'length': '150', 'max_atmosphering_speed': '950', 'crew': '30-165', 'passengers': '600',
                 'cargo_capacity': '3000000', 'consumables': '1 year', 'hyperdrive_rating': '2.0', 'MGLT': '60',
                 'starship_class': 'corvette', 'pilots': [], 'films': ['https://swapi.dev/api/films/1/',
                                                                       'https://swapi.dev/api/films/3/',
                                                                       'https://swapi.dev/api/films/6/'],
                 'created': '2014-12-10T14:20:33.369000Z', 'edited': '2014-12-20T21:23:49.867000Z',
                 'url': 'https://swapi.dev/api/starships/2/'}

        expected_result = {'name': 'CR90 corvette', 'model': 'CR90 corvette',
                           'manufacturer': 'Corellian Engineering Corporation', 'cost_in_credits': '3500000',
                           'length': '150', 'max_atmosphering_speed': '950', 'crew': '30-165', 'passengers': '600',
                           'cargo_capacity': '3000000', 'consumables': '1 year', 'hyperdrive_rating': '2.0',
                           'MGLT': '60',
                           'starship_class': 'corvette', 'pilots': [], 'films': ['https://swapi.dev/api/films/1/',
                                                                                 'https://swapi.dev/api/films/3/',
                                                                                 'https://swapi.dev/api/films/6/'],
                           }
        self.assertEqual(requesting_sw.remove_fields(input), expected_result, "Fields not removed correctly")

    def test_replace_urls(self):
        input = {'name': 'Millennium Falcon', 'model': 'YT-1300 light freighter',
                 'manufacturer': 'Corellian Engineering Corporation', 'cost_in_credits': '100000',
                 'length': '34.37', 'max_atmosphering_speed': '1050', 'crew': '4',
                 'passengers': '6', 'cargo_capacity': '100000', 'consumables': '2 months',
                 'hyperdrive_rating': '0.5', 'MGLT': '75', 'starship_class': 'Light freighter',
                 'pilots': ['https://swapi.dev/api/people/13/', 'https://swapi.dev/api/people/14/',
                            'https://swapi.dev/api/people/25/', 'https://swapi.dev/api/people/31/'],
                 'films': ['https://swapi.dev/api/films/1/', 'https://swapi.dev/api/films/2/',
                           'https://swapi.dev/api/films/3/'],
                 'created': '2014-12-10T16:59:45.094000Z', 'edited': '2014-12-20T21:23:49.880000Z',
                 'url': 'https://swapi.dev/api/starships/10/'}

        expected = {'name': 'Millennium Falcon', 'model': 'YT-1300 light freighter',
                    'manufacturer': 'Corellian Engineering Corporation', 'cost_in_credits': '100000',
                    'length': '34.37', 'max_atmosphering_speed': '1050', 'crew': '4',
                    'passengers': '6', 'cargo_capacity': '100000', 'consumables': '2 months',
                    'hyperdrive_rating': '0.5', 'MGLT': '75', 'starship_class': 'Light freighter',
                    'pilots': [ObjectId('62e256c5a83a9f6743af6bc0'), ObjectId('62e256d16e8b658385726d83'),
                               ObjectId('62e256d866351cbececb694c'), ObjectId('62e256dec59ed8bc181c8361')],
                    'films': ['https://swapi.dev/api/films/1/', 'https://swapi.dev/api/films/2/',
                              'https://swapi.dev/api/films/3/'],
                    'created': '2014-12-10T16:59:45.094000Z', 'edited': '2014-12-20T21:23:49.880000Z',
                    'url': 'https://swapi.dev/api/starships/10/'}

        self.assertEqual(requesting_sw.replace_urls(input, self.db), expected, "Object IDs not inserted correctly")


if __name__ == "__main__":
    unittest.main()
