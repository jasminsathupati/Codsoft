# Define a list to store tasks
tasks = []

# Function to add a new task
def add_task():
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    task = {
        'title': title,
        'description': description,
        'status': 'Incomplete'
    }
    tasks.append(task)
    print("Task added successfully!")

# Function to view all tasks
def view_tasks():
    print("\n--- Your Tasks ---")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. Title: {task['title']}")
        print(f"   Description: {task['description']}")
        print(f"   Status: {task['status']}")
        print("------------------")

# Function to mark a task as complete
def complete_task():
    view_tasks()
    try:
        index = int(input("Enter the index of the task to mark as complete: ")) - 1
        tasks[index]['status'] = 'Complete'
        print("Task marked as complete!")
    except IndexError:
        print("Invalid index! Please enter a valid index.")
    except ValueError:
        print("Invalid input! Please enter a valid integer index.")

# Function to delete a task
def delete_task():
    view_tasks()
    try:
        index = int(input("Enter the index of the task to delete: ")) - 1
        del tasks[index]
        print("Task deleted successfully!")
    except IndexError:
        print("Invalid index! Please enter a valid index.")
    except ValueError:
        print("Invalid input! Please enter a valid integer index.")

# Function to display the main menu
def display_menu():
    print("\n---- To-Do List Application ----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Exit")

# Main function to run the application
def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            complete_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Thank you for using the To-Do List Application. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()