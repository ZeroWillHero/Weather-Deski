import requests
import json 
from threading import Thread



def getWeather(location):
        APIKEY = "ef9afc4621d67cbede1620e9bed69dd8"
        
        API_URL = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={APIKEY}"

        response = requests.get(API_URL)
        # print(response.status_code)

        if response.status_code == 200:
            
            json_content = json.loads(response.content)
            weather = json_content['weather']

            if weather :
                data = weather[0]

                return data['description']
            

