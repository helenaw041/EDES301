"""
--------------------------------------------------------------------------
Button Driver with LED Cycling
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

Button Driver

  This driver can support buttons that have either a pull up resistor between the
button and the processor pin (i.e. the input is "High" / "1" when the button is
not pressed) and will be connected to ground when the button is pressed (i.e. 
the input is "Low" / "0" when the button is pressed), or a pull down resistor 
between the button and the processor pin (i.e. the input is "Low" / "0" when the 
button is not pressed) and will be connected to power when the button is pressed
(i.e. the input is "High" / "1" when the button is pressed).

  To select the pull up configuration, press_low=True.  To select the pull down
configuration, press_low=False.


Software API:

  Button(pin, press_low)
    - Provide pin that the button monitors
    
    wait_for_press()
      - Wait for the button to be pressed 
      - Function consumes time
        
    is_pressed()
      - Return a boolean value (i.e. True/False) on if button is pressed
      - Function consumes no time
    
    get_last_press_duration()
      - Return the duration the button was last pressed

    cleanup()
      - Clean up HW
      
    Callback Functions:
      These functions will be called at the various times during a button 
      press cycle.  There is also a corresponding function to get the value
      from each of these callback functions in case they return something.
    
      - set_pressed_callback(function)
        - Excuted every "sleep_time" while the button is pressed
      - set_unpressed_callback(function)
        - Excuted every "sleep_time" while the button is unpressed
      - set_on_press_callback(function)
        - Executed once when the button is pressed
      - set_on_release_callback(function)
        - Executed once when the button is released
      
      - get_pressed_callback_value()
      - get_unpressed_callback_value()
      - get_on_press_callback_value()
      - get_on_release_callback_value()      


"""
import os
import time
import threading
import newapi as API

import Adafruit_BBIO.GPIO as GPIO

# ------------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------------
LED_PINS      = ["P2_2", "P2_4", "P2_6", "P2_8"]  # Pins for the LEDs
TIMEZONES = ["Eastern", "Central", "Mountain", "Pacific"] 
BUTTON_PIN = "P2_3"
HIGH          = GPIO.HIGH
LOW           = GPIO.LOW

# ------------------------------------------------------------------------
# Global variables
# ------------------------------------------------------------------------

current_led = 0 # tracks the current LED 
current_zone_index = 0  # Tracks which time zone is being displayed


# ------------------------------------------------------------------------
# Functions / Classes
# ------------------------------------------------------------------------

