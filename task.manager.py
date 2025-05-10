import os
import time

filer = "tasks.txt"
if not os.path.exists(filer):
    with open (filer, "w") as file:
        pass

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def start():
    print("What should I help you with?\n")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")
clear_screen()
start()
choice = 0
while choice != 4:
    time.sleep(1)
    try:
        choice = int(input("\nCommand: "))
    except ValueError:
        print("That action doesn't exist.")
        time.sleep(1)
        clear_screen()
        start()
    if choice == 1:
        clear_screen()
        with open(filer, "r") as file:
            lines = file.readlines()
        if not lines:
            print("\nNo tasks yet.")
        else:
            for i, task in enumerate(lines,start=1):
                print(f"{i}: {task.strip()}")
            back = "null"
            while back != "back":
                back = str(input("\nType 'back' to go back: "))
                back = back.lower()
                if back == "back":
                    time.sleep(1)
                    clear_screen()
                    start()
    elif choice == 2:
        clear_screen()
        task = str(input("\nWhat should the new task be?: "))
        with open (filer,"a") as file:
            file.write(f"{task} \n")
            print(f"Succesfully added {task} as a task.")
        time.sleep(2)
        clear_screen()
        start()
    elif choice == 3:
            clear_screen()
            with open(filer, "r") as file:
                lines = file.readlines()
            if not lines:
                print("\nNo tasks yet.")
            else:
                for i, task in enumerate(lines,start=1):
                    print(f"{i}: {task.strip()}")
            delete = str(input("\nWhich task do you want deleted?(insert a number): "))
            if delete.isdigit():
                delete = int(delete)
            with open(filer, "r") as file:
                lines = file.readlines()
            if 1 <= delete <= len(lines):
                del lines[delete-1]
                with open(filer, "w") as file:
                    file.writelines(lines)
                    print(f"Task number {delete} has been deleted.")
                    time.sleep(2)
                    clear_screen()
                    start()
            else:
                print("That task number doesn't exist.")
    elif choice == 4:
        clear_screen()
        print("Goodbye!\n")
    else:
        clear_screen()
        print("That action doesn't exist.")        
