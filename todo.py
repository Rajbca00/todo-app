import json
import os

from constants import JSON_FILE


class Todo:
    def __init__(self):
        self.todos = []
        self.load_todo_file()

    def load_todo_file(self):
        if os.path.exists(JSON_FILE):
            with open(JSON_FILE, "r") as f:
                self.todos = json.load(f)

    def update_todo_file(self):
        json_object = json.dumps(self.todos)
        with open(JSON_FILE, "w") as f:
            f.write(json_object)

    def add_task(self):
        description = input("Enter task description: ").strip()
        if not description:
            print(f"Invalid description provided. Please enter a valid description.")
            return

        self.todos.append({"description": description, "completed": False})
        self.update_todo_file()

    def display_tasks(self):
        print("Your to-do list:")
        if len(self.todos) == 0:
            print("(empty)")
        else:
            for i, todo in enumerate(self.todos):
                print(
                    f"{i+1}. [{'x' if todo['completed'] == True else ' '}]  {todo['description']}"
                )

    def mark_completed(self):
        task_number = input("Enter the task number to mark as completed: ")
        if not task_number.isdigit():
            print(
                "Invalid task number input provided. Value should be a valid integer."
            )
            return

        task_number = int(task_number) - 1

        if task_number < 0 and task_number >= len(self.todos):
            print(
                f"Invalid task number input provided. Todo number {task_number} not exists."
            )
            return

        task_number = int(task_number) - 1
        self.todos[task_number]["completed"] = True
        print("Task marked as completed!")
        self.update_todo_file()

    def remove_completed_tasks(self):
        self.todos = [todo for todo in self.todos if todo["completed"] == False]
        print("Completed tasks removed!")
        self.update_todo_file()
