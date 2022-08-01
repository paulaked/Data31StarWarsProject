import requests

def test_length():
    assert len(get_starships()) == 36

def test_type():
    assert type(get_starships()) == type([])


"""Using Get Request only returned the first 10 results and so I did not use."""


# def get_starships():
#     list_of_starship_urls = []
#     url = "https://swapi.dev/api/starships/?"
#     request = requests.get(url)
#     json_data = requests.get(url).json()
#     for i in range(len(json_data["results"])):
#         list_of_starship_urls.append(json_data["results"][i]["url"])
#     return list_of_starship_urls


def get_starships():  # this f will output a list of all the starships in the API
    count_starships = 0  # counts how many starships have been located so far.
    i = 1  # starts by looking for a starship in pos 1
    list_of_starships = []  # this will be the list containing all the star ship urls
    while count_starships < 36:  # The Star Wars API has 36 starships: https://swapi.dev/about
        url = "https://swapi.dev/api/starships/" + str(i)
        request = requests.get(url)
        if request.status_code == 200:  # if the url exists we have found a starship
            json_data = requests.get(url).json()
            count_starships = count_starships + 1  # we have found a starship so we add this to the count
            list_of_starships.append(json_data["url"])  # so we add the starship to our list of starships
        i = i + 1  # now we test the next available url
    return (list_of_starships)

#Task 2: create a function that takes in a starship and outputs the starship with new object ID's.

def test_pilot_ID_list():
    test_list = []
    characters = db.characters.find(
        {"$or": [{"name": "Chewbacca"}, {"name": "Han Solo"}, {"name": "Lando Calrissian"}, {"name": "Nien Nunb"}]})
    for character in characters:
        character_id = character["_id"]
        test_list.append(character_id)
    assert pilot_ID_list("https://swapi.dev/api/starships/10/") == test_list

