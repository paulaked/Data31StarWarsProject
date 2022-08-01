
from app import requesting_sw
import sys


if __name__ == '__main__':
    db = requesting_sw.create_db_collection('starwars31') # runs the database collection creation function
    requesting_sw.starship_data(db) # function call from requesting_sw to extract the data
    requesting_sw.read_db_collection(db) # function to read and output the collection
