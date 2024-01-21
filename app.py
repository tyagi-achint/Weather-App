import requests
import datetime
from api_key import api_key

user_input = input("Enter city: ")

currentWeather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID={api_key}")

if currentWeather_data.json().get('cod') == '404':
    print("No City Found")
else:
    currentWeather = currentWeather_data.json()['weather'][0]['main']
    currentTemp = currentWeather_data.json()['main']['temp']
    country = currentWeather_data.json()['sys']['country']
    currentHumidity = currentWeather_data.json()['main']['humidity']
    currentFeels_like = currentWeather_data.json()['main']['feels_like']

    print("Current Weather:")
    print(f"Weather: {currentWeather}")
    print(f"Temperature: {currentTemp}°C")
    print(f"Country: {country}")
    print(f"Humidity: {currentHumidity}%")
    print(f"Feels Like: {currentFeels_like}°C")
    print("\n")

todayWeather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/forecast?q={user_input}&APPID={api_key}&units=metric")

if todayWeather_data.json().get('cod') == '404':
    print("No City Found")
else:


    api_response = todayWeather_data.json()


    current_date = datetime.datetime.now().strftime('%Y-%m-%d')


    current_day_details = [item for item in api_response['list'] if item['dt_txt'].startswith(current_date)]

    for entry in current_day_details:
        timestamp = datetime.datetime.utcfromtimestamp(entry['dt']).strftime('%Y-%m-%d %H:%M:%S')
        temperature = entry['main']['temp']
        feels_like = entry['main']['feels_like']
        description = entry['weather'][0]['main']

        print(f"Timestamp: {timestamp}, Temperature: {temperature}°C, Feels Like: {feels_like}°C, Description: {description}")
