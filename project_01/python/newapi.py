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