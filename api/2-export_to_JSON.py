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

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    user_id, username = get_user_info(employee_id)

    if user_id is None:
        print(f"User with ID {employee_id} not found.")
        sys.exit(1)

    response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")
    tasks = response.json()

    json_data = {user_id: []}

    for task in tasks:
        task_completed_status = task['completed']
        task_title = task['title']
        json_data[user_id].append({"task": task_title, "completed": task_completed_status, "username": username})

    json_filename = f"{user_id}.json"

    with open(json_filename, 'w') as jsonfile:
        json.dump(json_data, jsonfile, indent=2)

    print(f"Data has been exported to {json_filename}")

if __name__ == "__main__":
    main()
