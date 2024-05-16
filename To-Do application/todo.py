import os
import json
from datetime import datetime

def load_tasks():
    if os.path.exists('tasks.json'):
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
        return tasks
    else:
        return []


def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            status = "Completed" if task['completed'] else "Pending"
            print(f"{i}. {task['task']} - {status}")

def add_task(tasks, new_task, due_date=None):
    task_details = {'task': new_task, 'completed': False, 'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    
    if due_date:
        task_details['due_date'] = due_date
    
    tasks.append(task_details)
    save_tasks(tasks)
    print("Task added successfully.")

def complete_task(tasks, task_index):
    if 0 < task_index <= len(tasks):
        tasks[task_index - 1]['completed'] = True
        tasks[task_index - 1]['completed_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        save_tasks(tasks)
        print("Task marked as completed.")
    else:
        print("Invalid task index.")

def delete_task(tasks, task_index):
    if 0 < task_index <= len(tasks):
        deleted_task = tasks.pop(task_index - 1)
        save_tasks(tasks)
        print(f"Task '{deleted_task['task']}' deleted successfully.")
    else:
        print("Invalid task index.")

def main():
    tasks = load_tasks()

    while True:
        print("\n1. Display Tasks\n2. Add Task\n3. Complete Task\n4. Delete Task\n5. Quit")
        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            new_task = input("Enter the new task: ")
            due_date = input("Enter the due date (optional, format: YYYY-MM-DD HH:MM): ")
            add_task(tasks, new_task, due_date)
        elif choice == '3':
            display_tasks(tasks)
            task_index = int(input("Enter the task index to mark as completed: "))
            complete_task(tasks, task_index)
        elif choice == '4':
            display_tasks(tasks)
            task_index = int(input("Enter the task index to delete: "))
            delete_task(tasks, task_index)
        elif choice == '5':
            print("Quitting the to-do list application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
