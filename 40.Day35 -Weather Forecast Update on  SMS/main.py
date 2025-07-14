import requests
from twilio.rest import Client
import os


API_KEY = '5c4f3c0cf70da6f00c21892a789afbc5'
OWM_Endpoint = "http://api.openweathermap.org/data/2.5/forecast"




account_SID = 'ACc15ec90986a12f96d29d03cc50b47cb3'
Auth_Token = '[AuthToken]'



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
print(Weather_data)

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

