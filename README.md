# Data 31 Star Wars Project

Coded By: Amir Naghieh.

Trello: https://trello.com/b/NFJFUhQ3/starwarsapi

## Instructions
-Run your mongo shell

-Run the requesting_sw.py file: please wait patiently for several minutes as the request retrieves data from the swapi API.

-If requesting_sw.py gives a 'Maximum requests reached' error, the reason is that my code uses up alot of requests, and you have used up quite a few requests prior to running this file. Please use a vpn to reset your daily limit using swapi API, and try running the file again.

## Note

-Looking back at the code, the code makes too many requests to the API, because it makes additional get requests per link in 'pilots'. To fix this problem I would save the people in a new list, and match the number contained within the link string to the people uid: this will greatly reduce the get requests.
