from os import system


def add_task ():
    system("cls")
    User_Task = input("Enter your task:")
    with open ("DATA_BASE.txt","a+") as f:
        f.write(User_Task)
        print(f"{User_Task} TASK ADDED SUCCESSFULLY !")
        
    
    
def view_task ():
    system("cls")
    with open ("DATA_BASE.txt","r") as f:
        readline = f.readlines()
        
        if not readline:
            print("NO TASK IS THERE")
            return
            
        for i,t in enumerate(readline,start=1):
            print(f"{i} - {t}")
        
    
            
        
def remove_task ():
    system("cls")
    with open ("DATA_BASE.txt","r") as f:
        
        readline = f.readlines()
        
        if not readline:
            print("NO TASK IS THERE")
            return
            
        print("Type '$' to go back\n")
        for i,t in enumerate(readline,start=1):
            print(f"{i} - {t}")
        User_del = input("Enter a Task to delete:  ")
        
        if User_del == "$":
            return
        
        if not User_del.isdigit() or not(1<=int(User_del)<=len(readline)):
            print("Invalid Input")
            return
            
        del readline[int(User_del)-1]
        
    with open ("DATA_BASE.txt","w") as f:
        f.writelines(readline)
        
        
        
        
        
         

    
        


while True:
    print("*"+"TO DO".center(25,"-")+"*")
    print (" _______________________ ")
    print ("*                       *")
    print ("|    1. Add Task        |")
    print ("|    2. View Task       |")
    print ("|    3. Remove Task     |")
    print ("|    4. Exit            |")
    print ("*_______________________*\n")


    user_choice = int(input("Enter your choice: "))
    
    if user_choice == 1:
        
        add_task()
    elif user_choice == 2:
        
        view_task()
    elif user_choice == 3:
        remove_task()
        
    elif user_choice == 4:
        exit()
    
        




