from django.db import models

# Create your models here.
from django.db import models

class DjangoData(models.Model):
    Country = models.CharField(max_length=100)
    Year = models.IntegerField()
    Age = models.CharField(max_length=100)
    M = models.IntegerField()
    F = models.IntegerField()
 
        

class airdatabase:
    city : str
    co   : int
    so2  : int
    no2  : int  
    
    
#----------------prediction model creation------------------

import numpy as np
import pandas as pd
# Sample historical data (date, CO2 level, temperature, humidity)
data = {    
    'date': pd.date_range(start='2024-01-01', end='2024-03-13'),
    'CO2_level': np.random.uniform(300, 500, 73),  # Random CO2 levels for 73 days
    'temperature': np.random.uniform(10, 30, 73),  # Random temperature for 73 days
    'humidity': np.random.uniform(30, 80, 73),      # Random humidity for 73 days
    'NO2_level': np.random.uniform(5, 50, 73),
    'SO2_level': np.random.uniform(1, 20, 73),    # Random SO2 levels for 73 days   
}

df = pd.DataFrame(data)