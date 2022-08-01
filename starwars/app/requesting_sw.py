import requests
import json

headers = {'Content-Type':'application/json'}
starship_req = requests.get("https://swapi.dev/api/starships/",headers=headers)

print(starship_req.json())


#trying to see pilots list
resp = starship_req.json()
pilot_list=[]
def pilotlist():
    for i in range(1,36):
        pilot_list.append(resp["results"][i]["pilots"])
        return pilot_list
print(pilotlist())

