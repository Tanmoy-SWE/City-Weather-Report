from django.shortcuts import render
import urllib.request
import json
import math
import requests

def index(request):
    return render(request, 'index.html')

# Create your views here.
def showWeather(request):
        city =  request.GET.get('search')
        API_key = '464180b8505f4807a4494e41590e7e67'
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"

        response = requests.get(url).json()

        temp = response['main']['temp']
        temp = math.floor((temp * 1.8) - 459.67)  # Convert to °F

        feels_like = response['main']['feels_like']
        feels_like = math.floor((feels_like * 1.8) - 459.67)  # Convert to °F

        humidity = response['main']['humidity']
        Temperature = {
            'temp': temp,
            'feels_like': feels_like,
            'humidity': humidity
        }
        return render(request,'Weather.html',Temperature)
