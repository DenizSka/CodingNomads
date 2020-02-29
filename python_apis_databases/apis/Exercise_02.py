'''
Building on the previous example, create a list of all of the emails of the users and print
the list to the console.

'''

import requests
import json

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"
response = requests.get(base_url)
# whenever there is a stringified list of dictionaries, json.loads(your_data) function can be used to convert it to a list.
dict_ = json.loads(response.text)

list_ = []
for one in dict_['data']:
    list_.append(one["email"])
print(list_)

