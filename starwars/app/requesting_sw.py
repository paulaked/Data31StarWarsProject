import requests
import json

new = []
def get_starships(first=0,last=76):
    for uid in range(first,last):
        req = requests.get(f"https://www.swapi.tech/api/starships/{uid}")
        data = req.json()
        if data["message"] == "ok":
            new.append(data["result"])
        else:
            continue
    return new


def replace_links(first_index=1):
    for num in range(first_index,len(new)):
        for index, item in enumerate(new[num]["properties"]["pilots"]):
            req1 = requests.get(item)
            data1 = req1.json()
            ids = data1["result"]["_id"]
            characters = f"ObjectID('{ids}')"
            count = num
            ney = new[count]["properties"]["pilots"]
            ney[index] = characters
    return new
