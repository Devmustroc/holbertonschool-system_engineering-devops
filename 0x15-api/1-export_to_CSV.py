#!/usr/bin/python3
"""
accessing a url with employee ID to return information
"""

import csv
import requests
from sys import argv

if __name__ == '__main__':
    employee_id = int(argv[1])
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                        format(employee_id)).json()
    todo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                        format(employee_id)).json()

    task_done = []
    for task in todo:
        if task.get('completed') is True:
            task_done.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".
          format(user.get('name'), len(task_done), len(todo)))
    for done in task_done:
        print("\t {}".format(done))

    with open('{}.csv'.format(employee_id), "w") as csv_f:
        data = csv.writer(csv_f, quoting=csv.QUOTE_ALL)
        for task in todo:
            data.writerow(
                [employee_id,
                 user.get('username'),
                 task.get('completed'),
                 task.get('title')])
