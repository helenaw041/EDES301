"""
--------------------------------------------------------------------------
Weather API Function Calls
--------------------------------------------------------------------------
License:   
Copyright 2025 - Helena Wang

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this 
list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------

"""

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
                       
API_KEY = "" # REPLACE WITH YOUR API KEY  
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