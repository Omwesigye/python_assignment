import requests
import pandas as pd

API_KEY = '6a161dc532c177fa088a2435a01dfd39'

# Coordinates for Kampala, Uganda
lat = 0.347596
lon = 32.582520

# Define API endpoint for OpenWeatherMap's 5 day / 3 hour forecast (free tier)
url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"

response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    # Extract relevant data for DataFrame
    if 'list' in data:
        df = pd.json_normalize(data['list'])
        print(df.head())
        # Save DataFrame to CSV
        df.to_csv('kampala_weather_forecast.csv', index=False)
        print("Data saved to kampala_weather_forecast.csv")
    else:
        print("No forecast data found in response.")
else:
    print(f"Error: {response.status_code} - {response.text}")