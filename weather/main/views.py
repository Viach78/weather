from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm


# Create your views here.

def index(request):
    appid = 'eeb4a90891d880640c4afdd29101473b'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'temp_min': res["main"]["temp_min"],
            'temp_max': res["main"]["temp_max"],
            'icon': res["weather"][0]["icon"],
        }
        all_cities.append(city_info)

    context = {
        'all_info': all_cities,
        'form': form,
    }

    return render(request, 'main/index.html', context)
