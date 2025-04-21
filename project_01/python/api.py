"""
--------------------------------------------------------------------------
Time Zones Button Fetcher
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
Fetches times from four time zones across the USA.
"""

import time
from WorldTimeAPI import service as serv
import Adafruit_BBIO.GPIO as GPIO
from datetime import datetime

# ------------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------------
# Setup: Time zones and locations
CITIES = {
    "Eastern":  {"area": "America", "location": "New_York"},
    "Central":  {"area": "America", "location": "Chicago"},
    "Mountain": {"area": "America", "location": "Denver"},
    "Pacific":  {"area": "America", "location": "Los_Angeles"}
}

# Button pin
BUTTON_PIN = "P2_10"

# Setup button pin
GPIO.setup(BUTTON_PIN, GPIO.IN)

# ------------------------------------------------------------------------
# Global Variables
# ------------------------------------------------------------------------


# Time storage
eastern_time = None
central_time = None
mountain_time = None
pacific_time = None

# Date tracking
last_date_check = datetime.now()

# Create client
client = serv.Client("timezone")

def fetch_time_and_date():
    global eastern_time, central_time, mountain_time, pacific_time
    print("Fetching current time and date...")
    try:
        eastern_time = client.get(**CITIES["Eastern"]).datetime
        central_time = client.get(**CITIES["Central"]).datetime
        mountain_time = client.get(**CITIES["Mountain"]).datetime
        pacific_time = client.get(**CITIES["Pacific"]).datetime

        print(f"Eastern:  {eastern_time}")
        print(f"Central:  {central_time}")
        print(f"Mountain: {mountain_time}")
        print(f"Pacific:  {pacific_time}")
    except Exception as e:
        print("Error retrieving time:", e)

def update_times_only():
    global eastern_time, central_time, mountain_time, pacific_time

    # Add 1 second to simulate real-time ticking
    eastern_time += datetime.timedelta(seconds=1)
    central_time += datetime.timedelta(seconds=1)
    mountain_time += datetime.timedelta(seconds=1)
    pacific_time += datetime.timedelta(seconds=1)

    # Format and display just time
    print(f"Eastern Time: {eastern_time.time()}")

def is_button_pressed():
    return GPIO.input(BUTTON_PIN) == GPIO.HIGH
print(fetch_time_and_date())
# Initial fetch
fetch_time_and_date()

try:
    while True:
        now = datetime.now()

        # Refresh date once per hour
        if (now - last_date_check).seconds >= 3600:
            fetch_time_and_date()
            last_date_check = now
        else:
            update_times_only()

        # Manual override
        if is_button_pressed():
            print("Button pressed! Manual time + date fetch.")
            fetch_time_and_date()
            last_date_check = datetime.now()

        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("Exited program.")