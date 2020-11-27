from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=1b817375f5efd5d0c38e6dacea2899f1'
    
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
    else:
        form = CityForm()
    cities = City.objects.all()

    weather_data = []

    for citys in cities:

        r = requests.get(url.format(citys.city)).json()

        city_weather = {
            'city' : citys.city,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }

        weather_data.append(city_weather)

    context = {'weather_data' : weather_data, 'form' : form}
    return render(request, 'index.html', context)
