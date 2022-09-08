#!/usr/bin/python3
"""Script to export data in the JSON format."""

import json
import requests
import sys

if __name__ == "__main__":
    id = int(sys.argv[1])
    dictionary = {id: []}
    r_user = requests.get(f'https://jsonplaceholder.typicode.com/users/')
    r_user = r_user.json()
    for user in r_user:
        if user['id'] == id:
            username = user['username']
    r_todos = requests.get(f'https://jsonplaceholder.typicode.com/todos/')
    r_todos = r_todos.json()
    for task in r_todos:
        if task['userId'] == id:
            newdict = {
                "task": task['title'],
                "completed": task['completed'],
                "username": username
            }
            dictionary[id].append(newdict)
    json_object = json.dumps(dictionary)
    with open(f"{sys.argv[1]}.json", "w") as file:
        file.write(json_object)
