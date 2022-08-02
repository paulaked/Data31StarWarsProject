# Data 31 Star Wars Project

## Instructions

The character data in your MongoDB database has been pulled from https://swapi.dev/.
As well as 'people', the API has data on starships.
Using Python, write code to pull data on all available starships from the API.
The "pilots" key contains URLs pointing to the characters who pilot the starship.
Use these to replace 'pilots' with a list of ObjectIDs from our characters collection, then insert the starships into their own collection in MongoDB.
(Make sure you drop any existing starships collections.)

You have until Monday EOD.

## Requirements

- Use good coding principles.  That means testing, appropriate comments, good naming conventions and handling errors gracefully.
- Follow PEP 8
- Create a job board in Trello or similar to keep track of your user stories.  Provide a link to that job board in your version of this README.
- Your code should utilise functional programming OR object-oriented programming
- Use Test Driven Development: write your tests first

## Using this repo

- Branch off from main.
- Use your own name for the name of the branch (e.g. mine would be PaulaKedra - please copy this format).
- Make sure you commit and push to the remote repo frequently to keep your work up-to-date.
- The gitignore should catch most unnecessary project files, but do pay attention to what you are adding to the repo.
- Replace this README with an appropriate README for your project (including a link to your job board).

MY TRELLO JOB BOARD
https://trello.com/b/Ct7ObMDK/starwars

In order for this code to work you will need to have a database in mongo db named 'starwars31' with a collection named 'characters'.
The code creates a collection called starships which includes all the star ships that can be attained through the api mentioned above. 
The collection also includes star ships that don't have registered pilots and where there are pilots for the ships the pilot's ObjectID are present.
To execute the code run the main.py file. Functions are used and imported in the main file, the functions that are used to get the star ships data from 
the api are located in the app folder, in the Update.py file. Additionally, the functions used to add the 'starship' (results_list) collection to the 
database can be found in the database.py file. Testing has been done using unit testing and they have all passed, they can be found in the test_starwars.py file. 
Planning was done using a job board which is linked below.