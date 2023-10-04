import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    # Fetch data from the API
    response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")
    tasks = response.json()

    # Get the user information
    user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    user_data = user_response.json()
    user_id = user_data['id']
    username = user_data['username']

    # Define the CSV file name
    csv_filename = f"{user_id}.csv"

    # Open the CSV file for writing
    with open(csv_filename, 'w', newline='') as csvfile:
        # Create a CSV writer
        csv_writer = csv.writer(csvfile)

        # Write the header row
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        # Write the task data
        for task in tasks:
            task_completed_status = task['completed']
            task_title = task['title']
            csv_writer.writerow([user_id, username, str(task_completed_status), task_title])

    print(f"Data has been exported to {csv_filename}")
