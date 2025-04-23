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

# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

if __name__ == '__main__':

    print("display test")

    # Turn backlight on
    lcd.backlight = True
    # Print a two line message
    lcd.message = "Hello\nCircuitPython"
    # Wait 5s
    time.sleep(5)
    lcd.clear()
    # Print two line message right to left
    lcd.text_direction = lcd.RIGHT_TO_LEFT
    lcd.message = "Hello\nCircuitPython"
    # Wait 5s
    time.sleep(5)
    # Return text direction to left to right
    lcd.text_direction = lcd.LEFT_TO_RIGHT
    # Display cursor
    lcd.clear()
    lcd.cursor = True
    lcd.message = "Cursor! "
    # Wait 5s
    time.sleep(5)
    # Display blinking cursor
    lcd.clear()
    lcd.blink = True
    lcd.message = "Blinky Cursor!"
    # Wait 5s
    time.sleep(5)
    lcd.blink = False
    lcd.clear()
    # Create message to scroll
    scroll_msg = "<-- Scroll"
    lcd.message = scroll_msg
    # Scroll message to the left
    for i in range(len(scroll_msg)):
        time.sleep(0.5)
        lcd.move_left()
    lcd.clear()
    lcd.message = "Going to sleep\nCya later!"
    time.sleep(5)
    # Turn backlight off
    lcd.backlight = False
    time.sleep(2)



    if (False):
        # Use a Keyboard Interrupt (i.e. "Ctrl-C") to exit the test
        try:
            while(True):
                # Clear and display message
                lcd.clear()
                lcd.message = 'Hello, World!'
                time.sleep(1)
                # lcd.display_line_2('hello')\
                
        except KeyboardInterrupt:
            GPIO.cleanup()
        

    print("Test Complete")