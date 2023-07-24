#!/usr/bin/python3
"""Python script gathers data from an API"""


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

    with open('{}.csv'.format(user_id), 'w') as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'
                       .format(user_id, name, task.get('completed'),
                               task.get('title')))


if __name__ == "__main__":
    get_list()
