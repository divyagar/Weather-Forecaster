from django.http import HttpResponse
from django.shortcuts import render, redirect
import requests, json

def base(request):
    return render(request, 'forecastApp/base.html')

def home(request):
    return render(request, 'forecastApp/home.html')

def weather(request):
    city = request.GET.get('city', default = '')
    coords = request.GET.get('coord', default = '')
    if coords == '':
        url = 'http://api.openweathermap.org/data/2.5/forecast?q=' + city + '&appid=6c0b089798f68086bb3c981f57bc890e'

    else:
        lst = coords.split(",")
        if(len(lst) >= 2):
            url = 'http://api.openweathermap.org/data/2.5/forecast?lat=' + lst[0] + '&lon=' + lst[1] + '&appid=6c0b089798f68086bb3c981f57bc890e'
        else:
            url = 'http://api.openweathermap.org/data/2.5/forecast?lat=&lon=&appid=6c0b089798f68086bb3c981f57bc890e'

    f = requests.get(url)
    data = f.json()
    if(data['cod'] != '200'):
        request.session['data'] = data
        return redirect(error)
    args = {'data' : data}
    args['sperange'] = [*range(1, 9)]
    return render(request, 'forecastApp/weather.html', args)

def search(request):
    return render(request, 'forecastApp/search.html')

def error(request):
    data = request.session['data']
    # data = {"cod" : 404, 'message' : "error"}
    return render(request, 'forecastApp/error.html', data);