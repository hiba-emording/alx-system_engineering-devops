#!/usr/bin/python3
"""Returns information about employee ID TODO list progress"""

import csv
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

    with open(f"{employee_id}.csv", mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                username,
                task.get('completed'),
                task.get('title')
            ])
