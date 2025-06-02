print("Welcome to tip calculator! ".center(100,"-"))
bill=float(input("What was the total bill : ".rjust(63," ")))
tip=float(input("How much tip would you like to 10$ , 15$ , 20$ or more : ".rjust(80," ")))
each_split=int(input("How many people to split the bill : ".rjust(75," ")))

# tip_percent = float

total_bill =float(bill +(bill*(tip /100)))
split=total_bill/each_split
print(f"Total bill [incld tip]: {total_bill:.2f}".rjust(63," "))
print(f"Each person pay: {split:.2f}".rjust(63," "))

