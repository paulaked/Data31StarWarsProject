import pymongo
import requests

client = pymongo.MongoClient()
db = client["starwars31"]


# drop existing starships collections
def drop_starships():
    if db.starships.find({}) != "":
        db.starships.delete_many({})
        # drops the entire collection
    db.starships.drop()
