import requests
import json

# all the data that I will extract and transform will be contained and updated within 'new'
new = []

# this function will extract data from every starship in the API. I've hardcoded the number of starships to be extracted (76).
# the better way would be to use the next page link to use for iterations.
def get_starships(first=0,last=76):
    for uid in range(first,last):
        req = requests.get(f"https://www.swapi.tech/api/starships/{uid}")
        data = req.json()
        if data["message"] == "ok":
            new.append(data["result"])
        else:
            continue
    return new

#this function accesses the data in 'new' defined above, enters the links, extracts the objectids, and replaces the links with the objectids.
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
