#!/usr/bin/python3

"""script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
export data in .json"""

import json
import requests
import sys

if __name__ == "__main__":
    _, emp_id = sys.argv
    response = requests.get(
        "https://jsonplaceholder.typicode.com/todos/",
        params={"userId": emp_id})

    # get username
    if response.status_code == 200 and response.text != "[]":
        todo_list = response.json()
        response = requests.get(
            "https://jsonplaceholder.typicode.com/users/",
            params={"id": emp_id})
        user_name = response.json()[0]["username"]

        # delete keys not needed, change keys name, arrange in order
        order = ["task", "completed", "username"]
        sorted_todo_list = []

        for to_do in todo_list:
            to_do["task"] = to_do["title"]
            to_do["username"] = user_name
            sorted_dict = {}
            for key in order:
                sorted_dict[key] = to_do[key]
            sorted_todo_list.append(sorted_dict)

        user_todo_info = {
            emp_id: sorted_todo_list
        }
        with open(emp_id + '.json', 'w') as json_file:
            json.dump(user_todo_info, json_file)
