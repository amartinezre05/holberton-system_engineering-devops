#!/usr/bin/python3
"""  script to export data in the JSON format """
import json
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    empl_get = url + "users/"
    empl_tasks = url + "todos"

    users = requests.get(empl_get).json()
    data = {}
    with open("todo_all_employees.json", 'w') as f:
        for r in range(0, len(users)):
            empl = requests.get(empl_get + "{}".format(r + 1)).json()
            empl_task = requests.get(empl_tasks + "?userId={}".format(r + 1))
            name = empl.get('username')
            list_t = []
            for t in empl_task.json():
                empl_json = {}
                empl_json["task"] = t.get('title')
                empl_json["completed"] = t.get('completed')
                empl_json["username"] = name
                list_t.append(empl_json)
            data[r + 1] = list_t
        json.dump(data, f)
