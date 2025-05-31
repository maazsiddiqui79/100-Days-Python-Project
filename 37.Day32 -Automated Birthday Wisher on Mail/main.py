##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random message from message templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the message generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

import pandas as pd
import datetime as dt
import random
import smtplib

data = pd.read_csv("birthdays.csv")

lst = data.to_dict(orient="records")

name_lst = [i["name"] for i in lst]


email_lst = [i["email"] for i in lst]


month_lst = [i["month"] for i in lst]


day_lst = [i["day"] for i in lst]


date = dt.datetime.now()

for i in range(len(month_lst)):
    if date.month == month_lst[i] and date.day == day_lst[i]:
        birth_boy_name = name_lst[i]
        birth_boy_mail = email_lst[i]
        
        num = random.randint(1,3)
        with open(fr"letter_templates\letter_{num}.txt","r") as f:
            message = f.read()
            
            message =message.replace("[NAME]",birth_boy_name)
            
        
        
        
        sender_mail = "maaz.irshad.siddiqui@gmail.com"
        password ="tvud sggg rdle ywll"

        with smtplib.SMTP_SSL("smtp.gmail.com",port=465) as connection:
            connection.login(user=sender_mail,password=password)
            connection.sendmail(
                from_addr=sender_mail,
                to_addrs=birth_boy_mail,
                msg=message
            )
            
        print("Birthday mail sent to",birth_boy_name)

    
    


