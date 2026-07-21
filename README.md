## ⛈️ Weather forecast application using python and OpenWeatherMap API (console-based)

## Project Description:
Developed a weather forecast application using python that retrieves real-time weather forecast data from a weather API based on a user-entered city. The application processes JSON responses and displays important weather information in a clear, user-friendly format.

## Features:
- search weather forecast by city name.
- display a current and upcoming forecast information.
- show temperature, "feels like" temperature ,humidity, atmospheric pressure, wind speed, and weather conditions.
- handle invalid city names and API errors gracefully.
- present daa in a readable console interface.

## Installation:
1. Clone the repository
    ```
2. Install the required package:
```bash
pip install -r requirements.txt
```
3. Open the notebook:
```
Weather_forecast_using_OpenWeatherAPI.ipynb
```
4. Run all cells in jupyter notebook or jupyterlab
5. Enter your OpenWeather API key when required and execute the notebook.

## Technologies used:
- Python
- json
- rest api (OpenWeather API)
- datetime module
- 
## key python concepts used:

1. Functions, loops, conditional statements(if-else), exception and error handling, dictionaries and lists, user input/outputs, API integration, JSON parsing.

2. An API is a bridge that allows two applications to communicate with each other. simple flow: An app --> api request --> weather server --> api response --> app shows the weather of that place.

3. JSON is a lightweight format for storing and exchanging data. APIs commonly use JSON to send data.

## Sample Output::

Enter City Name:: Mumbai
============================================================
 WEATHER FORECAST APPLICATION 
============================================================

City:::Mumbai
Country:::IN

Next 5 forecasts

__________________________________________________
Date & Time:: 2026-07-06 06:00:00
Temperature:: 27.05 degree celcius
Feels Like:: 30.77 degree celcius
Humidity:: 89 %
Pressure:: 1003 hPa
Weather:: Rain
Description:: Moderate Rain
Wind Speed:: 10.98 m/s

## Future Improvements:
- GUI using Tkinter
- 5-Day Forecast
- Error Handling
- Weather Icons

## Author
Manvi
