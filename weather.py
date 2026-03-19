"""
weather.py — Fetches weather data from OpenWeatherMap API.

Think of this file as a "helper" that bot.py calls.
Keeping it separate makes the code cleaner and easier to understand.
"""

import os
import requests


# OpenWeatherMap free API base URL
API_BASE = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city: str) -> str:
    """
    Fetch current weather for a city and return a nicely formatted string.

    Args:
        city: The city name the user typed (e.g. "London", "Dhaka")

    Returns:
        A formatted weather report as a string (this gets sent to the user)
    """

    api_key = os.getenv("OPENWEATHER_API_KEY")

    # Safety check — make sure we have an API key
    if not api_key:
        return "⚠️ Weather service is not configured yet. Please contact the bot owner."

    # Build the request to the OpenWeatherMap API
    # units=metric means we get Celsius (use "imperial" for Fahrenheit)
    params = {
        "q": city,          # The city name
        "appid": api_key,   # Our API key
        "units": "metric",  # Celsius
    }

    try:
        # Make the HTTP request to OpenWeatherMap
        response = requests.get(API_BASE, params=params, timeout=10)
        data = response.json()  # Convert the response to a Python dictionary

        # Check if the city was not found
        if response.status_code == 404:
            return (
                f"❌ Sorry, I couldn't find '{city}'.\n\n"
                "Please check the spelling or try a nearby major city.\n"
                "Example: instead of 'NY' try 'New York'"
            )

        # Check for any other API error
        if response.status_code != 200:
            return f"⚠️ Something went wrong fetching weather for '{city}'. Try again!"

        # ─────────────────────────────────────
        # Extract the data we want from the API response
        # (The API returns a big JSON object — we pick out what we need)
        # ─────────────────────────────────────
        temp        = round(data["main"]["temp"])           # Current temp in °C
        feels_like  = round(data["main"]["feels_like"])     # Feels like temp
        humidity    = data["main"]["humidity"]              # Humidity %
        description = data["weather"][0]["description"]     # e.g. "light rain"
        wind_speed  = round(data["wind"]["speed"] * 3.6)   # Convert m/s → km/h
        country     = data["sys"]["country"]                # Country code e.g. "BD"
        city_name   = data["name"]                          # Confirmed city name

        # Pick an emoji based on weather condition
        emoji = get_weather_emoji(data["weather"][0]["main"])

        # Pick a practical tip based on the weather
        tip = get_weather_tip(data["weather"][0]["main"], temp)

        # Build the formatted reply message
        message = (
            f"{emoji} Weather in {city_name}, {country}\n"
            f"{'─' * 30}\n"
            f"🌡  Temperature:  {temp}°C (feels like {feels_like}°C)\n"
            f"🌤  Condition:    {description.capitalize()}\n"
            f"💧  Humidity:     {humidity}%\n"
            f"💨  Wind:         {wind_speed} km/h\n"
            f"{'─' * 30}\n"
            f"💡 {tip}"
        )

        return message

    except requests.exceptions.ConnectionError:
        return "⚠️ No internet connection. Please try again."
    except requests.exceptions.Timeout:
        return "⚠️ The weather service took too long. Please try again."
    except Exception as e:
        return f"⚠️ Unexpected error: {str(e)}"


def get_weather_emoji(condition: str) -> str:
    """Return an emoji based on the weather condition."""
    emojis = {
        "Clear":        "☀️",
        "Clouds":       "☁️",
        "Rain":         "🌧️",
        "Drizzle":      "🌦️",
        "Thunderstorm": "⛈️",
        "Snow":         "❄️",
        "Mist":         "🌫️",
        "Fog":          "🌫️",
        "Haze":         "🌁",
        "Smoke":        "💨",
        "Dust":         "🌪️",
        "Sand":         "🌪️",
        "Tornado":      "🌪️",
    }
    # Return the matching emoji, or a default cloud if not found
    return emojis.get(condition, "🌤️")


def get_weather_tip(condition: str, temp: int) -> str:
    """Return a practical tip based on weather condition and temperature."""

    if condition == "Rain" or condition == "Drizzle":
        return "Don't forget your umbrella! ☂️"
    elif condition == "Thunderstorm":
        return "Stay indoors if possible — thunderstorm warning! ⚡"
    elif condition == "Snow":
        return "Roads may be slippery. Dress warmly! 🧣"
    elif condition == "Clear" and temp > 30:
        return "Very hot! Stay hydrated and wear sunscreen. 🧴"
    elif condition == "Clear" and temp < 5:
        return "Clear but cold! Bundle up before heading out. 🧤"
    elif condition == "Clear":
        return "Great weather! Perfect for going outside. 😊"
    elif temp < 10:
        return "Cold outside — wear a warm jacket! 🧥"
    elif temp > 35:
        return "Extreme heat! Avoid going out during peak hours. 🥵"
    else:
        return "Have a great day! 😊"
