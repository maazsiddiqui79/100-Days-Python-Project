import random 
from os import system


scr  = 0



data = {
    "Oprah Winfrey": "Media mogul and talk show host, one of the most influential women globally, known for *The Oprah Winfrey Show*.",
    "Albert Einstein": "Renowned physicist famous for the theory of relativity.",
    "Jennifer Lopez": "American singer, actress, and businesswoman, known for her music and Hollywood success.",
    "Bill Gates": "Co-founder of Microsoft, philanthropist, and one of the pioneers of personal computing.",
    "Will Smith": "Hollywood actor and rapper, known for *The Fresh Prince of Bel-Air* and blockbuster films like *Men in Black*.",
    "Tiger Woods": "American professional golfer, one of the greatest players in golf history with multiple major championships.",
    "Robert Downey Jr.": "Renowned Hollywood actor famous for playing Iron Man in the Marvel franchise, known for his career comeback after overcoming addiction.",
    "Jeff Bezos": "Founder and former CEO of Amazon, one of the wealthiest individuals, and owner of Blue Origin, a space exploration company.",
    "Cristiano Ronaldo": "Portuguese footballer, one of the greatest players of all time, with five Ballon d'Or awards and record-breaking goals.",
    "Mahatma Gandhi": "Indian leader who played a key role in India’s independence through nonviolent resistance.",
    "Elon Musk": "CEO of Tesla, SpaceX, and other companies, known for revolutionizing electric vehicles and space exploration.",
    "Selena Gomez": "American singer and actress, known for her music career and role in *Wizards of Waverly Place*, also a UNICEF ambassador.",
    "Kylie Jenner": "American media personality, businesswoman, and founder of Kylie Cosmetics, known as the world’s youngest self-made billionaire.",
    "LeBron James": "Legendary basketball player with multiple NBA championships and MVP awards, also a major philanthropist.",
    "Mark Zuckerberg": "Co-founder of Facebook (now Meta), a key figure in the social media industry.",
    "Lionel Messi": "Argentine footballer and World Cup winner, widely regarded as one of the best players in football history.",
    "Taylor Swift": "American singer-songwriter with numerous Grammy awards and best-selling albums, known for her impactful lyrics.",
    "Justin Bieber": "Canadian singer and pop icon, discovered on YouTube, with multiple chart-topping hits and Grammy awards.",
    "Rihanna": "Barbadian singer, actress, and entrepreneur, founder of Fenty Beauty, and one of the richest female musicians.",
    "Stephen Hawking": "Theoretical physicist known for his work on black holes and cosmology."
}



follower_count = {
    "Oprah Winfrey": 15,
    "Albert Einstein": 20,
    "Jennifer Lopez": 10,
    "Bill Gates": 60,
    "Will Smith": 250,
    "Tiger Woods": 30,
    "Robert Downey Jr.": 100,
    "Jeff Bezos": 55,
    "Cristiano Ronaldo": 600,  # Very high social media following
    "Mahatma Gandhi": 150,
    "Elon Musk": 110,
    "Selena Gomez": 250,
    "Kylie Jenner": 30,
    "LeBron James": 150,
    "Mark Zuckerberg": 5,
    "Lionel Messi": 500,  
    "Taylor Swift": 50,
    "Justin Bieber": 290,
    "Rihanna": 20,
    "Stephen Hawking": 8
}


random_f2 = random.choice(list(data.keys()))
while True:
    random_f1 = random_f2
    random_f2 = random.choice(list(data.keys()))

    if random_f1 == random_f2:
        random_f2 = random.choice(list(data.keys()))


    correct_option = "a" if follower_count[random_f1] > follower_count[random_f2] else "b"
 
    print("Correct Option",correct_option.upper())



    print("Compare A:",random_f1," - ",data[random_f1])
    print("""
            _    __    
        | |  / /____
        | | / / ___/
        | |/ (__  ) 
        |___/____(_)
            """)
    print("Compare B:",random_f2," - ",data[random_f2])
    user_ip = input("Who has more followers? Type 'A' or 'B': ").lower()

    if user_ip == correct_option:
        scr +=1
        system("cls")
        print(f"You are right ! Current Score:{scr}")
    else:
        system("cls")
        print(f"You are Wrong ! Final Score:{scr}")
        break