import requests
import sys
import csv

def get_employee_data(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch employee details
    employee_response = requests.get(f"{base_url}/users/{employee_id}")
    employee_data = employee_response.json()
    user_id = employee_data.get("id")
    username = employee_data.get("username")

    # Fetch employee's TODO list
    todos_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    todos_data = todos_response.json()

    return user_id, username, todos_data

def export_to_csv(user_id, username, todos_data):
    filename = f"{user_id}.csv"

    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for todo in todos_data:
            task_completed_status = "True" if todo['completed'] else "False"
            task_title = todo['title']
            csv_writer.writerow([user_id, username, task_completed_status, task_title])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    try:
        user_id, username, todos_data = get_employee_data(employee_id)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

    export_to_csv(user_id, username, todos_data)
    print(f"Data exported to {user_id}.csv")
