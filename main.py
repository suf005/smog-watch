"""Command-line application for Smog Watch."""

from air_quality import fetch_air_quality
from config import CITIES


def get_aqi_category(aqi):
    """Return a simple health category for a US AQI value."""
    if aqi is None:
        return "Not available"
    if aqi <= 50:
        return "Good"
    if aqi <= 100:
        return "Moderate"
    if aqi <= 150:
        return "Unhealthy for Sensitive Groups"
    if aqi <= 200:
        return "Unhealthy"
    if aqi <= 300:
        return "Very Unhealthy"
    return "Hazardous"


def format_value(value, unit):
    """Format a reading while handling missing API values."""
    if value is None:
        return "Not available"
    return f"{value} {unit}".strip()


def choose_city():
    """Prompt for a city and return its name and coordinates."""
    cities = list(CITIES.items())
    print("Choose a city:")
    for number, (name, _) in enumerate(cities, start=1):
        print(f"{number}. {name}")

    while True:
        choice = input("Enter city number: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(cities):
            return cities[int(choice) - 1]
        print(f"Please enter a number from 1 to {len(cities)}.")


def display_report(data, location_name):
    """Print the air-quality report in the terminal."""
    units = data["units"]
    us_aqi = data["us_aqi"]
    european_aqi = data["european_aqi"]

    print("\n" + "=" * 48)
    print("                 SMOG WATCH")
    print("=" * 48)
    print(f"Location:             {location_name}")
    print(f"Reading time:         {data['time']}")
    print("-" * 48)
    print("AIR QUALITY")
    print(f"US AQI:               {format_value(us_aqi, units.get('us_aqi', ''))}")
    print(f"US AQI category:      {get_aqi_category(us_aqi)}")
    print(f"European AQI:         {format_value(european_aqi, units.get('european_aqi', ''))}")
    print("-" * 48)
    print("POLLUTANT LEVELS")
    print(f"PM2.5:                {format_value(data['pm2_5'], units.get('pm2_5', ''))}")
    print(f"PM10:                 {format_value(data['pm10'], units.get('pm10', ''))}")
    print("=" * 48)
    print("Source: Open-Meteo Air Quality API")
    print("Note: AQI is an indicator; people with health concerns should")
    print("follow local public-health guidance.")
    print("=" * 48 + "\n")


def main():
    location_name, (latitude, longitude) = choose_city()
    print(f"\nFetching the latest air-quality data for {location_name}...")
    try:
        data = fetch_air_quality(latitude, longitude)
        display_report(data, location_name)
    except RuntimeError as error:
        print(f"\nError: {error}")
        print("Please try again later.\n")


if __name__ == "__main__":
    main()
