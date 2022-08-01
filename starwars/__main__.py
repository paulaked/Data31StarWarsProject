
from app import requesting_sw
import sys


if __name__ == '__main__':
    db = requesting_sw.create_db_collection('starwars31') # runs the database collection creation function
    requesting_sw.starship_data(db) # function call from requesting_sw
    requesting_sw.read_db_collection(db) # function to read the collection






   # Replace this with code to run your app