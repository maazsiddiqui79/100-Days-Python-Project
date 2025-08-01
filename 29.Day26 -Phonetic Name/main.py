import pandas 

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


data = pandas.read_csv("nato_phonetic_alphabet.csv")

# print(data)

    

csv_dict ={row.letter:row.code for index,row in data.iterrows()}
# print(csv_dict)



#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
while True:
    user_ip_1 = int(input("\n📋 1. List all phonetics word\n🆕 2. Enter another specific word\n❌ 3. Exit\n👉 Enter your choice: "))
    
    if user_ip_1 == 1:
        print("\n📚 Listing all phonetic words:")
        for k, v in csv_dict.items():
            print(f"{k} : {k} ---> {v}")
            
    elif user_ip_1 == 2:
        user_ip = input("✍️ Enter Your Name: ")
        
        wrds = list(user_ip)
        try:
            symbols = [
                '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
                ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
            for x in symbols:
                if x in user_ip:
                    raise KeyError("Sorry,Your Word Contain Symbol Which dont have Phonetic Word")
            
        except KeyError as k:
            print("ERROR: ",k)
        else:
            print("🔠 Letters:", wrds)

            phonetic = [v for i in wrds for k, v in csv_dict.items() if i.lower() == k.lower()]

            print(f"\n🎯 Phonetic Code Word of {user_ip.upper()}:")
            n = 0
            for i in phonetic:
                print(f"{wrds[n]} --> {i}")
                n += 1
            
    else:
        print("👋 Bye!")
        exit()




# for i in wrds:
#     for index,row in csv_dict.items():
#         if i.lower() == row.letter.lower():
#             phonetic.append(row.code)