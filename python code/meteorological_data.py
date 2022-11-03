# source
# https://github.com/m0rp43us/openmeteopy
import pandas as pd

from openmeteo_py import Hourly,Daily,Options,OWmanager

# Latitude, Longitude for Los Angeles, CA
latitude = 34.00
longitude = -118.47

hourly = Hourly()
daily = Daily()
options = Options(latitude,longitude)

mgr = OWmanager(options,
    hourly.temperature_2m(),
    daily.temperature_2m_min())


meteo1 = mgr.get_data(3,2, 'None')

# header value is based on the dataframe. so take the xlsx to find what value you should put for header. | i.e. row-1==header
data = pd.read_excel('C:\\Users\\agome\\OneDrive\Desktop\\Github Projects\\Pack a Sweater\\Pack-a-Sweater\\python code\\None_hourly.xlsx', sheet_name='Sheet1', index_col=None, usecols = "C", header = 18, nrows=0)
eveningLowTemp = data.columns.values[0] # I chose the temperature to take if for 5pm... when it starts to get chilly
eveningLowTemp = (eveningLowTemp * (9/5))+32

# NOTE: I had to convert to Fahrenheit

#print(eveningLowTemp)


#print (data)

# This command wil print the data to shell
#print(meteo1)

# Download data
#meteo = mgr.get_data()
#print(meteo)
