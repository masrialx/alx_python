import requests
import sys

def get_employee_data(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    
    # Fetch employee details
    employee_response = requests.get(f"{base_url}/users/{employee_id}")
    employee_data = employee_response.json()
    employee_name = employee_data.get("name")

    # Fetch employee's TODO list
    todos_response = requests.get(f"{base_url}/users/{employee_id}/todos")
    todos_data = todos_response.json()

    # Calculate the number of completed and total tasks
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for todo in todos_data if todo['completed'])

    return employee_name, completed_tasks, total_tasks, todos_data

def display_employee_progress(employee_name, completed_tasks, total_tasks, completed_task_titles):
    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
    for title in completed_task_titles:
        print(f"    {title}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    
    employee_id = int(sys.argv[1])

    try:
        employee_name, completed_tasks, total_tasks, todos_data = get_employee_data(employee_id)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

    completed_task_titles = [todo['title'] for todo in todos_data if todo['completed']]
    
    display_employee_progress(employee_name, completed_tasks, total_tasks, completed_task_titles)
