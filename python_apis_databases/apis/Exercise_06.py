'''

Create an application that interfaces with the user via the CLI - prompt the user with a menu such as:

Please select from the following options (enter the number of the action you'd like to take):
1) Create a new account (POST)
2) View all your tasks (GET)
3) View your completed tasks (GET)
4) View only your incomplete tasks (GET)
5) Create a new task (POST)
6) Update an existing task (PATCH/PUT)
7) Delete a task (DELETE)

It is your responsibility to build out the application to handle all menu options above.


'''
import requests
from pprint import pprint
#
# # 1) Create a new account (POST)
post_req = {
    "first_name": "NewDeniz",
    "last_name": "User",
    "email": "newuser1@codingnomads.co",
}

base_url1 = "http://demo.codingnomads.co:8080/tasks_api/users"
response1 = requests.post(base_url1, json=post_req)
print(response1)

# 1a) Get my user id
user_id = None
base_url2 = "http://demo.codingnomads.co:8080/tasks_api/users?email=newuser1@codingnomads.co"
response2 = requests.get(base_url2)
data = response2.json()
user_id = data["data"][0]["id"]
pprint(user_id)

# 2) View all your tasks (GET)
base_url3 = f"http://demo.codingnomads.co:8080/tasks_api/users/{user_id}/tasks"
response3 = requests.get(base_url3)
print(response3.json())

# 3) View your completed tasks (GET)
base_url4 = f"http://demo.codingnomads.co:8080/tasks_api/users/{user_id}/tasks?complete=true"
response4 = requests.get(base_url4)
print(response4.json())

# 4) View only your incomplete tasks (GET)
base_url5 = f"http://demo.codingnomads.co:8080/tasks_api/users/{user_id}/tasks?complete=false"
response5 = requests.get(base_url5)
print(response5.json())

# 5) Create a new task (POST)
new_task = {
    "completed": False,
    "description": "wash the dishes",
    "name": "task",
    "userId": user_id
}
base_url6 = f"http://demo.codingnomads.co:8080/tasks_api/tasks"
response6 = requests.post(base_url6, json=new_task)
print(response6.json())

# 6) Update an existing task (PATCH/PUT)
put_request = {
    "id": user_id,
    "first_name": "Deniz",
    "last_name": "User",
    "email": "newuser1@codingnomads.com",
}
base_url7 = f"http://demo.codingnomads.co:8080/tasks_api/users"
response7 = requests.put(base_url7, json=put_request)
print(response7.json())

# 7) Delete a task (DELETE)
base_url8 = "http://demo.codingnomads.co:8080/tasks_api/users"
response8 = requests.delete(base_url8 + f"/{user_id}")
print(response8)