class Button():
    """ Button Class """
    pin                           = None
    
    unpressed_value               = None
    pressed_value                 = None
    
    sleep_time                    = None
    press_duration                = None

    pressed_callback              = None
    pressed_callback_value        = None
    unpressed_callback            = None
    unpressed_callback_value      = None
    on_press_callback             = None
    on_press_callback_value       = None
    on_release_callback           = None
    on_release_callback_value     = None
    
    
    def __init__(self, pin=None, press_low=False, sleep_time=0.1):
        """ Initialize variables and set up the button """
        if (pin == None):
            raise ValueError("Pin not provided for Button()")
        else:
            self.pin = pin
        
        # For pull up resistor configuration:    press_low = True
        # For pull down resistor configuration:  press_low = False
        if press_low:
            self.unpressed_value = HIGH
            self.pressed_value   = LOW
        else:
            self.unpressed_value = LOW
            self.pressed_value   = HIGH
        
        # By default sleep time is "0.1" seconds
        self.sleep_time      = sleep_time
        self.press_duration  = 0.0        

        # Initialize the hardware components        
        self._setup()
    
    # End def
    
    
    def _setup(self):
        """ Setup the hardware components. """
        # Initialize Button
        # Use the Adafruit_BBIO.GPIO library to set up the button
        GPIO.setup(self.pin, GPIO.IN) # pin mode-input
        for led_pin in LED_PINS:
            GPIO.setup(led_pin, GPIO.OUT)  # Set up each LED pin as output
            GPIO.output(led_pin, LOW)  # Turn all LEDs off initially

    # End def


    def is_pressed(self):
        """ Is the Button pressed?
        
           Returns:  True  - Button is pressed
                     False - Button is not pressed
        """
        # Return the comparison of input value of the GPIO pin of 
        #   the buton (i.e. self.pin) to the "pressed value" of the class
        
        return GPIO.input(self.pin) == 0

    # End def


    def wait_for_press(self):
        """ Wait for the button to be pressed.  This function will 
           wait for the button to be pressed and released so there
           are no race conditions.
           
           Use the callback functions to peform actions while waiting
           for the button to be pressed or get values after the button
           is pressed.
        
           Arguments:  None
           Returns:    None
        """
        button_press_time = None
        
        # Wait for button press
        #   Execute the unpressed callback function based on the sleep time
        #
        # Update while loop condition to compare the input value of the  
        #   GPIO pin of the button
        #
        while(not self.is_pressed()):
        
            if self.unpressed_callback is not None:
                self.unpressed_callback_value = self.unpressed_callback()
            
            time.sleep(self.sleep_time)
            
        # Record time
        button_press_time = time.time()
        
        # Executed the on press callback function
        if self.on_press_callback is not None:
            self.on_press_callback_value = self.on_press_callback()
        
        # Wait for button release
        #   Execute the pressed callback function based on the sleep time
        #
        # Update while loop condition to compare the input value of the  
        #   GPIO pin of the button
        while(self.is_pressed()):
        
            if self.pressed_callback is not None:
                self.pressed_callback_value = self.pressed_callback()
            
            # pauses execution of the program for a little after each callback   
            time.sleep(self.sleep_time)
        
        # Record the press duration
        self.press_duration = time.time() - button_press_time

        # Executed the on release callback function
        if self.on_release_callback is not None:
            self.on_release_callback_value = self.on_release_callback()        
        
    # End def

    
    def get_last_press_duration(self):
        """ Return the last press duration """
        return self.press_duration
    
    # End def
    
    
    def cleanup(self):
        """ Clean up the button hardware. """
        # Nothing to do for GPIO
        pass
    
    # End def
    
    
    # -----------------------------------------------------
    # Callback Functions
    # -----------------------------------------------------

    def set_pressed_callback(self, function):
        """ Function excuted every "sleep_time" while the button is pressed """
        self.pressed_callback = function
        
    
    # End def

    def get_pressed_callback_value(self):
        """ Return value from pressed_callback function """
        return self.pressed_callback_value
    
    # End def
    
    def set_unpressed_callback(self, function):
        """ Function excuted every "sleep_time" while the button is unpressed """
        self.unpressed_callback = function
    
    # End def

    def get_unpressed_callback_value(self):
        """ Return value from unpressed_callback function """
        return self.unpressed_callback_value
    
    # End def

    def set_on_press_callback(self, function):
        """ Function excuted once when the button is pressed """
        self.on_press_callback = function
    
    # End def

    def get_on_press_callback_value(self):
        """ Return value from on_press_callback function """
        return self.on_press_callback_value
    
    # End def

    def set_on_release_callback(self, function):
        """ Function excuted once when the button is released """
        self.on_release_callback = function
    
    # End def

    def get_on_release_callback_value(self):
        """ Return value from on_release_callback function """
        return self.on_release_callback_value
    
    # End def    
    
# End class

# ------------------------------------------------------------------------
# LED Control Function for Callback
# ------------------------------------------------------------------------

