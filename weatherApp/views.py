from django.shortcuts import render

# Create your views here.


import urllib.request
import json
from datetime import datetime
from django.http import HttpResponse


# class HttpResponseUnauthorized(HttpResponse):
#    def __init__(self):
#        super().__init__('401 Unauthorized', status=401)


def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        source = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=APITOKEN').read()
        list_of_data = json.loads(source)

        data = {
            "main": str(list_of_data['weather'][0]['main']),
            "icon": list_of_data['weather'][0]['icon'],
            "city_name": str(list_of_data['name']) + ', ' + str(list_of_data['sys']['country']),
            "description": str(list_of_data['weather'][0]['description']),
            "temp": str(list_of_data['main']['temp']) + '°C ',
            "temp_max_min": '[' + str(list_of_data['main']['temp_min']) + ', ' + str(
                list_of_data['main']['temp_max']) + ']ºC',
            "clouds": str(list_of_data['clouds']['all']) + '%',
            "pressure": str(list_of_data['main']['pressure']) + ' hPa',
            "humidity": str(list_of_data['main']['humidity']) + '%',
            "sun": datetime.utcfromtimestamp(int(list_of_data['sys']['sunrise'])).strftime('%H:%M:%S') + ', ' + datetime.utcfromtimestamp(int(list_of_data['sys']['sunset'])).strftime('%H:%M:%S'),
            "wind": '(' + str(list_of_data['wind']['speed']) + ' m/s, ' + st    r(list_of_data['wind']['deg']) + 'º)',
        }
        print(data)
    else:
        data = {}

    return render(request, "main/index.html", data)
