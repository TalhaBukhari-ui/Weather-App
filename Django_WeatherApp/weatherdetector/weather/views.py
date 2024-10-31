from django.shortcuts import render
import json
import urllib.request
from urllib.parse import quote
from datetime import datetime 
from .models import Countries
# Create your views here.
def index(request):
    if request.method == "POST":
        today = datetime.today()
        date = today.strftime("%d %B")
        day = today.strftime("%A")

        city = request.POST['city']
        city = quote(city)
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+ '').read()
        json_data = json.loads(res)

        data = {
            'country_code': str(json_data['sys']['country']),
            'coordinate': '('+str(json_data['coord']['lon']) + ', '+ str(json_data['coord']['lat'])+')',
            'temp':str(int(json_data['main']['temp'])-273),
            'pressure':str(json_data['main']['pressure']),
            'humidity':str(json_data['main']['humidity']),
            'date':date,
            'day':day,
            'city':str(json_data['name']),
            'rain':str(json_data.get('rain', {}).get('1h', 0)),
            'wind_speed':str(json_data['wind']['speed']),
            'wind_dir':float(json_data['wind']['deg']),
            'icon':str(json_data['weather'][0]['main']),
            'icon_description':str(json_data['weather'][0]['description']).capitalize(),
            'country_flag': Countries.objects.filter(code = json_data['sys']['country'])[0].flag
        }
        print('ICON is broo '+data['icon'])
    else:
        city=''
        data={}
        
    return render(request, 'index.html',{'city':city, 'data':data})