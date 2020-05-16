#!/usr/bin/python3
"""
    script that, using REST API, for a given employee ID,
    returns information about his/her TODO list progress.
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    empl_get = requests.get(
        url + "users/{}".format(argv[1])).json()
    empl_tasks = requests.get(
        url + "todos?userId={}".format(argv[1])).json()

    name = empl_get.get('name')
    completed = []
    for t in empl_tasks:
        if t.get('completed'):
            completed.append(t)
    print("Employee {} is done with tasks({}/{}):".
          format(name, len(completed), len(empl_tasks)))
    for t in completed:
        print("\t {}".format(t.get('title')))
