import requests
import os
import time
import digitalio
import board
import Adafruit_BBIO.GPIO as GPIO
import adafruit_character_lcd.character_lcd

# Define the LCD module pins
LCD_RS = digitalio.DigitalInOut(board.P2_35)
LCD_EN = digitalio.DigitalInOut(board.P2_33)
LCD_D4 = digitalio.DigitalInOut(board.P2_24)
LCD_D5 = digitalio.DigitalInOut(board.P2_22)
LCD_D6 = digitalio.DigitalInOut(board.P2_20)
LCD_D7 = digitalio.DigitalInOut(board.P2_18)

# Setup the LCD
lcd = adafruit_character_lcd.character_lcd.Character_LCD(LCD_RS, LCD_EN, LCD_D4, LCD_D5, LCD_D6, LCD_D7,
                       columns=16, lines=2)
                       
API_KEY = 'b39e769915f04f8c9d2214812252404'  # 🔑 Replace with your real key
BASE_URL = 'http://api.weatherapi.com/v1/current.json'

def get_weather(city):
    """Fetch current weather for a given city."""
    params = {
        'key': API_KEY,
        'q': city,
        'aqi': 'no'
    }
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        #lcd.clear()
        #lcd.message = "" + data['location']['name'] + ": " + str(data['current']['temp_f']) + "°F" + "\n" + data['current']['condition']['text']
        return {
            'location': data['location']['name'],
            'region': data['location']['region'],
            'temp_f': data['current']['temp_f'],
            'condition': data['current']['condition']['text'], 
            
        }
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
        return None

weather = get_weather("Houston")
if weather:
    print(f"{weather['location']} ({weather['region']}): {weather['temp_f']}°F - {weather['condition']}")