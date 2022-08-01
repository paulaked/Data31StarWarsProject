import requests
import pymongo

client = pymongo.MongoClient()
db = client['starwars31']
db.starships.drop()             # Drops the starships collection if it already exists.
new_col = db["starships"]       # Creates a new starships collection

# The block of code below is used to count the number of starships in the API.

url = "https://swapi.dev/api/starships/?"
request = requests.get(url)
json_data = requests.get(url).json()
no_of_starships = json_data["count"]

# Function 1: takes in a starship and outputs the corrosponding pilot object ID's as a list.

def get_starships():
    count_starships = 0                             # Counts how many starships have been located so far.
    i = 1                                           # Starts by looking for a starship in pos 1
    list_of_starships = []                          # This will be the list containing all the star ship urls
    while count_starships < no_of_starships:
        url = "https://swapi.dev/api/starships/" + str(i)
        request = requests.get(url)
        if request.status_code == 200:              # If the url exists we have found a starship
            json_data = requests.get(url).json()
            count_starships = count_starships + 1               # We have found a starship so we add this to the count
            list_of_starships.append(json_data["url"])          # Add the new starship to the list of starships.
        i = i + 1  # now we test the next available url
    return (list_of_starships)


"""Using Get Request only returned the first 10 results 
and so I did not use the following code. I have kept it 
in as if I found out how to change the limit this would 
have been optimal."""

# def get_starships():
#     list_of_starship_urls = []
#     url = "https://swapi.dev/api/starships/?"
#     request = requests.get(url)
#     json_data = requests.get(url).json()
#     for i in range(len(json_data["results"])):
#         list_of_starship_urls.append(json_data["results"][i]["url"])
#     return list_of_starship_urls

# Funcction 2: takes in a starship and outputs the corrosponding pilot object ID's as a list.

def pilot_ID_list(url):

    request = requests.get(url)
    json_data = requests.get(url).json()
    pilot_ID_list = []                          # The pilot's IDs are added to this list then this list replaces the url list.
    for i in range(len(json_data["pilots"])):   # Iterate through each pilot in the list.
        url = json_data["pilots"][i]            # Obtaining the url of the pilot.
        request = requests.get(url)
        json_data_2 = requests.get(url).json()
        pilot_name = json_data_2["name"]        # Obtaining the name of the pilot.
        characters = db.characters.find({"name": pilot_name}, {"name": 1, "_id": 1})
        for character in characters:
            character_id = character["_id"]     # Obtaining the object ID of the pilot
            pilot_ID_list.append(character_id)  # Adding the object ID of the pilot to a list
    return (pilot_ID_list)

# Function 3 - creates a dictionary of the starship, replacing the pilot ID urls with object IDs of the pilots.

def combine_starships_and_pilotID(url, pilot_ID_list):
    request = requests.get(url)
    json_data = requests.get(url).json()
    json_data["pilots"] = pilot_ID_list     # Adding the pilotID list.
    del json_data["created"]                # Removing unwanted information.
    del json_data["edited"]
    del json_data["url"]
    return (json_data)

# Function 4 - Adding the new data to the new collection.

def add_to_collection(json_data):
    x = new_col.insert_one(json_data)
