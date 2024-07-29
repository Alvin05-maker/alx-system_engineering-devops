#!/usr/bin/python3

"""script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""

import requests
import sys

if __name__ == "__main__":
    _, emp_id = sys.argv
    response = requests.get(
        "https://jsonplaceholder.typicode.com/todos/",
        params={"userId": emp_id})

    if response.status_code == 200 and response.text != "[]":
        todo_info = response.json()
        response = requests.get(
            "https://jsonplaceholder.typicode.com/users/",
            params={"id": emp_id})

        user_name = response.json()[0]["name"]

        completed_tasks = [
            task for task in todo_info if task["completed"]]
        print("Employee {} is done with tasks({}/{}):".format(
            user_name, len(completed_tasks), len(todo_info)
        ))
        [print(f"\t {task['title']}") for task in completed_tasks]
