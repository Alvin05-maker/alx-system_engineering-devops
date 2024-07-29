#!/usr/bin/python3

"""script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
export data in .json"""

import json
import requests


def get_employee_data(emp_id):
    """get data about employee with id todo list"""

    response = requests.get(
        "https://jsonplaceholder.typicode.com/todos/",
        params={"userId": emp_id})

    # get username
    if response.status_code == 200 and response.text != "[]":
        todo_list = response.json()
        response = requests.get(
            "https://jsonplaceholder.typicode.com/users/",
            params={"id": emp_id})
        username = response.json()[0]["username"]

        # delete keys not needed, change keys name, arrange in order
        order = ["username", "task", "completed"]
        sorted_todo_list = []

        for to_do in todo_list:
            to_do["task"] = to_do["title"]
            to_do["username"] = username
            sorted_dict = {}
            for key in order:
                sorted_dict[key] = to_do[key]
            sorted_todo_list.append(sorted_dict)

        return sorted_todo_list


if __name__ == "__main__":
    all_employee_data = {}

    for emp_id in range(1, 11):
        all_employee_data[emp_id] = get_employee_data(emp_id=emp_id)

    with open("todo_all_employees.json", 'w') as json_file:
        json.dump(all_employee_data, json_file)
