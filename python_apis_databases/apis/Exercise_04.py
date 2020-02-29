'''
Write a program that makes a PUT request to update your user information to a new first_name, last_name and email.

Again make a GET request to confirm that your information has been updated.

'''
import requests

put_req = {
    "first_name": "Denny",
    "last_name": "Ska",
    "email": "didi@codingnomads.co",
}
base_url = "http://demo.codingnomads.co:8080/tasks_api/users"
response1 = requests.put(base_url, json=put_req)
print(response1)

params = {
    "email": "didi@codingnomads.co"
}

response2 = requests.get(base_url, params=params)
print(response2)
