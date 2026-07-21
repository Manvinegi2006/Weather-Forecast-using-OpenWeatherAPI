{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "532c3e81-1b86-4d04-a32e-9dcf250275f1",
   "metadata": {},
   "source": [
    "<h1 style=\"text-align: center;\">WEATHER FORECAST APPLICATION (console-based)</h1>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9a87b3dc-a3b5-4035-b308-2276b11fd18a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "2ca89bc6-0083-4fa1-9c81-c45a01fb25e8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: requests in C:\\Users\\sky\\AppData\\Local\\Programs\\Python\\Python314\\Lib\\site-packages (2.32.5)\n",
      "Requirement already satisfied: charset_normalizer<4,>=2 in C:\\Users\\sky\\AppData\\Local\\Programs\\Python\\Python314\\Lib\\site-packages (from requests) (3.4.4)\n",
      "Requirement already satisfied: idna<4,>=2.5 in C:\\Users\\sky\\AppData\\Local\\Programs\\Python\\Python314\\Lib\\site-packages (from requests) (3.11)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in C:\\Users\\sky\\AppData\\Local\\Programs\\Python\\Python314\\Lib\\site-packages (from requests) (2.5.0)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in C:\\Users\\sky\\AppData\\Local\\Programs\\Python\\Python314\\Lib\\site-packages (from requests) (2025.10.5)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: Ignoring invalid distribution ~ip (C:\\Users\\sky\\AppData\\Local\\Programs\\Python\\Python314\\Lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution ~ip (C:\\Users\\sky\\AppData\\Local\\Programs\\Python\\Python314\\Lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution ~ip (C:\\Users\\sky\\AppData\\Local\\Programs\\Python\\Python314\\Lib\\site-packages)\n",
      "\n",
      "[notice] A new release of pip is available: 26.0.1 -> 26.1.2\n",
      "[notice] To update, run: python.exe -m pip install --upgrade pip\n"
     ]
    }
   ],
   "source": [
    "#!pip install requests"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c5427d9e-d785-437c-b85a-71d6711e2c3c",
   "metadata": {},
   "source": [
    "### importing Libraries"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1da69f6e-b880-458e-b521-46370a1f9858",
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "import json\n",
    "from datetime import datetime"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "037c8e60-8516-4b90-bcae-bf129e5ccc84",
   "metadata": {},
   "source": [
    "##### PROJECT: Weather forecast application using python and OpenWeatherMap API (console-based)\n",
    "#### Project Description: \n",
    "Developed a weather forecast application using python that retrieves real-time weather forecast data from a weather API based on a user-entered city.\n",
    "The application processes JSON responses and displays important weather information in a clear, user-friendly format.\n",
    "\n",
    "#### Features:\n",
    "- search wather forecasts by city name.\n",
    "- display a current and upcoming forecast information.\n",
    "- show temperature, \"feels like\" temperature ,humidity, atmospheric pressure, wind speed, and weather conditions.\n",
    "- handle invalid city names and API errors gracefully.\n",
    "- present daa in a readable console interface.\n",
    "\n",
    "#### Technologies used:\n",
    "- Python\n",
    "- json\n",
    "- rest api (OpenWeather API)\n",
    "- datetime module\n",
    "\n",
    "#### key python concepts used:\n",
    "Functions, loops, conditional statements(if-else), exception and error handling, dictionaries and lists, user input/outputs, API integration, JSON parsing.\n",
    "\n",
    "- An API is a bridge that allows two applications to communicate with each other.\n",
    "simple flow:  An app --> api request --> weather server --> api response --> app shows the weather of that place.\n",
    "\n",
    "- JSON is a lightweight format for storing and exchanging data. APIs commonly use JSON to send data."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "1544bc3e-e883-484c-bcb1-623550fe522d",
   "metadata": {},
   "outputs": [],
   "source": [
    "# creating a free API key from OpenWeatherMap:\n",
    "api_key='59db61962e8dc9326e6227328f2476cf'\n",
    "base_url='https://api.openweathermap.org/data/2.5/forecast'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "d4127fc7-8dfc-48f2-bad0-b5bce82c542d",
   "metadata": {},
   "outputs": [],
   "source": [
    "#function to get weather forecast\n",
    "def weather_forecast(city):\n",
    "    params={'q':city,'appid':api_key,'units':'metric'}\n",
    "    response=requests.get(base_url,params=params)\n",
    "\n",
    "    if response.status_code==200:\n",
    "        data=response.json()\n",
    "        print('='*60)\n",
    "        print(' WEATHER FORECAST APPLICATION ')\n",
    "        print('='*60)\n",
    "        print(f'\\nCity:::{data['city']['name']}')\n",
    "        print(f'Country:::{data['city']['country']}')\n",
    "        print('\\nNext 5 forecasts\\n')\n",
    "\n",
    "        for forecast in data['list'][:5]:\n",
    "            date_time=forecast['dt_txt']\n",
    "            temperature=forecast['main']['temp']\n",
    "            feels_like=forecast['main']['feels_like']\n",
    "            humidity=forecast['main']['humidity']\n",
    "            pressure=forecast['main']['pressure']\n",
    "            weather=forecast['weather'][0]['main']\n",
    "            description=forecast['weather'][0]['description']\n",
    "            wind=forecast['wind']['speed']\n",
    "            print('_'*50)\n",
    "            print('Date & Time::',date_time)\n",
    "            print('Temperature::',temperature,'degree celcius')\n",
    "            print('Feels Like::',feels_like,'degree celcius')\n",
    "            print('Humidity::',humidity,'%')\n",
    "            print('Pressure::',pressure,'hPa')\n",
    "            print('Weather::',weather)\n",
    "            print('Description::',description.title())\n",
    "            print('Wind Speed::',wind,'m/s')\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "df1b9775-2702-47be-9bf1-0d30037dcc6b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter City Name:: Mumbai\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "============================================================\n",
      " WEATHER FORECAST APPLICATION \n",
      "============================================================\n",
      "\n",
      "City:::Mumbai\n",
      "Country:::IN\n",
      "\n",
      "Next 5 forecasts\n",
      "\n",
      "__________________________________________________\n",
      "Date & Time:: 2026-07-06 06:00:00\n",
      "Temperature:: 27.05 degree celcius\n",
      "Feels Like:: 30.77 degree celcius\n",
      "Humidity:: 89 %\n",
      "Pressure:: 1003 hPa\n",
      "Weather:: Rain\n",
      "Description:: Moderate Rain\n",
      "Wind Speed:: 10.98 m/s\n",
      "__________________________________________________\n",
      "Date & Time:: 2026-07-06 09:00:00\n",
      "Temperature:: 27.06 degree celcius\n",
      "Feels Like:: 30.69 degree celcius\n",
      "Humidity:: 88 %\n",
      "Pressure:: 1003 hPa\n",
      "Weather:: Rain\n",
      "Description:: Moderate Rain\n",
      "Wind Speed:: 10.76 m/s\n",
      "__________________________________________________\n",
      "Date & Time:: 2026-07-06 12:00:00\n",
      "Temperature:: 27.1 degree celcius\n",
      "Feels Like:: 30.58 degree celcius\n",
      "Humidity:: 86 %\n",
      "Pressure:: 1002 hPa\n",
      "Weather:: Rain\n",
      "Description:: Moderate Rain\n",
      "Wind Speed:: 11.08 m/s\n",
      "__________________________________________________\n",
      "Date & Time:: 2026-07-06 15:00:00\n",
      "Temperature:: 27.17 degree celcius\n",
      "Feels Like:: 30.77 degree celcius\n",
      "Humidity:: 86 %\n",
      "Pressure:: 1003 hPa\n",
      "Weather:: Rain\n",
      "Description:: Moderate Rain\n",
      "Wind Speed:: 9.1 m/s\n",
      "__________________________________________________\n",
      "Date & Time:: 2026-07-06 18:00:00\n",
      "Temperature:: 27.49 degree celcius\n",
      "Feels Like:: 31.9 degree celcius\n",
      "Humidity:: 88 %\n",
      "Pressure:: 1003 hPa\n",
      "Weather:: Rain\n",
      "Description:: Moderate Rain\n",
      "Wind Speed:: 9.82 m/s\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "\n",
      "Search another city? (yes/y or no/n): y\n",
      "Enter City Name:: Delhi\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "============================================================\n",
      " WEATHER FORECAST APPLICATION \n",
      "============================================================\n",
      "\n",
      "City:::Delhi\n",
      "Country:::IN\n",
      "\n",
      "Next 5 forecasts\n",
      "\n",
      "__________________________________________________\n",
      "Date & Time:: 2026-07-06 06:00:00\n",
      "Temperature:: 39.18 degree celcius\n",
      "Feels Like:: 43.73 degree celcius\n",
      "Humidity:: 35 %\n",
      "Pressure:: 998 hPa\n",
      "Weather:: Clouds\n",
      "Description:: Broken Clouds\n",
      "Wind Speed:: 2.38 m/s\n",
      "__________________________________________________\n",
      "Date & Time:: 2026-07-06 09:00:00\n",
      "Temperature:: 40.03 degree celcius\n",
      "Feels Like:: 44.11 degree celcius\n",
      "Humidity:: 32 %\n",
      "Pressure:: 997 hPa\n",
      "Weather:: Rain\n",
      "Description:: Light Rain\n",
      "Wind Speed:: 1.46 m/s\n",
      "__________________________________________________\n",
      "Date & Time:: 2026-07-06 12:00:00\n",
      "Temperature:: 39.63 degree celcius\n",
      "Feels Like:: 42.85 degree celcius\n",
      "Humidity:: 31 %\n",
      "Pressure:: 996 hPa\n",
      "Weather:: Rain\n",
      "Description:: Light Rain\n",
      "Wind Speed:: 2.94 m/s\n",
      "__________________________________________________\n",
      "Date & Time:: 2026-07-06 15:00:00\n",
      "Temperature:: 39.42 degree celcius\n",
      "Feels Like:: 41.62 degree celcius\n",
      "Humidity:: 29 %\n",
      "Pressure:: 995 hPa\n",
      "Weather:: Rain\n",
      "Description:: Light Rain\n",
      "Wind Speed:: 3.08 m/s\n",
      "__________________________________________________\n",
      "Date & Time:: 2026-07-06 18:00:00\n",
      "Temperature:: 37.24 degree celcius\n",
      "Feels Like:: 39.45 degree celcius\n",
      "Humidity:: 34 %\n",
      "Pressure:: 996 hPa\n",
      "Weather:: Rain\n",
      "Description:: Light Rain\n",
      "Wind Speed:: 2.4 m/s\n"
     ]
    }
   ],
   "source": [
    "while True:\n",
    "    city=input('Enter City Name::')\n",
    "    weather_forecast(city)\n",
    "\n",
    "    choice=input('\\nSearch another city? (yes/y or no/n):').lower().strip()\n",
    "    \n",
    "    if choice not in ['yes','y']:\n",
    "        print('\\nThank You for using Weather Forecast App!')\n",
    "        break\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f9e4e18d-5a41-44ce-bfe2-2fa91e0f844f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.14.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
