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

    def create_db_collection(name_db):
        '''
        Function to create a database collection
        :return:
        '''

        client = pymongo.MongoClient() # connect to database
        db = client["starwars31"] #database client 'starwars31'


        try:
            db.create_collection("starships") # function tries to checks if the collection already pre-exists
        except:
            print("Collection 'starships' already exists.. current collection will be deleted...") #if collection pre-exists
            db.starships.drop() #current collection dropped
            db.create_collection("starships") #new collected created
            print("New 'starships' Collection is created..")
        return db #return updated db











