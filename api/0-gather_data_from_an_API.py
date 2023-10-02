import requests
import sys

def get_employee_data(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch employee details
    employee_response = requests.get(f"{base_url}/users/{employee_id}")
    employee_data = employee_response.json()
    employee_name = employee_data.get("name")

    # Fetch employee's TODO list
    todos_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    todos_data = todos_response.json()

    return employee_name, todos_data

def display_employee_progress(employee_name, todos_data):
    completed_tasks = [todo for todo in todos_data if todo['completed']]
    total_tasks = len(todos_data)

    print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")
    for task in completed_tasks:
        print(f"    {task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    try:
        employee_name, todos_data = get_employee_data(employee_id)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

    display_employee_progress(employee_name, todos_data)
