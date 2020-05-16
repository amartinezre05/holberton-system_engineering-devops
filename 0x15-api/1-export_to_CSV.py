#!/usr/bin/python3
"""  script to export data in the CSV format """
import csv
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    empl_get = requests.get(
        url + "users/{}".format(argv[1])).json()
    empl_tasks = requests.get(
        url + "todos?userId={}".format(argv[1])).json()

    name = empl_get.get('username')
    with open("{}.csv".format(argv[1]), 'w') as f:
        wr = csv.writer(f, quoting=csv.QUOTE_ALL)
        for t in empl_tasks:
            t_title = t.get('title')
            t_compl = t.get('completed')
            wr.writerow([argv[1], name, t_compl, t_title])
