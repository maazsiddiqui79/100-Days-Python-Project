from os import system
def clac ():
    while True :
        num1 = float(input("Enter First Number: "))
        operator = str(input("\n+\n-\n*\n\\ \nEnter operator: "))
        if operator not in ["+","-","*","/"]:
            result = print("INVALID OPERATOR")
            continue  
             
        num2 = float(input("Enter Second Number: "))
    
        match operator:
            case "+":
                result = num1 + num2
            case "-":
                result = num1 - num2
            case "*":
                result = num1 * num2
            case "/":
                if num2 == 0:
                    result = print("Cannot divide by 0")
                    break
                else:
                    result = num1 / num2
            
                
        print( f"{num1} {operator} {num2} = {result}")       
        Continuity = str(input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower())
        
        
        while Continuity == 'y'.lower():
            result2 = result
            operator = str(input("\n+\n-\n*\n\ \nEnter operator: "))
            
            num2 = float(input("Enter Second Number: "))
            if operator not in ["+","-","*","/"]:
                result = print("INVALID OPERATOR")
                continue
                        
            match operator:
                case "+":
                    result += num2
                case "-":
                    result -= num2
                case "*":
                    result *= num2
                case "/":
                    if num2 == 0:
                        result = print("Cannot divide by 0")
                        continue  
                    else:
                        result /= num2

            print( f"{result2} {operator} {num2} = {result:.2f}")       
    
            Continuity = str(input(f"Type 'y' to continue calculating with {result:.2f}, or type 'n' to start a new calculation: "))
            if Continuity == 'n'.lower():
                system("cls")
                result =0
        
print(clac())
  


