import requests
import sys

def get_employee_info(employee_id):
    # Define the base URL for the API
    base_url = "https://jsonplaceholder.typicode.com/"

    # Make a request to get employee details
    employee_url = f"{base_url}users/{employee_id}"
    employee_response = requests.get(employee_url)

    if employee_response.status_code != 200:
        print(f"Employee with ID {employee_id} not found.")
        sys.exit(1)

    employee_data = employee_response.json()
    employee_name = employee_data["name"]

    # Make a request to get TODO list for the employee
    todo_url = f"{base_url}users/{employee_id}/todos"
    todo_response = requests.get(todo_url)

    if todo_response.status_code != 200:
        print(f"TODO list for employee with ID {employee_id} not found.")
        sys.exit(1)

    todo_data = todo_response.json()
    
    # Calculate completed tasks and total tasks
    completed_tasks = sum(1 for task in todo_data if task["completed"])
    total_tasks = len(todo_data)

    # Display employee's TODO list progress
    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
    for task in todo_data:
        if task["completed"]:
            print(f"\t{task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    get_employee_info(employee_id)
