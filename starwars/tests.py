from functions import *
# Function 1: takes in a starship and outputs the corrosponding pilot object ID's as a list.

# Tests that the code is finding all the required starships.

def test_length():
    assert len(get_starships()) == no_of_starships

# Tests that the function is outputting in the desired format.

def test_type_1():
    assert type(get_starships()) == type([])

def test_type_2():
    assert type(get_starships()[0]) == str

# Funcction 2: takes in a starship and outputs the corrosponding pilot object ID's as a list.

def test_pilot_ID_list():
    test_list = []
    characters = db.characters.find(
        {"$or": [{"name": "Chewbacca"}, {"name": "Han Solo"}, {"name": "Lando Calrissian"}, {"name": "Nien Nunb"}]})
        # These are the names of pilots in starships 10.
    for character in characters:
        character_id = character["_id"]
        test_list.append(character_id)
        # Creating the list of pilot ids that the function should also create.
    assert pilot_ID_list("https://swapi.dev/api/starships/10/") == test_list
    # Asserting that the function does as intended.

# Function 3 - creates a dictionary of the starship, replacing the pilot ID urls with object IDs of the pilots.

# This test checks that the output is in the type expected.

def test_combine_starships_and_pilotID():
    assert type(combine_starships_and_pilotID("https://swapi.dev/api/starships/12",pilot_ID_list("https://swapi.dev/api/starships/12"))) == type({"test": "test"})

# This tests checks that unwnated information has not been included.

def test_combine_starships_and_pilotID_2():
    assert combine_starships_and_pilotID("https://swapi.dev/api/starships/12",pilot_ID_list("https://swapi.dev/api/starships/12")).get("created") == None

# Function 4 - Adding the new data to the new collection.

# This test checks that the updated starship dictionaries are being
# added to the new collection and the IDs are of the right data type.

def test_add_to_collection():
    updated_starship = combine_starships_and_pilotID("https://swapi.dev/api/starships/12",
                                      pilot_ID_list("https://swapi.dev/api/starships/12"))
    add_to_collection(updated_starship)
    for item in db.starships.find({"name": "X-wing"}):
        characters = db.characters.find({"name": "Luke Skywalker"}, {"name": 1, "_id": 1})
        for character in characters:
            character_id = character["_id"]                             # Obtaining the object ID of the pilot
    assert(type(item["pilots"][0])) == type(character_id)               # Checking that the object IDs in the collection are of type bson.
