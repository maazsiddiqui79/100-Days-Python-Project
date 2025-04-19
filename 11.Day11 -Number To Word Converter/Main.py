from colorama import Fore,Style
ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
        "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen", "Twenty"]

tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]


def number_to_word(n):       
    if n == 0:    
        return "Zero"
    elif n <= 20:    
        return ones[n]
    elif n <= 99:
        return tens[n // 10] + (" " + ones[n % 10] if n % 10 != 0 else "")
    
    elif n <= 9_99:
        return ones[n // 100] + " Hundered " + (number_to_word(n % 100) if n % 100 != 0 else "")
    
    elif n <= 9_999:
        return ones[n // 1_000] + " Thousand " + (number_to_word(n % 1_000) if n % 1_000 != 0 else "")
    
    elif n <= 99_999:
        return number_to_word(n // 1_000) + " Thousand " + (number_to_word(n % 1_000) if n % 1_000 != 0 else "")
       
    elif n <= 99_99_999:
        return number_to_word(n // 1_00_000) + " Lakh " + (number_to_word(n % 1_00_000) if n % 1_00_000 != 0 else "")
    
    elif n <= 99_99_99_999:
        return number_to_word(n // 1_00_00_000) + " Core " + (number_to_word(n % 1_00_00_000) if n % 1_00_00_000 != 0 else "")
    elif n <= 99999_99_99_999:
        return number_to_word(n // 1_00_00_000) + " Core " + (number_to_word(n % 1_00_00_000) if n % 1_00_00_000 != 0 else "")
    
    else:
        return "Exceeds the limt.. ."


while not False:
    num = int(input("Enter a number from 0 - 99999,99,99,999: "))
    print(f" {Fore.LIGHTBLUE_EX + str(num)}  Converted to Words :  {Fore.CYAN+number_to_word(num)} ")
    
    
    print(Style.RESET_ALL)

