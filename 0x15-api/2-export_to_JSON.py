#!/usr/bin/python3
"""Python script gathers data from an API"""

import json
import requests
from sys import argv


def get_list():
    """Get and display info about todo list progress"""
    user_id = argv[1]
    emp_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)

    response = requests.get(emp_url)
    name = response.json().get('username')

    todo_url = "{}/todos".format(emp_url)
    response = requests.get(todo_url)
    tasks = response.json()

    dictionary = {user_id: []}
    for task in tasks:
        dictionary[user_id].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": name
        })
    with open('{}.json'.format(user_id), 'w') as filename:
        json.dump(dictionary, filename)


if __name__ == "__main__":
    get_list()
