#!/usr/bin/python3
"""
Script to retrieve TODO list progress of an employee from a given REST API
and export the data in JSON format.
"""

import sys
import requests
import json

def get_employee_todo_progress(employee_id):
    """
    Retrieves and displays the TODO list progress of a given employee.
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    try:
        user_response = requests.get(user_url)
        user_data = user_response.json()
        employee_name = user_data.get('name')

        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        json_data = {employee_id: []}
        for task in todos_data:
            json_data[employee_id].append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": employee_name
            })

        json_filename = f"{employee_id}.json"
        with open(json_filename, 'w') as json_file:
            json.dump(json_data, json_file, indent=4)

        print(f"JSON file '{json_filename}' has been created with the TODO list of Employee {employee_name}.")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)
    
    employee_id = sys.argv[1]
    if not employee_id.isdigit():
        print("Employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_progress(employee_id)

