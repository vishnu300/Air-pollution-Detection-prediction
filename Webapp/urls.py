from django.urls import path
from .import views
from.import models

urlpatterns = [
    
    path('my/', views.loginPage, name='my'),
    
    path('weather/past', views.past ) ,
    path('weather/future', views.modelCo2 ) ,
    path('weather/all' , views.page),
    
    path('weather/', views.airpollution_dase),
    
    path('weather/login', views.loginPage),
    
    path('weather/regisitration', views.regisPage),
    
    path('airdatabase/', views.airpollution_dase),
    
    path('weather/get-weather_json/', views.get_weather, name='get_weather'),

]





