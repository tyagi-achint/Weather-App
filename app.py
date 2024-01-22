from flask import Flask, render_template, request
import requests
import datetime
from api_key import api_key

app = Flask(__name__)

def format_timestamp(timestamp, timezone_offset):
    dt_object = datetime.datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
    
    local_time = dt_object + datetime.timedelta(seconds=timezone_offset)
    
    formatted_timestamp = local_time.strftime('%I %p')
    return formatted_timestamp

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['city']
        currentWeather_data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID={api_key}")

        if currentWeather_data.json().get('cod') == '404':
            error_message = "No City Found"
            return render_template('index.html', error_message=error_message)

        currentWeather = currentWeather_data.json()['weather'][0]['main']
        currentTemp = currentWeather_data.json()['main']['temp']
        country = currentWeather_data.json()['sys']['country']
        currentHumidity = currentWeather_data.json()['main']['humidity']
        currentFeels_like = currentWeather_data.json()['main']['feels_like']
        
        timezone_offset = currentWeather_data.json()['timezone']

        todayWeather_data = requests.get(
            f"https://api.openweathermap.org/data/2.5/forecast?q={user_input}&APPID={api_key}&units=metric")

        api_response = todayWeather_data.json()
        current_date = datetime.datetime.now().strftime('%Y-%m-%d')
        current_day_details = [item for item in api_response['list'] if item['dt_txt'].startswith(current_date)]

        for entry in current_day_details:
            entry['formatted_timestamp'] = format_timestamp(entry['dt_txt'], timezone_offset)

        return render_template('index.html', city=user_input, currentWeather=currentWeather, currentTemp=currentTemp,
                               country=country, currentHumidity=currentHumidity, currentFeels_like=currentFeels_like,
                               current_day_details=current_day_details)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
