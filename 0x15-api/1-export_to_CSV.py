#!/usr/bin/python3
"""Script to export data in the CSV format."""

import csv
import requests
import sys

if __name__ == "__main__":
    f = open('{}.csv'.format(sys.argv[1]), 'w', encoding='UTF8', newline='')
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    id = int(sys.argv[1])
    r_user = requests.get('https://jsonplaceholder.typicode.com/users/')
    r_user = r_user.json()
    for user in r_user:
        if user['id'] == id:
            username = user['username']
    r_todos = requests.get('https://jsonplaceholder.typicode.com/todos/')
    r_todos = r_todos.json()
    for task in r_todos:
        if task['userId'] == id:
            status = task['completed']
            task = task['title']
            writer.writerow([id, username, status, task])
    f.close()
