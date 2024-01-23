# Weather App Readme

This repository contains a simple web application built using Flask that allows users to check the current weather and forecast for a given city. The application uses the OpenWeatherMap API to retrieve weather data.

## Project Structure

- `app.py`: The main Python file containing the Flask application.
- `index.html`: The HTML template for the web interface.
- `static/`: Directory containing static files such as images and CSS.
- `Dockerfile`: Docker configuration file for containerizing the application.
- `requirements.txt`: File specifying the Python dependencies for the project.

## Running the Application

### Local Development

1. Make sure you have Python installed on your machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Create an OpenWeatherMap API key and save it in a file named `api_key.py` in the same directory as `app.py`.
4. Run the application using the command `python app.py`.
5. Open a web browser and navigate to [http://localhost:5000](http://localhost:5000).

### Docker

1. Make sure you have Docker installed on your machine.
2. Build the Docker image using the command `docker build -t weather-app .`.
3. Run the Docker container using the command `docker run -p 5000:5000 weather-app`.
4. Open a web browser and navigate to [http://localhost:5000](http://localhost:5000).

## Usage

1. Enter the name of a city in the provided input field.
2. Click the "Get Weather" button to retrieve and display weather information.
3. The application will show the current temperature, weather condition, humidity, and "feels like" temperature.
4. Additionally, it displays a forecast for the current day, including temperature, weather condition, and "feels like" temperature at various times.

## Error Handling

- If the entered city is not found, an error message "No City Found" will be displayed.

## Credits

- The application was designed and developed by [Achint Tyagi](https://tyagi-achint.github.io/).

