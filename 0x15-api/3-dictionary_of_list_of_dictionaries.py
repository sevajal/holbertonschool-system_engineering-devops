#!/usr/bin/python3
"""Script to export data in the JSON format."""

import json
import requests

if __name__ == "__main__":
    dict_usernames = {}
    r_user = requests.get(f'https://jsonplaceholder.typicode.com/users/')
    r_user = r_user.json()
    for user in r_user:
        id = user['id']
        dict_usernames[user['id']] = user['username']
    dictionary = {}
    r_todos = requests.get(f'https://jsonplaceholder.typicode.com/todos/')
    r_todos = r_todos.json()
    for id, username in dict_usernames.items():
        dictionary[id] = []
        for task in r_todos:
            if task['userId'] == id:
                newdict = {
                    "username": username,
                    "task": task['title'],
                    "completed": task['completed']
                }
                dictionary[id].append(newdict)
    json_object = json.dumps(dictionary)
    with open("todo_all_employees.json", "w") as file:
        file.write(json_object)
