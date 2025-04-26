"""
--------------------------------------------------------------------------
Character LCD Display test
--------------------------------------------------------------------------
License:   
Copyright 2025 - CircuitPython modified by Helena Wang

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