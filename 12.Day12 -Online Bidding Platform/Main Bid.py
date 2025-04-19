from os import system
auction_db = {}




print("""
                            ____________
                            \          /
                             )--------(
                             |""""""""|_.-._,.---------.,_.-._
                             |        | | |               | | ''-.
                             |        |_| |_             _| |_..-'
                             |________| '-'''---------'' '-'
                            ))-------((
                           //_________\\
       *BANG!* 💥  ===>  //------------\\
                        //_______________\\
                          
      """)

end =False
while not end :
    user_name = input("Enter Your name: ")
    user_bid_amt = int(input("What is your Bid $: "))
    auction_db[user_name] = user_bid_amt
    system("cls")
    # print(auction_db)
    continue_bid = int(input("Is There any other bidders? Type '1' for yes or '0' no: "))
    if continue_bid == 1:
         pass
    else:
        system("cls") # Clears the terminal
        print(f"The Winner is {max(auction_db,key=auction_db.get)} by {max(auction_db.values())} $")
        
        end = True
    
         
     
    
    
