#!/usr/bin/python3
'''
A python script that fetches REST API for employees information
and convert it into a json format
Requirements:

>>Records all tasks that are owned by this employee
{ "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME",
"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ],
"USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME",
"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}
>>File name must be: todo_all_employees.json
'''
import json
import re
import requests


# Note: 'requests' is a third-party library hence it's installed
if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    try:
        users = requests.get(f"{url}/users").json()
        usersNamesAndIds = [[u.get("username"), u.get("id")] for u in users]
        userDict = {}
        for u in usersNamesAndIds:
            userTodos = requests.get(f"{url}/todos?userid={u[1]}").json()
            userTaskStatus = []
            for t in userTodos:
                status = {
                            "username": u[0],
                            "task": t.get("title"),
                            "completed": t.get("completed")}
                userTaskStatus.append(status)
            userDict[u[1]] = userTaskStatus
        with open("todo_all_employees.json", "w") as jsonfile:
            json.dump(userDict, jsonfile)
    except Exception as e:
        pass
