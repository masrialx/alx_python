import csv
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
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    user_id, username = get_user_info(employee_id)

    if user_id is None:
        print(f"User with ID {employee_id} not found.")
        sys.exit(1)

    response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")
    tasks = response.json()

    csv_filename = f"{user_id}.csv"

    with open(csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in tasks:
            task_completed_status = task['completed']
            task_title = task['title']
            csv_writer.writerow([user_id, username, str(task_completed_status), task_title])

    print(f"Data has been exported to {csv_filename}")

if __name__ == "__main__":
    main()
