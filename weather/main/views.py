from django.shortcuts import render
import requests


# Create your views here.

def index(request):
    appid = 'eeb4a90891d880640c4afdd29101473b'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    city = 'London'
    res = requests.get(url.format(city)).json()

    city_info = {
        'city': city,
        'temp': res['main']['temp'],
        'icon': res['weather'][0]['icon'],
    }

    context = {
        'info': city_info
    }

    return render(request, 'main/index.html', context)
