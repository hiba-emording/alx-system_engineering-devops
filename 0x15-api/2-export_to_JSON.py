#!/usr/bin/python3
"""Returns information about employee ID TODO list progress"""

import json
import requests
import sys


if __name__ == "__main__":

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        sys.exit(1)

    url = "https://jsonplaceholder.typicode.com/"

    user_response = requests.get(f"{url}users/{employee_id}")

    user = user_response.json()

    todos_response = requests.get(
        f"{url}todos", params={"userId": employee_id}
    )

    todos = todos_response.json()

    username = user.get('username')

    tasks_data = []
    for task in todos:
        task_data = {
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        }
        tasks_data.append(task_data)

    with open(f"{employee_id}.json", mode='w') as file:
        json.dump({str(employee_id): tasks_data}, file)
