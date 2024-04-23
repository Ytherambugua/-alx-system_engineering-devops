#!/usr/bin/python3
"""
Script to export data from the JSONPlaceholder API to JSON format.
"""

import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 1:
        sys.exit(1)

    url_users = 'https://jsonplaceholder.typicode.com/users'
    url_todos = 'https://jsonplaceholder.typicode.com/todos'

    response_users = requests.get(url_users)
    response_todos = requests.get(url_todos)

    if response_users.status_code != 200 or response_todos.status_code != 200:
        sys.exit(1)

    users = response_users.json()
    todos = response_todos.json()

    data = {}
    for user in users:
        user_id = str(user['id'])
        data[user_id] = []
        for todo in todos:
            if todo['userId'] == user['id']:
                todo_data = {
                    "username": user['username'],
                    "task": todo['title'],
                    "completed": todo['completed']
                }
                data[user_id].append(todo_data)

    with open('todo_all_employees.json', 'w') as f:
        json.dump(data, f)

