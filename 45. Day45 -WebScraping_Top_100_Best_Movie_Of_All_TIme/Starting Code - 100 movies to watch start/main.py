# import requests
# from bs4 import BeautifulSoup

# URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# # Write your code below this line 👇

# response = requests.get(url=URL)

# data =response.text

# print("🎥 Top 100 Movies of All Time ✨")

# soup = BeautifulSoup(data,"lxml")
# movie = [ i.getText() for i in soup.find_all(name="h3",class_="title")]
# movie = movie[::-1]

# year = [ int(i.getText()) for i in soup.find_all(name="strong")]
# year.insert(0,2000)
# year.insert(0,2007)
# year= year[::-1]



# for i in range(100):
#     print(f"{movie[i]} ({year[i]})")

import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style, init

# Initialize colorama (for Windows compatibility)
init(autoreset=True)

# Archived URL of Empire's Top 100 Movies
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Send GET request to the URL
response = requests.get(url=URL)

# Extract HTML content from the response
data = response.text

# Print header for the list
print(Fore.CYAN + Style.BRIGHT + "\n🎥 Top 100 Movies of All Time ✨\n")

# Parse the HTML using BeautifulSoup with lxml parser
soup = BeautifulSoup(data, "lxml")

# Extract movie titles from h3 tags with class "title"
movie = [i.getText() for i in soup.find_all(name="h3", class_="title")]
movie = movie[::-1]  # Reverse the list to go from 1 to 100

# Extract years from strong tags and adjust the list
year = [int(i.getText()) for i in soup.find_all(name="strong")]
year.insert(0, 2000)  # Manually inserting missing years
year.insert(0, 2007)
year = year[::-1]  # Reverse year list to match movie order

# Loop through the first 100 items and print with color
for i in range(100):
    print(Fore.GREEN + f"{movie[i]}" + Fore.MAGENTA + f" ({year[i]})")
    
print(Fore.RED+f"+---------------------------------------------------END---------------------------------------------------+")
