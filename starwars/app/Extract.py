# import libraries request and pymongo

import requests
import pymongo

# create the connection with the Star Wars database - Mongo

client = pymongo.MongoClient()
db = client['starwars']

# starships address

starships_address = 'https://www.swapi.tech/api/starships'

# function that requests the data from an url and returns as json


def get_data(url):
    starship_url = requests.get(url)
    starship_url = starship_url.json()
    return starship_url


# for loop to iterate through all urls in the starships url
starship_url_pages = []
for value in get_data(starships_address)['results']:
    starship_url_pages.append(value['url'])

# since the api urls are displayed on multiple pages this function
# extracts the url for all the pages(4 in total)


def get_all_url():
    current_page = get_data(starships_address)
    while current_page['next'] != None:
        current_page = requests.get(current_page['next'])
        current_page = current_page.json()
        for item in current_page['results']:
            starship_url_pages.append(item['url'])
    return starship_url_pages

# function to get the pilot name and find the respective id on character collection.
# finally, replaces the pilot values with ids.


def replace_pilots_with_id():
    starships = []
    for i in get_all_url():
        url_values = requests.get(i)
        url_values = url_values.json()
        result = url_values['result']
        properties = result['properties']
        pilot_url = properties['pilots']
        pilot_name = []
        for pilot in pilot_url:
            pilot_content = requests.get(pilot).json()
            pilot_name.append(pilot_content['result']['properties']['name'])
        pilots_id = []
        for i in pilot_name:
            for n in db.characters.find({'name': i}):
                pilots_id.append(n["_id"])
        url_values['result']['properties']['pilots'] = pilots_id
        starships.append(url_values)

    return starships


# Drops the existing collection called Starship from the Mongo Database:

db.drop_collection("Starship")
print('Starship Collection has been dropped from the Mongo Database')

# Creating a collection called Starship if non-existent on the Mongo Database:

db.create_collection("Starship")
print('The Starship collection has been created')

# For loop to insert Starships into the collection on Mongo database:

for i in replace_pilots_with_id():
    db.Starship.insert_one(i)
print("The Starships have been added to the collection")