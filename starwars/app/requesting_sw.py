import json
import requests
import pymongo


class GetStarwarsAPI:

    def get_data_api(self):
        '''
        function to test if API is responding
        :return: the status code of the API
        '''
        status_code = requests.get("https://swapi.dev/")
        return status_code