def cycle_leds():
    """ Callback function to cycle through LEDs on button press """
    global current_led, current_zone_index
    # Turn off all LEDs
    for led_pin in LED_PINS:
        GPIO.output(led_pin, LOW)
    
    
    try:
        eastern_time = API.get_current_time(timezone='America/New_York')
        central_time = API.get_current_time(timezone='America/Chicago')
        mountain_time = API.get_current_time(timezone='America/Denver')
        pacific_time = API.get_current_time(timezone='America/Los_Angeles')

        if current_zone_index == 0 and eastern_time:
            # lcd.display_line_1("Your Text")
            # lcd.display_line_2("Your Text")
            print("ET:", eastern_time['dayOfWeek'])
            print(eastern_time['date'], eastern_time['time'])
        elif current_zone_index == 1 and central_time:
            print("CT:", central_time['dayOfWeek'])
            print(central_time['date'], central_time['time'])
        elif current_zone_index == 2 and mountain_time:
            print("MT:", mountain_time['dayOfWeek'])
            print(mountain_time['date'], mountain_time['time'])
        elif current_zone_index == 3 and pacific_time:
            print("PT:", pacific_time['dayOfWeek'])
            print(pacific_time['date'], pacific_time['time'])
        else:
            print("Retrieving...")

    except Exception as e:
        print("Error fetching time:", e)
    
    
    # Cycle through time zones
    current_zone_index = (current_zone_index + 1) % len(TIMEZONES)
    current_zone = TIMEZONES[current_zone_index]
    
    # Turn on the next LED in the cycle
    GPIO.output(LED_PINS[current_led], HIGH)
    # Update the current LED index for the next press
    current_led = (current_led + 1) % len(LED_PINS)  # Cycle between 0-3
    
    # Get the correct time object (this pulls from the API-updated values)
    # if statements get all 4 objects from other file and use conditionals to display one. 
    # time_obj = get_time_object_for(current_zone)
    # Update LCD
    # lcd.display_time(time_obj, current_zone)

def update_times():
    global eastern_time, central_time, mountain_time, pacific_time
    
    while True:
        try:
            eastern_time = API.get_current_time(timezone='America/New_York')
            central_time = API.get_current_time(timezone='America/Chicago')
            mountain_time = API.get_current_time(timezone='America/Denver')
            pacific_time = API.get_current_time(timezone='America/Los_Angeles')
            
            print("\n[Time Update]")
            if current_zone_index == 1 and eastern_time:
                # lcd.display_line_1("Your Text")
                # lcd.display_line_2("Your Text")
                print("ET:", eastern_time['dayOfWeek'])
                print(eastern_time['date'], eastern_time['time'])
            elif current_zone_index == 2 and central_time:
                print("CT:", central_time['dayOfWeek'])
                print(central_time['date'], central_time['time'])
            elif current_zone_index == 3 and mountain_time:
                print("MT:", mountain_time['dayOfWeek'])
                print(mountain_time['date'], mountain_time['time'])
            elif current_zone_index == 0 and pacific_time:
                print("PT:", pacific_time['dayOfWeek'])
                print(pacific_time['date'], pacific_time['time'])
            else:
                print("Retrieving...")
            print("--------------------------------------------------")
            
        except Exception as e:
            print(f"[Error] Failed to update time: {e}")
        time.sleep(15)  # Wait 30 seconds
        
# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

if __name__ == '__main__':

    print("LED cycling Button test")

    # Create instantiation of the button
    button = Button("P2_3", press_low = False)
    
    # Set the initial LED state (first LED ON)
    GPIO.output(LED_PINS[0], HIGH)  # First LED lights up on boot
    
    # Set the callback function to cycle LEDs on button press
    button.set_on_press_callback(cycle_leds)
    
    # Start time updater thread
    time_thread = threading.Thread(target=update_times, daemon=True)
    time_thread.start()

    # Use a Keyboard Interrupt (i.e. "Ctrl-C") to exit the test
    try:
        while(True):
            # Wait for button press and cycle the LEDs
            button.wait_for_press()
            # Check if the button is pressed
            print("Is the button pressed?")
            print("    {0}".format(button.is_pressed()))
            print(GPIO.input(BUTTON_PIN))
            
    except KeyboardInterrupt:
        for led_pin in LED_PINS:
            GPIO.output(led_pin, LOW)
        GPIO.cleanup()
        

    print("Test Complete")
    