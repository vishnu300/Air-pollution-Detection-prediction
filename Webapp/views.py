from django.shortcuts import render,redirect
import requests

def loginPage(req):
    return render(req, 'login.html')

def past(req):
    return render(req, 'past.html')

def future(req):
    return render(req, 'future.html')

def page(req):
    return render(req, 'all_FPP.html')

 #-------------To check API working or not in JSON data Humidity-Temp---------

from django.http import JsonResponse

def get_weather(request):
    api_key = '3c961dc2d1aec7f8e9f57ddae49b1dd9'
    url = f'https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid={api_key}'

    response = requests.get(url)
    data = response.json()
    # Process the weather data as needed
    return JsonResponse(data)

# ---- Registration Form -------------------------------------------------

from django.contrib.auth.models import User
def regisPage(req):
    if req.method == 'POST':
        name = req.POST['name']
        email_id = req.POST['email']
        password = req.POST['pas']
        re_password = req.POST['re_pass']
        
        user= User.objects.create_user(username=name ,password =password, email= email_id)
        user.save()
        print('user created')
        return redirect('/')
    else:
        return render(req, 'regisitration.html')
    
#-----------------------------Database model connection-----------------------

from .models import airdatabase

def airpollution_dase(request):
    name = airdatabase()
    name.city = 'kochi'
    name.co  = 469
    name.so2 = 5
    name.no2 = 32
    return render(request, 'MainPage.html', {'name':name})

#---------------------------MySQL Database Show data------------------------------

from .models import DjangoData

def airpollution_database(request):
    data = DjangoData.objects.all()
    return render(request, 'MainPage.html', {'chart_data': data})

#------------------Model Creation Machine Learning Prediction CO,NO2,SO2-----------

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

from .models import df
#---------------------------model spilt-------------------------------------------

X = df[['temperature', 'humidity']]   #Features
y = df['CO2_level']                   #Target variable
y_no2 = df['NO2_level']               #Target variable
y_so2 = df['SO2_level']               #Target variable

#-----------------------------model Training--------------------------------------

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

X_train, X_test, y_train_no2, y_test = train_test_split(X, y_no2, test_size=0.2, random_state=42)

X_train, X_test, y_train_so2, y_test = train_test_split(X, y_so2, test_size=0.2, random_state=42)

#-----------------------model selection suitable model-----------------------------

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

mode_no2 = RandomForestRegressor(n_estimators=100, random_state=42)
mode_no2.fit(X_train, y_train_no2)

model_so2 = RandomForestRegressor(n_estimators=100, random_state=42)
model_so2.fit(X_train, y_train_so2)

#----------------------------create function for suitable arrangement---------------

def modelCo2(request):

    # Predicting CO2,NO2,SO2 level for tomorrow based on current weather conditions
    
    if request.method == 'POST':
        current_temperature = int(request.POST['hum'])
        current_humidity = int(request.POST['tem'])
        
        prediction = model.predict([[current_temperature, current_humidity]])
        prediction1 = mode_no2.predict([[current_temperature, current_humidity]])
        prediction2 = model_so2.predict([[current_temperature, current_humidity]])
    else:
        current_temperature = 25
        current_humidity= 50
    
    prediction = model.predict([[current_temperature, current_humidity]])
    prediction1 = mode_no2.predict([[current_temperature, current_humidity]])
    prediction2 = model_so2.predict([[current_temperature, current_humidity]])
    
    # -----------api connection into future ---Humodity and Temperature--------------------
    
    api_key = '3c961dc2d1aec7f8e9f57ddae49b1dd9'
    url = f'https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    
    return render(request,'future.html',{'valuesco2':prediction,'valuesno2':prediction1,'valuesso2':prediction2,'data_api': data} )