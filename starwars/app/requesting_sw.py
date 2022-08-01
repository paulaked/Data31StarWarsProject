import json
import requests
import pymongo


#class GetStarwarsAPI:

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

    def get_data_from_api(url):
        '''
        Function to return data from API
        :return: retrieves requested Json data
        '''
        response = requests.get(url) #requests json data from url
        return response.json() #return the json data


    def starship_data(db):
        '''
        Function to transform the Json data and populate it into starships collections
        in a 'name':['Starship name'], 'pilots':['pilots objectID'] format
        :param db:the database
        :return: database collection starship
        '''
        page_number = 1
        while not False:
            starships_data = get_data_from_api("https://swapi.dev/api/starships/?page=" + str(page_number))

            for starship in starships_data['results']:

                list_of_pilots = []

            if starships_data['next'] is None:
                print("All pages checked...")
                True
            else:
                page_number = page_number + 1
        return False















