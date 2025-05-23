import random
print("PassWord Generator\n".upper())

lst =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","j","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

symbol=["!","@","#","$","%","^","&","*","_","+","?",")","(","[","]","~"]

lst_num =[0,9,8,7,6,5,4,3,2,1,]

passcode = []
size =int( input("How many letters would you like in your password:"))
symbol_n =int( input("How many Symbol would you like in your password:"))
num = int(input("How many Numbers would you like in your password:"))


passcode.extend(random.choices(symbol,k=symbol_n))
    
for i in range(num+1):
    passcode.append(random.choice(lst_num))
    
for i in range(size+1):
    passcode.append(random.choice(lst))
print(passcode)
random.shuffle(passcode)
print(passcode)

password = ""
for char in passcode:
  password += str(char)

print(f"Your password is: {password}")

# or use string instead of list and use += to add element