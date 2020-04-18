from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

def index(request):
    appid = '82b797b6ebc625032318e16f1b42c016'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    cities = City.objects.all()
    all_cities = []


    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    for city in cities:
        res = requests.get(url.format(city.name)).json()

        city_info ={
            'id': city.id,
            'city': city.name,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"]

        }
        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form}
    return render(request, 'myapp/index.html', context)


def simple(response):
    return render(response, 'myapp/simple.html')

def contact(response):
    return render(response, 'myapp/contact.html', {'values': ['Если у Вас остались вопросы, задавайте их по телефону', '+7 968 762 36 75', 'zavalishev@yandex.ru']})


def delete(request, id):
    try:
        city = City.objects.get(id=id)
        city.delete()
        return HttpResponseRedirect("/")
    except city.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


# Create your views here.
