import requests
from twilio.rest import Client
import os


API_KEY = os.environ.get("OWM_Endpoint_Key")
OWM_Endpoint = "http://api.openweathermap.org/data/2.5/forecast"


account_SID = os.environ.get("day_35_accSID")
Auth_Token = os.environ.get("Auth_Token_Day35")



para ={
    "lat":19.0686,
    "lon":72.8400,
    "appid":API_KEY,
    "cnt":4
    
}

response = requests.get(url=OWM_Endpoint,params=para)
response.raise_for_status()

print(response)
Weather_data = response.json()

will_rain = False

for i in Weather_data["list"]:
    condition_code = i["weather"][0]["id"]
    if int(condition_code) <=550:
        will_rain =True
        
if will_rain:        
    # print("Umbrella Leke jana")
    
    client = Client(account_SID,Auth_Token)
    message = client.messages \
        .create(
        body=f"Rain alert! Temp: {Weather_data["list"][0]["main"]["temp"]-273.15:.1f}°C,Hum: {Weather_data["list"][0]["main"]["humidity"]}%,Wind: {Weather_data["list"][0]["wind"]["speed"]}km/h, Visibility: {Weather_data["list"][0]["visibility"]/1000}Km.,Sea Level Pressure: {Weather_data["list"][0]["main"]["sea_level"]} hPa",
        from_ ="+13163893457",
        to="+918850281310"
    )
    
    print(message.sid)
    print(message.status)

