from todo import Todo


def main():
    print("Welcome to the To-Do List Application!")

    todo = Todo()
    choice = 0
    print(
        "1. Add a task \n2. Display tasks \n3. Mark task as completed \n4. Remove completed tasks \n5. Exit"
    )
    while choice != 5:
        choice = input("Choose an option: ")
        if choice.isdigit() == False:
            continue

        choice = int(choice)

        match choice:
            case 1:
                todo.add_task()
            case 2:
                todo.display_tasks()
            case 3:
                todo.mark_completed()
            case 4:
                todo.remove_completed_tasks()
            case 5:
                todo.update_todo_file()
                quit()


if __name__ == "__main__":
    main()
