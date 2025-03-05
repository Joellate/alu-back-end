import requests
import sys

def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com/"
    
    # Fetch user data
    user_response = requests.get(f"{base_url}users/{employee_id}")
    if user_response.status_code != 200:
        print("Error: Employee not found")
        return
    user_data = user_response.json()
    
    # Fetch TODO list data
    todos_response = requests.get(f"{base_url}todos", params={"userId": employee_id})
    if todos_response.status_code != 200:
        print("Error fetching TODO list")
        return
    todos = todos_response.json()
    
    # Extract data
    employee_name = user_data.get("name")
    total_tasks = len(todos)
    completed_tasks = [task for task in todos if task.get("completed")]
    num_completed = len(completed_tasks)
    
    # Print output
    print(f"Employee {employee_name} is done with tasks({num_completed}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
    else:
        get_employee_todo_progress(int(sys.argv[1]))
