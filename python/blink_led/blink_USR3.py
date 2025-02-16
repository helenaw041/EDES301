"""
--------------------------------------------------------------------------
Blink
--------------------------------------------------------------------------
Author: Helena Wang |hw101 |at| rice |dot| edu|

Copyright 2025 - Helena Wang

License:   

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, 
this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE 
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE 
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF 
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF 
THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------

Blink will blink the USR3 LED at 5 Hz

--------------------------------------------------------------------------
"""

# NOTE - Import Statements
import Adafruit_BBIO.GPIO as GPIO
import time

# Define the pin for USR3 LED
USR3_LED = "USR3"

# ------------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------------

# NOTE - No constants are needed 

# ------------------------------------------------------------------------
# Global variables
# ------------------------------------------------------------------------

# NOTE - No global variables are needed 

# ------------------------------------------------------------------------
# Functions
# ------------------------------------------------------------------------

# NOTE - No functions are needed 

# End def

# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

# Set up the USR3 LED pin as an output
GPIO.setup(USR3_LED, GPIO.OUT)

# Blink LED at 5 Hz (5 full on/off cycles per second)
if __name__ == "__main__":

    while True:
        GPIO.output(USR3_LED, GPIO.HIGH) # Turn the LED on
        time.sleep(0.1)                  # Wait for 100 ms
        GPIO.output(USR3_LED, GPIO.LOW)  # Turn the LED off
        time.sleep(0.1)                  # Wait for 100ms
