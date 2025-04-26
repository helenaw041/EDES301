<h1> Digital ClockBuddy </h1>

1. "run.sh" file runs "button.py" (main) on boot. 
2. "display.py" uses the "adafruit_character_lcd.character_lcd" library to interact with the Adafruit White on Blue Character LCD
3. "newapi.py" contains function definitions to retrieve time and date data from "https://timeapi.io"
4. "weatherapi.py" contains function definitions to retrieve temperature and weather conditions data from "http://api.weatherapi.com"
5. NOTE: Replace line 56 in "weatherapi.py" with your own API Key
6. "button.py" is the main file and controls the two buttons (button 1 cycles between time zones and button 2 displays temperature and weather for 5 seconds)
