#!/usr/bin/python3
'''
A python script that uses REST API, for given employer ID passed as a
command line argument, returns information about his/her TODO list progress.
'''

import re
import requests
import sys


# Note: 'requests' is a third-party library hence its installed
if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    arg = re.fullmatch(r'\d+', sys.argv[1])
    if arg:
        try:
            emplId = int(sys.argv[1])
            tasks = requests.get(f"{url}/todos?userId={emplId}").json()
            numTasks = len(tasks)
            numCompTasks = len([x for x in tasks if x['completed']])
            userData = requests.get(f"{url}/users/{emplId}")
            userName = userData.json().get('name')
            TasksTitle = [x.get('title') for x in tasks if x.get('completed')]
            print(f"Employee {userName} is done with\
            tasks({numCompTasks}/{numTasks}):")
            if numCompTasks > 0:
                for title in TasksTitle:
                    print(f"\t {title}")
        except Exception as e:
            pass
