#!/usr/bin/python3
'''
A python script that uses REST API, for given employer ID passed as a
command line argument, convert the employee's information into a json
file
Requirements:

>>Records all tasks that are owned by this employee
>>Format must be: { "USER_ID": [{"task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS,
"username": "USERNAME"}, {"task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}

>>File name must be: USER_ID.json
'''
import json
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
            userInfo = requests.get(f"{url}/users/{userId}")
            userInfoToDict = userInfo.json()
            userName = userInfoToDict.get("username")
            allTasks = requests.get(f"{url}/todos")
            allTasksToDict = allTasks.json()
            dictData = {userId: []}
            for task in allTasksToDict:
                taskTitle = task.get("title")
                taskCompletedStatus = task.get("completed")
                dictData[userId].append({
                                            "task": taskTitle,
                                            "completed": taskCompletedStatus,
                                            "username": userName})
            with open(f"{userId}.json", "w") as jsonfile:
                json.dump(dictData, jsonfile)
        except Exception as e:
            pass
