import requests
import sys

def fetch_employee_data(employee_id):
    # Define the base URL for the API
    base_url = "https://jsonplaceholder.typicode.com/"

    # Construct the URLs for employee details and their todo list
    employee_url = f"{base_url}users/{employee_id}"
    todo_url = f"{base_url}users/{employee_id}/todos"

    # Make requests to get employee details and todo list
    try:
        employee_response = requests.get(employee_url)
        employee_response.raise_for_status()
        todo_response = requests.get(todo_url)
        todo_response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(f"Error: {e}")
        sys.exit(1)

    # Parse JSON responses
    employee_data = employee_response.json()
    todo_data = todo_response.json()

    return employee_data, todo_data

def main():
    # Check if an employee ID is provided as a command line argument
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    # Fetch employee data and todo list
    employee_data, todo_data = fetch_employee_data(employee_id)

    # Extract relevant information
    employee_name = employee_data.get("name")
    total_tasks = len(todo_data)
    completed_tasks = sum(1 for task in todo_data if task.get("completed"))

    # Print employee todo list progress
    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
    for task in todo_data:
        if task.get("completed"):
            print(f"\t{task.get('title')}")

if __name__ == "__main__":
    main()
