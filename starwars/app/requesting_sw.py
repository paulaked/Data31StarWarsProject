import requests     #importing libraries
import json
import pymongo
client = pymongo.MongoClient()  #creating mongodb client
db = client['starwars31']   #creating reference "db" to database

headers = {'Content-Type':'application/json'} #configuration to make the return a json


def link_to_pilot(pilots): #function to loop through pilots
    if not pilots:
        return []   #returning empty array if pilot list is empty

    ids = []
    for link in pilots: #getting names of pilots
        character_req = requests.get(link,headers=headers) #requesting pilot characters from api
        name = character_req.json()["name"] #turn result into json and index by "name"
        id = db.characters.find({"name":name}, {"name":1, "_id":1})
        ids.append(id)

    return ids

def starships_with_objectid():
    starship_req = requests.get("https://swapi.dev/api/starships/",
                                headers=headers)  # requesting data from api using configuration
    starships = starship_req.json()["results"]  # turn result into json and index by "results"
    for starship in starships:
        #{..., pilots: [], ...},
        starship["pilots"] = link_to_pilot(starship["pilots"])

    return starships
print(starships_with_objectid())




# #trying to see pilots list
# resp = starship_req.json()
# pilot_list=[]
# def pilotlist():
#     for i in range(1,36):
#         pilot_list.append(resp["results"][i]["pilots"])
#         return pilot_list
# print(pilotlist())

