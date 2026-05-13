# main.py for weather app program

from weather import Weather
from helper import weather_status

city = input("Enter city: ")
temp = float(input("Enter temperature: "))

weather = Weather(city, temp)

print("City:", weather.city)
print("Temperature:", weather.temperature)
print("Condition:", weather_status(weather.temperature))