import json
import requests
import sys

def get_user_info(employee_id):
    user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    if user_response.status_code == 200:
        user_data = user_response.json()
        return user_data['id'], user_data['username']
    else:
        return None, None

def export_all_tasks():
    all_tasks = {}

    for employee_id in range(1, 11):  # Assuming you have 10 employees with IDs from 1 to 10
        user_id, username = get_user_info(employee_id)

        if user_id is not None:
            response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")
            tasks = response.json()

            task_list = []
            for task in tasks:
                task_list.append({
                    "username": username,
                    "task": task['title'],
                    "completed": task['completed']
                })

            all_tasks[str(user_id)] = task_list

    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(all_tasks, jsonfile, indent=2)

    print("Data has been exported to todo_all_employees.json")

if __name__ == "__main__":
    export_all_tasks()
