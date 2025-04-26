"""
--------------------------------------------------------------------------
Time API Function Calls
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
import json

def get_current_time(timezone='UTC'):
    url = f"https://timeapi.io/api/Time/current/zone?timeZone={timezone}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

def convert_time_zone(from_timezone, to_timezone, date_time):
     url = "https://timeapi.io/api/Conversion/ConvertTimeZone"
     headers = {'Content-Type': 'application/json'}
     payload = {
          "fromTimeZone": from_timezone,
          "toTimeZone": to_timezone,
          "dateTime": date_time
     }
     try:
          response = requests.post(url, headers=headers, data=json.dumps(payload))
          response.raise_for_status()
          return response.json()
     except requests.exceptions.RequestException as e:
          print(f"Request failed: {e}")
          return None
     
# Example usage
if __name__ == "__main__":
    eastern_time = get_current_time(timezone='America/New_York')
    central_time = get_current_time(timezone='America/Chicago')
    mountain_time = get_current_time(timezone='America/Denver')
    pacific_time = get_current_time(timezone='America/Los_Angeles')

    if eastern_time:
        print("Current time in Eastern Time (New York):", eastern_time)
    if central_time:
        print("Current time in Central Time (Chicago):", central_time)
    if mountain_time:
        print("Current time in Mountain Time (Denver):", mountain_time)
    if pacific_time:
        print("Current time in Pacific Time (Los Angeles):", pacific_time)
    
    
    converted_time = convert_time_zone(from_timezone="UTC", to_timezone="America/New_York", date_time="2023-10-20T10:00:00")
    if converted_time:
        print("Converted Time:", converted_time)