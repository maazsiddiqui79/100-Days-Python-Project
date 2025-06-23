from bs4 import BeautifulSoup
import requests
import pprint
import spotipy




ip = input("Enter a year YYYY-MM-DD: ")

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

URL ="https://www.billboard.com/charts/hot-100/"+ip
print(URL)

response = requests.get(url=URL,headers=header)
response.raise_for_status()
print(response)

soup= BeautifulSoup(response.text,"lxml")
title_song = [ i.getText().strip() for i in soup.select("li ul li h3")]


print(title_song)

# ------------------------------Spotify --------------------------


Client_ID = "142473e5604749e2a1483788505e9c01"
Client_Secret = "d4689246d49d4923a784b12f1b1e5b7d"
SCOPE ="playlist-modify-private"
REDIRECT_URL ="https://example.com/callback"


sp_Aouth = spotipy.oauth2.SpotifyOAuth(client_id=Client_ID,
                                       client_secret=Client_Secret,
                                       redirect_uri=REDIRECT_URL,
                                       scope=SCOPE,
                                       show_dialog=True,
                                       cache_path="token.txt")




sp = spotipy.Spotify(auth_manager=sp_Aouth)

# USER_ID = sp.current_user()["id"]  #31oeifbpu5l6ikp56btusepkfole
USER_ID = "31oeifbpu5l6ikp56btusepkfole" #31oeifbpu5l6ikp56btusepkfole

print("Id: ",USER_ID)

song_uri = []

year = ip.split("-")[0]

for i in range(len(title_song)):
    try:
        x = sp.search(q=f"track:{i} year:{year}",type="track")
        x = x["tracks"]["items"][0]["external_urls"]["spotify"] #type:ignore
        song_uri.append(x)
        print(i,song_uri[i])
    except :
        print(i,"Not Available")
        
print(song_uri)
des="""It is day 46 of 100 days of python the goal is to scrap Top 100 songs from specific date from a website and makeup playlist of songs and hosted on Spotify.
"""
play_list = None
play_list = sp.user_playlist_create(user=USER_ID,
                                    name="Day46 Web- Scrapping n Creating Spotify playlist",
                                    public=False,)

pprint.pp(play_list)
play_list_id = play_list["id"]#type:ignore

print(play_list_id)

add = sp.playlist_add_items(playlist_id=play_list_id,
                            items=song_uri)
pprint.pp(add)


