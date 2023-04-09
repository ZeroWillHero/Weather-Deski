import ctypes
import requests
import json
from weather import getWeather
from getImage import imageDownloader
import time 



def setWallpaper (path) :

    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path , 0)



def runApp () :

    UNSPLASH_ACCESS_KEY = "XRqqG6pFiZooGFnS5y7Tm2pVYSsRAlI6NSlYowqIpnE"
    

    # get weather 

    location = str(input("Enter Your current city here : "))

    while True :
        weather = getWeather(location)
        print (weather)

        print (imageDownloader(weather,UNSPLASH_ACCESS_KEY))
        path = "D:\programming\python other projects\Desktop Wallpaper Changer\wallpaper.jpg"
        setWallpaper(path)
        time.sleep(10)
        


if __name__ == '__main__' :
    runApp()
    