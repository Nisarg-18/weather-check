from django.shortcuts import render
import requests
# Create your views here.
def getWeather(request):
    data={}
    if 'city' in request.GET:
        city=request.GET['city']
        if city:
            response=requests.get('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=0258532f02b780dd5716c7485767f65d&units=metric')
            if response.status_code==200:
                weather_data=response.json()
                data={
                    'temp':weather_data['main']['temp'],
                    'mintemp':weather_data['main']['temp_min'],
                    'maxtemp':weather_data['main']['temp_max'],
                    'feelslike':weather_data['main']['feels_like'],
                    'desc':weather_data['weather'][0]['description'],
                    'pressure':weather_data['main']['pressure'],
                    'humidity':weather_data['main']['humidity'],
                    'city':city,
                }
            else:
                data={
                    'message':'Could not find the City, Please try again.'
                }
    return render(request, 'webpages/home.html',data)