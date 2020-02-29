'''
Write the necessary code to make a POST request to:

    http://demo.codingnomads.co:8080/tasks_api/users

and create a user with your information.

Make a GET request to confirm that your user information has been saved.

'''

import requests

post_req = {
    "first_name": "Deniz",
    "last_name": "Skantz",
    "email": "deniz@codingnomads.co",
}

# json or data works differently: it’s all about the request body.
base_url = "http://demo.codingnomads.co:8080/tasks_api/users"
response1 = requests.post(base_url, json=post_req)
print(response1)

params = {
    "last_name": "Skantz"
}

# params is all about the query string, and so is primarily used on GET requests
response2 = requests.get(base_url, params=params)
print(response2)
