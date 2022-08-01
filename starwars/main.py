import requests
import pymongo
client = pymongo.MongoClient()
db = client['starwars31']
db.starships.drop()                                  #drops the starships collection if it already exists.
new_col = db["starships"]                            #creates a new starships collection


def test_length():
    assert len(get_starships()) == 36               #tests that the code is finding all the requried starships.

def test_type():
    assert type(get_starships()) == type([])        #test that the function is outputting in the desired format.


"""Using Get Request only returned the first 10 results and so I did not use the following code. I have kept it in as if I found out how to change the limit this would have been optimal."""

# def get_starships():
#     list_of_starship_urls = []
#     url = "https://swapi.dev/api/starships/?"
#     request = requests.get(url)
#     json_data = requests.get(url).json()
#     for i in range(len(json_data["results"])):
#         list_of_starship_urls.append(json_data["results"][i]["url"])
#     return list_of_starship_urls


def get_starships():                                            # this f will output a list of all the starships in the API
    count_starships = 0                                         # counts how many starships have been located so far.
    i = 1                                                       # starts by looking for a starship in pos 1
    list_of_starships = []                                      # this will be the list containing all the star ship urls
    while count_starships < 36:                                 # The Star Wars API has 36 starships: https://swapi.dev/about
        url = "https://swapi.dev/api/starships/" + str(i)
        request = requests.get(url)
        if request.status_code == 200:                          # if the url exists we have found a starship
            json_data = requests.get(url).json()
            count_starships = count_starships + 1               # we have found a starship so we add this to the count
            list_of_starships.append(json_data["url"])          # so we add the starship to our list of starships
        i = i + 1  # now we test the next available url
    return (list_of_starships)

#Task 2: create a function that takes in a starship and outputs the corrosponding pilot object ID's as a list.

def test_pilot_ID_list():
    test_list = []
    characters = db.characters.find(
        {"$or": [{"name": "Chewbacca"}, {"name": "Han Solo"}, {"name": "Lando Calrissian"}, {"name": "Nien Nunb"}]})        #these are the names of pilots in starships 10.
    for character in characters:
        character_id = character["_id"]
        test_list.append(character_id)                                                                                      #the function should create this list of pilot IDs
    assert pilot_ID_list("https://swapi.dev/api/starships/10/") == test_list                                                #asserting that the function does as intended.

def pilot_ID_list(url):

    request = requests.get(url)
    json_data = requests.get(url).json()
    pilot_ID_list = []                          #the pilot's IDs are added to this list then this list replaces the url list.
    for i in range(len(json_data["pilots"])):   #iterate through each pilot in the list.
        url = json_data["pilots"][i]            #Obtaining the url of the pilot
        request = requests.get(url)
        json_data_2 = requests.get(url).json()
        pilot_name = json_data_2["name"]                 #Obtaining the name of the pilot.
        characters = db.characters.find({"name": pilot_name}, {"name": 1, "_id": 1})
        for character in characters:
            character_id = character["_id"]     #Obtaining the object ID of the pilot
            pilot_ID_list.append(character_id)  #Adding the object ID of the pilot to a list
    return (pilot_ID_list)

#Task 3 - creates json data of the starships, replacing the pilot ID urls with object IDs of the pilots.

#This tests checks that unwnated information has not been included.

def test_combine_starships_and_pilotID():
    assert combine_starships_and_pilotID("https://swapi.dev/api/starships/12",pilot_ID_list("https://swapi.dev/api/starships/12").get("created") == None


