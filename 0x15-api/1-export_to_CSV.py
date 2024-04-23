#!/usr/bin/python3
"""
Script to retrieve TODO list progress of an employee from a given REST API
and export the data in CSV format.
"""

import csv
import requests
import sys

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

        csv_filename = f"{employee_id}.csv"
        with open(csv_filename, mode='w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
            csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

            for task in todos_data:
                csv_writer.writerow([employee_id, employee_name, task.get('completed'), task.get('title')])

        print(f"CSV file '{csv_filename}' has been created with the TODO list of Employee {employee_name}.")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)
    
    employee_id = sys.argv[1]
    if not employee_id.isdigit():
        print("Employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_progress(employee_id)

