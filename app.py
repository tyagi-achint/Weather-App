import requests

api_key = '47907507f3828c7d281ea825a0b6e548'

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
    # print(todayWeather_data.json())
    # todayWeather = todayWeather_data.json()['list'][0]['weather'][0]['main']
    # todayTemp_min = todayWeather_data.json()['list'][0]['temp']['min']
    # todayTemp_max = todayWeather_data.json()['list'][0]['temp']['max']

    # todayTemp_morning = todayWeather_data.json()['list'][0]['temp']['morn']
    # todayTemp_evening = todayWeather_data.json()['list'][0]['temp']['eve']

    # todayFeelsLike_morning = todayWeather_data.json()['list'][0]['feels_like']['morn']
    # todayFeelsLike_evening = todayWeather_data.json()['list'][0]['feels_like']['eve']
    # print("Today's Weather Forecast:")
    # print(f"Weather: {todayWeather}")
    # print(f"Min Temperature: {todayTemp_min}°C")
    # print(f"Max Temperature: {todayTemp_max}°C")
    # print(f"Morning Temperature: {todayTemp_morning}°C")
    # print(f"Evening Temperature: {todayTemp_evening}°C")
    # print(f"Feels Like (Morning): {todayFeelsLike_morning}°C")
    # print(f"Feels Like (Evening): {todayFeelsLike_evening}°C")
    today_weather_data = todayWeather_data.json()['list'][0]['weather'][0]
    today_temp_data =todayWeather_data.json()['list'][0]['main']
    today_feels_like_data_morning = todayWeather_data.json()['list'][0]['feels_like']['morn']
    today_feels_like_data_evening = todayWeather_data.json()['list'][0]['feels_like']['eve']

    # Extracting required details
    today_weather = today_weather_data['main']
    today_temp_min = today_temp_data['temp_min']
    today_temp_max = today_temp_data['temp_max']
    today_temp_morning = today_temp_data['temp']['morn']
    today_temp_evening = today_temp_data['temp']['eve']
    today_feels_like_morning = today_feels_like_data_morning
    today_feels_like_evening = today_feels_like_data_evening

    # Display the information
    print("Today's Weather Forecast:")
    print(f"Weather: {today_weather}")
    print(f"Min Temperature: {today_temp_min}°C")
    print(f"Max Temperature: {today_temp_max}°C")
    print(f"Morning Temperature: {today_temp_morning}°C")
    print(f"Evening Temperature: {today_temp_evening}°C")
    print(f"Feels Like (Morning): {today_feels_like_morning}°C")
    print(f"Feels Like (Evening): {today_feels_like_evening}°C")