'''
Write a program that makes a DELETE request to remove the user your create in a previous example.

Again, make a GET request to confirm that information has been deleted.
'''

import requests

params = {
    "email":"didi@codingnomads.co"
}
base_url = "http://demo.codingnomads.co:8080/tasks_api/users"
response1 = requests.delete(base_url, json=params)
print(response1)


response2 = requests.get(base_url, params=params)
print(response2)

