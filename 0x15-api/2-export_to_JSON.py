#!/usr/bin/python3
"""  script to export data in the JSON format """
import json
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    empl_get = requests.get(
        url + "users/{}".format(argv[1])).json()
    empl_tasks = requests.get(
        url + "todos?userId={}".format(argv[1])).json()

    name = empl_get.get('username')
    data = []
    for t in empl_tasks:
        empl_json = {}
        empl_json["task"] = t.get('title')
        empl_json["completed"] = t.get('completed')
        empl_json["username"] = name
        data.append(empl_json)
    with open("{}.json".format(argv[1]), 'w') as f:
        json_empl = {argv[1]: data}
        json.dump(json_empl, f)
