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
    current_time_utc = get_current_time()
    if current_time_utc:
        print("Current time in UTC:", current_time_utc)

    current_time_pacific = get_current_time(timezone='America/Los_Angeles')
    if current_time_pacific:
        print("Current time in Los Angeles:", current_time_pacific)
    
    converted_time = convert_time_zone(from_timezone="UTC", to_timezone="America/New_York", date_time="2023-10-20T10:00:00")
    if converted_time:
        print("Converted Time:", converted_time)