#!/usr/bin/python3
"""Returns information about employee ID TODO list progress"""

import requests
import json


if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/"

    users_response = requests.get(url + "users")
    users = users_response.json()

    all_employee_data = {}

    for user_info in users:
        user_id = user_info.get("id")
        username = user_info.get("username")

        todos_response = requests.get(
                url + "todos", params={"userId": user_id}
                )
        todos = todos_response.json()

        tasks_data = []
        for task in todos:
            task_data = {
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username
            }
            tasks_data.append(task_data)

        all_employee_data[user_id] = tasks_data

    with open("todo_all_employees.json", mode='w') as file:
        json.dump(all_employee_data, file)
