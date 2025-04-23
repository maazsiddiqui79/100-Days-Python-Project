from os import system

todo_list = []

def add_task ():
    user_task = input("Enter your Task: ").lower()
    print("TASK ADDED SUCCESSFULLY !")
    todo_list.append(user_task)

    
    
def view_task ():
    print("Tasks :")
    if not todo_list:
        print("NO TASKS.")
    else:
        for i,t in enumerate(todo_list,start=1):
            print(f"{i} - {t}")
        
        # system("cls")
def remove_task ():
    
    print("Enter '0' for back")
    for i,t in enumerate(todo_list,start=1):
        print(f"{i} - {t}")
    user_del = int(input("Which Task do you want to delete: "))
    # print(todo_list[user_del-1])
    if user_del == 0:
        pass
    if 1 >= user_del >= len(todo_list):
        print("INVALID INPUT")
        pass
    else:
        todo_list.remove(todo_list[user_del-1])
        print("TASK REMOVED SUCCESSFULLY")
        
    
    # system("cls")
    
        


while True:
    print("\n")
    print (" _______________________ ")
    print ("*                       *")
    print ("|    1. Add Task        |")
    print ("|    2. View Task       |")
    print ("|    3. Remove Task     |")
    print ("|    4. Exit            |")
    print ("*_______________________*\n")


    user_choice = int(input("Enter your choice: "))
    
    if user_choice == 1:
        system("cls")
        add_task()
    elif user_choice == 2:
        system("cls")
        view_task()
    elif user_choice == 3:
        system("cls")
        remove_task()
    elif user_choice == 4:
        exit()
    
        




