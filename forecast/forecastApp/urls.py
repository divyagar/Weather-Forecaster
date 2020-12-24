from django.urls import path
from . import views
urlpatterns = [
    path('/', views.base),
    path('/home', views.home),
    path('/weather', views.weather, name = 'weather'),
    path('/search', views.search),
    path('/error', views.error, name = "error")
]