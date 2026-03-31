import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    if not API_KEY:
        raise ValueError("API key not found. Please set OPENWEATHER_API_KEY in .env")

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)

        if response.status_code == 429:
            print(" Rate limit exceeded. Please try again later.")
            return

        if response.status_code != 200:
            print(f"API Error: {response.status_code} - {response.reason}")
            return

        data = response.json()

        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]

        print(f"Temperature: {temp}°C")
        print(f"Condition: {weather}")

    except requests.exceptions.RequestException as e:
        print(f"Network error occurred: {e}")


if __name__ == "__main__":
    city = input("Enter city: ")
    get_weather(city)