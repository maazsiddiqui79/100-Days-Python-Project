import random
lst =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","j","u","v","w","x","y","z"," "]

lst_symbol=["~","!","@","#","$","%","^","&","*","_","+","?"," "]

lst_num =[0,9,8,7,6,5,4,3,2,1," "]



print("PASSWORD GENERATOR\n")
letter = input("\nDo you want Letter: in passcode[y on n]: ")
num = input("\nDo you want Number: in passcode[y on n]: ")
symbol = input("\nDo you want Symbol: in passcode[y on n]: ")
size = int(input("\nEnter the size of your Passcode: "))

pas = []

if letter.lower() == "y":
    pas.extend(lst)
elif letter.lower() == "n":
    pass
else:
    print("Enter a vaild option")
    
if num.lower() == "y":
    pas.extend(lst_num)
elif num.lower() == "n":
    pass
else:
    print("Enter a vaild option")
    
if symbol.lower() == "y":
    pas.extend(lst_symbol)
elif symbol.lower() == "n":
    pass
else:
    print("Enter a vaild option")

print(pas)
print("\nPassword:")
for i in range(size+1):
    print(random.choice(pas),end="")






# Using Switch Case


# import random
# print("PassWord Generator".upper())

# lst =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","j","u","v","w","x","y","z"," "]

# lst_with_symbol=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","j","u","v","w","x","y","z","!","@","#","$","%","^","&","*","_","+","?"," "]

# lst_num =["a","b","c","d"," ","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","j","u","v","w","x","y","z",0,9,8,7,6,5,4,3,2,1," "]

# lst_symbol =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","j","u","v","w","x","y","z",0,9,8,7,6,5,4,3,2,1,"!","@","#","$","%","^","&","*","_","+","?"," "]

# print("1.Alphabets only:\n2.Alphabets n Numbers:\n3.Alphabets,numbers and symbol:\n4.Alphabet n Symbol:")
# Type= int(input("\nWhat do you want in your password: "))

# a = int(input("\nEnter the size of your Passcode: "))


# match Type:
#     case 1:
#         print("\nPassword:")
#         print(random.choices(lst,k=a),end="")
        
#     case 2:
#         print("Password:")
#         for i in range(a+1):
#             print(random.choice(lst_num),end="")
        
#     case 3:
#         print("Password:")
#         for i in range(a+1):
#             print(random.choice(lst_symbol),end="")

#     case 4:
#         print("Password:")
#         for i in range(a+1):
#             print(random.choice(lst_with_symbol),end="")
            
#     case _:
#         print("Invalid chioce.")