#!/usr/bin/python3
'''
A python script that uses REST API, for given employer ID passed as a
command line argument, exports employee's data in the csv format.
Format: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
File name: USER_ID.csv
'''

import re
import requests
import sys


# Note: 'requests' is a third-party library hence it's installed
if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    arg = re.fullmatch(r'\d+', sys.argv[1])
    if arg:
        try:
            userId = int(sys.argv[1])
            tasks = requests.get(f"{url}/todos?userId={userId}").json()
            userData = requests.get(f"{url}/users/{userId}")
            username = userData.json().get('username')
            with open(f"{userId}.csv", "w") as csvfile:
                for t in tasks:
                    com = t.get("completed")
                    ti = t.get("title")
                    csvfile.write(f'"{userId}","{username}","{com},"{ti}"\n')
        except Exception as e:
            pass
