print("----Welcome to Python Pizza Deliveries!-----------")
print("Menu".center(50,"-"))
print("Small Pizza (S):$15")
print("Medium Pizza (M):$20")
print("large Pizza (L):$25")
print("Pepperoni S:+$2 M,L:+$3")
print("Cheese:+$2\n")

size = input("What Size Pizza do You want? [S,M,L] : ")
size_mrp =0

if size.upper() == "S":
    size_mrp += 15
elif size.upper() == "M":
    size_mrp += 20
elif size.upper() == "L":
    size_mrp += 25
else:
    print("Enter a valid size")
    exit()
    
pepperoni = input("Do you want Pepperoni on your Pizza [Y or N] : ")
pepperoni_mrp =0

if pepperoni.upper() == "Y":
    if size.upper() == "S":
        pepperoni_mrp +=2    
    if size.upper() == "M" or size.upper() == "L":
        pepperoni_mrp +=3  
elif pepperoni.upper() == "N":
    print()
      
else:
    print("Enter a valid option")
    exit()
    
cheese = input("Do you want cheese on your Pizza [Y or N] : ")
cheese_mrp =0

if cheese.upper() =="Y":
    cheese_mrp +=2
elif cheese.upper() == "N":
    print()
else:
    print("Enter a valid option")
    exit()
        
    

Total_bill= size_mrp+pepperoni_mrp+cheese_mrp
Qty = int(input("Pizza Qty : "))

print("Bill".center(50,"-"))
print(f"\nEach Pizza: {Total_bill}")
print(f"Total: {Total_bill*Qty}\n")
print("Thank You Visit Again".center(50,"-"))