#!/usr/bin/python3
"""
Script that, using a given REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
import sys

def fetch_employee_todo_list(employee_id):
    """
    Fetches the TODO list of a given employee from the API.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        dict: The JSON response containing the TODO list data.
    """
    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(employee_id)
    response = requests.get(url)
    return response.json()

def display_todo_progress(employee_id, todo_list):
    """
    Displays the progress of the TODO list for a given employee.

    Args:
        employee_id (int): The ID of the employee.
        todo_list (list): The TODO list data.
    """
    employee_name = todo_list[0]['username']
    total_tasks = len(todo_list)
    completed_tasks = [task for task in todo_list if task['completed']]
    num_completed_tasks = len(completed_tasks)

    print("Employee {} is done with tasks({}/{}):".format(employee_name, num_completed_tasks, total_tasks))
    for task in completed_tasks:
        print("\t", task['title'])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])
    todo_list = fetch_employee_todo_list(employee_id)
    display_todo_progress(employee_id, todo_list)

