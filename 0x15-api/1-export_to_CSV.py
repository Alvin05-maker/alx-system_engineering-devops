#!/usr/bin/python3

"""script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
export data to csv file"""

import csv
import requests
import sys

if __name__ == "__main__":
    _, emp_id = sys.argv
    response = requests.get(
        "https://jsonplaceholder.typicode.com/todos/",
        params={"userId": emp_id})

    if response.status_code == 200 and response.text != "[]":
        json_data = response.json()
        response = requests.get(
            "https://jsonplaceholder.typicode.com/users/",
            params={"id": emp_id})
        user_name = response.json()[0]["username"]
        json_data = [{**item, "name": user_name} for item in json_data]

        # remove attr not needed
        for item in json_data:
            del item['id']

        with open(emp_id + ".csv", "w", newline='') as csv_file:
            fieldnames = ["userId", "name", "completed", "title"]
            csv_writer = csv.DictWriter(
                csv_file, fieldnames=fieldnames, quoting=1)
            csv_writer.writerows(json_data)
