#!/usr/bin/python3
"""Script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress"""

import requests
import sys

if __name__ == "__main__":
    r_user = requests.get('https://jsonplaceholder.typicode.com/users/')
    r_user = r_user.json()
    for user in r_user:
        if user['id'] == int(sys.argv[1]):
            name = user['name']
    r_todos = requests.get('https://jsonplaceholder.typicode.com/todos/')
    r_todos = r_todos.json()
    total_tasks = 0
    completed = 0
    tasks_completed = []
    for task in r_todos:
        if task['userId'] == int(sys.argv[1]):
            total_tasks += 1
            if task['completed'] is True:
                completed += 1
                tasks_completed.append(task['title'])
    print("Employee {} is done with tasks({}/{}):".format(
        name, completed, total_tasks))
    for task in tasks_completed:
        print("\t {}".format(task))
