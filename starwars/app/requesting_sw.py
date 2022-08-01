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
