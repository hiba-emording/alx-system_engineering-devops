#!/usr/bin/python3
"""Returns information about employee ID TODO list progress"""

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

    completed = [t.get("title") for t in todos if t.get("completed")]

    print(f"Employee {user.get('name')} is done with tasks"
          f"({len(completed)}/{len(todos)}):")

    [print(f"\t {title}") for title in completed]
