#!/usr/bin/python3
"""Python script gathers data from an API"""


import requests
from sys import argv


def get_list():
    """Get and display info about todo list progress"""
    url = "https://jsonplaceholder.typicode.com"
    user_id = argv[1]

    employee = requests.get("{}/users/{}".format(url, user_id)).json()
    r = requests.get("{}/users/{}/todos".format(url, user_id)).json()

    done = filter(lambda y: y.get('completed'), r)
    done = [i for i in done]
    completed = len(done)

    print("Employee {} is done with tasks({}/{}):".format(
        employee.get('name'), completed, len(r)))

    for task in done:
        print("\t{}".format(task.get('title')))


if __name__ == "__main__":
    get_list()
