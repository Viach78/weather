from django.shortcuts import render
import requests


# Create your views here.

def index(request):
    appid = 'eeb4a90891d880640c4afdd29101473b'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid' + appid

    city = 'London'
    res = requests.get(url.format(city))

    print(res.text)
    return render(request, 'main/index.html')
