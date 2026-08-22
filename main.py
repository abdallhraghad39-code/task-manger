import json
import os 

# ******LOAD TASK*******

def load_tasks():
    try:
        with open("tasks.json", "r", encoding = "utf-8") as file:
            tasks = json.load(file)
            return tasks
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error: tasks.json is corrupted. Starting with an empty task list.")
        return []

# *******SAVE TASKS*******

def save_tasks(tasks):
    #To know where the file is being saved
    print("Saving file in:", os.getcwd())

    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)

# *******DISPLY MENU*******

def display_menu():
    print("\n==== Task Manger ====")
    print("1. ADD TASK")
    print("2. VIEW TASK")
    print("3. UPDATE TASK")
    print("4. DELETE TASK")
    print("5. COMPLETE TASK")
    print("6. EXIT")

# *******FIND TASK*******

def find_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task

    return None

# *******ADD TASK*******

def add_task(tasks):

    title = input("Enter task title: ").strip()

    if not title:
        print("Title cannot be empty.")
        return

    # Generate new ID
    if tasks:
        new_id = max(task["id"] for task in tasks) + 1
    else:
        new_id = 1

    task = {
        "id": new_id,
        "title": title,
        "completed": False
    }

    tasks.append(task)

    save_tasks(tasks)

    print("Task added successfully.")

# *******VIEW TASK*******

def view_tasks(tasks):
     if not tasks:
         print("No Tasks Found!")
         return

     print("\n===== YOUR TASKS =====")

     for task in tasks:
         status = "Completed" if task["completed"] else "Not Completed"

         print(
              f'{task["id"]}. '
              f'{task["title"]} - '
              f'{status}'
         )

# *******UPDATE TASK*******

def update_task(tasks):
    try:
        task_id = int(input("Enter task ID: "))

    except ValueError:
        print("Please enter a number.")
        return

    task = find_task(tasks, task_id)

    if task is None:
        print("No task with that ID.")
        return

    new_title = input("Enter new title: ").strip()

    if not new_title:
        print("Title cannot be empty.")
        return

    task["title"] = new_title

    save_tasks(tasks)

    print("Task updated successfully.")

# *******DELETE TASK*******
def delete_task(tasks):
    try:
        task_id = int(input("Enter task ID: "))

    except ValueError:
        print("Please enter a number.")
        return

    task = find_task(tasks, task_id)

    if task is None:
      print("No task with that ID.")
      return  

    tasks.remove(task)

    save_tasks(tasks)

    print("Task deleted successfully.")

# *******COMPLETE TASK*******

def complete_task(tasks):
    try:
        task_id = int(input("Enter task ID: "))

    except ValueError:
        print("Please enter a number.")
        return

    task = find_task(tasks, task_id)

    if task is None:
      print("No task with that ID.")
      return

    if task["completed"]:
        print("Task is already completed.")
        return

    task["completed"] = True

    save_tasks(tasks)

    print("Task completed successfully.")

# *******MAIN PROGRAM*******

def main():

    tasks = load_tasks()

    running = True
    while running:

        display_menu()

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            update_task(tasks)

        elif choice == "4":
            delete_task(tasks) 
        
        elif choice == "5":
            complete_task(tasks)  
            
        elif choice == "6":
            running = False
            print("Goodbye!")

        else:
            print("Invalid option.")

# START PROGRAM
if __name__ == "__main__":
    main()
