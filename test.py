import requests 
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="geoapiExercises")
city = input("what city do you want?: ") 
location = geolocator.geocode(city)
print("this is city name", location)
data = location.raw
print(data)
loc_data = data['display_name'].split()
zip_code = str(loc_data[-3]).strip(',')
print(zip_code)