from datetime import datetime
import os
import pytz
import requests
import math


api_key='432a128cb02deb7fc9bbd109b0a5c177'
api_url=('http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&appid={}')

api_url2=('http://api.openweathermap.org/data/2.5/forecast?q={}&mode=json&units=metric&appid={}')

def query_api(city):
    try:
        #print(api_url.format(city,api_key))
        data=requests.get(api_url.format(city,api_key)).json()
       
    except Exception as exc:
        print(exc)
        data=None
    return data


def query_api2(city):
     try:
        #print(api_url.format(city,api_key))
        
        data2=requests.get(api_url2.format(city,api_key)).json()
        #print(data2)
     except Exception as exc:
        print(exc)
        data2=None
     return data2