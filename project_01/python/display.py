import os
import time
import Adafruit_BBIO.GPIO as GPIO
import adafruit_character_lcd.character_lcd as LCD

# Define the LCD module pins
LCD_RS = "P2_35"
LCD_EN = "P2_33"
LCD_D4 = "P2_19"
LCD_D5 = "P2_17"
LCD_D6 = "P1_04"
LCD_D7 = "P1_02"

# Setup the LCD
lcd = LCD.Adafruit_CharLCD(LCD_RS, LCD_EN, LCD_D4, LCD_D5, LCD_D6, LCD_D7,
                       cols=16, lines=2)

# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

if __name__ == '__main__':

    print("display test")


    # Use a Keyboard Interrupt (i.e. "Ctrl-C") to exit the test
    try:
        while(True):
            # Clear and display message
            lcd.clear()
            lcd.display_line_1('Hello, World!')
            lcd.display_line_2('hello')
            
    except KeyboardInterrupt:
        GPIO.cleanup()
        

    print("Test Complete")