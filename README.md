# Data 31 Star Wars Project

## Instructions

The character data in your MongoDB database has been pulled from https://swapi.dev/.
As well as 'people', the API has data on starships.
Using Python, write code to pull data on all available starships from the API.
The "pilots" key contains URLs pointing to the characters who pilot the starship.
Use these to replace 'pilots' with a list of ObjectIDs from our characters collection, then insert the starships into their own collection in MongoDB.
(Make sure you drop any existing starships collections.)


## Goal of the project: Create a Starships Collection to include all the starships and reference Pilot IDs from the already existing Characters Collection.

I created a Trello Job Board and you can find it at https://trello.com/b/Y2i4Xn1E to follow my progress.

### Process

1. Explore the API found at https://swapi.dev/ 
2. Pull data on all available starships from the API.
3. The database I used is 'starwars' so you can change that if your database is named differently, please do make sure to change it in the requesting_sw.py file.
4. Look at the pilots by querying the characters collection in the database to add the Object ID to the pilot list in the Starships collection.


I used Functional Programming to go through the process and used pytest to test the functions.

 
Author: Susan Cynthia Musiime

